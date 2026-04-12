from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import re
from pathlib import Path
from threading import Lock

from ..bootstrap import bootstrap_repository
from ..config import Settings
from ..models import (
    CourseIngestResult,
    DraftProposal,
    EvidenceArtifact,
    ExtractedSource,
    GenerationResult,
    LayoutPagePlan,
    LayoutReview,
    ModuleManifest,
    SourceManifest,
    SourceSection,
    WikiPage,
)
from ..progress import ProgressCallback, noop_progress
from ..providers import LLMProvider
from ..retrieval import build_catalog
from ..sources import SourceRegistry, build_source_registry, discover_course_files
from ..sources.discovery import DiscoveredFile
from ..utils import (
    compact_text,
    extract_json_object,
    relative_posix,
    sha256_path,
    slugify,
    timestamp_slug,
    top_terms,
    utc_now,
)
from ..wiki.pages import build_course_page_path, build_page_path, render_page
from ..wiki.provenance import build_source_ref, render_citation
from .common import (
    append_log,
    infer_page_type,
    list_evidence_artifacts,
    ingest_metrics_path,
    list_source_manifests,
    regenerate_system_index,
    save_draft,
    save_evidence_artifact,
    save_ingest_metrics,
    save_layout_review,
    save_module_manifest,
    save_source_manifest,
    unique_slug,
)

FILE_INPUT_SOURCE_KINDS = {"markdown", "pdf", "office", "html", "notebook", "code", "text"}
COURSE_EVIDENCE_REUSE_VERSION = "course-evidence-v1"


@dataclass(slots=True)
class _SourceDraftResult:
    index: int
    manifest: SourceManifest
    proposal: DraftProposal | None = None
    error: str = ""


@dataclass(slots=True)
class _CourseExtractionResult:
    index: int
    source_manifest: SourceManifest
    extracted: ExtractedSource | None = None
    artifact: EvidenceArtifact | None = None
    reused: bool = False
    reused_failure: bool = False
    reused_from_evidence_id: str = ""
    error: str = ""


@dataclass(slots=True)
class _CourseDraftResult:
    index: int
    proposal: DraftProposal


@dataclass(slots=True)
class _BatchUsageTracker:
    module_id: str
    batch_id: str
    provider: str
    model: str
    created_at: str
    lock: Lock
    records: list[dict]
    summary: dict[str, float | int | None]
    by_stage: dict[str, dict[str, float | int | None]]


class IngestWorkflow:
    def __init__(
        self,
        settings: Settings,
        *,
        provider: LLMProvider | None = None,
        registry: SourceRegistry | None = None,
        progress: ProgressCallback | None = None,
    ) -> None:
        self.settings = settings
        self.provider = provider
        self.registry = registry or build_source_registry()
        self.progress = progress or noop_progress
        self._usage_tracker: _BatchUsageTracker | None = None
        bootstrap_repository(settings)

    def register_source(
        self,
        path: str | Path,
        *,
        kind: str,
        title: str | None = None,
        origin: str = "manual",
        scope: str = "general",
    ) -> SourceManifest:
        source_path = Path(path).resolve()
        if not source_path.exists():
            raise FileNotFoundError(f"Source path does not exist: {source_path}")
        try:
            relative_path = source_path.relative_to(self.settings.root_dir)
        except ValueError as exc:
            raise ValueError("Source path must live inside the repository root, typically under raw/.") from exc

        existing_ids = {manifest.source_id for manifest in list_source_manifests(self.settings)}
        base_name = title or source_path.stem
        source_id = unique_slug(base_name, existing=existing_ids)
        timestamp = utc_now()
        self._progress(f"Registering {relative_path.as_posix()} as a {kind} source.")
        manifest = SourceManifest(
            source_id=source_id,
            title=title or source_path.stem.replace("-", " ").title(),
            kind=kind,
            origin=origin,
            scope=scope,
            file_path=relative_path.as_posix(),
            checksum=sha256_path(source_path),
            ingest_status="registered",
            created_at=timestamp,
            updated_at=timestamp,
        )
        save_source_manifest(self.settings, manifest)
        regenerate_system_index(self.settings)
        append_log(self.settings, f"registered source `{manifest.source_id}` from `{manifest.file_path}`.")
        return manifest

    def ingest(self, *, source_ids: list[str] | None = None) -> list[DraftProposal]:
        self._require_extraction_provider()
        self._progress("Loading source manifests for ingest.")
        manifests = list_source_manifests(self.settings)
        if source_ids:
            wanted = set(source_ids)
            manifests = [manifest for manifest in manifests if manifest.source_id in wanted]
        else:
            manifests = [manifest for manifest in manifests if manifest.ingest_status in {"registered", "pending"}]

        proposals: list[DraftProposal] = []
        if not manifests:
            self._progress("No eligible sources were found for ingest.")
            return proposals

        worker_count = self._worker_count(len(manifests))
        self._progress(f"Preparing {len(manifests)} source(s) for drafting with concurrency={worker_count}.")
        results = self._run_in_parallel(
            [lambda index=index, manifest=manifest: self._build_source_draft_result(index, manifest) for index, manifest in enumerate(manifests, start=1)],
            max_workers=worker_count,
        )
        total = len(manifests)
        failed = 0
        for result in results:
            manifest = result.manifest
            if result.proposal is None:
                failed += 1
                manifest.extract_status = "failed"
                manifest.ingest_status = "registered"
                manifest.skip_reason = result.error
                manifest.updated_at = utc_now()
                save_source_manifest(self.settings, manifest)
                self._progress(f"[{result.index}/{total}] Failed to ingest {manifest.file_path}: {result.error}")
                continue
            proposal = result.proposal
            manifest.extract_status = "extracted"
            manifest.ingest_status = "drafted"
            manifest.updated_at = utc_now()
            save_draft(self.settings, proposal)
            save_source_manifest(self.settings, manifest)
            append_log(
                self.settings,
                f"drafted source `{manifest.source_id}` into proposal `{proposal.draft_id}`.",
            )
            proposals.append(proposal)
            self._progress(f"[{result.index}/{total}] Saved draft {proposal.draft_id}.")

        regenerate_system_index(self.settings)
        if failed:
            append_log(self.settings, f"failed to draft {failed} source(s) during ingest.")
        return proposals

    def ingest_course(
        self,
        path: str | Path,
        *,
        term: str | None = None,
        module_code: str | None = None,
    ) -> CourseIngestResult:
        self._require_extraction_provider()
        course_root = Path(path).resolve()
        if not course_root.exists() or not course_root.is_dir():
            raise FileNotFoundError(f"Course path does not exist or is not a directory: {course_root}")
        try:
            relative_root = course_root.relative_to(self.settings.root_dir)
        except ValueError as exc:
            raise ValueError("Course path must live inside the repository root, typically under raw/.") from exc

        self._progress(f"Discovering supported files under {relative_root.as_posix()}.")
        derived_term, derived_module = self._derive_course_identity(course_root, term=term, module_code=module_code)
        module_id = slugify(f"{derived_term}-{derived_module}")
        batch_id = f"{module_id}-{timestamp_slug().lower()}"
        usable, skipped = discover_course_files(course_root)
        self._progress(f"Found {len(usable)} usable file(s) and {len(skipped)} skipped file(s).")

        manifest = ModuleManifest(
            module_id=module_id,
            term=derived_term,
            module_code=derived_module,
            root_path=relative_root.as_posix(),
            batch_id=batch_id,
            status="discovering",
            discovered_files=len(usable) + len(skipped),
            usable_files=0,
            skipped_files=0,
            layout_review_state="not_started",
            draft_review_state="not_started",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={},
        )
        self._start_usage_tracking(module_id=module_id, batch_id=batch_id)

        evidence_artifacts: list[EvidenceArtifact] = []
        failed_extracts: list[dict[str, str]] = []
        prior_source_manifests = {
            item.source_id: item for item in list_source_manifests(self.settings, module_id=module_id)
        }
        prior_evidence_artifacts = self._latest_evidence_artifacts_by_source_id(module_id)

        total_usable = len(usable)
        worker_count = self._worker_count(total_usable)
        reuse_results: list[_CourseExtractionResult] = []
        extraction_tasks: list = []
        for index, discovered in enumerate(usable, start=1):
            source_manifest = self._build_course_source_manifest(
                course_root=course_root,
                module_id=module_id,
                batch_id=batch_id,
                term=derived_term,
                module_code=derived_module,
                discovered=discovered,
            )
            reused = self._reuse_course_source_result(
                index=index,
                source_manifest=source_manifest,
                previous_manifest=prior_source_manifests.get(source_manifest.source_id),
                previous_artifact=prior_evidence_artifacts.get(source_manifest.source_id),
            )
            if reused is not None:
                reuse_results.append(reused)
                continue
            reused_failure = self._reuse_failed_course_source_result(
                index=index,
                source_manifest=source_manifest,
                previous_manifest=prior_source_manifests.get(source_manifest.source_id),
            )
            if reused_failure is not None:
                reuse_results.append(reused_failure)
                continue
            extraction_tasks.append(
                lambda index=index, source_manifest=source_manifest: self._extract_course_source_result(
                    index=index,
                    source_manifest=source_manifest,
                )
            )

        if total_usable:
            reused_count = len(reuse_results)
            if reused_count:
                self._progress(
                    f"Reusing previously extracted evidence for {reused_count} file(s); "
                    f"extracting {total_usable - reused_count} file(s) with concurrency={worker_count}."
                )
            else:
                self._progress(f"Extracting course files with concurrency={worker_count}.")
        extraction_results: list[_CourseExtractionResult] = []
        for result in sorted(reuse_results, key=lambda item: item.index):
            extraction_results.append(result)
            source_manifest = result.source_manifest
            if result.artifact is None:
                source_manifest.extract_status = "failed"
                source_manifest.skip_reason = result.error
                source_manifest.ingest_status = "registered"
                source_manifest.updated_at = utc_now()
                save_source_manifest(self.settings, source_manifest)
                failed_extracts.append(
                    {
                        "path": source_manifest.module_relpath,
                        "reason": source_manifest.skip_reason,
                    }
                )
                if result.reused_failure:
                    self._progress(
                        f"[{result.index}/{total_usable}] Reused prior extraction failure for "
                        f"{source_manifest.module_relpath}: {result.error}"
                    )
                else:
                    self._progress(
                        f"[{result.index}/{total_usable}] Failed to extract {source_manifest.module_relpath}: {result.error}"
                    )
                continue

            source_manifest.extract_status = "extracted"
            source_manifest.ingest_status = "evidence_ready"
            source_manifest.updated_at = utc_now()
            save_source_manifest(self.settings, source_manifest)
            save_evidence_artifact(self.settings, result.artifact)
            evidence_artifacts.append(result.artifact)
            if result.reused:
                self._progress(
                    f"[{result.index}/{total_usable}] Reused evidence {result.artifact.evidence_id} "
                    f"from {result.reused_from_evidence_id}."
                )
            else:
                self._progress(f"[{result.index}/{total_usable}] Saved evidence {result.artifact.evidence_id}.")

        for result in self._iter_in_parallel(
            extraction_tasks,
            max_workers=worker_count,
        ):
            extraction_results.append(result)
            source_manifest = result.source_manifest
            if result.artifact is None:
                source_manifest.extract_status = "failed"
                source_manifest.skip_reason = result.error
                source_manifest.ingest_status = "registered"
                source_manifest.updated_at = utc_now()
                save_source_manifest(self.settings, source_manifest)
                failed_extracts.append(
                    {
                        "path": source_manifest.module_relpath,
                        "reason": source_manifest.skip_reason,
                    }
                )
                if result.reused_failure:
                    self._progress(
                        f"[{result.index}/{total_usable}] Reused prior extraction failure for "
                        f"{source_manifest.module_relpath}: {result.error}"
                    )
                else:
                    self._progress(
                        f"[{result.index}/{total_usable}] Failed to extract {source_manifest.module_relpath}: {result.error}"
                    )
                continue

            source_manifest.extract_status = "extracted"
            source_manifest.ingest_status = "evidence_ready"
            source_manifest.updated_at = utc_now()
            save_source_manifest(self.settings, source_manifest)
            save_evidence_artifact(self.settings, result.artifact)
            evidence_artifacts.append(result.artifact)
            if result.reused:
                self._progress(
                    f"[{result.index}/{total_usable}] Reused evidence {result.artifact.evidence_id} "
                    f"from {result.reused_from_evidence_id}."
                )
            else:
                self._progress(f"[{result.index}/{total_usable}] Saved evidence {result.artifact.evidence_id}.")

        all_skipped = [
            {"path": item.relative_path.as_posix(), "reason": item.skip_reason}
            for item in skipped
        ] + failed_extracts
        reused_count = sum(1 for result in extraction_results if result.reused)

        manifest.usable_files = len(evidence_artifacts)
        manifest.skipped_files = len(all_skipped)
        manifest.metadata = {
            "usable_files": [item.relative_path.as_posix() for item in usable],
            "skipped_files": all_skipped,
            "reused_evidence_files": reused_count,
        }

        if not usable:
            manifest.status = "provider_failed"
            manifest.layout_review_state = "rejected"
            manifest.draft_review_state = "blocked"
            manifest.updated_at = utc_now()
            manifest.metadata["provider_error"] = "No supported source files were discovered in the course directory."
            self._persist_usage_metrics(manifest)
            save_module_manifest(self.settings, manifest)
            regenerate_system_index(self.settings)
            append_log(self.settings, f"course `{module_id}` batch `{batch_id}` had no supported source files to ingest. {self._usage_summary_line()}".strip())
            self._progress(f"No supported source files were discovered for {module_id}.")
            return CourseIngestResult(
                module_manifest=manifest,
                evidence_artifacts=[],
                layout_review=None,
                draft_proposals=[],
            )

        if usable and not evidence_artifacts:
            manifest.status = "provider_failed" if self._looks_like_provider_failure(failed_extracts) else "layout_invalid"
            manifest.layout_review_state = "rejected"
            manifest.draft_review_state = "blocked"
            manifest.updated_at = utc_now()
            manifest.metadata["provider_error"] = _first_error_message(failed_extracts) or "All extractions failed."
            self._persist_usage_metrics(manifest)
            save_module_manifest(self.settings, manifest)
            regenerate_system_index(self.settings)
            append_log(
                self.settings,
                f"failed to extract any usable course files for `{module_id}` batch `{batch_id}`: {manifest.metadata['provider_error']} {self._usage_summary_line()}".strip(),
            )
            self._progress(f"All usable files failed during extraction for {module_id}.")
            return CourseIngestResult(
                module_manifest=manifest,
                evidence_artifacts=[],
                layout_review=None,
                draft_proposals=[],
            )

        nearby_pages = self._nearby_existing_pages(module_id, derived_term, evidence_artifacts)
        self._progress(f"Planning layout from {len(evidence_artifacts)} evidence artifact(s).")
        try:
            layout_review = self._build_layout_review(
                module_manifest=manifest,
                evidence_artifacts=evidence_artifacts,
                nearby_pages=nearby_pages,
            )
        except Exception as exc:
            manifest.status = "provider_failed" if self._looks_like_provider_failure_message(str(exc)) else "layout_invalid"
            manifest.layout_review_state = "rejected"
            manifest.draft_review_state = "blocked"
            manifest.updated_at = utc_now()
            manifest.metadata["layout_error"] = str(exc)
            self._persist_usage_metrics(manifest)
            save_module_manifest(self.settings, manifest)
            regenerate_system_index(self.settings)
            append_log(
                self.settings,
                f"rejected invalid layout plan for course `{module_id}` batch `{batch_id}`: {exc} {self._usage_summary_line()}".strip(),
            )
            self._progress(f"Layout planning failed for {module_id}: {exc}")
            return CourseIngestResult(
                module_manifest=manifest,
                evidence_artifacts=evidence_artifacts,
                layout_review=None,
                draft_proposals=[],
            )

        save_layout_review(self.settings, layout_review)

        self._progress(f"Drafting {len(layout_review.pages)} page(s) for layout review.")
        draft_proposals = self._draft_course_pages(
            module_manifest=manifest,
            layout_review=layout_review,
            evidence_artifacts=evidence_artifacts,
            nearby_pages=nearby_pages,
        )
        for proposal in draft_proposals:
            save_draft(self.settings, proposal)

        for source_manifest in list_source_manifests(self.settings, module_id=module_id, batch_id=batch_id):
            if source_manifest.extract_status == "extracted":
                source_manifest.ingest_status = "drafted"
                source_manifest.updated_at = utc_now()
                save_source_manifest(self.settings, source_manifest)

        manifest.status = "layout_pending"
        manifest.layout_review_state = "pending"
        manifest.draft_review_state = "pending" if draft_proposals else "not_started"
        manifest.updated_at = utc_now()
        self._persist_usage_metrics(manifest)
        save_module_manifest(self.settings, manifest)
        regenerate_system_index(self.settings)
        append_log(
            self.settings,
            (
                f"ingested course `{module_id}` batch `{batch_id}` into layout "
                f"`{layout_review.layout_id}` and {len(draft_proposals)} page drafts. {self._usage_summary_line()}"
            ).strip(),
        )
        self._progress(
            f"Queued layout {layout_review.layout_id} and {len(draft_proposals)} draft(s) for review. {self._usage_summary_line()}".strip()
        )
        return CourseIngestResult(
            module_manifest=manifest,
            evidence_artifacts=evidence_artifacts,
            layout_review=layout_review,
            draft_proposals=draft_proposals,
        )

    def _build_single_source_draft(self, extracted: ExtractedSource) -> DraftProposal:
        self._progress(f"Summarizing {extracted.title}.")
        page_type = infer_page_type(extracted.manifest.scope)
        target_path = build_page_path(self.settings.root_dir, title=extracted.title, page_type=page_type)
        proposal_type = "patch_page" if target_path.exists() else "create_page"
        summary = self._build_summary(extracted)
        source_refs = [build_source_ref(extracted.manifest.source_id, section.section_id) for section in extracted.sections]
        page = WikiPage(
            page_id=slugify(extracted.title),
            title=extracted.title,
            page_type=page_type,
            status="draft",
            summary=summary,
            aliases=[],
            tags=self._build_tags(extracted.manifest.scope, extracted.manifest.kind, page_type),
            related=[],
            source_refs=source_refs,
            topics=top_terms(extracted.text, limit=8),
            source_count=1 if source_refs else 0,
            lecture_number=self._lecture_number_from_text(extracted.title) or self._lecture_number_from_text(extracted.manifest.file_path),
            last_compiled_at=utc_now(),
            body=self._build_source_body(extracted, summary),
            page_kind="source",
            batch_id=extracted.manifest.batch_id,
            module_id=extracted.manifest.module_id,
        )
        draft_id = f"{slugify(extracted.title)}-{extracted.manifest.source_id}"
        return DraftProposal(
            draft_id=draft_id,
            target_page=relative_posix(target_path, self.settings.root_dir),
            proposal_type=proposal_type,
            rationale=f"Compiled from raw source `{extracted.manifest.source_id}`.",
            evidence_set=source_refs,
            proposed_markdown=render_page(page),
            approval_state="pending",
            created_at=utc_now(),
            updated_at=utc_now(),
            module_id=extracted.manifest.module_id,
            batch_id=extracted.manifest.batch_id,
            page_kind="source",
            assigned_source_refs=source_refs,
            metadata={
                "source_id": extracted.manifest.source_id,
                "page_type": page_type,
            },
        )

    def _derive_course_identity(
        self,
        course_root: Path,
        *,
        term: str | None,
        module_code: str | None,
    ) -> tuple[str, str]:
        relative = course_root.relative_to(self.settings.raw_dir.resolve())
        parts = relative.parts
        derived_term = term or (parts[0] if len(parts) >= 1 else "unknown-term")
        derived_module = module_code or (parts[1] if len(parts) >= 2 else course_root.name)
        return derived_term, derived_module

    def _build_course_source_manifest(
        self,
        *,
        course_root: Path,
        module_id: str,
        batch_id: str,
        term: str,
        module_code: str,
        discovered: DiscoveredFile,
    ) -> SourceManifest:
        relative_path = discovered.path.relative_to(self.settings.root_dir)
        module_relpath = discovered.relative_path.as_posix()
        base_slug = slugify(f"{module_code}-{module_relpath}")
        timestamp = utc_now()
        return SourceManifest(
            source_id=base_slug,
            title=self._title_from_relpath(discovered.relative_path),
            kind=discovered.kind,
            origin="course_ingest",
            scope=f"course/{term}/{module_code}",
            file_path=relative_path.as_posix(),
            checksum=sha256_path(discovered.path),
            ingest_status="registered",
            created_at=timestamp,
            updated_at=timestamp,
            module_id=module_id,
            batch_id=batch_id,
            module_relpath=module_relpath,
            content_class=discovered.content_class,
            extractor_metadata={"kind": discovered.kind},
            metadata={"module_code": module_code, "term": term},
        )

    def _latest_evidence_artifacts_by_source_id(self, module_id: str) -> dict[str, EvidenceArtifact]:
        latest: dict[str, EvidenceArtifact] = {}
        for artifact in list_evidence_artifacts(self.settings, module_id=module_id):
            current = latest.get(artifact.source_id)
            if current is None or artifact.updated_at > current.updated_at:
                latest[artifact.source_id] = artifact
        return latest

    def _reuse_course_source_result(
        self,
        *,
        index: int,
        source_manifest: SourceManifest,
        previous_manifest: SourceManifest | None,
        previous_artifact: EvidenceArtifact | None,
    ) -> _CourseExtractionResult | None:
        if not self._can_reuse_course_evidence(source_manifest, previous_manifest, previous_artifact):
            return None
        artifact = self._clone_evidence_artifact_for_batch(
            previous_artifact,
            source_manifest=source_manifest,
        )
        source_manifest.extractor_metadata["provider_file_input"] = bool(
            previous_manifest.extractor_metadata.get("provider_file_input")
        )
        source_manifest.extractor_metadata["reuse_signature"] = self._evidence_reuse_signature(
            source_manifest,
            provider_file_input=bool(source_manifest.extractor_metadata.get("provider_file_input")),
        )
        source_manifest.extractor_metadata["reused_from_evidence_id"] = previous_artifact.evidence_id
        source_manifest.extractor_metadata["reused_from_batch_id"] = previous_artifact.batch_id
        source_manifest.metadata["reused_from_batch_id"] = previous_artifact.batch_id
        return _CourseExtractionResult(
            index=index,
            source_manifest=source_manifest,
            artifact=artifact,
            reused=True,
            reused_from_evidence_id=previous_artifact.evidence_id,
        )

    def _reuse_failed_course_source_result(
        self,
        *,
        index: int,
        source_manifest: SourceManifest,
        previous_manifest: SourceManifest | None,
    ) -> _CourseExtractionResult | None:
        if previous_manifest is None:
            return None
        if previous_manifest.extract_status != "failed":
            return None
        if previous_manifest.source_id != source_manifest.source_id:
            return None
        if previous_manifest.file_path != source_manifest.file_path:
            return None
        if previous_manifest.kind != source_manifest.kind:
            return None
        if previous_manifest.checksum != source_manifest.checksum:
            return None
        if not self._is_sticky_course_extraction_failure(previous_manifest.skip_reason):
            return None
        source_manifest.extractor_metadata = dict(previous_manifest.extractor_metadata)
        source_manifest.metadata["reused_failed_extraction"] = True
        source_manifest.metadata["reused_from_failure_reason"] = previous_manifest.skip_reason
        return _CourseExtractionResult(
            index=index,
            source_manifest=source_manifest,
            reused_failure=True,
            error=previous_manifest.skip_reason,
        )

    def _can_reuse_course_evidence(
        self,
        source_manifest: SourceManifest,
        previous_manifest: SourceManifest | None,
        previous_artifact: EvidenceArtifact | None,
    ) -> bool:
        if previous_manifest is None or previous_artifact is None:
            return False
        if previous_manifest.extract_status != "extracted":
            return False
        if previous_manifest.source_id != source_manifest.source_id:
            return False
        if previous_manifest.file_path != source_manifest.file_path:
            return False
        if previous_manifest.kind != source_manifest.kind:
            return False
        if previous_manifest.checksum != source_manifest.checksum:
            return False
        if previous_artifact.source_id != source_manifest.source_id:
            return False
        if previous_artifact.source_path != source_manifest.file_path:
            return False
        previous_signature = str(
            previous_manifest.extractor_metadata.get("reuse_signature")
            or previous_artifact.metadata.get("reuse_signature")
            or ""
        ).strip()
        if not previous_signature:
            return True
        expected_signature = self._evidence_reuse_signature(
            source_manifest,
            provider_file_input=bool(previous_manifest.extractor_metadata.get("provider_file_input")),
        )
        return previous_signature == expected_signature

    def _is_sticky_course_extraction_failure(self, message: str) -> bool:
        normalized = message.lower()
        return any(
            token in normalized
            for token in (
                "no extractable text found",
                "unsupported mime type",
                "file_above_max_size",
                "file urls cannot be larger than 32mb",
                "request contains an invalid argument",
            )
        )

    def _clone_evidence_artifact_for_batch(
        self,
        artifact: EvidenceArtifact,
        *,
        source_manifest: SourceManifest,
    ) -> EvidenceArtifact:
        metadata = dict(artifact.metadata)
        metadata["source_checksum"] = source_manifest.checksum
        metadata["reuse_signature"] = self._evidence_reuse_signature(
            source_manifest,
            provider_file_input=bool(source_manifest.extractor_metadata.get("provider_file_input")),
        )
        metadata["reused_from_evidence_id"] = artifact.evidence_id
        metadata["reused_from_batch_id"] = artifact.batch_id
        return EvidenceArtifact(
            evidence_id=f"{source_manifest.batch_id}--{source_manifest.source_id}",
            source_id=source_manifest.source_id,
            module_id=source_manifest.module_id,
            batch_id=source_manifest.batch_id,
            source_path=source_manifest.file_path,
            source_refs=list(artifact.source_refs),
            summary=artifact.summary,
            key_topics=list(artifact.key_topics),
            content_class=artifact.content_class,
            extractor=artifact.extractor,
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata=metadata,
        )

    def _build_evidence_artifact(
        self,
        extracted: ExtractedSource,
        *,
        module_id: str,
        batch_id: str,
    ) -> EvidenceArtifact:
        self._progress(f"Summarizing evidence for {extracted.title}.")
        summary = self._build_summary(extracted, evidence_mode=True)
        source_refs = [build_source_ref(extracted.manifest.source_id, section.section_id) for section in extracted.sections]
        reuse_signature = self._evidence_reuse_signature(
            extracted.manifest,
            provider_file_input=bool(extracted.manifest.extractor_metadata.get("provider_file_input")),
        )
        return EvidenceArtifact(
            evidence_id=f"{batch_id}--{extracted.manifest.source_id}",
            source_id=extracted.manifest.source_id,
            module_id=module_id,
            batch_id=batch_id,
            source_path=extracted.manifest.file_path,
            source_refs=source_refs,
            summary=summary,
            key_topics=top_terms(extracted.text, limit=8),
            content_class=extracted.manifest.content_class or extracted.manifest.kind,
            extractor=extracted.manifest.kind,
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={
                "title": extracted.title,
                "module_relpath": extracted.manifest.module_relpath,
                "snippet": compact_text(extracted.text, limit=500),
                "source_checksum": extracted.manifest.checksum,
                "reuse_signature": reuse_signature,
            },
        )

    def _build_layout_review(
        self,
        *,
        module_manifest: ModuleManifest,
        evidence_artifacts: list[EvidenceArtifact],
        nearby_pages,
        feedback: str | None = None,
        previous_layout: LayoutReview | None = None,
    ) -> LayoutReview:
        all_source_refs = sorted({ref for artifact in evidence_artifacts for ref in artifact.source_refs})
        source_ref_aliases = self._source_ref_aliases(evidence_artifacts)
        lecture_strategy = self._lecture_layout_strategy(evidence_artifacts)
        deterministic_pages = self._deterministic_layout_pages(
            module_manifest,
            all_source_refs,
            lecture_pages=lecture_strategy["pages"],
        )
        known_source_refs = set(all_source_refs)
        nearby_page_ids = {entry.page_id for entry in nearby_pages}
        corrective_feedback = feedback
        prior_attempt = previous_layout
        last_error: ValueError | None = None

        for _attempt in range(3):
            try:
                pages: list[LayoutPagePlan] = list(deterministic_pages)
                provider_pages = self._provider_layout_pages(
                    module_manifest,
                    evidence_artifacts,
                    nearby_pages,
                    source_ref_aliases=source_ref_aliases,
                    feedback=corrective_feedback,
                    previous_layout=prior_attempt,
                    lecture_strategy=lecture_strategy,
                )
                provider_pages = self._filter_provider_layout_pages(
                    provider_pages,
                    lecture_strategy=lecture_strategy,
                )
                reserved_slugs = {page.slug for page in deterministic_pages}
                pages.extend(page for page in provider_pages if page.slug not in reserved_slugs)
                validated_pages = self._validate_layout_pages(
                    module_manifest=module_manifest,
                    pages=pages,
                    known_source_refs=known_source_refs,
                    nearby_page_ids=nearby_page_ids,
                )
                break
            except ValueError as exc:
                if not self.provider:
                    raise
                last_error = exc
                corrective_feedback = (
                    f"{feedback}\n\nPrevious layout was invalid: {exc}"
                    if feedback
                    else f"Previous layout was invalid: {exc}"
                )
                prior_attempt = LayoutReview(
                    layout_id=f"layout-{module_manifest.batch_id}",
                    module_id=module_manifest.module_id,
                    batch_id=module_manifest.batch_id,
                    approval_state="pending",
                    pages=pages,
                    created_at=utc_now(),
                    updated_at=utc_now(),
                    metadata={},
                )
        else:
            raise last_error or ValueError("Layout planner failed to produce a valid layout.")

        return LayoutReview(
            layout_id=f"layout-{module_manifest.batch_id}",
            module_id=module_manifest.module_id,
            batch_id=module_manifest.batch_id,
            approval_state="pending",
            pages=validated_pages,
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={
                "module_code": module_manifest.module_code,
                "term": module_manifest.term,
                "layout_strategy": lecture_strategy["strategy"],
                "lecture_pages": [
                    {"slug": page.slug, "title": page.title}
                    for page in lecture_strategy["pages"]
                ],
                "nearby_pages": [
                    {
                        "page_id": entry.page_id,
                        "title": entry.title,
                        "summary": entry.summary,
                    }
                    for entry in nearby_pages[:10]
                ],
            },
        )

    def _deterministic_layout_pages(
        self,
        module_manifest: ModuleManifest,
        all_source_refs: list[str],
        *,
        lecture_pages: list[LayoutPagePlan],
    ) -> list[LayoutPagePlan]:
        hub_path = build_course_page_path(
            self.settings.root_dir,
            term=module_manifest.term,
            module_code=module_manifest.module_code,
            page_kind="hub",
        )
        pages = [
            LayoutPagePlan(
                title=module_manifest.module_code,
                slug="hub",
                page_kind="hub",
                target_path=relative_posix(hub_path, self.settings.root_dir),
                summary=f"Course hub for {module_manifest.module_code} in {module_manifest.term}.",
                parent_slug="",
                related_page_ids=[],
                assigned_source_refs=all_source_refs,
                rationale="Mandatory course hub page.",
            ),
        ]
        for page in lecture_pages:
            normalized_path = build_course_page_path(
                self.settings.root_dir,
                term=module_manifest.term,
                module_code=module_manifest.module_code,
                page_kind="topic",
                slug=page.slug,
            )
            page.target_path = relative_posix(normalized_path, self.settings.root_dir)
        pages.extend(lecture_pages)
        return pages

    def _lecture_layout_strategy(self, evidence_artifacts: list[EvidenceArtifact]) -> dict[str, object]:
        grouped: dict[int, list[EvidenceArtifact]] = {}
        for artifact in evidence_artifacts:
            lecture_number = self._lecture_number_for_artifact(artifact)
            if lecture_number is None:
                continue
            grouped.setdefault(lecture_number, []).append(artifact)

        if len(grouped) < 3:
            return {"strategy": "generic", "pages": []}

        pages: list[LayoutPagePlan] = []
        for lecture_number in sorted(grouped):
            artifacts = grouped[lecture_number]
            lead_artifact = self._lead_lecture_artifact(artifacts)
            lecture_title = self._lecture_page_title(lecture_number, lead_artifact)
            pages.append(
                LayoutPagePlan(
                    title=lecture_title,
                    slug=f"lecture-{lecture_number:02d}",
                    page_kind="topic",
                    target_path="",
                    summary=compact_text(
                        f"{lecture_title} consolidates the numbered lecture materials for this module. "
                        f"{lead_artifact.summary}",
                        limit=220,
                    ),
                    parent_slug="hub",
                    related_page_ids=[],
                    assigned_source_refs=self._lecture_page_source_refs(artifacts),
                    rationale=(
                        "Deterministic lecture page created from numbered lecture materials so the course "
                        "layout stays flat and easy to review."
                    ),
                )
            )
        return {"strategy": "lecture-flat", "pages": pages}

    def _lecture_number_for_artifact(self, artifact: EvidenceArtifact) -> int | None:
        relpath = str(artifact.metadata.get("module_relpath", ""))
        title = str(artifact.metadata.get("title", artifact.source_id))
        in_lecture_dir = any(segment.lower() in {"lecture", "lectures"} for segment in Path(relpath).parts)
        if not in_lecture_dir and "lecture" not in title.lower():
            return None
        match = re.search(
            r"\b(?:lecture|lec|l|week|wk)\s*[-_ ]*0*(\d{1,2})\b",
            f"{title} {relpath}",
            flags=re.IGNORECASE,
        )
        if not match:
            return None
        return int(match.group(1))

    def _lead_lecture_artifact(self, artifacts: list[EvidenceArtifact]) -> EvidenceArtifact:
        return min(
            artifacts,
            key=lambda artifact: (
                0 if "slide" in str(artifact.metadata.get("title", "")).lower() else 1,
                1 if "supplement" in str(artifact.metadata.get("title", "")).lower() else 0,
                len(str(artifact.metadata.get("title", ""))),
            ),
        )

    def _lecture_page_title(self, lecture_number: int, artifact: EvidenceArtifact) -> str:
        title = str(artifact.metadata.get("title", artifact.source_id))
        cleaned = re.sub(
            r"(?i)^.*?\b(?:lecture|lec|l|week|wk)\s*[-_ ]*0*\d+\b",
            "",
            title,
        ).strip(" -_:")
        cleaned = re.sub(
            r"(?i)^(?:slides?|slide deck|notes?|post lecture supplement|supplement)\s*[-_:]*\s*",
            "",
            cleaned,
        ).strip(" -_:")
        if cleaned:
            return f"Lecture {lecture_number:02d}: {cleaned}"
        return f"Lecture {lecture_number:02d}"

    def _lecture_page_source_refs(self, artifacts: list[EvidenceArtifact]) -> list[str]:
        refs: list[str] = []
        seen: set[str] = set()
        for artifact in artifacts:
            for ref in artifact.source_refs[:3]:
                if ref not in seen:
                    seen.add(ref)
                    refs.append(ref)
            if len(refs) >= 8:
                break
        return refs

    def _provider_layout_pages(
        self,
        module_manifest: ModuleManifest,
        evidence_artifacts: list[EvidenceArtifact],
        nearby_pages,
        *,
        source_ref_aliases: dict[str, str],
        feedback: str | None = None,
        previous_layout: LayoutReview | None = None,
        lecture_strategy: dict[str, object] | None = None,
    ) -> list[LayoutPagePlan]:
        if not self.provider:
            return []
        self._progress(
            f"Requesting an LLM layout plan for {module_manifest.module_code} from "
            f"{len(evidence_artifacts)} evidence artifact(s)."
        )
        module_root = (
            Path("wiki")
            / "courses"
            / slugify(module_manifest.term)
            / slugify(module_manifest.module_code)
        ).as_posix()
        evidence_lines = []
        for artifact in evidence_artifacts:
            evidence_lines.append(
                f"- {artifact.source_id} :: {artifact.metadata.get('title', artifact.source_id)} :: "
                f"{artifact.content_class} :: refs={', '.join(artifact.source_refs[:5])} :: "
                f"topics={', '.join(artifact.key_topics[:6])} :: summary={artifact.summary}"
            )
        nearby_lines = [
            f"- {entry.page_id} :: {entry.title} :: {entry.summary}"
            for entry in nearby_pages[:10]
        ]
        revision_lines: list[str] = []
        if previous_layout:
            revision_lines.extend(["", "Existing layout pages:"])
            revision_lines.extend(
                f"- {page.slug} :: {page.title} :: {page.page_kind} :: parent={page.parent_slug or 'none'}"
                for page in previous_layout.pages
            )
        if feedback:
            revision_lines.extend(["", "Reviewer feedback:", feedback])
        lecture_strategy = lecture_strategy or {"strategy": "generic", "pages": []}
        lecture_lines: list[str] = []
        lecture_pages = lecture_strategy.get("pages", [])
        if lecture_strategy.get("strategy") == "lecture-flat" and lecture_pages:
            lecture_lines.extend(
                [
                    "",
                    "Lecture-first layout guidance:",
                    "This module has numbered lecture materials. The primary organizing principle must be the official lecture notes/slides.",
                    "Prefer a flat hierarchy under `hub` with one topic page per lecture.",
                    "Do not create deeper lecture subtrees or duplicate the recommended lecture pages below.",
                    "Do not create topic pages such as exam preparation, final exam preparation, midterm preparation, mock exams, past papers, revision, or study guides.",
                    "Assessment material, cheatsheets, tutorial files, schedules, announcements, and mock exams are supporting evidence for lecture pages, not separate pages by default.",
                    "Prefer zero additional topic pages unless they correspond to an official lecture/unit from the source material.",
                    "",
                    "Recommended lecture pages (already planned deterministically):",
                ]
            )
            lecture_lines.extend(
                f"- {page.slug} :: {page.title}"
                for page in lecture_pages
            )
        prompt = "\n".join(
            [
                "LAYOUT_PLAN_REQUEST",
                "Return JSON only.",
                "Provide only additional course child pages. Do not include the mandatory hub page.",
                "Schema: {\"pages\": [{\"title\": str, \"slug\": str, \"page_kind\": \"topic\", "
                "\"target_path\": str, \"summary\": str, \"parent_slug\": str, "
                "\"related_page_ids\": [str], \"assigned_source_refs\": [str], \"rationale\": str}]}",
                f"Course term: {module_manifest.term}",
                f"Course module: {module_manifest.module_code}",
                f"Course module root: {module_root}",
                f"Topic page paths must be exactly `{module_root}/topics/<slug>.md`.",
                "Use parent_slug to build hierarchy inside the course tree. parent_slug must be `hub` or another slug from this response, never `None` or `null`.",
                "Use related_page_ids only for already-published nearby page_ids listed below. If none apply, return `[]`.",
                "assigned_source_refs must use exact refs from the evidence list, including the `#section-N` suffix. Do not return bare source ids or invented refs.",
                "Prefer links inside the course subtree, but you may reference nearby existing page_ids when justified.",
                *lecture_lines,
                "",
                "Evidence artifacts:",
                *evidence_lines,
                "",
                "Nearby existing pages:",
                *(nearby_lines or ["- none"]),
                *revision_lines,
            ]
        )
        result = self.provider.generate(prompt, system_prompt="You design a compact, reviewable wiki tree for a university course module.")
        self._record_generation_usage(
            "layout_planning",
            result,
            label=module_manifest.module_id,
            extra={"page_count_hint": len(lecture_pages)},
        )
        payload = extract_json_object(result.text)
        pages_payload = payload.get("pages", [])
        if not isinstance(pages_payload, list):
            raise ValueError("Layout planner must return a `pages` list.")
        return [
            self._normalize_provider_layout_page(
                module_manifest,
                LayoutPagePlan.from_dict(item),
                source_ref_aliases=source_ref_aliases,
                evidence_artifacts=evidence_artifacts,
                nearby_page_ids={entry.page_id for entry in nearby_pages},
            )
            for item in pages_payload
        ]

    def _filter_provider_layout_pages(
        self,
        pages: list[LayoutPagePlan],
        *,
        lecture_strategy: dict[str, object],
    ) -> list[LayoutPagePlan]:
        filtered: list[LayoutPagePlan] = []
        for page in pages:
            if page.page_kind == "artifact":
                continue
            label = " ".join([page.slug, page.title, page.summary, page.rationale]).lower()
            if lecture_strategy.get("strategy") == "lecture-flat" and page.page_kind == "topic" and any(
                token in label
                for token in (
                    "exam preparation",
                    "final exam",
                    "midterm",
                    "mock exam",
                    "mock final",
                    "past paper",
                    "revision",
                    "study guide",
                    "practice exam",
                )
            ):
                continue
            if page.page_kind == "topic":
                page.parent_slug = "hub"
            filtered.append(page)
        return filtered

    def _normalize_provider_layout_page(
        self,
        module_manifest: ModuleManifest,
        page: LayoutPagePlan,
        *,
        source_ref_aliases: dict[str, str],
        evidence_artifacts: list[EvidenceArtifact],
        nearby_page_ids: set[str],
    ) -> LayoutPagePlan:
        if page.page_kind in {"hub", "inventory", "topic", "artifact"}:
            normalized_path = build_course_page_path(
                self.settings.root_dir,
                term=module_manifest.term,
                module_code=module_manifest.module_code,
                page_kind=page.page_kind,
                slug=page.slug if page.page_kind in {"topic", "artifact"} else None,
            )
            page.target_path = relative_posix(normalized_path, self.settings.root_dir)
        parent_slug = str(page.parent_slug).strip()
        if parent_slug.lower() in {"", "none", "null"}:
            parent_slug = ""
        page.parent_slug = parent_slug
        if page.page_kind in {"topic", "artifact"} and not page.parent_slug:
            page.parent_slug = "hub"
        page.related_page_ids = [
            page_id
            for page_id in (str(item).strip() for item in page.related_page_ids)
            if page_id and page_id.lower() not in {"none", "null"} and page_id in nearby_page_ids
        ]
        normalized_refs: list[str] = []
        seen_refs: set[str] = set()
        for ref in page.assigned_source_refs:
            candidate = str(ref).strip()
            if not candidate:
                continue
            if candidate.startswith("[source:") and candidate.endswith("]"):
                candidate = candidate[8:-1].strip()
            normalized = source_ref_aliases.get(
                candidate,
                source_ref_aliases.get(self._canonical_source_ref_key(candidate), candidate),
            )
            if normalized not in seen_refs:
                seen_refs.add(normalized)
                normalized_refs.append(normalized)
        if not normalized_refs and page.page_kind in {"topic", "artifact"}:
            normalized_refs = self._fallback_layout_page_source_refs(page, evidence_artifacts)
        if normalized_refs:
            page.assigned_source_refs = normalized_refs
        return page

    def _fallback_layout_page_source_refs(
        self,
        page: LayoutPagePlan,
        evidence_artifacts: list[EvidenceArtifact],
    ) -> list[str]:
        token_source = " ".join(
            [
                page.title,
                page.summary,
                page.slug.replace("-", " "),
                page.rationale,
            ]
        )
        query_tokens = {
            token
            for token in slugify(token_source).split("-")
            if len(token) > 2 and token not in {"topic", "artifact", "page", "course", "module"}
        }
        scored: list[tuple[int, EvidenceArtifact]] = []
        for artifact in evidence_artifacts:
            artifact_tokens = {
                token
                for token in slugify(
                    " ".join(
                        [
                            artifact.source_id,
                            artifact.metadata.get("title", ""),
                            artifact.summary,
                            " ".join(artifact.key_topics),
                            artifact.metadata.get("module_relpath", ""),
                        ]
                    )
                ).split("-")
                if token
            }
            score = len(query_tokens & artifact_tokens)
            if score > 0:
                scored.append((score, artifact))
        selected_artifacts = [
            artifact
            for _, artifact in sorted(
                scored,
                key=lambda item: (-item[0], item[1].source_id),
            )[:4]
        ]
        if not selected_artifacts:
            selected_artifacts = sorted(evidence_artifacts, key=lambda artifact: artifact.source_id)[:3]
        refs: list[str] = []
        seen_refs: set[str] = set()
        for artifact in selected_artifacts:
            for ref in artifact.source_refs[:2]:
                if ref not in seen_refs:
                    seen_refs.add(ref)
                    refs.append(ref)
            if len(refs) >= 6:
                break
        return refs

    def _source_ref_aliases(self, evidence_artifacts: list[EvidenceArtifact]) -> dict[str, str]:
        aliases: dict[str, str] = {}
        for artifact in evidence_artifacts:
            if not artifact.source_refs:
                continue
            primary_ref = artifact.source_refs[0]
            aliases[artifact.source_id] = primary_ref
            aliases[f"[source:{artifact.source_id}]"] = primary_ref
            aliases[artifact.evidence_id] = primary_ref
            aliases[self._canonical_source_ref_key(artifact.source_id)] = primary_ref
            aliases[self._canonical_source_ref_key(artifact.evidence_id)] = primary_ref
            for ref in artifact.source_refs:
                aliases[ref] = ref
                aliases[f"[source:{ref}]"] = ref
                aliases[self._canonical_source_ref_key(ref)] = ref
        return aliases

    def _canonical_source_ref_key(self, value: str) -> str:
        return re.sub(r"[^a-z0-9]+", "", value.strip().lower())

    def _validate_layout_pages(
        self,
        *,
        module_manifest: ModuleManifest,
        pages: list[LayoutPagePlan],
        known_source_refs: set[str],
        nearby_page_ids: set[str],
    ) -> list[LayoutPagePlan]:
        module_root = (
            Path("wiki")
            / "courses"
            / slugify(module_manifest.term)
            / slugify(module_manifest.module_code)
        ).as_posix()
        slugs: set[str] = set()
        for page in pages:
            page.validate()
            if page.slug in slugs:
                raise ValueError(f"Duplicate layout page slug: {page.slug}")
            slugs.add(page.slug)
            if not page.target_path.startswith(module_root):
                raise ValueError(f"Layout page path escapes module subtree: {page.target_path}")
            if page.page_kind == "hub" and not page.target_path.endswith("/index.md"):
                raise ValueError("Hub page must target index.md inside the module root.")
            if page.page_kind == "inventory" and not page.target_path.endswith("/inventory.md"):
                raise ValueError("Inventory page must target inventory.md inside the module root.")
            if page.page_kind == "topic" and "/topics/" not in page.target_path:
                raise ValueError("Topic pages must live under topics/.")
            if page.page_kind == "artifact" and "/artifacts/" not in page.target_path:
                raise ValueError("Artifact pages must live under artifacts/.")
            if not page.assigned_source_refs:
                raise ValueError(f"Layout page `{page.slug}` must reference at least one source ref.")
            unknown_refs = [ref for ref in page.assigned_source_refs if ref not in known_source_refs]
            if unknown_refs:
                raise ValueError(f"Layout page `{page.slug}` referenced unknown source refs: {', '.join(unknown_refs)}")
            unknown_related = [ref for ref in page.related_page_ids if ref not in nearby_page_ids]
            if unknown_related:
                raise ValueError(f"Layout page `{page.slug}` referenced unknown related page_ids: {', '.join(unknown_related)}")

        for page in pages:
            if page.parent_slug and page.parent_slug not in slugs:
                raise ValueError(f"Layout page `{page.slug}` references unknown parent slug `{page.parent_slug}`.")
        return pages

    def _draft_course_pages(
        self,
        *,
        module_manifest: ModuleManifest,
        layout_review: LayoutReview,
        evidence_artifacts: list[EvidenceArtifact],
        nearby_pages,
        feedback_by_slug: dict[str, str] | None = None,
        existing_drafts: dict[str, DraftProposal] | None = None,
    ) -> list[DraftProposal]:
        artifacts_by_ref = self._evidence_by_source_ref(evidence_artifacts)
        all_page_ids = {page.slug: self._module_page_id(module_manifest.module_id, page.slug) for page in layout_review.pages}
        proposals: list[DraftProposal] = []
        feedback_by_slug = feedback_by_slug or {}
        existing_drafts = existing_drafts or {}
        total_pages = len(layout_review.pages)
        worker_count = self._worker_count(total_pages)
        results = self._run_in_parallel(
            [
                lambda index=index, plan=plan: self._draft_course_page_result(
                    index=index,
                    module_manifest=module_manifest,
                    layout_review=layout_review,
                    evidence_artifacts=evidence_artifacts,
                    artifacts_by_ref=artifacts_by_ref,
                    nearby_pages=nearby_pages,
                    all_page_ids=all_page_ids,
                    feedback=feedback_by_slug.get(plan.slug),
                    existing_draft=existing_drafts.get(plan.slug),
                    plan=plan,
                )
                for index, plan in enumerate(layout_review.pages, start=1)
            ],
            max_workers=worker_count,
        )
        for result in results:
            proposals.append(result.proposal)
        return proposals

    def _draft_page_body(
        self,
        *,
        module_manifest: ModuleManifest,
        plan: LayoutPagePlan,
        evidence_artifacts: list[EvidenceArtifact],
        artifacts_by_ref: dict[str, EvidenceArtifact],
        nearby_pages,
        all_plans: list[LayoutPagePlan],
        feedback: str | None = None,
        existing_markdown: str | None = None,
    ) -> str:
        if plan.page_kind == "inventory":
            return self._render_inventory_body(module_manifest, evidence_artifacts)

        assigned_artifacts = self._artifacts_for_plan(plan, evidence_artifacts, artifacts_by_ref)
        if self.provider:
            prompt = "\n".join(
                [
                    "DRAFT_PAGE_REQUEST",
                    "Return markdown only. Do not include YAML frontmatter.",
                    f"Course term: {module_manifest.term}",
                    f"Course module: {module_manifest.module_code}",
                    f"Page title: {plan.title}",
                    f"Page kind: {plan.page_kind}",
                    f"Page summary: {plan.summary}",
                    f"Parent slug: {plan.parent_slug or 'none'}",
                    "Planned sibling pages:",
                    *[f"- {item.slug}: {item.title} ({item.page_kind})" for item in all_plans if item.slug != plan.slug],
                    "",
                    "Assigned evidence:",
                    *[
                        f"- {artifact.metadata.get('title', artifact.source_id)} :: refs={', '.join(artifact.source_refs[:5])} :: "
                        f"summary={artifact.summary} :: topics={', '.join(artifact.key_topics[:6])} :: "
                        f"snippet={artifact.metadata.get('snippet', '')}"
                        for artifact in assigned_artifacts
                    ],
                    "",
                    "Nearby published pages:",
                    *[
                        f"- {entry.page_id}: {entry.title} :: {entry.summary}"
                        for entry in nearby_pages[:8]
                    ],
                    "",
                    *(["Current draft markdown:", existing_markdown or "", ""] if existing_markdown else []),
                    *(["Reviewer feedback:", feedback or "", ""] if feedback else []),
                    "Use stable [source:...] citations exactly as provided when making factual claims.",
                    "Prefer cross-links inside the current course structure first.",
                    "If reviewer feedback is provided, revise the page accordingly while staying faithful to the evidence.",
                ]
            )
            direct_file_paths = self._draft_page_file_inputs(plan, assigned_artifacts)
            try:
                if direct_file_paths:
                    file_prompt = "\n".join(
                        [
                            prompt,
                            "",
                            "Uploaded source files:",
                            *[
                                f"- {artifact.metadata.get('title', artifact.source_id)} :: "
                                f"path={artifact.metadata.get('module_relpath', artifact.source_path)} :: "
                                f"refs={', '.join(artifact.source_refs[:8])}"
                                for artifact in assigned_artifacts
                            ],
                            "",
                            "Use the uploaded source files as the primary source of truth for depth and detail.",
                            "Use the evidence metadata above to preserve exact [source:...] citations.",
                            "For lecture/topic pages, follow the lecture order used in the attached materials instead of inventing a new structure.",
                            "Aim for exhaustive concept coverage across the attached files: include important definitions, subtopics, distinctions, examples, and recurring frameworks when they are supported by the files.",
                            "Synthesize the attached files section by section into one coherent page. Do not write separate mini-summaries for each file.",
                            "When multiple attached files cover the same topic, merge them into a single integrated explanation and note clarifications or extensions naturally.",
                            "Prefer a structure like: overview, lecture sections in teaching order, key examples, and takeaways, unless the attached files clearly suggest a better lecture-ordered structure.",
                        ]
                    )
                    result = self.provider.generate_with_files(
                        file_prompt,
                        files=direct_file_paths,
                        system_prompt=(
                            "You draft detailed, interlinked wiki pages from uploaded course source files. "
                            "Use the attached files for substance and the provided [source:...] refs for citations. "
                            "Preserve the lecture's teaching order, cover concepts thoroughly, and synthesize overlapping sections across files into one coherent set of notes."
                        ),
                    )
                    self._record_generation_usage(
                        "page_drafting",
                        result,
                        label=plan.slug,
                        extra={"file_count": len(direct_file_paths), "page_kind": plan.page_kind},
                    )
                else:
                    result = self.provider.generate(
                        prompt,
                        system_prompt="You draft concise, interlinked wiki pages from course evidence.",
                    )
                    self._record_generation_usage(
                        "page_drafting",
                        result,
                        label=plan.slug,
                        extra={"file_count": 0, "page_kind": plan.page_kind},
                    )
                if result.text.strip():
                    return self._normalize_page_body(plan.title, result.text)
            except Exception:
                pass

        return self._fallback_page_body(plan, assigned_artifacts)

    def _draft_page_file_inputs(
        self,
        plan: LayoutPagePlan,
        artifacts: list[EvidenceArtifact],
    ) -> list[Path]:
        if not self.provider or not getattr(self.provider, "supports_file_inputs", False):
            return []
        if plan.page_kind != "topic":
            return []

        files: list[Path] = []
        seen: set[Path] = set()
        for artifact in artifacts:
            if artifact.extractor not in FILE_INPUT_SOURCE_KINDS:
                continue
            path = self.settings.root_dir / artifact.source_path
            if not path.exists():
                continue
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            files.append(resolved)
        return files

    def _nearby_existing_pages(self, module_id: str, term: str, evidence_artifacts: list[EvidenceArtifact]):
        catalog = build_catalog(self.settings)
        course_prefix = f"wiki/courses/{slugify(term)}/"
        topic_tokens = {slugify(term), slugify(module_id)}
        for artifact in evidence_artifacts:
            topic_tokens.update(artifact.key_topics[:4])
        scored = []
        for entry in catalog:
            score = 0
            if entry.path.startswith(course_prefix):
                score += 2
            score += sum(1 for token in topic_tokens if token and token in entry.text.lower())
            if score > 0:
                scored.append((score, entry))
        return [entry for _, entry in sorted(scored, key=lambda item: item[0], reverse=True)[:12]]

    def _evidence_by_source_ref(self, artifacts: list[EvidenceArtifact]) -> dict[str, EvidenceArtifact]:
        mapping: dict[str, EvidenceArtifact] = {}
        for artifact in artifacts:
            for ref in artifact.source_refs:
                mapping[ref] = artifact
        return mapping

    def _artifacts_for_plan(
        self,
        plan: LayoutPagePlan,
        evidence_artifacts: list[EvidenceArtifact],
        artifacts_by_ref: dict[str, EvidenceArtifact],
    ) -> list[EvidenceArtifact]:
        seen: set[str] = set()
        selected: list[EvidenceArtifact] = []
        for ref in plan.assigned_source_refs:
            artifact = artifacts_by_ref.get(ref)
            if artifact and artifact.evidence_id not in seen:
                seen.add(artifact.evidence_id)
                selected.append(artifact)
        if selected:
            return selected
        return evidence_artifacts

    def _render_inventory_body(self, module_manifest: ModuleManifest, evidence_artifacts: list[EvidenceArtifact]) -> str:
        metadata = module_manifest.metadata
        skipped_files = metadata.get("skipped_files", [])
        lines = [
            f"# {module_manifest.module_code} Inventory",
            "",
            "## Batch",
            "",
            f"- Term: `{module_manifest.term}`",
            f"- Module: `{module_manifest.module_code}`",
            f"- Batch: `{module_manifest.batch_id}`",
            "",
            "## Usable Files",
            "",
        ]
        for artifact in evidence_artifacts:
            refs = ", ".join(f"[source:{ref}]" for ref in artifact.source_refs[:3])
            lines.append(
                f"- `{artifact.metadata.get('module_relpath', artifact.source_path)}`: {artifact.summary} ({refs})"
            )
        lines.extend(["", "## Skipped Files", ""])
        if skipped_files:
            for skipped in skipped_files:
                lines.append(f"- `{skipped['path']}`: {skipped['reason']}")
        else:
            lines.append("- None")
        return "\n".join(lines)

    def _fallback_page_body(self, plan: LayoutPagePlan, artifacts: list[EvidenceArtifact]) -> str:
        lines = [f"# {plan.title}", "", "## Overview", "", plan.summary]
        if plan.parent_slug:
            lines.extend(["", "## Context", "", f"Parent page slug: `{plan.parent_slug}`"])
        lines.extend(["", "## Evidence", ""])
        for artifact in artifacts[:8]:
            citation = f"[source:{artifact.source_refs[0]}]" if artifact.source_refs else ""
            lines.append(
                f"- `{artifact.metadata.get('title', artifact.source_id)}`: {artifact.summary} {citation}".rstrip()
            )
        return "\n".join(lines)

    def _build_summary(self, extracted: ExtractedSource, *, evidence_mode: bool = False) -> str:
        fallback = _first_sentences(extracted.text, limit=2)
        if not self.provider:
            return compact_text(fallback, limit=220)
        prompt = (
            "SOURCE_SUMMARY_REQUEST\n"
            "Summarize the following source for a course wiki evidence artifact. "
            "Keep it concise and factual.\n\n"
            f"Title: {extracted.title}\n"
            f"Kind: {extracted.manifest.kind}\n"
            f"Content:\n{compact_text(extracted.text, limit=2000)}"
        )
        try:
            result = self.provider.generate(prompt, system_prompt="You compile concise evidence summaries for a university course wiki.")
            self._record_generation_usage(
                "evidence_summary",
                result,
                label=extracted.manifest.source_id,
                extra={"kind": extracted.manifest.kind},
            )
            return compact_text(result.text or fallback, limit=220 if not evidence_mode else 320)
        except Exception:
            return compact_text(fallback, limit=220 if not evidence_mode else 320)

    def _build_source_body(self, extracted: ExtractedSource, summary: str) -> str:
        lines = [f"# {extracted.title}", "", "## Overview", ""]
        first_ref = render_citation(extracted.manifest.source_id, extracted.sections[0].section_id)
        lines.append(f"{summary} {first_ref}")
        lines.extend(["", "## Source Notes", ""])
        for section in extracted.sections[:6]:
            citation = render_citation(extracted.manifest.source_id, section.section_id)
            lines.append(f"### {section.heading}")
            lines.append("")
            lines.append(f"{compact_text(_collapse_lines(section.text), limit=420)} {citation}")
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    def _build_tags(self, scope: str, kind: str, page_type: str) -> list[str]:
        tags = {kind, page_type}
        tags.update(segment for segment in re.split(r"[/:\s]+", scope) if segment)
        return sorted(tags)

    def _build_course_tags(self, module_manifest: ModuleManifest, page_kind: str) -> list[str]:
        return sorted(
            {
                "course",
                module_manifest.term.lower(),
                module_manifest.module_code.lower(),
                page_kind,
            }
        )

    def _topics_for_course_page(self, plan: LayoutPagePlan, artifacts: list[EvidenceArtifact]) -> list[str]:
        topics: list[str] = []
        seen: set[str] = set()
        for artifact in artifacts:
            for topic in artifact.key_topics:
                normalized = topic.strip()
                if not normalized:
                    continue
                lowered = normalized.lower()
                if lowered in seen:
                    continue
                seen.add(lowered)
                topics.append(normalized)
                if len(topics) >= 10:
                    return topics
        summary_topics = top_terms(plan.summary, limit=4)
        for topic in summary_topics:
            lowered = topic.lower()
            if lowered in seen:
                continue
            seen.add(lowered)
            topics.append(topic)
            if len(topics) >= 10:
                break
        return topics

    def _source_count_from_refs(self, refs: list[str]) -> int:
        return len({ref.split("#", maxsplit=1)[0] for ref in refs})

    def _lecture_number_for_plan(self, plan: LayoutPagePlan) -> int | None:
        return self._lecture_number_from_text(plan.slug) or self._lecture_number_from_text(plan.title)

    def _lecture_number_from_text(self, value: str) -> int | None:
        match = re.search(r"(lecture|week|wk|l)\s*[-_ ]*(\d{1,2})", value, flags=re.IGNORECASE)
        if not match:
            return None
        try:
            return int(match.group(2))
        except ValueError:
            return None

    def _module_page_id(self, module_id: str, slug: str) -> str:
        return slugify(f"{module_id}-{slug}")

    def _title_from_relpath(self, path: Path) -> str:
        stem = path.stem.replace("-", " ").replace("_", " ")
        return stem.title()

    def _normalize_page_body(self, title: str, body: str) -> str:
        stripped = body.strip()
        if stripped.startswith("---"):
            raise ValueError("Page body generator must not return YAML frontmatter.")
        if not stripped.startswith("# "):
            return f"# {title}\n\n{stripped}\n"
        return stripped + "\n"

    def _extract_manifest(self, manifest: SourceManifest) -> ExtractedSource:
        if self._should_use_provider_file_input(manifest):
            try:
                extracted = self._extract_with_provider_file_input(manifest)
            except Exception as exc:
                if self._should_fallback_to_local_adapter(manifest, exc):
                    self._progress(
                        f"Provider extraction could not handle {manifest.file_path}; falling back to local {manifest.kind} extraction."
                    )
                else:
                    raise
            else:
                manifest.extractor_metadata["provider_file_input"] = True
                manifest.extractor_metadata["reuse_signature"] = self._evidence_reuse_signature(
                    manifest,
                    provider_file_input=True,
                )
                return extracted

        adapter = self.registry.for_kind(manifest.kind)
        extracted = adapter.extract(manifest, root_dir=self.settings.root_dir)
        manifest.extractor_metadata["provider_file_input"] = False
        manifest.extractor_metadata["reuse_signature"] = self._evidence_reuse_signature(
            manifest,
            provider_file_input=False,
        )
        return extracted

    def _should_use_provider_file_input(self, manifest: SourceManifest) -> bool:
        return bool(
            self.provider
            and getattr(self.provider, "supports_file_inputs", False)
            and manifest.kind in FILE_INPUT_SOURCE_KINDS
        )

    def _evidence_reuse_signature(self, manifest: SourceManifest, *, provider_file_input: bool) -> str:
        provider_label = self.provider.label if self.provider else "no-provider"
        extraction_mode = "provider_file_input" if provider_file_input else f"local_adapter:{manifest.kind}"
        return "|".join(
            [
                COURSE_EVIDENCE_REUSE_VERSION,
                provider_label,
                extraction_mode,
                manifest.kind,
            ]
        )

    def _should_fallback_to_local_adapter(self, manifest: SourceManifest, exc: Exception) -> bool:
        try:
            self.registry.for_kind(manifest.kind)
        except ValueError:
            return False
        message = str(exc).lower()
        if manifest.kind == "office" and "unsupported mime type" in message:
            return True
        return any(
            token in message
            for token in (
                "invalid_argument",
                "request contains an invalid argument",
                "file_above_max_size",
                "file urls cannot be larger than 32mb",
            )
        )

    def _require_extraction_provider(self) -> None:
        if self.provider and getattr(self.provider, "supports_file_inputs", False):
            return
        raise ValueError(
            "Ingestion requires a configured provider with file-input support. "
            "Set GEMINI_API_KEY or OPENAI_API_KEY and configure KWIKI_INGEST_PROVIDER/KWIKI_INGEST_MODEL as needed."
        )

    def _extract_with_provider_file_input(self, manifest: SourceManifest) -> ExtractedSource:
        path = self.settings.root_dir / manifest.file_path
        label = manifest.module_relpath or manifest.file_path
        self._progress(f"Uploading {label} for structured extraction.")
        prompt = "\n".join(
            [
                "FILE_EXTRACTION_REQUEST",
                "Return JSON only.",
                'Schema: {"title": str, "sections": [{"heading": str, "text": str}]}',
                "Extract the uploaded academic document into a small set of factual sections.",
                "Do not hallucinate missing content.",
                "Keep section text concise but faithful to the document.",
                f"Fallback title: {manifest.title}",
                f"Document kind: {manifest.kind}",
            ]
        )
        result = self.provider.generate_with_files(
            prompt,
            files=[path],
            system_prompt="You extract structured notes from uploaded academic files for a university course knowledge wiki.",
        )
        self._record_generation_usage(
            "provider_file_extraction",
            result,
            label=manifest.source_id,
            extra={"kind": manifest.kind, "file_path": manifest.file_path},
        )
        payload = extract_json_object(result.text)
        title = str(payload.get("title") or manifest.title).strip() or manifest.title
        sections_payload = payload.get("sections", [])
        if not isinstance(sections_payload, list) or not sections_payload:
            raise ValueError("Provider file extraction returned no sections.")
        sections: list[SourceSection] = []
        for index, item in enumerate(sections_payload, start=1):
            if not isinstance(item, dict):
                continue
            heading = str(item.get("heading") or f"Section {index}").strip()
            text = str(item.get("text") or "").strip()
            if not text:
                continue
            sections.append(SourceSection(section_id=f"section-{index}", heading=heading, text=text))
        if not sections:
            raise ValueError("Provider file extraction returned only empty sections.")
        return ExtractedSource(
            manifest=manifest,
            title=title,
            text="\n\n".join(f"{section.heading}\n{section.text}" for section in sections),
            sections=sections,
        )

    def _start_usage_tracking(self, *, module_id: str, batch_id: str) -> None:
        provider_label = self.provider.label if self.provider else "no-provider"
        provider_name, _, model = provider_label.partition("/")
        self._usage_tracker = _BatchUsageTracker(
            module_id=module_id,
            batch_id=batch_id,
            provider=provider_name or provider_label,
            model=model,
            created_at=utc_now(),
            lock=Lock(),
            records=[],
            summary=self._empty_usage_bucket(),
            by_stage={},
        )

    def _empty_usage_bucket(self) -> dict[str, float | int | None]:
        return {
            "calls": 0,
            "calls_with_usage": 0,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "estimated_input_cost_usd": 0.0,
            "estimated_output_cost_usd": 0.0,
            "estimated_total_cost_usd": 0.0,
        }

    def _record_generation_usage(
        self,
        stage: str,
        result: GenerationResult,
        *,
        label: str = "",
        extra: dict[str, object] | None = None,
    ) -> None:
        tracker = self._usage_tracker
        if tracker is None:
            return
        usage = result.usage
        with tracker.lock:
            stage_bucket = tracker.by_stage.setdefault(stage, self._empty_usage_bucket())
            tracker.summary["calls"] = int(tracker.summary["calls"] or 0) + 1
            stage_bucket["calls"] = int(stage_bucket["calls"] or 0) + 1
            if usage is not None:
                tracker.summary["calls_with_usage"] = int(tracker.summary["calls_with_usage"] or 0) + 1
                stage_bucket["calls_with_usage"] = int(stage_bucket["calls_with_usage"] or 0) + 1
                self._merge_usage_bucket(tracker.summary, usage)
                self._merge_usage_bucket(stage_bucket, usage)
            record = {
                "stage": stage,
                "label": label,
                "input_tokens": usage.input_tokens if usage else None,
                "output_tokens": usage.output_tokens if usage else None,
                "total_tokens": usage.total_tokens if usage else None,
                "estimated_total_cost_usd": usage.estimated_total_cost_usd if usage else None,
            }
            if extra:
                record.update(extra)
            tracker.records.append(record)

    def _merge_usage_bucket(self, bucket: dict[str, float | int | None], usage) -> None:
        bucket["input_tokens"] = int(bucket["input_tokens"] or 0) + usage.input_tokens
        bucket["output_tokens"] = int(bucket["output_tokens"] or 0) + usage.output_tokens
        bucket["total_tokens"] = int(bucket["total_tokens"] or 0) + usage.total_tokens
        bucket["estimated_input_cost_usd"] = round(float(bucket["estimated_input_cost_usd"] or 0.0) + float(usage.estimated_input_cost_usd or 0.0), 8)
        bucket["estimated_output_cost_usd"] = round(float(bucket["estimated_output_cost_usd"] or 0.0) + float(usage.estimated_output_cost_usd or 0.0), 8)
        bucket["estimated_total_cost_usd"] = round(float(bucket["estimated_total_cost_usd"] or 0.0) + float(usage.estimated_total_cost_usd or 0.0), 8)

    def _persist_usage_metrics(self, manifest: ModuleManifest) -> None:
        tracker = self._usage_tracker
        if tracker is None:
            return
        payload = {
            "module_id": tracker.module_id,
            "batch_id": tracker.batch_id,
            "provider": tracker.provider,
            "model": tracker.model,
            "created_at": tracker.created_at,
            "updated_at": utc_now(),
            "summary": tracker.summary,
            "by_stage": tracker.by_stage,
            "records": tracker.records,
        }
        save_ingest_metrics(self.settings, tracker.batch_id, payload)
        manifest.metadata["usage_summary"] = tracker.summary
        manifest.metadata["usage_by_stage"] = tracker.by_stage
        manifest.metadata["usage_metrics_path"] = str(ingest_metrics_path(self.settings, tracker.batch_id).relative_to(self.settings.root_dir))

    def _usage_summary_line(self) -> str:
        tracker = self._usage_tracker
        if tracker is None:
            return ""
        total_tokens = int(tracker.summary["total_tokens"] or 0)
        total_cost = float(tracker.summary["estimated_total_cost_usd"] or 0.0)
        return f"usage={total_tokens} tokens, estimated_cost_usd={total_cost:.6f}"

    def _progress(self, message: str) -> None:
        self.progress(message)

    def _build_source_draft_result(self, index: int, manifest: SourceManifest) -> _SourceDraftResult:
        self._progress(f"[{index}] Extracting {manifest.file_path}.")
        try:
            extracted = self._extract_manifest(manifest)
            self._progress(f"[{index}] Building draft for {manifest.source_id}.")
            proposal = self._build_single_source_draft(extracted)
        except Exception as exc:
            return _SourceDraftResult(index=index, manifest=manifest, error=str(exc))
        return _SourceDraftResult(index=index, manifest=manifest, proposal=proposal)

    def _extract_course_source_result(
        self,
        *,
        index: int,
        source_manifest: SourceManifest,
    ) -> _CourseExtractionResult:
        self._progress(f"[{index}] Extracting {source_manifest.module_relpath}.")
        try:
            extracted = self._extract_manifest(source_manifest)
            artifact = self._build_evidence_artifact(
                extracted,
                module_id=source_manifest.module_id,
                batch_id=source_manifest.batch_id,
            )
        except Exception as exc:
            return _CourseExtractionResult(index=index, source_manifest=source_manifest, error=str(exc))
        return _CourseExtractionResult(
            index=index,
            source_manifest=source_manifest,
            extracted=extracted,
            artifact=artifact,
        )

    def _draft_course_page_result(
        self,
        *,
        index: int,
        module_manifest: ModuleManifest,
        layout_review: LayoutReview,
        evidence_artifacts: list[EvidenceArtifact],
        artifacts_by_ref: dict[str, EvidenceArtifact],
        nearby_pages,
        all_page_ids: dict[str, str],
        feedback: str | None,
        existing_draft: DraftProposal | None,
        plan: LayoutPagePlan,
    ) -> _CourseDraftResult:
        self._progress(f"[{index}/{len(layout_review.pages)}] Drafting {plan.page_kind} page {plan.title}.")
        body = self._draft_page_body(
            module_manifest=module_manifest,
            plan=plan,
            evidence_artifacts=evidence_artifacts,
            artifacts_by_ref=artifacts_by_ref,
            nearby_pages=nearby_pages,
            all_plans=layout_review.pages,
            feedback=feedback,
            existing_markdown=existing_draft.proposed_markdown if existing_draft else None,
        )
        assigned_artifacts = self._artifacts_for_plan(plan, evidence_artifacts, artifacts_by_ref)
        page_type = "course" if plan.page_kind == "hub" else "concept"
        page = WikiPage(
            page_id=all_page_ids[plan.slug],
            title=plan.title,
            page_type=page_type,
            page_kind="synthesis" if page_type == "synthesis" else plan.page_kind,
            module_id=module_manifest.module_id,
            parent_page_id=all_page_ids.get(plan.parent_slug, ""),
            batch_id=module_manifest.batch_id,
            status="draft",
            summary=plan.summary,
            aliases=[],
            tags=self._build_course_tags(module_manifest, plan.page_kind),
            related=plan.related_page_ids,
            source_refs=plan.assigned_source_refs,
            topics=self._topics_for_course_page(plan, assigned_artifacts),
            source_count=self._source_count_from_refs(plan.assigned_source_refs),
            lecture_number=self._lecture_number_for_plan(plan),
            last_compiled_at=utc_now(),
            body=body,
        )
        target = self.settings.root_dir / plan.target_path
        proposal = DraftProposal(
            draft_id=f"{module_manifest.batch_id}-{plan.slug}",
            target_page=relative_posix(target, self.settings.root_dir),
            proposal_type="patch_page" if target.exists() else "create_page",
            rationale=plan.rationale or f"Drafted from course batch `{module_manifest.batch_id}`.",
            evidence_set=plan.assigned_source_refs,
            proposed_markdown=render_page(page),
            approval_state="pending",
            created_at=utc_now(),
            updated_at=utc_now(),
            module_id=module_manifest.module_id,
            batch_id=module_manifest.batch_id,
            page_kind=plan.page_kind,
            parent_page_id=page.parent_page_id,
            assigned_source_refs=plan.assigned_source_refs,
            metadata={
                "layout_id": layout_review.layout_id,
                "page_slug": plan.slug,
                "page_type": page_type,
            },
        )
        return _CourseDraftResult(index=index, proposal=proposal)

    def _worker_count(self, total_tasks: int) -> int:
        if total_tasks <= 0:
            return 1
        return max(1, min(self.settings.ingest_concurrency, total_tasks))

    def _run_in_parallel(self, tasks: list, *, max_workers: int) -> list:
        if not tasks:
            return []
        if max_workers <= 1:
            return [task() for task in tasks]
        results: list = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(task) for task in tasks]
            for future in as_completed(futures):
                results.append(future.result())
        return sorted(results, key=lambda item: item.index)

    def _iter_in_parallel(self, tasks: list, *, max_workers: int):
        if not tasks:
            return
        if max_workers <= 1:
            for task in tasks:
                yield task()
            return
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(task) for task in tasks]
            for future in as_completed(futures):
                yield future.result()

    def _looks_like_provider_failure(self, failures: list[dict[str, str]]) -> bool:
        return any(self._looks_like_provider_failure_message(item.get("reason", "")) for item in failures)

    def _looks_like_provider_failure_message(self, message: str) -> bool:
        normalized = message.lower()
        return any(
            token in normalized
            for token in (
                "provider request failed",
                "gemini request failed",
                "requires a gemini_api_key",
                "requires an api key",
                "google-genai",
                "insufficient_quota",
                "rate limit",
                "429",
            )
        )


def _first_sentences(text: str, *, limit: int) -> str:
    cleaned = _collapse_lines(text)
    parts = [segment.strip() for segment in re.split(r"(?<=[.!?])\s+", cleaned) if segment.strip()]
    if not parts:
        return cleaned
    return " ".join(parts[:limit])


def _collapse_lines(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _first_error_message(failures: list[dict[str, str]]) -> str:
    for item in failures:
        reason = item.get("reason", "").strip()
        if reason:
            return reason
    return ""
