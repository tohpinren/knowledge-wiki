from __future__ import annotations

from collections import Counter
from pathlib import Path
import re

from ..bootstrap import bootstrap_repository
from ..config import Settings
from ..models import DraftProposal, EvidenceArtifact, LayoutReview, LayoutPagePlan, WikiPage
from ..progress import ProgressCallback, noop_progress
from ..providers import LLMProvider
from ..utils import compact_text
from ..utils import ensure_parent, utc_now
from ..utils import slugify
from ..wiki.frontmatter import split_frontmatter
from ..wiki.graph import write_knowledge_graph
from ..wiki.index import regenerate_wiki_index
from ..wiki.pages import collect_page_source_refs, extract_related_refs, iter_page_paths, read_page, render_page
from .ingest import IngestWorkflow
from .common import (
    append_log,
    list_drafts,
    list_evidence_artifacts,
    list_layout_reviews,
    list_source_manifests,
    load_draft,
    load_layout_review,
    load_module_manifest,
    load_source_manifest,
    regenerate_system_index,
    save_draft,
    save_layout_review,
    save_module_manifest,
    save_source_manifest,
)


class ReviewWorkflow:
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

    def list_pages(
        self,
        *,
        module_id: str | None = None,
        page_kind: str | None = None,
    ) -> list[dict[str, str]]:
        pages: list[dict[str, str]] = []
        for path in iter_page_paths(self.settings.wiki_dir):
            try:
                page = read_page(path)
            except Exception:
                continue
            if page.status != "canonical":
                continue
            if module_id and page.module_id != module_id:
                continue
            if page_kind and page.page_kind != page_kind:
                continue
            relative_path = path.relative_to(self.settings.root_dir).as_posix()
            pages.append(self.describe_page(relative_path, page=page))
        return sorted(
            pages,
            key=lambda item: (
                item["module_id"],
                {"hub": 0, "inventory": 1, "topic": 2, "artifact": 3}.get(item["page_kind"], 9),
                item["title"].lower(),
                item["path"],
            ),
        )

    def inspect_page(self, page_ref: str) -> dict[str, object]:
        page_path = self._resolve_page_path(page_ref)
        if not page_path.exists():
            raise ValueError(f"Page `{page_ref}` does not exist.")
        return self._page_inspection(page_path)

    def describe_page(self, page_ref: str, *, page: WikiPage | None = None) -> dict[str, str]:
        page_path = self._resolve_page_path(page_ref)
        loaded = page or read_page(page_path)
        relative_path = page_path.relative_to(self.settings.root_dir).as_posix()
        return {
            "path": relative_path,
            "title": loaded.title,
            "page_kind": loaded.page_kind or loaded.page_type,
            "module_id": loaded.module_id or "",
            "choice_label": f"[{loaded.page_kind or loaded.page_type}] {loaded.title} :: {relative_path}",
        }

    def list_layouts(
        self,
        *,
        state: str | None = None,
        module_id: str | None = None,
        batch_id: str | None = None,
    ) -> list[LayoutReview]:
        self._progress("Loading layout reviews.")
        return list_layout_reviews(self.settings, state=state, module_id=module_id, batch_id=batch_id)

    def load_layout(self, layout_id: str) -> LayoutReview:
        return load_layout_review(self.settings, layout_id)

    def inspect_layout(self, layout_id: str) -> dict[str, object]:
        layout = load_layout_review(self.settings, layout_id)
        return self._layout_inspection(layout)

    def approve_layout(self, layout_id: str) -> LayoutReview:
        self._progress(f"Approving layout {layout_id}.")
        layout = load_layout_review(self.settings, layout_id)
        pending_drafts = list_drafts(
            self.settings,
            state="pending",
            module_id=layout.module_id,
            batch_id=layout.batch_id,
        )
        if layout.approval_state == "rejected":
            raise ValueError(f"Layout `{layout_id}` is already rejected.")
        if layout.approval_state == "approved" and not pending_drafts:
            raise ValueError(f"Layout `{layout_id}` is already approved.")
        if layout.approval_state == "pending":
            layout.approval_state = "approved"
            layout.updated_at = utc_now()
            save_layout_review(self.settings, layout)
        self._progress(
            f"Publishing {len(pending_drafts)} pending draft(s) for approved layout {layout.layout_id}."
        )
        for draft in pending_drafts:
            self._publish_draft_record(draft)

        approved_drafts = list_drafts(
            self.settings,
            state="approved",
            module_id=layout.module_id,
            batch_id=layout.batch_id,
        )
        kept_paths = {draft.target_page for draft in approved_drafts}
        pruned_paths = self._prune_generated_module_pages(layout.module_id, kept_paths=kept_paths)

        if pending_drafts:
            self._update_module_after_draft_change(layout.module_id, layout.batch_id)
        else:
            self._mark_module_published_without_drafts(layout.module_id, layout.batch_id)

        layout.metadata["auto_published_draft_count"] = len(pending_drafts)
        layout.metadata["pruned_page_count"] = len(pruned_paths)
        layout.updated_at = utc_now()
        save_layout_review(self.settings, layout)
        self._progress(f"Updating module state for {layout.module_id} and regenerating derived knowledge artifacts.")
        self._refresh_derived_outputs()
        append_log(
            self.settings,
            f"approved layout `{layout_id}` for module `{layout.module_id}` and auto-published "
            f"{len(pending_drafts)} draft(s)"
            + (f", pruning {len(pruned_paths)} stale page(s)," if pruned_paths else ",")
            + " then regenerated wiki index, graph, and system index.",
        )
        return layout

    def reject_layout(self, layout_id: str) -> LayoutReview:
        self._progress(f"Rejecting layout {layout_id}.")
        layout = load_layout_review(self.settings, layout_id)
        if layout.approval_state != "pending":
            raise ValueError(f"Layout `{layout_id}` is already {layout.approval_state}.")
        layout.approval_state = "rejected"
        layout.updated_at = utc_now()
        save_layout_review(self.settings, layout)
        self._update_module_after_layout(layout.module_id, state="rejected")
        self._progress(f"Updating module state for {layout.module_id} and regenerating the system index.")
        regenerate_system_index(self.settings)
        append_log(self.settings, f"rejected layout `{layout_id}` for module `{layout.module_id}`.")
        return layout

    def revise_layout(self, layout_id: str, feedback: str) -> LayoutReview:
        if not self.provider:
            raise ValueError("Revising a layout requires an LLM provider.")
        self._progress(f"Revising layout {layout_id}.")
        layout = load_layout_review(self.settings, layout_id)
        if layout.approval_state == "approved":
            raise ValueError(f"Layout `{layout_id}` is already approved and cannot be revised in place.")
        module_manifest = load_module_manifest(self.settings, layout.module_id)
        existing_drafts = list_drafts(self.settings, module_id=layout.module_id, batch_id=layout.batch_id)
        if any(draft.approval_state == "approved" for draft in existing_drafts):
            raise ValueError("Cannot revise a layout after any draft in the batch has been approved.")

        evidence_artifacts = list_evidence_artifacts(self.settings, module_id=layout.module_id, batch_id=layout.batch_id)
        self._progress(f"Loaded {len(evidence_artifacts)} evidence artifact(s) for {layout.module_id}.")
        ingest = IngestWorkflow(self.settings, provider=self.provider, progress=self.progress)
        nearby_pages = ingest._nearby_existing_pages(module_manifest.module_id, module_manifest.term, evidence_artifacts)
        self._progress("Generating a revised layout plan from reviewer feedback.")
        revised = ingest._build_layout_review(
            module_manifest=module_manifest,
            evidence_artifacts=evidence_artifacts,
            nearby_pages=nearby_pages,
            feedback=feedback,
            previous_layout=layout,
        )
        revised.layout_id = layout.layout_id
        revised.created_at = layout.created_at
        revised.approval_state = "pending"
        merged_metadata = dict(layout.metadata)
        merged_metadata.update(revised.metadata)
        revised.metadata = merged_metadata
        history = list(revised.metadata.get("revision_history", []))
        history.append({"revised_at": utc_now(), "feedback": feedback})
        revised.metadata["revision_history"] = history
        revised.metadata["last_feedback"] = feedback
        save_layout_review(self.settings, revised)

        self._progress("Regenerating page drafts from the revised layout.")
        revised_drafts = ingest._draft_course_pages(
            module_manifest=module_manifest,
            layout_review=revised,
            evidence_artifacts=evidence_artifacts,
            nearby_pages=nearby_pages,
            feedback_by_slug={page.slug: feedback for page in revised.pages},
            existing_drafts={draft.metadata.get("page_slug", ""): draft for draft in existing_drafts},
        )
        revised_slugs = {draft.metadata.get("page_slug") for draft in revised_drafts}
        for draft in existing_drafts:
            page_slug = draft.metadata.get("page_slug", "")
            if page_slug not in revised_slugs:
                draft.approval_state = "rejected"
                draft.updated_at = utc_now()
                draft.metadata["superseded_by_layout_revision"] = feedback
                save_draft(self.settings, draft)
        for draft in revised_drafts:
            prior = next((item for item in existing_drafts if item.draft_id == draft.draft_id), None)
            if prior:
                revision_history = list(prior.metadata.get("revision_history", []))
                revision_history.append({"revised_at": utc_now(), "feedback": f"layout:{feedback}"})
                draft.metadata["revision_history"] = revision_history
            save_draft(self.settings, draft)

        module_manifest.status = "layout_pending"
        module_manifest.layout_review_state = "pending"
        module_manifest.draft_review_state = "pending"
        module_manifest.updated_at = utc_now()
        save_module_manifest(self.settings, module_manifest)
        self._progress("Updating module state and regenerating the system index.")
        regenerate_system_index(self.settings)
        append_log(self.settings, f"revised layout `{layout_id}` for module `{layout.module_id}`.")
        return revised

    def revise_page(self, page_ref: str, feedback: str) -> tuple[str, WikiPage]:
        if not self.provider:
            raise ValueError("Revising a page requires an LLM provider.")
        page_path = self._resolve_page_path(page_ref)
        if not page_path.exists():
            raise ValueError(f"Page `{page_ref}` does not exist.")
        if page_path.suffix.lower() != ".md":
            raise ValueError(f"Page `{page_ref}` must be a markdown file.")

        self._progress(f"Revising canonical page {page_path.relative_to(self.settings.root_dir)}.")
        page = read_page(page_path)
        if page.status != "canonical":
            raise ValueError(f"Page `{page_ref}` is `{page.status}`, not canonical.")

        revised_body = self._revised_page_body(page, page_path, feedback)
        page.body = revised_body
        page.summary = compact_text(_strip_markdown(revised_body), limit=220)
        page.related = extract_related_refs(page)
        page.source_refs = collect_page_source_refs(page)
        page.source_count = len({ref.split("#", maxsplit=1)[0] for ref in page.source_refs})
        page.topics = self._updated_page_topics(page)
        page.last_compiled_at = utc_now()
        page_path.write_text(render_page(page), encoding="utf-8")

        self._progress("Regenerating the wiki index, graph, and system index.")
        self._refresh_derived_outputs()
        relative_path = page_path.relative_to(self.settings.root_dir).as_posix()
        append_log(
            self.settings,
            f"revised page `{relative_path}` with reviewer feedback, then regenerated wiki index and graph.",
        )
        return relative_path, page

    def _canonical_markdown(self, markdown: str) -> str:
        frontmatter, body = split_frontmatter(markdown)
        page = WikiPage.from_parts(frontmatter, body)
        page.status = "canonical"
        page.last_compiled_at = utc_now()
        return render_page(page)

    def _prune_generated_module_pages(self, module_id: str, *, kept_paths: set[str]) -> list[str]:
        manifest = load_module_manifest(self.settings, module_id)
        module_root = (
            self.settings.root_dir
            / "wiki"
            / "courses"
            / slugify(manifest.term)
            / slugify(manifest.module_code)
        )
        if not module_root.exists():
            return []

        removed: list[str] = []
        for path in iter_page_paths(module_root):
            relative_path = path.relative_to(self.settings.root_dir).as_posix()
            if relative_path in kept_paths:
                continue
            try:
                page = read_page(path)
            except Exception:
                continue
            if page.status != "canonical":
                continue
            if page.module_id != module_id:
                continue
            if not page.batch_id:
                continue
            path.unlink(missing_ok=True)
            removed.append(relative_path)

        for directory in sorted(module_root.rglob("*"), reverse=True):
            if directory.is_dir():
                try:
                    directory.rmdir()
                except OSError:
                    pass
        return removed

    def _layout_inspection(self, layout: LayoutReview) -> dict[str, object]:
        module = load_module_manifest(self.settings, layout.module_id)
        evidence_artifacts = list_evidence_artifacts(
            self.settings,
            module_id=layout.module_id,
            batch_id=layout.batch_id,
        )
        titles_by_ref: dict[str, str] = {}
        for artifact in evidence_artifacts:
            title = str(artifact.metadata.get("title") or artifact.source_id)
            for ref in artifact.source_refs:
                titles_by_ref[ref] = title
        ordered_pages = sorted(layout.pages, key=self._layout_page_sort_key)
        kind_counts = Counter(page.page_kind for page in ordered_pages)
        strategy = str(layout.metadata.get("layout_strategy", "generic")).strip() or "generic"

        lines = [
            f"# {module.module_code} Layout Review",
            "",
            f"- Layout ID: `{layout.layout_id}`",
            f"- Module: `{layout.module_id}`",
            f"- Batch: `{layout.batch_id}`",
            f"- State: `{layout.approval_state}`",
            f"- Strategy: `{strategy}`",
            f"- Pages: `{len(ordered_pages)}` total "
            f"({kind_counts.get('hub', 0)} hub, {kind_counts.get('inventory', 0)} inventory, "
            f"{kind_counts.get('topic', 0)} topic, {kind_counts.get('artifact', 0)} artifact)",
            "",
            "## Page Plan",
            "",
        ]
        page_rows: list[list[object]] = []
        for page in ordered_pages:
            source_titles = self._source_titles_for_page(page, titles_by_ref)
            lines.append(
                f"- `{page.slug}` [{page.page_kind}] {page.title} "
                f"(parent={page.parent_slug or 'root'}, refs={len(page.assigned_source_refs)}, "
                f"related={len(page.related_page_ids)})"
            )
            if source_titles:
                lines.append(f"  sources: {', '.join(source_titles)}")
            page_rows.append(
                [
                    page.slug,
                    page.title,
                    page.page_kind,
                    page.parent_slug or "root",
                    len(page.assigned_source_refs),
                    ", ".join(source_titles),
                    ", ".join(page.related_page_ids),
                ]
            )
        return {
            "summary_markdown": "\n".join(lines),
            "page_rows": page_rows,
            "raw_payload": layout.to_dict(),
        }

    def _page_inspection(self, page_path: Path) -> dict[str, object]:
        page = read_page(page_path)
        evidence_artifacts = (
            list_evidence_artifacts(
                self.settings,
                module_id=page.module_id,
                batch_id=page.batch_id,
            )
            if page.module_id and page.batch_id
            else []
        )
        artifacts_by_ref = {
            ref: artifact
            for artifact in evidence_artifacts
            for ref in artifact.source_refs
        }
        evidence_rows: list[list[str]] = []
        source_titles: list[str] = []
        seen_titles: set[str] = set()
        for ref in page.source_refs:
            artifact = artifacts_by_ref.get(ref)
            title = str(artifact.metadata.get("title", artifact.source_id)) if artifact else "Unknown source"
            source_path = str(artifact.metadata.get("module_relpath", artifact.source_path)) if artifact else ""
            summary = compact_text(artifact.summary, limit=90) if artifact else ""
            evidence_rows.append([ref, title, source_path, summary])
            if title not in seen_titles:
                seen_titles.add(title)
                source_titles.append(title)
        relative_path = page_path.relative_to(self.settings.root_dir).as_posix()
        lines = [
            f"# {page.title}",
            "",
            f"- Path: `{relative_path}`",
            f"- Status: `{page.status}`",
            f"- Kind: `{page.page_kind or page.page_type}`",
            f"- Module: `{page.module_id or 'n/a'}`",
            f"- Batch: `{page.batch_id or 'n/a'}`",
            f"- Parent: `{page.parent_page_id or 'root'}`",
            f"- Evidence refs: `{len(page.source_refs)}`",
            f"- Topics: `{', '.join(page.topics) or 'n/a'}`",
            f"- Lecture: `{page.lecture_number if page.lecture_number is not None else 'n/a'}`",
            "",
            "## Summary",
            "",
            page.summary,
        ]
        if source_titles:
            lines.extend(["", "## Key Sources", ""])
            lines.extend(f"- {title}" for title in source_titles[:8])
        return {
            "summary_markdown": "\n".join(lines),
            "evidence_rows": evidence_rows,
            "raw_payload": {
                "path": relative_path,
                "frontmatter": page.frontmatter(),
                "body": page.body,
            },
            "proposed_markdown": render_page(page),
        }

    def _layout_page_sort_key(self, page: LayoutPagePlan) -> tuple[int, int, str]:
        if page.page_kind == "hub":
            return (0, 0, page.slug)
        if page.page_kind == "inventory":
            return (1, 0, page.slug)
        lecture_match = page.slug.startswith("lecture-")
        if lecture_match:
            return (2, _lecture_slug_number(page.slug), page.slug)
        if page.page_kind == "topic":
            return (3, 0, page.slug)
        return (4, 0, page.slug)

    def _source_titles_for_page(
        self,
        page: LayoutPagePlan,
        titles_by_ref: dict[str, str],
    ) -> list[str]:
        titles: list[str] = []
        seen: set[str] = set()
        for ref in page.assigned_source_refs:
            title = titles_by_ref.get(ref)
            if title and title not in seen:
                seen.add(title)
                titles.append(title)
            if len(titles) >= 3:
                break
        return titles

    def _update_module_after_layout(self, module_id: str, *, state: str) -> None:
        manifest = load_module_manifest(self.settings, module_id)
        manifest.layout_review_state = state
        if state == "approved":
            manifest.status = "drafts_pending"
            manifest.draft_review_state = "pending"
        elif state == "rejected":
            manifest.status = "layout_rejected"
        manifest.updated_at = utc_now()
        save_module_manifest(self.settings, manifest)

    def _update_module_after_draft_change(self, module_id: str, batch_id: str) -> None:
        manifest = load_module_manifest(self.settings, module_id)
        drafts = list_drafts(self.settings, module_id=module_id, batch_id=batch_id)
        pending = [draft for draft in drafts if draft.approval_state == "pending"]
        approved = [draft for draft in drafts if draft.approval_state == "approved"]
        if pending:
            manifest.status = "drafts_pending"
            manifest.draft_review_state = "pending"
        elif approved:
            manifest.status = "published"
            manifest.draft_review_state = "approved"
            self._mark_module_sources_published(module_id, batch_id)
        else:
            manifest.status = "drafts_rejected"
            manifest.draft_review_state = "rejected"
        manifest.updated_at = utc_now()
        save_module_manifest(self.settings, manifest)

    def _mark_module_published_without_drafts(self, module_id: str, batch_id: str) -> None:
        manifest = load_module_manifest(self.settings, module_id)
        manifest.layout_review_state = "approved"
        manifest.status = "published"
        manifest.draft_review_state = "approved"
        manifest.updated_at = utc_now()
        save_module_manifest(self.settings, manifest)
        self._mark_module_sources_published(module_id, batch_id)

    def _mark_module_sources_published(self, module_id: str, batch_id: str) -> None:
        for manifest in list_source_manifests(self.settings, module_id=module_id, batch_id=batch_id):
            if manifest.extract_status == "extracted":
                manifest.ingest_status = "published"
                manifest.updated_at = utc_now()
                save_source_manifest(self.settings, manifest)

    def _publish_draft_record(self, draft: DraftProposal) -> None:
        target_path = self.settings.root_dir / draft.target_page
        ensure_parent(target_path)
        target_path.write_text(self._canonical_markdown(draft.proposed_markdown), encoding="utf-8")
        self._progress(f"Wrote canonical page {draft.target_page}.")
        draft.approval_state = "approved"
        draft.updated_at = utc_now()
        save_draft(self.settings, draft)

        source_id = draft.metadata.get("source_id")
        if source_id:
            manifest = load_source_manifest(self.settings, source_id)
            manifest.ingest_status = "published"
            manifest.updated_at = utc_now()
            save_source_manifest(self.settings, manifest)

    def _revised_page_body(self, page: WikiPage, page_path: Path, feedback: str) -> str:
        if page.module_id and page.batch_id:
            layouts = list_layout_reviews(self.settings, module_id=page.module_id, batch_id=page.batch_id)
            if layouts:
                layout = layouts[-1]
                page_slug = self._page_slug_for_page(page, page_path)
                plan = next((item for item in layout.pages if item.slug == page_slug), None)
                if plan:
                    module_manifest = load_module_manifest(self.settings, page.module_id)
                    evidence_artifacts = list_evidence_artifacts(
                        self.settings,
                        module_id=page.module_id,
                        batch_id=page.batch_id,
                    )
                    ingest = IngestWorkflow(self.settings, provider=self.provider, progress=self.progress)
                    nearby_pages = ingest._nearby_existing_pages(module_manifest.module_id, module_manifest.term, evidence_artifacts)
                    return ingest._draft_page_body(
                        module_manifest=module_manifest,
                        plan=plan,
                        evidence_artifacts=evidence_artifacts,
                        artifacts_by_ref=ingest._evidence_by_source_ref(evidence_artifacts),
                        nearby_pages=nearby_pages,
                        all_plans=layout.pages,
                        feedback=feedback,
                        existing_markdown=page.body,
                    )

        prompt = "\n".join(
            [
                "REVISE_PAGE_REQUEST",
                "Return markdown only. Do not include YAML frontmatter.",
                f"Page title: {page.title}",
                f"Page id: {page.page_id}",
                f"Current page kind: {page.page_kind or page.page_type}",
                "Current canonical markdown:",
                page.body,
                "",
                "Reviewer feedback:",
                feedback,
                "",
                "Revise the page accordingly while preserving factual claims and useful source citations.",
            ]
        )
        self._progress("Generating revised page content from reviewer feedback.")
        result = self.provider.generate(prompt, system_prompt="You revise canonical wiki pages based on reviewer feedback.")
        return _normalize_revised_body(page.title, result.text)

    def _page_slug_for_page(self, page: WikiPage, page_path: Path) -> str:
        if page.page_kind == "hub":
            return "hub"
        if page.page_kind == "inventory":
            return "inventory"
        if page.module_id:
            prefix = f"{page.module_id}-"
            if page.page_id.startswith(prefix):
                return page.page_id[len(prefix) :]
        return page_path.stem

    def _resolve_page_path(self, page_ref: str) -> Path:
        candidate = Path(page_ref)
        if not candidate.is_absolute():
            candidate = self.settings.root_dir / candidate
        resolved = candidate.resolve()
        try:
            resolved.relative_to(self.settings.root_dir)
        except ValueError as exc:
            raise ValueError(f"Page `{page_ref}` must live under `{self.settings.root_dir}`.") from exc
        return resolved

    def _refresh_derived_outputs(self) -> None:
        regenerate_wiki_index(self.settings)
        write_knowledge_graph(self.settings)
        regenerate_system_index(self.settings)

    def _updated_page_topics(self, page: WikiPage) -> list[str]:
        if page.topics:
            seen: set[str] = set()
            topics: list[str] = []
            for topic in page.topics:
                lowered = topic.strip().lower()
                if not lowered or lowered in seen:
                    continue
                seen.add(lowered)
                topics.append(topic.strip())
            if topics:
                return topics
        return _keywords_from_text(f"{page.title}\n{page.summary}\n{page.body}", limit=8)

    def _progress(self, message: str) -> None:
        self.progress(message)


def _normalize_revised_body(title: str, body: str) -> str:
    stripped = body.strip()
    if stripped.startswith("---"):
        raise ValueError("Draft revision must not return YAML frontmatter.")
    if not stripped.startswith("# "):
        return f"# {title}\n\n{stripped}\n"
    return stripped + "\n"


def _strip_markdown(text: str) -> str:
    return " ".join(line.strip("# ").strip() for line in text.splitlines() if line.strip())


def _lecture_slug_number(slug: str) -> int:
    parts = slug.split("-")
    if len(parts) < 2:
        return 0
    try:
        return int(parts[1])
    except ValueError:
        return 0


def _keywords_from_text(text: str, *, limit: int) -> list[str]:
    words = [word for word in re.findall(r"[A-Za-z][A-Za-z0-9&/-]+", text) if len(word) > 3]
    seen: set[str] = set()
    keywords: list[str] = []
    for word in words:
        lowered = word.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        keywords.append(word)
        if len(keywords) >= limit:
            break
    return keywords
