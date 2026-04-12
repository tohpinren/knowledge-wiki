from __future__ import annotations

from collections import Counter
import re

from ..models import CatalogEntry, RetrievalHit
from ..utils import STOPWORDS, compact_text, tokenize


def search_catalog(entries: list[CatalogEntry], query: str, *, max_results: int = 5) -> list[RetrievalHit]:
    query_tokens = _meaningful_query_tokens(query)
    if not query_tokens:
        return []

    ranked: list[RetrievalHit] = []
    for entry in entries:
        title_tokens = tokenize(entry.title)
        summary_tokens = tokenize(entry.summary)
        body_tokens = tokenize(entry.text)
        title_score = _overlap_score(query_tokens, title_tokens) * 4
        summary_score = _overlap_score(query_tokens, summary_tokens) * 2
        body_score = _overlap_score(query_tokens, body_tokens)
        phrase_bonus = 3 if query.lower() in entry.text.lower() else 0
        score = float(title_score + summary_score + body_score + phrase_bonus)
        if score <= 0:
            continue
        ranked.append(
            RetrievalHit(
                path=entry.path,
                page_id=entry.page_id,
                title=entry.title,
                score=score,
                snippet=_build_snippet(entry.text, query_tokens),
                source_refs=entry.source_refs[:8],
            )
        )

    return sorted(ranked, key=lambda hit: hit.score, reverse=True)[:max_results]


def _overlap_score(query_tokens: list[str], candidate_tokens: list[str]) -> int:
    query_counts = Counter(query_tokens)
    candidate_counts = Counter(candidate_tokens)
    return sum(min(query_counts[token], candidate_counts[token]) for token in query_counts)


def _build_snippet(text: str, query_tokens: list[str]) -> str:
    passages = _candidate_passages(text)
    if not passages:
        return compact_text(text, limit=420)

    scored: list[tuple[int, int, str]] = []
    for index, passage in enumerate(passages):
        passage_tokens = tokenize(passage)
        overlap = _overlap_score(query_tokens, passage_tokens)
        if overlap <= 0:
            continue
        lowered = passage.lower()
        phrase_bonus = sum(2 for token in query_tokens if token in lowered)
        scored.append((overlap + phrase_bonus, index, passage))

    if not scored:
        return compact_text(text, limit=420)

    top_passages = [
        compact_text(passage, limit=320)
        for _, _, passage in sorted(scored, key=lambda item: (-item[0], item[1]))[:2]
    ]
    return "\n\n".join(top_passages)


def _meaningful_query_tokens(query: str) -> list[str]:
    filtered = [
        token
        for token in tokenize(query)
        if len(token) > 2 and token not in STOPWORDS and not token.isdigit()
    ]
    return filtered or tokenize(query)


def _candidate_passages(text: str) -> list[str]:
    chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n", text) if chunk.strip()]
    if chunks:
        return chunks
    return [line.strip() for line in text.splitlines() if line.strip()]
