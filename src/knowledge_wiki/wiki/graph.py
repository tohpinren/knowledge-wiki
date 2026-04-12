from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import re
from typing import Any

from ..config import Settings
from ..models import WikiPage
from ..utils import slugify, write_json
from ..workflows.common import list_evidence_artifacts, list_source_manifests
from .pages import extract_related_refs, iter_page_paths, read_page


HEADING_RE = re.compile(r"^##+\s+(.+)$", flags=re.MULTILINE)


def build_knowledge_graph(settings: Settings) -> tuple[dict[str, Any], str]:
    pages: list[tuple[str, WikiPage]] = []
    for path in iter_page_paths(settings.wiki_dir):
        try:
            page = read_page(path)
        except Exception:
            continue
        if page.status != "canonical":
            continue
        pages.append((path.relative_to(settings.root_dir).as_posix(), page))

    source_manifests = list_source_manifests(settings)
    evidence_artifacts = list_evidence_artifacts(settings)
    evidence_by_ref = {
        ref: artifact
        for artifact in evidence_artifacts
        for ref in artifact.source_refs
    }

    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    seen_nodes: set[str] = set()
    seen_edges: set[tuple[str, str, str]] = set()
    page_node_ids: dict[str, str] = {}
    module_hubs: dict[str, str] = {}
    page_concepts: dict[str, set[str]] = defaultdict(set)

    def add_node(node_id: str, kind: str, **payload: Any) -> None:
        if node_id in seen_nodes:
            return
        seen_nodes.add(node_id)
        node = {"id": node_id, "kind": kind}
        node.update(payload)
        nodes.append(node)

    def add_edge(source: str, target: str, kind: str, provenance: str) -> None:
        key = (source, target, kind)
        if source == target or key in seen_edges:
            return
        seen_edges.add(key)
        edges.append(
            {
                "source": source,
                "target": target,
                "kind": kind,
                "provenance": provenance,
            }
        )

    for relative_path, page in pages:
        node_id = f"page:{page.page_id}"
        page_node_ids[page.page_id] = node_id
        if page.page_kind == "hub" and page.module_id:
            module_hubs[page.module_id] = node_id
        add_node(
            node_id,
            "page",
            title=page.title,
            path=relative_path,
            page_type=page.page_type,
            page_kind=page.page_kind,
            module_id=page.module_id,
            parent_page_id=page.parent_page_id,
            lecture_number=page.lecture_number,
            source_count=page.source_count,
            topics=list(page.topics),
            updated=page.last_compiled_at,
        )

    for manifest in source_manifests:
        add_node(
            f"source:{manifest.source_id}",
            "source",
            title=manifest.title,
            path=manifest.file_path,
            module_id=manifest.module_id,
            kind_name=manifest.kind,
        )

    for artifact in evidence_artifacts:
        add_node(
            f"evidence:{artifact.evidence_id}",
            "evidence",
            title=str(artifact.metadata.get("title") or artifact.source_id),
            path=artifact.source_path,
            module_id=artifact.module_id,
            source_id=artifact.source_id,
            content_class=artifact.content_class,
            topics=list(artifact.key_topics),
        )

    for relative_path, page in pages:
        page_node = page_node_ids[page.page_id]
        related_refs = extract_related_refs(page)
        if page.parent_page_id and page.parent_page_id in page_node_ids:
            add_edge(page_node_ids[page.parent_page_id], page_node, "parent_of", "deterministic")
        if page.module_id and page.module_id in module_hubs and page.page_kind != "hub":
            hub_node = module_hubs[page.module_id]
            add_edge(hub_node, page_node, "contains", "deterministic")
            add_edge(page_node, hub_node, "same_module", "deterministic")
        for target in related_refs:
            if target in page_node_ids:
                add_edge(page_node, page_node_ids[target], "related_to", "deterministic")
        source_ids = {ref.split("#", maxsplit=1)[0] for ref in page.source_refs}
        for source_id in sorted(source_ids):
            add_edge(page_node, f"source:{source_id}", "derived_from", "deterministic")
        for ref in page.source_refs:
            artifact = evidence_by_ref.get(ref)
            if artifact:
                add_edge(page_node, f"evidence:{artifact.evidence_id}", "derived_from", "deterministic")

        concepts = _page_concepts(page)
        page_concepts[page_node].update(concepts)
        for concept in sorted(concepts):
            concept_node = f"concept:{slugify(concept)}"
            add_node(concept_node, "concept", title=concept)
            add_edge(page_node, concept_node, "mentions", "inferred")

    module_pages: dict[str, list[str]] = defaultdict(list)
    for _, page in pages:
        if page.module_id:
            module_pages[page.module_id].append(page_node_ids[page.page_id])

    for page_nodes in module_pages.values():
        for source, target in combinations(sorted(page_nodes), 2):
            add_edge(source, target, "same_module", "deterministic")
            add_edge(target, source, "same_module", "deterministic")

    topic_to_pages: dict[str, list[str]] = defaultdict(list)
    for page_node, concepts in page_concepts.items():
        for concept in concepts:
            topic_to_pages[slugify(concept)].append(page_node)
    for page_nodes in topic_to_pages.values():
        if len(page_nodes) < 2:
            continue
        for source, target in combinations(sorted(set(page_nodes)), 2):
            add_edge(source, target, "same_topic", "inferred")
            add_edge(target, source, "same_topic", "inferred")

    graph = {
        "version": 1,
        "nodes": nodes,
        "edges": edges,
    }
    report = _render_graph_report(pages, nodes, edges, topic_to_pages)
    return graph, report


def write_knowledge_graph(settings: Settings) -> dict[str, Any]:
    graph, report = build_knowledge_graph(settings)
    settings.graph_dir.mkdir(parents=True, exist_ok=True)
    write_json(settings.graph_dir / "graph.json", graph)
    settings.graph_dir.joinpath("GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    return graph


def load_knowledge_graph(settings: Settings) -> dict[str, Any] | None:
    path = settings.graph_dir / "graph.json"
    if not path.exists():
        return None
    import json

    return json.loads(path.read_text(encoding="utf-8"))


def _page_concepts(page: WikiPage) -> set[str]:
    concepts = {topic.strip() for topic in page.topics if topic.strip()}
    for heading in HEADING_RE.findall(page.body):
        cleaned = heading.strip().strip(":")
        if 3 <= len(cleaned) <= 80:
            concepts.add(cleaned)
    return concepts


def _render_graph_report(
    pages: list[tuple[str, WikiPage]],
    nodes: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    topic_to_pages: dict[str, list[str]],
) -> str:
    node_counts = Counter(node["kind"] for node in nodes)
    edge_counts = Counter(edge["kind"] for edge in edges)
    module_counts = Counter(page.module_id for _, page in pages if page.module_id)
    lines = [
        "# Knowledge Graph Report",
        "",
        f"- Nodes: `{len(nodes)}`",
        f"- Edges: `{len(edges)}`",
        "",
        "## Node Counts",
        "",
    ]
    for kind, count in sorted(node_counts.items()):
        lines.append(f"- `{kind}`: {count}")
    lines.extend(["", "## Edge Counts", ""])
    for kind, count in sorted(edge_counts.items()):
        lines.append(f"- `{kind}`: {count}")
    if module_counts:
        lines.extend(["", "## Modules", ""])
        for module_id, count in sorted(module_counts.items()):
            lines.append(f"- `{module_id}`: {count} page(s)")
    prominent_topics = sorted(
        (
            (len(set(page_nodes)), topic)
            for topic, page_nodes in topic_to_pages.items()
            if len(set(page_nodes)) > 1
        ),
        reverse=True,
    )[:10]
    if prominent_topics:
        lines.extend(["", "## Shared Topics", ""])
        for count, topic in prominent_topics:
            lines.append(f"- `{topic}` appears across {count} page(s)")
    return "\n".join(lines) + "\n"
