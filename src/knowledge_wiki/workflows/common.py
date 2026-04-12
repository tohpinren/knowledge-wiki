from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from ..config import Settings
from ..models import DraftProposal, EvidenceArtifact, LayoutReview, ModuleManifest, SourceManifest
from ..utils import read_json, slugify, utc_now, write_json


def source_manifest_path(settings: Settings, source_id: str) -> Path:
    return settings.source_manifest_dir / f"{source_id}.json"


def module_manifest_path(settings: Settings, module_id: str) -> Path:
    return settings.module_manifest_dir / f"{module_id}.json"


def draft_path(settings: Settings, draft_id: str) -> Path:
    return settings.drafts_dir / f"{draft_id}.json"


def layout_path(settings: Settings, layout_id: str) -> Path:
    return settings.layouts_dir / f"{layout_id}.json"


def evidence_path(settings: Settings, evidence_id: str) -> Path:
    return settings.evidence_dir / f"{evidence_id}.json"


def ingest_metrics_path(settings: Settings, batch_id: str) -> Path:
    return settings.ingest_metrics_dir / f"{batch_id}.json"


def save_source_manifest(settings: Settings, manifest: SourceManifest) -> None:
    write_json(source_manifest_path(settings, manifest.source_id), manifest.to_dict())


def load_source_manifest(settings: Settings, source_id: str) -> SourceManifest:
    return SourceManifest.from_dict(read_json(source_manifest_path(settings, source_id)))


def list_source_manifests(
    settings: Settings,
    *,
    module_id: str | None = None,
    batch_id: str | None = None,
) -> list[SourceManifest]:
    manifests = [
        SourceManifest.from_dict(read_json(path))
        for path in sorted(settings.source_manifest_dir.glob("*.json"))
    ]
    if module_id:
        manifests = [manifest for manifest in manifests if manifest.module_id == module_id]
    if batch_id:
        manifests = [manifest for manifest in manifests if manifest.batch_id == batch_id]
    return manifests


def save_module_manifest(settings: Settings, manifest: ModuleManifest) -> None:
    write_json(module_manifest_path(settings, manifest.module_id), manifest.to_dict())


def load_module_manifest(settings: Settings, module_id: str) -> ModuleManifest:
    return ModuleManifest.from_dict(read_json(module_manifest_path(settings, module_id)))


def list_module_manifests(settings: Settings) -> list[ModuleManifest]:
    return [
        ModuleManifest.from_dict(read_json(path))
        for path in sorted(settings.module_manifest_dir.glob("*.json"))
    ]


def save_evidence_artifact(settings: Settings, artifact: EvidenceArtifact) -> None:
    write_json(evidence_path(settings, artifact.evidence_id), artifact.to_dict())


def save_ingest_metrics(settings: Settings, batch_id: str, payload: dict) -> None:
    write_json(ingest_metrics_path(settings, batch_id), payload)


def load_evidence_artifact(settings: Settings, evidence_id: str) -> EvidenceArtifact:
    return EvidenceArtifact.from_dict(read_json(evidence_path(settings, evidence_id)))


def list_evidence_artifacts(
    settings: Settings,
    *,
    module_id: str | None = None,
    batch_id: str | None = None,
) -> list[EvidenceArtifact]:
    artifacts = [
        EvidenceArtifact.from_dict(read_json(path))
        for path in sorted(settings.evidence_dir.glob("*.json"))
        if path.name != "README.md"
    ]
    if module_id:
        artifacts = [artifact for artifact in artifacts if artifact.module_id == module_id]
    if batch_id:
        artifacts = [artifact for artifact in artifacts if artifact.batch_id == batch_id]
    return artifacts


def save_layout_review(settings: Settings, review: LayoutReview) -> None:
    write_json(layout_path(settings, review.layout_id), review.to_dict())


def load_layout_review(settings: Settings, layout_id: str) -> LayoutReview:
    return LayoutReview.from_dict(read_json(layout_path(settings, layout_id)))


def list_layout_reviews(
    settings: Settings,
    *,
    module_id: str | None = None,
    batch_id: str | None = None,
    state: str | None = None,
) -> list[LayoutReview]:
    reviews = [
        LayoutReview.from_dict(read_json(path))
        for path in sorted(settings.layouts_dir.glob("*.json"))
    ]
    if module_id:
        reviews = [review for review in reviews if review.module_id == module_id]
    if batch_id:
        reviews = [review for review in reviews if review.batch_id == batch_id]
    if state:
        reviews = [review for review in reviews if review.approval_state == state]
    return reviews


def save_draft(settings: Settings, proposal: DraftProposal) -> None:
    write_json(draft_path(settings, proposal.draft_id), proposal.to_dict())


def load_draft(settings: Settings, draft_id: str) -> DraftProposal:
    return DraftProposal.from_dict(read_json(draft_path(settings, draft_id)))


def list_drafts(
    settings: Settings,
    *,
    state: str | None = None,
    module_id: str | None = None,
    batch_id: str | None = None,
) -> list[DraftProposal]:
    drafts = [
        DraftProposal.from_dict(read_json(path))
        for path in sorted(settings.drafts_dir.glob("*.json"))
    ]
    if state:
        drafts = [draft for draft in drafts if draft.approval_state == state]
    if module_id:
        drafts = [draft for draft in drafts if draft.module_id == module_id]
    if batch_id:
        drafts = [draft for draft in drafts if draft.batch_id == batch_id]
    return drafts


def append_log(settings: Settings, message: str) -> None:
    log_path = settings.system_dir / "log.md"
    prefix = "# Update Log\n\n"
    if not log_path.exists():
        log_path.write_text(prefix, encoding="utf-8")
    existing = log_path.read_text(encoding="utf-8")
    if not existing.startswith("# Update Log"):
        existing = prefix + existing
    updated = existing.rstrip() + f"\n- {utc_now()} {message}\n"
    log_path.write_text(updated, encoding="utf-8")


def regenerate_system_index(settings: Settings) -> None:
    modules = list_module_manifests(settings)
    manifests = list_source_manifests(settings)
    evidence = list_evidence_artifacts(settings)
    layouts = list_layout_reviews(settings)
    drafts = list_drafts(settings)

    module_status_counts = Counter(manifest.status for manifest in modules)
    source_counts = Counter(manifest.ingest_status for manifest in manifests)
    layout_counts = Counter(review.approval_state for review in layouts)
    draft_counts = Counter(draft.approval_state for draft in drafts)
    graph_path = settings.graph_dir / "graph.json"
    graph_node_count = 0
    graph_edge_count = 0
    if graph_path.exists():
        payload = json.loads(graph_path.read_text(encoding="utf-8"))
        graph_node_count = len(payload.get("nodes", []))
        graph_edge_count = len(payload.get("edges", []))

    lines = [
        "# System Index",
        "",
        "## Course Batches",
        "",
        f"- Total: {len(modules)}",
        f"- Awaiting planning: {module_status_counts.get('awaiting_planning', 0)}",
        f"- Layout pending: {module_status_counts.get('layout_pending', 0)}",
        f"- Layout approved: {module_status_counts.get('layout_approved', 0)}",
        f"- Drafts pending: {module_status_counts.get('drafts_pending', 0)}",
        f"- Published: {module_status_counts.get('published', 0)}",
        "",
        "## Source Manifests",
        "",
        f"- Total: {len(manifests)}",
        f"- Registered: {source_counts.get('registered', 0)}",
        f"- Evidence ready: {source_counts.get('evidence_ready', 0)}",
        f"- Drafted: {source_counts.get('drafted', 0)}",
        f"- Published: {source_counts.get('published', 0)}",
        "",
        "## Evidence Artifacts",
        "",
        f"- Total: {len(evidence)}",
        "",
        "## Layout Reviews",
        "",
        f"- Pending: {layout_counts.get('pending', 0)}",
        f"- Approved: {layout_counts.get('approved', 0)}",
        f"- Rejected: {layout_counts.get('rejected', 0)}",
        "",
        "## Generated Publish Plans",
        "",
        f"- Pending: {draft_counts.get('pending', 0)}",
        f"- Approved: {draft_counts.get('approved', 0)}",
        f"- Rejected: {draft_counts.get('rejected', 0)}",
        "",
        "## Knowledge Graph",
        "",
        f"- Nodes: {graph_node_count}",
        f"- Edges: {graph_edge_count}",
    ]

    pending_layouts = [review for review in layouts if review.approval_state == "pending"]
    if pending_layouts:
        lines.extend(["", "## Pending Layout Queue", ""])
        for review in pending_layouts:
            lines.append(f"- `{review.layout_id}` -> `{review.module_id}`")

    pending_drafts = [draft for draft in drafts if draft.approval_state == "pending"]
    if pending_drafts:
        lines.extend(["", "## Pending Generated Publish Queue", ""])
        for draft in pending_drafts:
            target = draft.target_page
            prefix = f"{draft.module_id} " if draft.module_id else ""
            lines.append(f"- `{draft.draft_id}` -> {prefix}`{target}`")

    settings.system_dir.joinpath("index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def infer_page_type(scope: str) -> str:
    lowered = scope.strip().lower()
    if lowered.startswith("course"):
        return "course"
    if lowered.startswith("project"):
        return "project"
    if lowered.startswith("synthesis"):
        return "synthesis"
    return "concept"


def unique_slug(base: str, *, existing: set[str]) -> str:
    slug = slugify(base)
    if slug not in existing:
        return slug
    counter = 2
    while f"{slug}-{counter}" in existing:
        counter += 1
    return f"{slug}-{counter}"
