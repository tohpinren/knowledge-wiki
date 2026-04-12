from __future__ import annotations

import json
import re

from ..bootstrap import bootstrap_repository
from ..config import Settings
from ..models import QueryAnswer, RetrievalHit, SynthesisSuggestion
from ..progress import ProgressCallback, noop_progress
from ..providers import LLMProvider
from ..retrieval import build_catalog, search_catalog
from ..utils import STOPWORDS, compact_text, slugify, tokenize
from ..wiki.graph import load_knowledge_graph
from ..wiki.pages import read_page


class QueryWorkflow:
    def __init__(
        self,
        settings: Settings,
        *,
        provider: LLMProvider | None = None,
        progress: ProgressCallback | None = None,
    ) -> None:
        self.settings = settings
        self.provider = provider
        self.progress = progress or noop_progress
        bootstrap_repository(settings)

    def answer(
        self,
        question: str,
        *,
        max_results: int | None = None,
    ) -> QueryAnswer:
        limit = max_results or self.settings.max_retrieval_hits
        self._progress("Reading wiki index for query navigation.")
        hits = self._search_index_then_pages(question, max_results=limit)
        if hits:
            self._progress(f"Found {len(hits)} published wiki hit(s).")
        else:
            self._progress("No published wiki hits found.")

        citations = list(dict.fromkeys(ref for hit in hits for ref in hit.source_refs))
        answer_markdown = self._compose_answer(question, hits)
        suggested_synthesis = self._suggest_synthesis(question, answer_markdown, hits)
        answer = QueryAnswer(
            question=question,
            answer_markdown=answer_markdown,
            hits=hits,
            raw_fallback_used=False,
            citations=citations,
            suggested_synthesis=suggested_synthesis,
        )
        return answer

    def _compose_answer(self, question: str, hits: list[RetrievalHit]) -> str:
        if not hits:
            return (
                "I could not find enough information in the published wiki to answer this question. "
                "Try ingesting or revising the relevant wiki pages first."
            )

        if self.provider:
            answer = self._provider_answer(question, hits)
            if answer:
                return answer

        lines = ["## Summary", ""]
        references = ", ".join(f"`{hit.title}`" for hit in hits[:3])
        lines.append(f"This answer is grounded in the compiled wiki pages {references}.")
        lines.extend(["", "## Evidence", ""])
        for hit in hits:
            refs = ", ".join(f"[source:{ref}]" for ref in hit.source_refs[:3]) if hit.source_refs else "no source refs"
            lines.append(f"- `{hit.title}`: {hit.snippet} ({refs})")
        return "\n".join(lines)

    def _provider_answer(self, question: str, hits: list[RetrievalHit]) -> str | None:
        self._progress(f"Composing an answer with the provider from {len(hits)} hit(s).")
        prompt_lines = [
            "Answer the question using only the provided wiki page evidence.",
            "Preserve source citations exactly when you use them.",
            "Read the provided page bodies carefully. Prefer the most directly relevant section instead of summarizing every page equally.",
            "If one page clearly answers the question, answer directly from it.",
            "If the wiki evidence is insufficient, say plainly that the answer is not available in the published wiki.",
            "",
            f"Question: {question}",
            "",
            "Relevant wiki pages:",
        ]
        for hit in hits:
            page_context = self._page_context(hit.path)
            prompt_lines.append(f"## {hit.title}")
            prompt_lines.append(f"Path: {hit.path}")
            prompt_lines.append(f"Relevant excerpt:\n{hit.snippet}")
            if hit.source_refs:
                prompt_lines.append("Citations: " + ", ".join(f"[source:{ref}]" for ref in hit.source_refs[:6]))
            prompt_lines.append("Full page body:")
            prompt_lines.append(page_context)
            prompt_lines.append("")
        try:
            result = self.provider.generate(
                "\n".join(prompt_lines),
                system_prompt="You answer questions from a maintained knowledge wiki and keep citations intact.",
            )
        except Exception:
            return None
        text = result.text.strip()
        return text or None

    def _search_index_then_pages(self, question: str, *, max_results: int) -> list[RetrievalHit]:
        index_entries = self._load_index_entries()
        if not index_entries:
            self._progress("Wiki index is empty; falling back to catalog search.")
            catalog = build_catalog(self.settings)
            self._progress(f"Searching the wiki catalog for up to {max_results} hit(s).")
            return search_catalog(catalog, question, max_results=max_results)

        self._progress(f"Searching wiki index for up to {max_results} relevant page(s).")
        ranked_entries: list[tuple[float, dict[str, object]]] = []
        for entry in index_entries:
            score = _score_index_entry(entry, question)
            if score > 0:
                ranked_entries.append((score, entry))

        top_entries = [
            entry
            for _, entry in sorted(ranked_entries, key=lambda item: item[0], reverse=True)[: max_results * 2]
        ]
        expanded_entries = self._expand_with_graph_neighbors(top_entries, index_entries, max_results=max_results)
        hits: list[RetrievalHit] = []
        for entry in expanded_entries:
            page_path = self.settings.wiki_dir / str(entry["path"])
            if not page_path.exists():
                continue
            page = read_page(page_path)
            full_text = f"{page.title}\n{page.summary}\n{page.body}"
            snippet = _relevant_excerpt(full_text, question, limit=500)
            score = float(_score_index_entry(entry, question) + (_excerpt_score(full_text, question) * 2))
            if score <= 0:
                continue
            hits.append(
                RetrievalHit(
                    path=f"wiki/{entry['path']}",
                    page_id=page.page_id,
                    title=page.title,
                    score=score,
                    snippet=snippet,
                    source_refs=page.source_refs[:8],
                )
            )
        return _dedupe_hits(sorted(hits, key=lambda hit: hit.score, reverse=True))[:max_results]

    def _load_index_entries(self) -> list[dict[str, object]]:
        index_path = self.settings.wiki_dir / "index.md"
        if not index_path.exists():
            return []
        entries: list[dict[str, object]] = []
        for line in index_path.read_text(encoding="utf-8").splitlines():
            payload = _parse_index_line(line)
            if payload:
                entries.append(payload)
        return entries

    def _expand_with_graph_neighbors(
        self,
        entries: list[dict[str, object]],
        index_entries: list[dict[str, object]],
        *,
        max_results: int,
    ) -> list[dict[str, object]]:
        if not entries:
            return []
        index_by_page_path = {
            f"wiki/{entry['path']}": entry
            for entry in index_entries
        }
        expanded = list(entries)
        seen_paths = {str(entry["path"]) for entry in entries}
        graph = load_knowledge_graph(self.settings)
        if not graph:
            return expanded
        nodes_by_id = {node["id"]: node for node in graph.get("nodes", [])}
        for node in graph.get("nodes", []):
            if node.get("kind") != "page":
                continue
            node_path = str(node.get("path", ""))
            relative_path = node_path.removeprefix("wiki/")
            if relative_path not in seen_paths:
                continue
            for edge in graph.get("edges", []):
                if edge.get("source") != node["id"] or edge.get("kind") not in {
                    "related_to",
                    "same_topic",
                    "parent_of",
                    "contains",
                    "same_module",
                }:
                    continue
                neighbor = nodes_by_id.get(str(edge.get("target")))
                if not neighbor or neighbor.get("kind") != "page":
                    continue
                neighbor_path = str(neighbor.get("path", ""))
                if neighbor_path in index_by_page_path and neighbor_path.removeprefix("wiki/") not in seen_paths:
                    expanded.append(index_by_page_path[neighbor_path])
                    seen_paths.add(neighbor_path.removeprefix("wiki/"))
                if len(expanded) >= max_results * 3:
                    return expanded
        return expanded

    def _page_context(self, page_ref: str) -> str:
        path = self.settings.root_dir / page_ref
        page = read_page(path)
        return compact_text(page.body, limit=12000)

    def _suggest_synthesis(
        self,
        question: str,
        answer_markdown: str,
        hits: list[RetrievalHit],
    ) -> SynthesisSuggestion | None:
        if not hits or _answer_is_insufficient(answer_markdown):
            return None
        suggestion = self._provider_suggest_synthesis(question, answer_markdown, hits)
        if suggestion is not None:
            return suggestion
        title = _suggestion_title(question)
        citations = list(dict.fromkeys(ref for hit in hits for ref in hit.source_refs))
        summary = compact_text(_strip_markdown(answer_markdown), limit=220)
        body = answer_markdown.strip()
        if not body.startswith("# "):
            body = f"# {title}\n\n{body}"
        return SynthesisSuggestion(
            title=title,
            path=f"wiki/syntheses/{slugify(title)}.md",
            summary=summary,
            body=body + "\n",
            citations=citations,
        )

    def _provider_suggest_synthesis(
        self,
        question: str,
        answer_markdown: str,
        hits: list[RetrievalHit],
    ) -> SynthesisSuggestion | None:
        if not self.provider:
            return None
        prompt_lines = [
            "SUGGEST_SYNTHESIS_REQUEST",
            "Decide whether the answer is reusable enough to save as a synthesis page.",
            'Return strict JSON with keys: save (bool), title (str), summary (str), body (str).',
            "If it is not worth saving, return {\"save\": false}.",
            "",
            f"Question: {question}",
            "Answer:",
            answer_markdown,
            "",
            "Supporting wiki pages:",
        ]
        for hit in hits[:5]:
            prompt_lines.append(f"- {hit.title} :: {hit.path}")
        try:
            result = self.provider.generate(
                "\n".join(prompt_lines),
                system_prompt="You decide whether a query answer should become a reusable synthesis page.",
            )
        except Exception:
            return None
        try:
            payload = json.loads(result.text)
        except Exception:
            return None
        if not payload.get("save"):
            return None
        title = str(payload.get("title", "")).strip() or _suggestion_title(question)
        summary = compact_text(str(payload.get("summary", "")).strip() or _strip_markdown(answer_markdown), limit=220)
        body = str(payload.get("body", "")).strip() or answer_markdown.strip()
        if not body.startswith("# "):
            body = f"# {title}\n\n{body}"
        citations = list(dict.fromkeys(ref for hit in hits for ref in hit.source_refs))
        return SynthesisSuggestion(
            title=title,
            path=f"wiki/syntheses/{slugify(title)}.md",
            summary=summary,
            body=body + "\n",
            citations=citations,
        )

    def _progress(self, message: str) -> None:
        self.progress(message)


def _meaningful_query_tokens(question: str) -> list[str]:
    filtered = [
        token
        for token in tokenize(question)
        if len(token) > 2 and token not in STOPWORDS and not token.isdigit()
    ]
    return filtered or tokenize(question)


def _excerpt_score(text: str, question: str) -> int:
    query_tokens = _meaningful_query_tokens(question)
    passage_tokens = tokenize(text)
    return sum(1 for token in query_tokens if token in passage_tokens)


def _relevant_excerpt(text: str, question: str, *, limit: int = 500) -> str:
    passages = [chunk.strip() for chunk in re.split(r"\n\s*\n", text) if chunk.strip()]
    if not passages:
        return compact_text(text, limit=limit)
    query_tokens = _meaningful_query_tokens(question)
    scored: list[tuple[int, int, str]] = []
    for index, passage in enumerate(passages):
        passage_tokens = tokenize(passage)
        score = sum(1 for token in query_tokens if token in passage_tokens)
        if score <= 0:
            continue
        scored.append((score, index, passage))
    if not scored:
        return compact_text(text, limit=limit)
    top_passages = [
        compact_text(passage, limit=min(limit, 320))
        for _, _, passage in sorted(scored, key=lambda item: (-item[0], item[1]))[:2]
    ]
    return "\n\n".join(top_passages)


def _parse_index_line(line: str) -> dict[str, object] | None:
    match = re.match(r"^- \[(?P<title>[^\]]+)\]\((?P<path>[^)]+)\)(?P<rest>.*)$", line.strip())
    if not match:
        return None
    payload: dict[str, object] = {
        "title": match.group("title").strip(),
        "path": match.group("path").strip(),
    }
    rest = match.group("rest").strip()
    if not rest:
        return payload
    for segment in [part.strip() for part in rest.split("::") if part.strip()]:
        key, separator, raw_value = segment.partition("=")
        if not separator:
            continue
        payload[key.strip()] = _parse_index_scalar(raw_value.strip())
    return payload


def _parse_index_scalar(raw_value: str) -> object:
    if raw_value == "null":
        return None
    if raw_value.startswith(('"', "[", "{")):
        return json.loads(raw_value)
    if re.fullmatch(r"-?\d+", raw_value):
        return int(raw_value)
    if re.fullmatch(r"-?\d+\.\d+", raw_value):
        return float(raw_value)
    return raw_value


def _score_index_entry(entry: dict[str, object], question: str) -> float:
    query_tokens = _meaningful_query_tokens(question)
    haystack_parts = [
        str(entry.get("title", "")),
        str(entry.get("summary", "")),
        str(entry.get("type", "")),
        str(entry.get("kind", "")),
        str(entry.get("module", "")),
        str(entry.get("lecture", "")),
        " ".join(str(item) for item in entry.get("topics", [])),
    ]
    haystack = " ".join(part for part in haystack_parts if part)
    tokens = tokenize(haystack)
    score = float(sum(1 for token in query_tokens if token in tokens))
    if question.lower() in haystack.lower():
        score += 3
    if entry.get("lecture") and any(token in {"lecture", "week"} for token in query_tokens):
        score += 1
    return score


def _dedupe_hits(hits: list[RetrievalHit]) -> list[RetrievalHit]:
    seen: set[str] = set()
    deduped: list[RetrievalHit] = []
    for hit in hits:
        if hit.path in seen:
            continue
        seen.add(hit.path)
        deduped.append(hit)
    return deduped


def _answer_is_insufficient(answer_markdown: str) -> bool:
    normalized = answer_markdown.lower()
    return any(
        phrase in normalized
        for phrase in (
            "could not find enough information in the published wiki",
            "not available in the published wiki",
            "does not contain enough information",
            "insufficient",
        )
    )


def _suggestion_title(question: str) -> str:
    cleaned = re.sub(r"^(what|how|why|when|where|is|are|does|do|can)\s+", "", question.strip(), flags=re.I)
    cleaned = cleaned.rstrip(" ?")
    cleaned = cleaned or question.strip().rstrip(" ?")
    return cleaned[:1].upper() + cleaned[1:]


def _strip_markdown(text: str) -> str:
    stripped = re.sub(r"^#+\s+", "", text, flags=re.MULTILINE)
    stripped = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", stripped)
    stripped = re.sub(r"\[source:[^\]]+\]", "", stripped)
    return " ".join(part.strip() for part in stripped.splitlines() if part.strip())
