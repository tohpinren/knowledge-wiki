from __future__ import annotations

import threading
import time

from knowledge_wiki.models import GenerationResult, GenerationUsage, WikiPage
from knowledge_wiki.wiki.pages import read_page, write_page
from knowledge_wiki.workflows import IngestWorkflow, ReviewWorkflow
from knowledge_wiki.workflows.common import (
    list_drafts,
    list_evidence_artifacts,
    list_module_manifests,
    list_source_manifests,
)

from .conftest import write_notebook, write_text_pdf


def _build_course_tree(settings) -> None:
    course_root = settings.raw_dir / "Y1S1" / "CS1231S"
    (course_root / "lectures").mkdir(parents=True)
    (course_root / "labs").mkdir()
    (course_root / "code").mkdir()
    (course_root / "node_modules").mkdir()

    (course_root / "lectures" / "week1.md").write_text(
        "# Week 1\n\nLogic and proofs.", encoding="utf-8"
    )
    (course_root / "lectures" / "week2.html").write_text(
        "<h1>Week 2</h1><p>Induction and recurrence.</p>", encoding="utf-8"
    )
    write_text_pdf(course_root / "lectures" / "slides.pdf", "Sets, relations, and proofs.")
    (course_root / "lectures" / "deck.pptx").write_bytes(b"pptx")
    write_notebook(course_root / "labs" / "lab1.ipynb")
    (course_root / "code" / "checker.py").write_text(
        "def check():\n    return 'proof'\n", encoding="utf-8"
    )
    (course_root / "lectures" / "diagram.png").write_bytes(b"png")
    (course_root / "node_modules" / "ignored.js").write_text(
        "console.log('ignored')", encoding="utf-8"
    )


def _build_lecture_flat_course_tree(settings) -> None:
    course_root = settings.raw_dir / "Y1S1" / "ACC1701X"
    lecture_root = course_root / "Lecture"
    lecture_root.mkdir(parents=True)

    (lecture_root / "Lecture 01 Slides.md").write_text(
        "# Lecture 01\n\nAccounting in business.", encoding="utf-8"
    )
    (lecture_root / "Lecture 01 Supplement.md").write_text(
        "# Supplement 01\n\nExtra lecture 1 details.", encoding="utf-8"
    )
    (lecture_root / "Lecture 02 Slides.md").write_text(
        "# Lecture 02\n\nMechanics of accounting.", encoding="utf-8"
    )
    (lecture_root / "Lecture 03 Slides.md").write_text(
        "# Lecture 03\n\nAdjusting accounts.", encoding="utf-8"
    )


def test_ingest_course_creates_module_manifest_evidence_layout_and_drafts(
    settings, scripted_provider
) -> None:
    _build_course_tree(settings)

    result = IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )

    assert result.module_manifest.module_id == "y1s1-cs1231s"
    assert result.module_manifest.status == "layout_pending"
    assert result.layout_review is not None
    assert len(result.evidence_artifacts) == 6
    assert len(result.draft_proposals) == 2

    module_manifests = list_module_manifests(settings)
    assert len(module_manifests) == 1
    assert list_evidence_artifacts(settings, module_id="y1s1-cs1231s")
    source_manifests = list_source_manifests(settings, module_id="y1s1-cs1231s")
    assert len(source_manifests) == 6
    assert all(
        manifest.batch_id == result.module_manifest.batch_id for manifest in source_manifests
    )
    assert any(
        path.endswith("slides.pdf")
        for _, files, _ in scripted_provider.file_calls
        for path in files
    )
    assert any(
        path.endswith("deck.pptx") for _, files, _ in scripted_provider.file_calls for path in files
    )
    assert (
        "layout pending"
        in settings.system_dir.joinpath("index.md").read_text(encoding="utf-8").lower()
    )


def test_ingest_course_parallelizes_file_extraction(settings, parallel_tracking_provider) -> None:
    _build_course_tree(settings)
    settings.ingest_concurrency = 4

    result = IngestWorkflow(settings, provider=parallel_tracking_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )

    assert result.module_manifest.status == "layout_pending"
    assert parallel_tracking_provider.max_active_file_calls > 1


def test_ingest_course_persists_completed_extractions_before_batch_finishes(
    settings, scripted_provider
) -> None:
    _build_course_tree(settings)
    settings.ingest_concurrency = 2

    class SlowOneProvider(type(scripted_provider)):
        def generate_with_files(
            self, prompt: str, *, files, system_prompt: str | None = None
        ) -> GenerationResult:
            if files and str(files[0]).endswith("lectures/slides.pdf"):
                time.sleep(1.5)
            return super().generate_with_files(prompt, files=files, system_prompt=system_prompt)

    provider = SlowOneProvider()
    workflow = IngestWorkflow(settings, provider=provider)
    result_box: dict[str, object] = {}

    def run() -> None:
        result_box["result"] = workflow.ingest_course(settings.raw_dir / "Y1S1" / "CS1231S")

    thread = threading.Thread(target=run)
    thread.start()

    deadline = time.time() + 5
    evidence_seen = False
    while time.time() < deadline:
        if any("cs1231s" in path.name for path in settings.evidence_dir.glob("*.json")):
            evidence_seen = True
            break
        time.sleep(0.1)

    thread.join(timeout=10)
    assert evidence_seen
    assert "result" in result_box


def test_ingest_course_persists_usage_metrics(settings, scripted_provider) -> None:
    class UsageProvider(type(scripted_provider)):
        def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
            result = super().generate(prompt, system_prompt=system_prompt)
            result.usage = GenerationUsage(
                provider="gemini",
                model="gemini-2.5-flash-lite",
                input_tokens=100,
                output_tokens=20,
                total_tokens=120,
                estimated_input_cost_usd=0.00001,
                estimated_output_cost_usd=0.000008,
                estimated_total_cost_usd=0.000018,
            )
            return result

        def generate_with_files(
            self, prompt: str, *, files, system_prompt: str | None = None
        ) -> GenerationResult:
            result = super().generate_with_files(prompt, files=files, system_prompt=system_prompt)
            result.usage = GenerationUsage(
                provider="gemini",
                model="gemini-2.5-flash-lite",
                input_tokens=200,
                output_tokens=50,
                total_tokens=250,
                estimated_input_cost_usd=0.00002,
                estimated_output_cost_usd=0.00002,
                estimated_total_cost_usd=0.00004,
            )
            return result

    provider = UsageProvider()
    _build_course_tree(settings)

    result = IngestWorkflow(settings, provider=provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )

    metrics_path = settings.ingest_metrics_dir / f"{result.module_manifest.batch_id}.json"
    assert metrics_path.exists()
    metrics_text = metrics_path.read_text(encoding="utf-8")
    assert f'"provider": "{provider.name}"' in metrics_text
    assert '"layout_planning"' in metrics_text
    assert '"provider_file_extraction"' in metrics_text
    assert result.module_manifest.metadata["usage_metrics_path"].endswith(
        f"{result.module_manifest.batch_id}.json"
    )
    assert result.module_manifest.metadata["usage_summary"]["total_tokens"] > 0
    assert result.module_manifest.metadata["usage_summary"]["estimated_total_cost_usd"] > 0


def test_topic_page_drafting_uses_direct_source_files(settings, scripted_provider) -> None:
    _build_lecture_flat_course_tree(settings)

    IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "ACC1701X"
    )

    draft_file_calls = [
        (prompt, files)
        for prompt, files, _ in scripted_provider.file_calls
        if "DRAFT_PAGE_REQUEST" in prompt and "Page title: Lecture 01" in prompt
    ]

    assert draft_file_calls
    assert any(
        path.endswith("Lecture 01 Slides.md") for _, files in draft_file_calls for path in files
    )
    assert any(
        path.endswith("Lecture 01 Supplement.md") for _, files in draft_file_calls for path in files
    )
    assert any("follow the lecture order" in prompt.lower() for prompt, _ in draft_file_calls)
    assert any("exhaustive concept coverage" in prompt.lower() for prompt, _ in draft_file_calls)
    assert any("section by section" in prompt.lower() for prompt, _ in draft_file_calls)


def test_ingest_course_reuses_existing_evidence_for_unchanged_files(
    settings, scripted_provider
) -> None:
    _build_course_tree(settings)

    first = IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )
    first_extraction_calls = sum(
        1 for prompt, _, _ in scripted_provider.file_calls if "FILE_EXTRACTION_REQUEST" in prompt
    )

    second = IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )

    assert first.module_manifest.status == "layout_pending"
    assert second.module_manifest.status == "layout_pending"
    assert (
        sum(
            1
            for prompt, _, _ in scripted_provider.file_calls
            if "FILE_EXTRACTION_REQUEST" in prompt
        )
        == first_extraction_calls
    )
    assert second.module_manifest.metadata["reused_evidence_files"] == 6
    second_artifacts = list_evidence_artifacts(
        settings, module_id="y1s1-cs1231s", batch_id=second.module_manifest.batch_id
    )
    assert len(second_artifacts) == 6
    assert all("reuse_signature" in artifact.metadata for artifact in second_artifacts)


def test_ingest_course_marks_provider_failed_when_all_extractions_fail(
    settings, failing_file_provider
) -> None:
    _build_course_tree(settings)

    result = IngestWorkflow(settings, provider=failing_file_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )

    assert result.module_manifest.status == "provider_failed"
    assert result.layout_review is None
    assert not result.evidence_artifacts
    assert "insufficient_quota" in result.module_manifest.metadata["provider_error"]
    source_manifests = list_source_manifests(settings, module_id="y1s1-cs1231s")
    assert source_manifests
    assert {manifest.extract_status for manifest in source_manifests} == {"failed"}


def test_two_stage_review_publishes_nested_course_pages_and_updates_indexes(
    settings, scripted_provider
) -> None:
    _build_course_tree(settings)

    ingest_result = IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )
    review = ReviewWorkflow(settings)

    layout = review.approve_layout(ingest_result.layout_review.layout_id)

    module_manifest = list_module_manifests(settings)[0]
    assert module_manifest.status == "published"
    assert layout.metadata["auto_published_draft_count"] == len(ingest_result.draft_proposals)
    assert {
        draft.approval_state
        for draft in list_drafts(
            settings, module_id="y1s1-cs1231s", batch_id=ingest_result.module_manifest.batch_id
        )
    } == {"approved"}

    hub_path = settings.root_dir / "wiki/courses/y1s1/cs1231s/index.md"
    topic_path = settings.root_dir / "wiki/courses/y1s1/cs1231s/topics/core-concepts.md"

    assert hub_path.exists()
    assert topic_path.exists()
    assert read_page(hub_path).status == "canonical"
    wiki_index = settings.wiki_dir.joinpath("index.md").read_text(encoding="utf-8")
    assert "CS1231S" in wiki_index
    assert "source_count=" in wiki_index
    assert "topics=" in wiki_index
    assert settings.graph_dir.joinpath("graph.json").exists()
    assert settings.graph_dir.joinpath("GRAPH_REPORT.md").exists()
    assert "auto-published" in settings.system_dir.joinpath("log.md").read_text(encoding="utf-8")
    assert {
        manifest.ingest_status
        for manifest in list_source_manifests(settings, module_id="y1s1-cs1231s")
    } == {"published"}


def test_revise_layout_regenerates_course_plan_and_drafts(settings, scripted_provider) -> None:
    _build_course_tree(settings)

    ingest_result = IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )
    review = ReviewWorkflow(settings, provider=scripted_provider)

    revised = review.revise_layout(
        ingest_result.layout_review.layout_id,
        "Make the hierarchy clearer and reflect the reviewer feedback in the generated pages.",
    )

    revised_drafts = list_drafts(
        settings, module_id="y1s1-cs1231s", batch_id=ingest_result.module_manifest.batch_id
    )

    assert revised.approval_state == "pending"
    assert revised.metadata["last_feedback"].startswith("Make the hierarchy clearer")
    assert any(page.title == "Core Concepts Revised" for page in revised.pages)
    assert any("Applied reviewer feedback" in draft.proposed_markdown for draft in revised_drafts)


def test_revise_page_updates_published_course_page(settings, scripted_provider) -> None:
    _build_course_tree(settings)

    ingest_result = IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )
    review = ReviewWorkflow(settings, provider=scripted_provider)
    review.approve_layout(ingest_result.layout_review.layout_id)

    page_path, page = review.revise_page(
        "wiki/courses/y1s1/cs1231s/topics/core-concepts.md",
        "Tighten the overview and make the evidence more explicit.",
    )

    assert page_path == "wiki/courses/y1s1/cs1231s/topics/core-concepts.md"
    assert "Applied reviewer feedback" in page.body
    assert page.status == "canonical"
    assert settings.graph_dir.joinpath("graph.json").exists()
    assert (
        "revised page `wiki/courses/y1s1/cs1231s/topics/core-concepts.md`"
        in settings.system_dir.joinpath("log.md").read_text(encoding="utf-8")
    )


def test_approve_layout_retries_auto_publish_for_previously_approved_batch(
    settings, scripted_provider
) -> None:
    _build_course_tree(settings)

    ingest_result = IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )
    review = ReviewWorkflow(settings)
    layout = review.load_layout(ingest_result.layout_review.layout_id)
    layout.approval_state = "approved"
    from knowledge_wiki.workflows.common import (
        load_module_manifest,
        save_layout_review,
        save_module_manifest,
    )

    save_layout_review(settings, layout)
    manifest = load_module_manifest(settings, ingest_result.module_manifest.module_id)
    manifest.status = "drafts_pending"
    manifest.layout_review_state = "approved"
    manifest.draft_review_state = "pending"
    save_module_manifest(settings, manifest)

    republished = review.approve_layout(ingest_result.layout_review.layout_id)

    assert republished.approval_state == "approved"
    assert republished.metadata["auto_published_draft_count"] == len(ingest_result.draft_proposals)
    assert settings.root_dir.joinpath("wiki/courses/y1s1/cs1231s/index.md").exists()


def test_approve_layout_prunes_stale_generated_module_pages(settings, scripted_provider) -> None:
    _build_course_tree(settings)

    ingest_result = IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )
    review = ReviewWorkflow(settings)

    inventory_path = settings.root_dir / "wiki/courses/y1s1/cs1231s/inventory.md"
    artifact_path = settings.root_dir / "wiki/courses/y1s1/cs1231s/artifacts/legacy-artifact.md"
    write_page(
        inventory_path,
        WikiPage(
            page_id="y1s1-cs1231s-inventory",
            title="CS1231S Inventory",
            page_type="course",
            page_kind="inventory",
            module_id="y1s1-cs1231s",
            parent_page_id="y1s1-cs1231s",
            batch_id="old-batch",
            status="canonical",
            summary="Legacy inventory page.",
            aliases=[],
            tags=["course"],
            related=[],
            source_refs=["legacy#section-1"],
            last_compiled_at="2026-04-01T00:00:00+00:00",
            body="# Legacy Inventory\n",
        ),
    )
    write_page(
        artifact_path,
        WikiPage(
            page_id="legacy-artifact",
            title="Legacy Artifact",
            page_type="course",
            page_kind="artifact",
            module_id="y1s1-cs1231s",
            parent_page_id="y1s1-cs1231s",
            batch_id="old-batch",
            status="canonical",
            summary="Legacy artifact page.",
            aliases=[],
            tags=["course"],
            related=[],
            source_refs=["legacy#section-2"],
            last_compiled_at="2026-04-01T00:00:00+00:00",
            body="# Legacy Artifact\n",
        ),
    )

    review.approve_layout(ingest_result.layout_review.layout_id)

    assert not inventory_path.exists()
    assert not artifact_path.exists()
    assert settings.root_dir.joinpath("wiki/courses/y1s1/cs1231s/index.md").exists()
    assert settings.root_dir.joinpath("wiki/courses/y1s1/cs1231s/topics/core-concepts.md").exists()
