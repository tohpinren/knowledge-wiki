from __future__ import annotations

import re
from collections import defaultdict
from datetime import UTC, datetime, timedelta

from ..bootstrap import bootstrap_repository
from ..config import Settings
from ..models import LintFinding
from ..progress import ProgressCallback, noop_progress
from ..retrieval import build_catalog
from ..utils import STOPWORDS, slugify, tokenize
from ..wiki.graph import build_knowledge_graph
from .common import list_layout_reviews, list_source_manifests


class LintWorkflow:
    def __init__(self, settings: Settings, *, progress: ProgressCallback | None = None) -> None:
        self.settings = settings
        self.progress = progress or noop_progress
        bootstrap_repository(settings)

    def run(self) -> list[LintFinding]:
        self._progress("Building the published wiki catalog for lint checks.")
        entries = build_catalog(self.settings)
        self._progress(f"Running lint rules across {len(entries)} page(s).")
        graph, _ = build_knowledge_graph(self.settings)
        manifests_by_source_id = {
            manifest.source_id: manifest for manifest in list_source_manifests(self.settings)
        }
        graph_contains = defaultdict(set)
        for edge in graph.get("edges", []):
            if edge.get("kind") == "contains":
                graph_contains[str(edge.get("source"))].add(str(edge.get("target")))
        by_page_id = {entry.page_id: entry for entry in entries}
        known_targets = set(by_page_id)
        known_targets.update(slugify(entry.title) for entry in entries)
        known_targets.update(
            slugify(entry.path.rsplit("/", maxsplit=1)[-1].removesuffix(".md")) for entry in entries
        )
        backlinks: dict[str, set[str]] = defaultdict(set)
        for entry in entries:
            for target in entry.related:
                backlinks[target].add(entry.page_id)

        findings: list[LintFinding] = []
        for entry in entries:
            if not entry.source_refs:
                findings.append(
                    LintFinding(
                        kind="weak_provenance",
                        severity="medium",
                        message=f"Page `{entry.title}` has no source references.",
                        path=entry.path,
                    )
                )
            if entry.lecture_number is not None and entry.source_count == 0:
                findings.append(
                    LintFinding(
                        kind="missing_source_coverage",
                        severity="medium",
                        message=f"Lecture page `{entry.title}` has no linked source files.",
                        path=entry.path,
                    )
                )
            elif entry.lecture_number is not None and entry.source_count == 1:
                findings.append(
                    LintFinding(
                        kind="weak_source_coverage",
                        severity="low",
                        message=f"Lecture page `{entry.title}` is backed by only one source file.",
                        path=entry.path,
                    )
                )
            if not entry.related and not backlinks.get(entry.page_id):
                findings.append(
                    LintFinding(
                        kind="orphan_page",
                        severity="medium",
                        message=f"Page `{entry.title}` is disconnected from the wiki graph.",
                        path=entry.path,
                    )
                )
            for target in entry.related:
                if target not in known_targets:
                    findings.append(
                        LintFinding(
                            kind="missing_related_target",
                            severity="medium",
                            message=f"Page `{entry.title}` references missing target `{target}`.",
                            path=entry.path,
                            details={"target": target},
                        )
                    )
                    continue
                if target in by_page_id and entry.page_id not in by_page_id[target].related:
                    findings.append(
                        LintFinding(
                            kind="missing_backlink",
                            severity="low",
                            message=f"Page `{entry.title}` links to `{target}` without a reciprocal backlink.",
                            path=entry.path,
                            details={"target": target},
                        )
                    )
            if entry.page_kind == "hub" and entry.module_id:
                child_pages = [
                    item
                    for item in entries
                    if item.module_id == entry.module_id and item.parent_page_id == entry.page_id
                ]
                if child_pages:
                    graph_children = graph_contains.get(f"page:{entry.page_id}", set())
                    if len(graph_children) != len(child_pages):
                        findings.append(
                            LintFinding(
                                kind="stale_module_hub",
                                severity="low",
                                message=f"Hub page `{entry.title}` is out of sync with its lecture/topic children.",
                                path=entry.path,
                            )
                        )

        for finding in self._stale_layout_findings():
            findings.append(finding)
        for finding in self._conflicting_summary_findings(entries):
            findings.append(finding)
        for finding in self._possible_contradiction_findings(entries):
            findings.append(finding)
        for finding in self._inconsistent_topic_findings(entries):
            findings.append(finding)
        for finding in self._missing_cross_link_findings(entries):
            findings.append(finding)
        for finding in self._missing_concept_page_findings(entries):
            findings.append(finding)
        for finding in self._stale_page_coverage_findings(entries, manifests_by_source_id):
            findings.append(finding)
        for finding in self._research_gap_findings(entries):
            findings.append(finding)

        self._progress(f"Collected {len(findings)} lint finding(s).")
        return findings

    def render_markdown(self, findings: list[LintFinding]) -> str:
        if not findings:
            return "No lint findings."
        lines = ["# Lint Findings", ""]
        for finding in findings:
            location = f" at `{finding.path}`" if finding.path else ""
            lines.append(f"- `{finding.severity}` `{finding.kind}`{location}: {finding.message}")
        return "\n".join(lines)

    def _stale_layout_findings(self) -> list[LintFinding]:
        findings: list[LintFinding] = []
        threshold = datetime.now(UTC) - timedelta(days=7)
        for layout in list_layout_reviews(self.settings, state="pending"):
            try:
                created = datetime.fromisoformat(layout.created_at)
            except ValueError:
                continue
            if created < threshold:
                findings.append(
                    LintFinding(
                        kind="stale_layout",
                        severity="low",
                        message=f"Layout `{layout.layout_id}` has been pending for more than 7 days.",
                        path=f"system/reviews/layouts/{layout.layout_id}.json",
                    )
                )
        return findings

    def _conflicting_summary_findings(self, entries) -> list[LintFinding]:
        findings: list[LintFinding] = []
        grouped = defaultdict(list)
        for entry in entries:
            if entry.page_type != "concept":
                continue
            grouped[slugify(entry.title)].append(entry)
        for key, group in grouped.items():
            if len(group) < 2:
                continue
            summaries = {entry.summary.strip().lower() for entry in group}
            if len(summaries) > 1:
                findings.append(
                    LintFinding(
                        kind="conflicting_summary",
                        severity="medium",
                        message=f"Concept cluster `{key}` has divergent summaries across multiple pages.",
                    )
                )
        return findings

    def _inconsistent_topic_findings(self, entries) -> list[LintFinding]:
        findings: list[LintFinding] = []
        grouped = defaultdict(list)
        for entry in entries:
            for topic in entry.topics:
                grouped[slugify(topic)].append(entry)
        for topic, group in grouped.items():
            if len(group) < 2:
                continue
            topic_sets = {tuple(sorted(item.topics)) for item in group}
            if len(topic_sets) > 1:
                findings.append(
                    LintFinding(
                        kind="inconsistent_topics",
                        severity="low",
                        message=f"Topic cluster `{topic}` has inconsistent topic metadata across related pages.",
                    )
                )
        return findings

    def _missing_cross_link_findings(self, entries) -> list[LintFinding]:
        findings: list[LintFinding] = []
        grouped = defaultdict(list)
        by_id = {entry.page_id: entry for entry in entries}
        for entry in entries:
            for topic in entry.topics:
                grouped[slugify(topic)].append(entry.page_id)
        for topic, page_ids in grouped.items():
            unique_ids = sorted(set(page_ids))
            if len(unique_ids) < 3:
                continue
            linked = False
            for page_id in unique_ids:
                related = set(by_id[page_id].related)
                if related.intersection(unique_ids):
                    linked = True
                    break
            if not linked:
                findings.append(
                    LintFinding(
                        kind="missing_cross_links",
                        severity="low",
                        message=f"Topic cluster `{topic}` appears across multiple pages without cross-links.",
                    )
                )
        return findings

    def _possible_contradiction_findings(self, entries) -> list[LintFinding]:
        findings: list[LintFinding] = []
        grouped = defaultdict(list)
        for entry in entries:
            keys = {slugify(entry.title)}
            keys.update(slugify(topic) for topic in entry.topics)
            for key in keys:
                if key:
                    grouped[key].append(entry)
        for key, group in grouped.items():
            if len(group) < 2:
                continue
            detected = False
            for index, left in enumerate(group):
                left_claim = _claim_text(left)
                left_tokens = set(_content_tokens(left_claim))
                for right in group[index + 1 :]:
                    right_claim = _claim_text(right)
                    shared = left_tokens.intersection(_content_tokens(right_claim))
                    if len(shared) < 2:
                        continue
                    if _has_negation(left_claim) != _has_negation(right_claim):
                        findings.append(
                            LintFinding(
                                kind="possible_contradiction",
                                severity="low",
                                message=f"Topic cluster `{key}` may contain contradictory claims across pages.",
                                details={"pages": [left.path, right.path]},
                            )
                        )
                        detected = True
                        break
                if detected:
                    break
        return findings

    def _missing_concept_page_findings(self, entries) -> list[LintFinding]:
        findings: list[LintFinding] = []
        topic_to_pages = defaultdict(set)
        known_page_slugs = {slugify(entry.title) for entry in entries}
        known_page_slugs.update(
            slugify(entry.path.rsplit("/", maxsplit=1)[-1].removesuffix(".md")) for entry in entries
        )
        for entry in entries:
            for topic in entry.topics:
                topic_to_pages[slugify(topic)].add(entry.page_id)
        for topic, page_ids in sorted(topic_to_pages.items()):
            if len(page_ids) < 3:
                continue
            if topic in known_page_slugs:
                continue
            findings.append(
                LintFinding(
                    kind="missing_concept_page",
                    severity="medium",
                    message=f"Topic `{topic}` appears across multiple pages but has no dedicated page.",
                    details={"pages": sorted(page_ids)},
                )
            )
        return findings

    def _stale_page_coverage_findings(self, entries, manifests_by_source_id) -> list[LintFinding]:
        findings: list[LintFinding] = []
        for entry in entries:
            if not entry.last_compiled_at or not entry.source_refs:
                continue
            try:
                compiled_at = datetime.fromisoformat(entry.last_compiled_at)
            except ValueError:
                continue
            newest_source = None
            newest_source_id = None
            for ref in entry.source_refs:
                source_id = ref.split("#", maxsplit=1)[0]
                manifest = manifests_by_source_id.get(source_id)
                if not manifest:
                    continue
                try:
                    updated_at = datetime.fromisoformat(manifest.updated_at)
                except ValueError:
                    continue
                if newest_source is None or updated_at > newest_source:
                    newest_source = updated_at
                    newest_source_id = source_id
            if newest_source and newest_source > compiled_at:
                findings.append(
                    LintFinding(
                        kind="stale_page_coverage",
                        severity="medium",
                        message=f"Page `{entry.title}` may be stale relative to newer source `{newest_source_id}`.",
                        path=entry.path,
                        details={"source_id": newest_source_id},
                    )
                )
        return findings

    def _research_gap_findings(self, entries) -> list[LintFinding]:
        findings: list[LintFinding] = []
        topic_to_entries = defaultdict(list)
        for entry in entries:
            for topic in entry.topics:
                topic_to_entries[slugify(topic)].append(entry)
        for topic, group in sorted(topic_to_entries.items()):
            unique_pages = {entry.page_id for entry in group}
            if len(unique_pages) < 2:
                continue
            total_sources = sum(max(entry.source_count, 0) for entry in group)
            has_synthesis = any(entry.page_type == "synthesis" for entry in group)
            if total_sources <= len(unique_pages) and not has_synthesis:
                findings.append(
                    LintFinding(
                        kind="research_gap",
                        severity="low",
                        message=f"Topic `{topic}` appears repeatedly but has thin source coverage and no synthesis page.",
                        details={"pages": sorted(unique_pages)},
                    )
                )
        return findings

    def _progress(self, message: str) -> None:
        self.progress(message)


def _claim_text(entry) -> str:
    lines = [line.strip() for line in entry.text.splitlines() if line.strip()]
    snippet = " ".join(lines[:4])
    return f"{entry.summary} {snippet}".strip().lower()


def _content_tokens(text: str) -> list[str]:
    return [
        token
        for token in tokenize(text)
        if len(token) > 3 and token not in STOPWORDS and not token.isdigit()
    ]


def _has_negation(text: str) -> bool:
    return bool(re.search(r"\b(no|not|never|cannot|can't|without|only)\b", text))
