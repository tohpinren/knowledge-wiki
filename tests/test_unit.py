from __future__ import annotations

from pathlib import Path

import pytest

from knowledge_wiki.models import CatalogEntry, EvidenceArtifact, GenerationResult, LayoutPagePlan, ModuleManifest, SourceManifest, WikiPage
from knowledge_wiki.providers.base import LLMProvider, ProviderError
from knowledge_wiki.providers import build_provider
from knowledge_wiki.providers.gemini import _gemini_usage
from knowledge_wiki.providers.openai_compatible import _openai_usage
from knowledge_wiki.retrieval.search import search_catalog
from knowledge_wiki.sources.discovery import classify_path, discover_course_files
from knowledge_wiki.sources.notebook import NotebookSourceAdapter
from knowledge_wiki.sources.office import extract_office_text
from knowledge_wiki.sources.pdf import PDFSourceAdapter
from knowledge_wiki.config import Settings
from knowledge_wiki.utils import extract_json_object, utc_now
from knowledge_wiki.wiki.frontmatter import split_frontmatter
from knowledge_wiki.wiki.pages import render_page
from knowledge_wiki.wiki.provenance import extract_source_refs, render_citation
from knowledge_wiki.workflows import IngestWorkflow, LintWorkflow, QueryWorkflow
from knowledge_wiki.workflows.common import save_source_manifest

from .conftest import ScriptedCourseProvider, write_notebook


def test_frontmatter_round_trip_preserves_course_page_fields() -> None:
    page = WikiPage(
        page_id="y1s1-cs1231s-core-concepts",
        title="Core Concepts",
        page_type="concept",
        page_kind="topic",
        module_id="y1s1-cs1231s",
        parent_page_id="y1s1-cs1231s-hub",
        batch_id="y1s1-cs1231s-20260406t000000z",
        status="canonical",
        summary="Reusable concepts from the course.",
        aliases=["concepts"],
        tags=["course", "topic"],
        related=["proof-techniques"],
        source_refs=["logic-notes#section-1"],
        topics=["logic", "proofs"],
        source_count=1,
        lecture_number=2,
        last_compiled_at=utc_now(),
        body="# Core Concepts\n\nProof structure matters [source:logic-notes#section-1]\n",
    )

    document = render_page(page)
    frontmatter, body = split_frontmatter(document)
    loaded = WikiPage.from_parts(frontmatter, body)

    assert loaded.page_kind == "topic"
    assert loaded.module_id == "y1s1-cs1231s"
    assert loaded.parent_page_id == "y1s1-cs1231s-hub"
    assert loaded.batch_id.endswith("z")
    assert loaded.topics == ["logic", "proofs"]
    assert loaded.source_count == 1
    assert loaded.lecture_number == 2


def test_discover_course_files_ignores_vendor_and_reports_skips(tmp_path: Path) -> None:
    course_root = tmp_path / "raw" / "Y1S1" / "CS1231S"
    (course_root / "notes").mkdir(parents=True)
    (course_root / "node_modules").mkdir()
    (course_root / ".git").mkdir()
    (course_root / "notes" / "lecture1.md").write_text("# Lecture 1\n\nLogic.", encoding="utf-8")
    (course_root / "notes" / "diagram.png").write_bytes(b"png")
    (course_root / "node_modules" / "ignored.js").write_text("console.log('x')", encoding="utf-8")

    usable, skipped = discover_course_files(course_root)

    assert [item.relative_path.as_posix() for item in usable] == ["notes/lecture1.md"]
    assert [item.relative_path.as_posix() for item in skipped] == ["notes/diagram.png"]
    assert skipped[0].skip_reason == "unsupported_extension"


def test_classify_path_handles_supported_and_hidden_files(tmp_path: Path) -> None:
    html_path = tmp_path / "lecture.html"
    html_path.write_text("<h1>Lecture</h1>", encoding="utf-8")
    hidden_path = tmp_path / ".DS_Store"
    hidden_path.write_text("", encoding="utf-8")

    html_discovered = classify_path(html_path)
    hidden_discovered = classify_path(hidden_path)

    assert html_discovered.usable is True
    assert html_discovered.kind == "html"
    assert hidden_discovered.usable is False
    assert hidden_discovered.skip_reason == "ignored_file"


def test_provider_usage_extractors_normalize_token_usage() -> None:
    gemini_usage = _gemini_usage(
        {
            "usage_metadata": {
                "prompt_token_count": 1000,
                "candidates_token_count": 200,
                "total_token_count": 1200,
            }
        },
        provider="gemini",
        model="gemini-2.5-flash-lite",
    )
    openai_usage = _openai_usage(
        {
            "usage": {
                "input_tokens": 400,
                "output_tokens": 80,
                "total_tokens": 480,
            }
        },
        provider="openai_compatible",
        model="gpt-5.4-mini",
    )

    assert gemini_usage is not None
    assert gemini_usage.total_tokens == 1200
    assert gemini_usage.estimated_total_cost_usd == pytest.approx(0.00018)
    assert openai_usage is not None
    assert openai_usage.total_tokens == 480
    assert openai_usage.estimated_total_cost_usd == pytest.approx(0.00026)


def test_build_provider_passes_timeout_settings(settings) -> None:
    settings.file_env[settings.gemini_api_key_env] = "key"
    settings.ingest_provider_name = "gemini"
    settings.ingest_model_name = "gemini-2.5-flash"
    settings.ingest_timeout_ms = 12345

    provider = build_provider(settings, purpose="ingest")

    assert provider is not None
    assert provider.name == "gemini"
    assert getattr(provider, "timeout_ms") == 12345


def test_notebook_adapter_extracts_markdown_and_code(settings) -> None:
    notebook_path = settings.raw_dir / "example.ipynb"
    write_notebook(notebook_path)
    manifest = SourceManifest(
        source_id="example-notebook",
        title="Example Notebook",
        kind="notebook",
        origin="course_ingest",
        scope="course/Y1S1/CS1231S",
        file_path="raw/example.ipynb",
        checksum="abc123",
        ingest_status="registered",
        created_at=utc_now(),
        updated_at=utc_now(),
    )

    extracted = NotebookSourceAdapter().extract(manifest, root_dir=settings.root_dir)

    assert "Notebook Title" in extracted.text
    assert any(section.heading == "Code Cell" for section in extracted.sections)


def test_office_extraction_falls_back_to_mdls(monkeypatch, tmp_path: Path) -> None:
    document = tmp_path / "slides.docx"
    document.write_bytes(b"docx")

    class Result:
        def __init__(self, returncode: int, stdout: str) -> None:
            self.returncode = returncode
            self.stdout = stdout

    def fake_run(cmd, capture_output, text, check):
        if "textutil" in cmd[0]:
            return Result(1, "")
        return Result(0, '"Converted content from metadata"')

    monkeypatch.setattr("knowledge_wiki.sources.office.subprocess.run", fake_run)

    assert extract_office_text(document) == "Converted content from metadata"


def test_layout_validation_rejects_duplicate_slugs(settings) -> None:
    workflow = IngestWorkflow(settings, provider=ScriptedCourseProvider())
    manifest = ModuleManifest(
        module_id="y1s1-cs1231s",
        term="Y1S1",
        module_code="CS1231S",
        root_path="raw/Y1S1/CS1231S",
        batch_id="y1s1-cs1231s-batch",
        status="layout_pending",
        discovered_files=2,
        usable_files=2,
        skipped_files=0,
        layout_review_state="pending",
        draft_review_state="pending",
        created_at=utc_now(),
        updated_at=utc_now(),
    )
    pages = [
        LayoutPagePlan(
            title="Hub",
            slug="hub",
            page_kind="hub",
            target_path="wiki/courses/y1s1/cs1231s/index.md",
            summary="Hub",
            parent_slug="",
            related_page_ids=[],
            assigned_source_refs=["source-a#section-1"],
        ),
        LayoutPagePlan(
            title="Duplicate Hub",
            slug="hub",
            page_kind="topic",
            target_path="wiki/courses/y1s1/cs1231s/topics/hub.md",
            summary="Duplicate",
            parent_slug="hub",
            related_page_ids=[],
            assigned_source_refs=["source-a#section-1"],
        ),
    ]

    with pytest.raises(ValueError):
        workflow._validate_layout_pages(
            module_manifest=manifest,
            pages=pages,
            known_source_refs={"source-a#section-1"},
            nearby_page_ids=set(),
        )


def test_provider_layout_paths_are_normalized_to_course_tree(settings) -> None:
    class InvalidPathProvider(LLMProvider):
        def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
            return GenerationResult(
                text=(
                    '{"pages":['
                    '{"title":"Core Concepts","slug":"core-concepts","page_kind":"topic","target_path":"wiki/bad.md","summary":"Summary","parent_slug":"","related_page_ids":[],"assigned_source_refs":["source-a#section-1"],"rationale":"Topic."}'
                    "]}"
                )
            )

    workflow = IngestWorkflow(settings, provider=InvalidPathProvider())
    manifest = ModuleManifest(
        module_id="y1s1-cs1231s",
        term="Y1S1",
        module_code="CS1231S",
        root_path="raw/Y1S1/CS1231S",
        batch_id="y1s1-cs1231s-batch",
        status="discovering",
        discovered_files=1,
        usable_files=1,
        skipped_files=0,
        layout_review_state="not_started",
        draft_review_state="not_started",
        created_at=utc_now(),
        updated_at=utc_now(),
    )
    artifact = CatalogEntry(
        path="wiki/courses/y1s1/cs1231s/topics/core-concepts.md",
        page_id="nearby-page",
        title="Nearby",
        page_type="concept",
        summary="Nearby page.",
        text="Nearby content",
        related=[],
        source_refs=["source-a#section-1"],
    )
    evidence = [
        EvidenceArtifact(
            evidence_id="evidence-a",
            source_id="source-a",
            module_id="y1s1-cs1231s",
            batch_id="y1s1-cs1231s-batch",
            source_path="raw/Y1S1/CS1231S/week1.md",
            source_refs=["source-a#section-1"],
            summary="Week 1 summary",
            key_topics=["logic"],
            content_class="notes",
            extractor="test",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "Week 1"},
        )
    ]

    review = workflow._build_layout_review(
        module_manifest=manifest,
        evidence_artifacts=evidence,
        nearby_pages=[artifact],
    )

    by_slug = {page.slug: page for page in review.pages}
    assert by_slug["core-concepts"].target_path == "wiki/courses/y1s1/cs1231s/topics/core-concepts.md"
    assert by_slug["core-concepts"].parent_slug == "hub"


def test_provider_layout_source_ids_are_normalized_to_known_source_refs(settings) -> None:
    class BareSourceIdProvider(LLMProvider):
        def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
            return GenerationResult(
                text=(
                    '{"pages":['
                    '{"title":"Introduction To Accounting","slug":"introduction-to-accounting","page_kind":"topic","target_path":"wiki/bad.md","summary":"Summary","parent_slug":"","related_page_ids":[],"assigned_source_refs":["acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf","[source:acc1701x-cs1-pdf]"],"rationale":"Topic."}'
                    "]}"
                )
            )

    workflow = IngestWorkflow(settings, provider=BareSourceIdProvider())
    manifest = ModuleManifest(
        module_id="y1s1-acc1701x",
        term="Y1S1",
        module_code="ACC1701X",
        root_path="raw/Y1S1/ACC1701X",
        batch_id="y1s1-acc1701x-batch",
        status="discovering",
        discovered_files=2,
        usable_files=2,
        skipped_files=0,
        layout_review_state="not_started",
        draft_review_state="not_started",
        created_at=utc_now(),
        updated_at=utc_now(),
    )
    evidence = [
        EvidenceArtifact(
            evidence_id="batch--acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf",
            source_id="acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/Lecture/Lecture 01 Slides - Accounting in Business and FS Overview.pdf",
            source_refs=[
                "acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf#section-1",
                "acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf#section-2",
            ],
            summary="Week 1 summary",
            key_topics=["accounting"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "Lecture 01"},
        ),
        EvidenceArtifact(
            evidence_id="batch--acc1701x-cs1-pdf",
            source_id="acc1701x-cs1-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/cs1.pdf",
            source_refs=["acc1701x-cs1-pdf#section-1"],
            summary="Cheatsheet summary",
            key_topics=["cheatsheet"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "cs1"},
        ),
    ]

    review = workflow._build_layout_review(
        module_manifest=manifest,
        evidence_artifacts=evidence,
        nearby_pages=[],
    )

    plan = next(page for page in review.pages if page.slug == "introduction-to-accounting")
    assert plan.assigned_source_refs == [
        "acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf#section-1",
        "acc1701x-cs1-pdf#section-1",
    ]


def test_provider_layout_missing_source_refs_falls_back_to_matching_evidence(settings) -> None:
    class EmptySourceRefsProvider(LLMProvider):
        def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
            return GenerationResult(
                text=(
                    '{"pages":['
                    '{"title":"Intro To Accounting","slug":"intro-to-accounting","page_kind":"topic","target_path":"wiki/bad.md","summary":"Foundational accounting concepts and statements.","parent_slug":"","related_page_ids":[],"assigned_source_refs":[],"rationale":"Cover the module introduction and core accounting ideas."}'
                    "]}"
                )
            )

    workflow = IngestWorkflow(settings, provider=EmptySourceRefsProvider())
    manifest = ModuleManifest(
        module_id="y1s1-acc1701x",
        term="Y1S1",
        module_code="ACC1701X",
        root_path="raw/Y1S1/ACC1701X",
        batch_id="y1s1-acc1701x-batch",
        status="discovering",
        discovered_files=2,
        usable_files=2,
        skipped_files=0,
        layout_review_state="not_started",
        draft_review_state="not_started",
        created_at=utc_now(),
        updated_at=utc_now(),
    )
    evidence = [
        EvidenceArtifact(
            evidence_id="batch--acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf",
            source_id="acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/Lecture/Lecture 01 Slides - Accounting in Business and FS Overview.pdf",
            source_refs=[
                "acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf#section-1",
                "acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf#section-2",
            ],
            summary="Introduces accounting in business and financial statement foundations.",
            key_topics=["accounting", "statements", "business"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "Lecture 01"},
        ),
        EvidenceArtifact(
            evidence_id="batch--acc1701x-cs1-pdf",
            source_id="acc1701x-cs1-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/cs1.pdf",
            source_refs=["acc1701x-cs1-pdf#section-1"],
            summary="Cheatsheet covering core accounting concepts.",
            key_topics=["accounting", "concepts"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "cs1"},
        ),
    ]

    review = workflow._build_layout_review(
        module_manifest=manifest,
        evidence_artifacts=evidence,
        nearby_pages=[],
    )

    plan = next(page for page in review.pages if page.slug == "intro-to-accounting")
    assert plan.assigned_source_refs
    assert set(plan.assigned_source_refs) == {
        "acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf#section-1",
        "acc1701x-lecture-lecture-01-slides-accounting-in-business-and-fs-overview-pdf#section-2",
        "acc1701x-cs1-pdf#section-1",
    }


def test_provider_layout_near_miss_source_ref_is_normalized_to_known_ref(settings) -> None:
    class NearMissSourceRefProvider(LLMProvider):
        def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
            return GenerationResult(
                text=(
                    '{"pages":['
                    '{"title":"Mock Exam 2 Solution Notes","slug":"mock-exam-2-solution-notes","page_kind":"topic","target_path":"wiki/bad.md","summary":"Worked mock exam solution.","parent_slug":"","related_page_ids":[],"assigned_source_refs":["acc1701x-mock-finals-acc-1701x-mock-exam-2-solution-pdf#section-1"],"rationale":"Capture the solved mock exam notes."}'
                    "]}"
                )
            )

    workflow = IngestWorkflow(settings, provider=NearMissSourceRefProvider())
    manifest = ModuleManifest(
        module_id="y1s1-acc1701x",
        term="Y1S1",
        module_code="ACC1701X",
        root_path="raw/Y1S1/ACC1701X",
        batch_id="y1s1-acc1701x-batch",
        status="discovering",
        discovered_files=1,
        usable_files=1,
        skipped_files=0,
        layout_review_state="not_started",
        draft_review_state="not_started",
        created_at=utc_now(),
        updated_at=utc_now(),
    )
    evidence = [
        EvidenceArtifact(
            evidence_id="batch--acc1701x-mock-finals-acc1701x-mock-exam-2-solution-pdf",
            source_id="acc1701x-mock-finals-acc1701x-mock-exam-2-solution-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/Mock Finals/ACC1701X Mock Exam #2 Solution.pdf",
            source_refs=[
                "acc1701x-mock-finals-acc1701x-mock-exam-2-solution-pdf#section-1",
                "acc1701x-mock-finals-acc1701x-mock-exam-2-solution-pdf#section-2",
            ],
            summary="Solved mock exam.",
            key_topics=["mock", "exam", "solution"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "Mock Exam 2 Solution"},
        ),
    ]

    review = workflow._build_layout_review(
        module_manifest=manifest,
        evidence_artifacts=evidence,
        nearby_pages=[],
    )

    plan = next(page for page in review.pages if page.slug == "mock-exam-2-solution-notes")
    assert plan.assigned_source_refs == [
        "acc1701x-mock-finals-acc1701x-mock-exam-2-solution-pdf#section-1",
    ]


def test_provider_layout_invalid_parent_and_related_ids_are_sanitized(settings) -> None:
    class InvalidRelationshipProvider(LLMProvider):
        def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
            return GenerationResult(
                text=(
                    '{"pages":['
                    '{"title":"Accounting Fundamentals","slug":"accounting-fundamentals","page_kind":"topic","target_path":"wiki/bad.md","summary":"Foundational accounting concepts.","parent_slug":null,"related_page_ids":["acc1701x-mechanics-of-accounting"],"assigned_source_refs":["acc1701x-cs1-pdf#section-1"],"rationale":"Intro topic."}'
                    "]}"
                )
            )

    workflow = IngestWorkflow(settings, provider=InvalidRelationshipProvider())
    manifest = ModuleManifest(
        module_id="y1s1-acc1701x",
        term="Y1S1",
        module_code="ACC1701X",
        root_path="raw/Y1S1/ACC1701X",
        batch_id="y1s1-acc1701x-batch",
        status="discovering",
        discovered_files=1,
        usable_files=1,
        skipped_files=0,
        layout_review_state="not_started",
        draft_review_state="not_started",
        created_at=utc_now(),
        updated_at=utc_now(),
    )
    evidence = [
        EvidenceArtifact(
            evidence_id="batch--acc1701x-cs1-pdf",
            source_id="acc1701x-cs1-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/cs1.pdf",
            source_refs=["acc1701x-cs1-pdf#section-1"],
            summary="Cheatsheet covering core accounting concepts.",
            key_topics=["accounting", "concepts"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "cs1"},
        ),
    ]

    review = workflow._build_layout_review(
        module_manifest=manifest,
        evidence_artifacts=evidence,
        nearby_pages=[],
    )

    plan = next(page for page in review.pages if page.slug == "accounting-fundamentals")
    assert plan.parent_slug == "hub"
    assert plan.related_page_ids == []


def test_provider_layout_is_retried_after_invalid_response(settings) -> None:
    class RetryLayoutProvider(LLMProvider):
        def __init__(self) -> None:
            self.calls = 0

        def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
            self.calls += 1
            if self.calls == 1:
                return GenerationResult(
                    text=(
                        '{"pages":['
                        '{"title":"Accounting Fundamentals","slug":"accounting-fundamentals","page_kind":"topic","target_path":"wiki/bad.md","summary":"Foundational accounting concepts.","parent_slug":"made-up-parent","related_page_ids":[],"assigned_source_refs":["acc1701x-cs1-pdf#section-1"],"rationale":"Intro topic."}'
                        "]}"
                    )
                )
            return GenerationResult(
                text=(
                    '{"pages":['
                    '{"title":"Accounting Fundamentals","slug":"accounting-fundamentals","page_kind":"topic","target_path":"wiki/bad.md","summary":"Foundational accounting concepts.","parent_slug":"hub","related_page_ids":[],"assigned_source_refs":["acc1701x-cs1-pdf#section-1"],"rationale":"Intro topic."}'
                    "]}"
                )
            )

    provider = RetryLayoutProvider()
    workflow = IngestWorkflow(settings, provider=provider)
    manifest = ModuleManifest(
        module_id="y1s1-acc1701x",
        term="Y1S1",
        module_code="ACC1701X",
        root_path="raw/Y1S1/ACC1701X",
        batch_id="y1s1-acc1701x-batch",
        status="discovering",
        discovered_files=1,
        usable_files=1,
        skipped_files=0,
        layout_review_state="not_started",
        draft_review_state="not_started",
        created_at=utc_now(),
        updated_at=utc_now(),
    )
    evidence = [
        EvidenceArtifact(
            evidence_id="batch--acc1701x-cs1-pdf",
            source_id="acc1701x-cs1-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/cs1.pdf",
            source_refs=["acc1701x-cs1-pdf#section-1"],
            summary="Cheatsheet covering core accounting concepts.",
            key_topics=["accounting", "concepts"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "cs1"},
        ),
    ]

    review = workflow._build_layout_review(
        module_manifest=manifest,
        evidence_artifacts=evidence,
        nearby_pages=[],
    )

    plan = next(page for page in review.pages if page.slug == "accounting-fundamentals")
    assert provider.calls == 1
    assert plan.parent_slug == "hub"
    assert plan.assigned_source_refs == ["acc1701x-cs1-pdf#section-1"]


def test_numbered_lecture_materials_create_flat_lecture_pages(settings) -> None:
    workflow = IngestWorkflow(settings, provider=ScriptedCourseProvider())
    manifest = ModuleManifest(
        module_id="y1s1-acc1701x",
        term="Y1S1",
        module_code="ACC1701X",
        root_path="raw/Y1S1/ACC1701X",
        batch_id="y1s1-acc1701x-batch",
        status="discovering",
        discovered_files=4,
        usable_files=4,
        skipped_files=0,
        layout_review_state="not_started",
        draft_review_state="not_started",
        created_at=utc_now(),
        updated_at=utc_now(),
    )
    evidence = [
        EvidenceArtifact(
            evidence_id="batch--lecture-01-slides",
            source_id="acc1701x-lecture-lecture-01-slides-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/Lecture/Lecture 01 Slides - Accounting in Business and FS Overview.pdf",
            source_refs=["acc1701x-lecture-lecture-01-slides-pdf#section-1"],
            summary="Introduces accounting in business and financial statements.",
            key_topics=["accounting", "financial statements"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={
                "title": "Lecture 01 Slides - Accounting in Business and FS Overview",
                "module_relpath": "Lecture/Lecture 01 Slides - Accounting in Business and FS Overview.pdf",
            },
        ),
        EvidenceArtifact(
            evidence_id="batch--lecture-01-supplement",
            source_id="acc1701x-lecture-lecture-01-supplement-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/Lecture/Lecture 01 Post Lecture Supplement.pdf",
            source_refs=["acc1701x-lecture-lecture-01-supplement-pdf#section-1"],
            summary="Extra practice for lecture 1.",
            key_topics=["accounting", "practice"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={
                "title": "Lecture 01 Post Lecture Supplement",
                "module_relpath": "Lecture/Lecture 01 Post Lecture Supplement.pdf",
            },
        ),
        EvidenceArtifact(
            evidence_id="batch--lecture-02-slides",
            source_id="acc1701x-lecture-lecture-02-slides-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/Lecture/Lecture 02 Slides - Mechanics of Accounting.pdf",
            source_refs=["acc1701x-lecture-lecture-02-slides-pdf#section-1"],
            summary="Covers the mechanics of accounting.",
            key_topics=["mechanics", "accounting"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={
                "title": "Lecture 02 Slides - Mechanics of Accounting",
                "module_relpath": "Lecture/Lecture 02 Slides - Mechanics of Accounting.pdf",
            },
        ),
        EvidenceArtifact(
            evidence_id="batch--lecture-03-slides",
            source_id="acc1701x-lecture-lecture-03-slides-pdf",
            module_id="y1s1-acc1701x",
            batch_id="y1s1-acc1701x-batch",
            source_path="raw/Y1S1/ACC1701X/Lecture/Lecture 03 Slides - Adjusting Accounts.pdf",
            source_refs=["acc1701x-lecture-lecture-03-slides-pdf#section-1"],
            summary="Explains adjusting accounts.",
            key_topics=["adjusting", "accounts"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={
                "title": "Lecture 03 Slides - Adjusting Accounts",
                "module_relpath": "Lecture/Lecture 03 Slides - Adjusting Accounts.pdf",
            },
        ),
    ]

    review = workflow._build_layout_review(
        module_manifest=manifest,
        evidence_artifacts=evidence,
        nearby_pages=[],
    )

    by_slug = {page.slug: page for page in review.pages}
    assert review.metadata["layout_strategy"] == "lecture-flat"
    assert by_slug["lecture-01"].title == "Lecture 01: Accounting in Business and FS Overview"
    assert by_slug["lecture-01"].parent_slug == "hub"
    assert set(by_slug["lecture-01"].assigned_source_refs) == {
        "acc1701x-lecture-lecture-01-slides-pdf#section-1",
        "acc1701x-lecture-lecture-01-supplement-pdf#section-1",
    }
    assert by_slug["lecture-02"].title == "Lecture 02: Mechanics of Accounting"
    assert by_slug["lecture-03"].title == "Lecture 03: Adjusting Accounts"


def test_lecture_layout_strategy_detects_capitalized_lecture_directory(settings) -> None:
    workflow = IngestWorkflow(settings, provider=ScriptedCourseProvider())
    evidence = [
        EvidenceArtifact(
            evidence_id="batch--week-01",
            source_id="module-week-01-pdf",
            module_id="y1s1-demo",
            batch_id="y1s1-demo-batch",
            source_path="raw/Y1S1/DEMO/Lecture/Week 01.pdf",
            source_refs=["module-week-01-pdf#section-1"],
            summary="Week 1 lecture notes.",
            key_topics=["intro"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "Week 01 Intro", "module_relpath": "Lecture/Week 01.pdf"},
        ),
        EvidenceArtifact(
            evidence_id="batch--week-02",
            source_id="module-week-02-pdf",
            module_id="y1s1-demo",
            batch_id="y1s1-demo-batch",
            source_path="raw/Y1S1/DEMO/Lecture/Week 02.pdf",
            source_refs=["module-week-02-pdf#section-1"],
            summary="Week 2 lecture notes.",
            key_topics=["journal"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "Week 02 Journals", "module_relpath": "Lecture/Week 02.pdf"},
        ),
        EvidenceArtifact(
            evidence_id="batch--week-03",
            source_id="module-week-03-pdf",
            module_id="y1s1-demo",
            batch_id="y1s1-demo-batch",
            source_path="raw/Y1S1/DEMO/Lecture/Week 03.pdf",
            source_refs=["module-week-03-pdf#section-1"],
            summary="Week 3 lecture notes.",
            key_topics=["adjustments"],
            content_class="notes",
            extractor="pdf",
            created_at=utc_now(),
            updated_at=utc_now(),
            metadata={"title": "Week 03 Adjustments", "module_relpath": "Lecture/Week 03.pdf"},
        ),
    ]

    strategy = workflow._lecture_layout_strategy(evidence)

    assert strategy["strategy"] == "lecture-flat"
    assert [page.slug for page in strategy["pages"]] == ["lecture-01", "lecture-02", "lecture-03"]


def test_lecture_flat_layout_filters_exam_preparation_topics(settings) -> None:
    workflow = IngestWorkflow(settings, provider=ScriptedCourseProvider())

    kept = workflow._filter_provider_layout_pages(
        [
            LayoutPagePlan(
                title="Exam Preparation",
                slug="exam-preparation",
                page_kind="topic",
                target_path="wiki/courses/y1s1/demo/topics/exam-preparation.md",
                summary="Study materials for finals and mock exams.",
                parent_slug="hub",
                related_page_ids=[],
                assigned_source_refs=["demo#section-1"],
                rationale="Organize mock exam and finals prep.",
            ),
            LayoutPagePlan(
                title="Tutorial 01 Supporting Notes",
                slug="tutorial-01-supporting-notes",
                page_kind="topic",
                target_path="wiki/courses/y1s1/demo/topics/tutorial-01-supporting-notes.md",
                summary="Worked tutorial solutions.",
                parent_slug="lecture-01",
                related_page_ids=[],
                assigned_source_refs=["demo#section-1"],
                rationale="Supplementary worked notes.",
            ),
        ],
        lecture_strategy={"strategy": "lecture-flat", "pages": []},
    )

    assert [page.slug for page in kept] == ["tutorial-01-supporting-notes"]


def test_pdf_source_falls_back_when_provider_returns_invalid_argument(settings, monkeypatch) -> None:
    class InvalidArgumentProvider(LLMProvider):
        supports_file_inputs = True

        def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
            return GenerationResult(text="")

        def generate_with_files(
            self,
            prompt: str,
            *,
            files: list[Path],
            system_prompt: str | None = None,
        ) -> GenerationResult:
            raise ProviderError("Gemini request failed: 400 INVALID_ARGUMENT. Request contains an invalid argument.")

    monkeypatch.setattr("knowledge_wiki.sources.pdf._extract_pdf_text", lambda path: "Recovered local PDF text")

    source_path = settings.raw_dir / "textbook.pdf"
    source_path.write_bytes(b"%PDF-1.4")
    manifest = SourceManifest(
        source_id="textbook-pdf",
        title="Textbook",
        kind="pdf",
        origin="manual",
        scope="general",
        file_path="raw/textbook.pdf",
        checksum="abc123",
        ingest_status="registered",
        created_at=utc_now(),
        updated_at=utc_now(),
    )

    extracted = IngestWorkflow(settings, provider=InvalidArgumentProvider())._extract_manifest(manifest)

    assert extracted.title == "Textbook"
    assert "Recovered local PDF text" in extracted.text
    assert manifest.extractor_metadata["provider_file_input"] is False


def test_large_pdf_fallback_requires_pypdf(settings, monkeypatch) -> None:
    monkeypatch.setattr("knowledge_wiki.sources.pdf._load_pdf_reader", lambda: None)

    source_path = settings.raw_dir / "large.pdf"
    source_path.write_bytes(b"%PDF-1.4\n" + b"x" * (21 * 1024 * 1024))
    manifest = SourceManifest(
        source_id="large-pdf",
        title="Large PDF",
        kind="pdf",
        origin="manual",
        scope="general",
        file_path="raw/large.pdf",
        checksum="abc123",
        ingest_status="registered",
        created_at=utc_now(),
        updated_at=utc_now(),
    )

    adapter = PDFSourceAdapter()
    with pytest.raises(ValueError, match="requires pypdf for large PDFs"):
        adapter.extract(manifest, root_dir=settings.root_dir)


def test_extract_json_object_sanitizes_invalid_backslash_escapes() -> None:
    payload = extract_json_object('{"title":"Example","sections":[{"heading":"Overview","text":"Profit \\q Loss"}]}')

    assert payload["sections"][0]["text"] == "Profit \\q Loss"


def test_office_source_falls_back_when_provider_rejects_unsupported_mime(settings, monkeypatch) -> None:
    class MimeRejectingProvider(LLMProvider):
        supports_file_inputs = True

        def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
            return GenerationResult(text="")

        def generate_with_files(
            self,
            prompt: str,
            *,
            files: list[Path],
            system_prompt: str | None = None,
        ) -> GenerationResult:
            raise ProviderError("Gemini request failed: 400 INVALID_ARGUMENT. Unsupported MIME type: application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    class Result:
        def __init__(self, returncode: int, stdout: str) -> None:
            self.returncode = returncode
            self.stdout = stdout

    def fake_run(cmd, capture_output, text, check):
        if "textutil" in cmd[0]:
            return Result(0, "Office fallback content")
        return Result(1, "")

    monkeypatch.setattr("knowledge_wiki.sources.office.subprocess.run", fake_run)

    source_path = settings.raw_dir / "slides.docx"
    source_path.write_bytes(b"docx")
    manifest = SourceManifest(
        source_id="slides-docx",
        title="Slides",
        kind="office",
        origin="manual",
        scope="general",
        file_path="raw/slides.docx",
        checksum="checksum",
        ingest_status="registered",
        created_at=utc_now(),
        updated_at=utc_now(),
    )

    extracted = IngestWorkflow(settings, provider=MimeRejectingProvider())._extract_manifest(manifest)

    assert "Office fallback content" in extracted.text
    assert manifest.extractor_metadata["provider_file_input"] is False


def test_search_catalog_ranks_title_and_summary_matches_first() -> None:
    entries = [
        CatalogEntry(
            path="wiki/courses/y1s1/cs1231s/topics/core-concepts.md",
            page_id="core-concepts",
            title="Core Concepts",
            page_type="concept",
            summary="Logic, proofs, and induction.",
            text="Core Concepts\nLogic, proofs, and induction appear across the course.",
            related=[],
            source_refs=["logic-notes#section-1"],
        ),
        CatalogEntry(
            path="wiki/courses/y1s1/cs2040s/topics/data-structures.md",
            page_id="data-structures",
            title="Data Structures",
            page_type="concept",
            summary="Trees and heaps.",
            text="Data Structures\nTrees, heaps, and implementations.",
            related=[],
            source_refs=["ds-notes#section-1"],
        ),
    ]

    hits = search_catalog(entries, "logic proofs induction", max_results=2)

    assert hits[0].page_id == "core-concepts"
    assert hits[0].score > 0


def test_search_catalog_prefers_relevant_passage_over_first_stopword_match() -> None:
    entries = [
        CatalogEntry(
            path="wiki/courses/y1s1/acc1701x/topics/lecture-11.md",
            page_id="lecture-11",
            title="Lecture 11: Statement Of Cash Flows",
            page_type="concept",
            summary="Cash flow lecture.",
            text=(
                "Lecture 11: Statement Of Cash Flows\n\n"
                "Cash flow is important for business operations.\n\n"
                "Cash Flows from Operations (Indirect Method)\n"
                "The indirect method starts with profit before tax and adjusts for non-cash items and working capital changes."
            ),
            related=[],
            source_refs=["lecture-11#section-1"],
        )
    ]

    hits = search_catalog(entries, "What is Cash Flows from Operations, indirect method", max_results=5)

    assert hits
    assert "indirect method" in hits[0].snippet.lower()
    assert "profit before tax" in hits[0].snippet.lower()


def test_provenance_helpers_render_and_extract_tokens() -> None:
    citation = render_citation("logic-notes", "section-2")
    assert citation == "[source:logic-notes#section-2]"
    assert extract_source_refs(f"Proof technique {citation}") == ["logic-notes#section-2"]


def test_settings_load_model_from_repo_env(tmp_path: Path, monkeypatch) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    (root / ".env").write_text("KWIKI_MODEL=gpt-5.4\n", encoding="utf-8")
    for key in ("KWIKI_MODEL", "KWIKI_INGEST_MODEL", "KWIKI_QA_MODEL"):
        monkeypatch.delenv(key, raising=False)

    settings = Settings.from_root(root)

    assert settings.model_name == "gpt-5.4"
    assert settings.ingest_model_name == "gpt-5.4"
    assert settings.qa_model_name == "gpt-5.4"


def test_settings_resolve_task_specific_provider_and_model_env(tmp_path: Path, monkeypatch) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    (root / ".env").write_text(
        "\n".join(
            [
                "KWIKI_PROVIDER=openai_compatible",
                "KWIKI_MODEL=gpt-5.4-mini",
                "KWIKI_INGEST_PROVIDER=gemini",
                "KWIKI_INGEST_MODEL=gemini-2.5-flash-lite",
                "KWIKI_QA_MODEL=gemini-2.5-flash",
                "KWIKI_INGEST_CONCURRENCY=6",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    for key in (
        "KWIKI_PROVIDER",
        "KWIKI_MODEL",
        "KWIKI_INGEST_PROVIDER",
        "KWIKI_INGEST_MODEL",
        "KWIKI_QA_PROVIDER",
        "KWIKI_QA_MODEL",
        "KWIKI_INGEST_CONCURRENCY",
    ):
        monkeypatch.delenv(key, raising=False)

    settings = Settings.from_root(root)

    assert settings.provider_name == "openai_compatible"
    assert settings.model_name == "gpt-5.4-mini"
    assert settings.ingest_provider_name == "gemini"
    assert settings.ingest_model_name == "gemini-2.5-flash-lite"
    assert settings.qa_provider_name == "openai_compatible"
    assert settings.qa_model_name == "gemini-2.5-flash"
    assert settings.ingest_concurrency == 6


def test_settings_default_to_gemini_split_models(tmp_path: Path, monkeypatch) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    for key in (
        "KWIKI_PROVIDER",
        "KWIKI_MODEL",
        "KWIKI_INGEST_PROVIDER",
        "KWIKI_INGEST_MODEL",
        "KWIKI_QA_PROVIDER",
        "KWIKI_QA_MODEL",
        "KWIKI_INGEST_CONCURRENCY",
    ):
        monkeypatch.delenv(key, raising=False)

    settings = Settings.from_root(root)

    assert settings.ingest_provider_name == "gemini"
    assert settings.ingest_model_name == "gemini-2.5-flash-lite"
    assert settings.qa_provider_name == "gemini"
    assert settings.qa_model_name == "gemini-2.5-flash"
    assert settings.ingest_concurrency == 4


def test_build_provider_uses_purpose_specific_configuration(tmp_path: Path, monkeypatch) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    (root / ".env").write_text(
        "\n".join(
            [
                "GEMINI_API_KEY=test-gemini",
                "OPENAI_API_KEY=test-openai",
                "KWIKI_INGEST_PROVIDER=gemini",
                "KWIKI_INGEST_MODEL=gemini-2.5-flash-lite",
                "KWIKI_QA_PROVIDER=openai_compatible",
                "KWIKI_QA_MODEL=gpt-5.4-mini",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    for key in (
        "GEMINI_API_KEY",
        "OPENAI_API_KEY",
        "KWIKI_INGEST_PROVIDER",
        "KWIKI_INGEST_MODEL",
        "KWIKI_QA_PROVIDER",
        "KWIKI_QA_MODEL",
    ):
        monkeypatch.delenv(key, raising=False)

    settings = Settings.from_root(root)
    ingest_provider = build_provider(settings, purpose="ingest")
    qa_provider = build_provider(settings, purpose="qa")

    assert ingest_provider is not None
    assert ingest_provider.name == "gemini"
    assert ingest_provider.model == "gemini-2.5-flash-lite"
    assert qa_provider is not None
    assert qa_provider.name == "openai_compatible"
    assert qa_provider.model == "gpt-5.4-mini"


def test_gemini_provider_supports_text_and_file_inputs(monkeypatch, tmp_path: Path) -> None:
    class FakeResponse:
        def __init__(self, text: str) -> None:
            self.text = text

        def model_dump(self, **_: object) -> dict[str, object]:
            return {"text": self.text}

    class FakeUploaded:
        def __init__(self, name: str) -> None:
            self.name = name

    class FakeFiles:
        def __init__(self) -> None:
            self.deleted: list[str] = []

        def upload(self, *, file: str):
            return FakeUploaded(f"uploaded:{Path(file).name}")

        def delete(self, *, name: str) -> None:
            self.deleted.append(name)

    class FakeModels:
        def __init__(self) -> None:
            self.calls: list[tuple[str, object, object]] = []

        def generate_content(self, *, model: str, contents, config=None):
            self.calls.append((model, contents, config))
            return FakeResponse("Gemini output")

    fake_files = FakeFiles()
    fake_models = FakeModels()

    class FakeClient:
        def __init__(self, *, api_key: str) -> None:
            self.api_key = api_key
            self.files = fake_files
            self.models = fake_models

    monkeypatch.setattr("knowledge_wiki.providers.gemini.genai", type("FakeGenai", (), {"Client": FakeClient}))

    root = tmp_path / "repo"
    root.mkdir()
    (root / ".env").write_text(
        "GEMINI_API_KEY=test-gemini\nKWIKI_INGEST_PROVIDER=gemini\nKWIKI_INGEST_MODEL=gemini-2.5-flash-lite\n",
        encoding="utf-8",
    )
    file_path = root / "sample.txt"
    file_path.write_text("sample", encoding="utf-8")

    settings = Settings.from_root(root)
    provider = build_provider(settings, purpose="ingest")
    assert provider is not None

    text_result = provider.generate("hello", system_prompt="system")
    file_result = provider.generate_with_files("summarize", files=[file_path], system_prompt="system")

    assert text_result.text == "Gemini output"
    assert file_result.text == "Gemini output"
    assert fake_models.calls[0][0] == "gemini-2.5-flash-lite"
    assert fake_models.calls[1][0] == "gemini-2.5-flash-lite"
    assert fake_files.deleted == ["uploaded:sample.txt"]


def test_query_without_published_hits_reports_wiki_only_insufficiency(settings) -> None:
    for index in range(4):
        source_path = settings.raw_dir / f"source-{index}.txt"
        source_path.write_text("proof induction logic", encoding="utf-8")
        manifest = SourceManifest(
            source_id=f"source-{index}",
            title=f"Source {index}",
            kind="text",
            origin="manual",
            scope="general",
            file_path=f"raw/source-{index}.txt",
            checksum=f"checksum-{index}",
            ingest_status="registered",
            created_at=utc_now(),
            updated_at=utc_now(),
        )
        save_source_manifest(settings, manifest)

    answer = QueryWorkflow(settings).answer("logic proof induction")

    assert answer.raw_fallback_used is False
    assert not answer.hits
    assert "published wiki" in answer.answer_markdown.lower()


def test_lint_reports_semantic_course_findings(settings) -> None:
    save_source_manifest(
        settings,
        SourceManifest(
            source_id="hub-source",
            title="Hub Source",
            kind="markdown",
            origin="manual",
            scope="course/Y1S1/ACC1701X",
            file_path="raw/hub-source.md",
            checksum="hub",
            ingest_status="published",
            created_at="2026-04-01T00:00:00+00:00",
            updated_at="2026-04-01T00:00:00+00:00",
        ),
    )
    save_source_manifest(
        settings,
        SourceManifest(
            source_id="lecture-01",
            title="Lecture 01",
            kind="markdown",
            origin="manual",
            scope="course/Y1S1/ACC1701X",
            file_path="raw/lecture-01.md",
            checksum="lecture-01",
            ingest_status="published",
            created_at="2026-04-01T00:00:00+00:00",
            updated_at="2026-05-01T00:00:00+00:00",
        ),
    )
    save_source_manifest(
        settings,
        SourceManifest(
            source_id="induction",
            title="Induction Notes",
            kind="markdown",
            origin="manual",
            scope="general",
            file_path="raw/induction.md",
            checksum="induction",
            ingest_status="published",
            created_at="2026-04-01T00:00:00+00:00",
            updated_at="2026-04-01T00:00:00+00:00",
        ),
    )
    save_source_manifest(
        settings,
        SourceManifest(
            source_id="topic-a",
            title="Topic A",
            kind="markdown",
            origin="manual",
            scope="general",
            file_path="raw/topic-a.md",
            checksum="topic-a",
            ingest_status="published",
            created_at="2026-04-01T00:00:00+00:00",
            updated_at="2026-04-01T00:00:00+00:00",
        ),
    )
    save_source_manifest(
        settings,
        SourceManifest(
            source_id="topic-b",
            title="Topic B",
            kind="markdown",
            origin="manual",
            scope="general",
            file_path="raw/topic-b.md",
            checksum="topic-b",
            ingest_status="published",
            created_at="2026-04-01T00:00:00+00:00",
            updated_at="2026-04-01T00:00:00+00:00",
        ),
    )
    save_source_manifest(
        settings,
        SourceManifest(
            source_id="topic-c",
            title="Topic C",
            kind="markdown",
            origin="manual",
            scope="general",
            file_path="raw/topic-c.md",
            checksum="topic-c",
            ingest_status="published",
            created_at="2026-04-01T00:00:00+00:00",
            updated_at="2026-04-01T00:00:00+00:00",
        ),
    )
    pages = [
        (
            settings.root_dir / "wiki/courses/y1s1/acc1701x/index.md",
            WikiPage(
                page_id="y1s1-acc1701x-hub",
                title="ACC1701X",
                page_type="course",
                page_kind="hub",
                module_id="y1s1-acc1701x",
                parent_page_id="",
                batch_id="batch-1",
                status="canonical",
                summary="Accounting module hub.",
                aliases=[],
                tags=["course"],
                related=[],
                source_refs=["hub-source#section-1"],
                topics=["accounting"],
                source_count=1,
                lecture_number=None,
                last_compiled_at=utc_now(),
                body="# ACC1701X\n",
            ),
        ),
        (
            settings.root_dir / "wiki/courses/y1s1/acc1701x/topics/lecture-01.md",
            WikiPage(
                page_id="y1s1-acc1701x-lecture-01",
                title="Lecture 01: Intro",
                page_type="concept",
                page_kind="topic",
                module_id="y1s1-acc1701x",
                parent_page_id="y1s1-acc1701x-hub",
                batch_id="batch-1",
                status="canonical",
                summary="Intro lecture.",
                aliases=[],
                tags=["course"],
                related=["missing-page"],
                source_refs=["lecture-01#section-1"],
                topics=["induction", "logic"],
                source_count=1,
                lecture_number=1,
                last_compiled_at="2026-04-10T00:00:00+00:00",
                body="# Lecture 01\n\n## Induction\n\nIntro [source:lecture-01#section-1]\n",
            ),
        ),
        (
            settings.root_dir / "wiki/concepts/induction-overview.md",
            WikiPage(
                page_id="induction-overview",
                title="Induction Overview",
                page_type="concept",
                page_kind="topic",
                module_id="",
                parent_page_id="",
                batch_id="seed",
                status="canonical",
                summary="Induction overview.",
                aliases=[],
                tags=["concept"],
                related=[],
                source_refs=["induction#section-1"],
                topics=["induction"],
                source_count=1,
                lecture_number=None,
                last_compiled_at=utc_now(),
                body="# Induction Overview\n",
            ),
        ),
        (
            settings.root_dir / "wiki/concepts/induction-examples.md",
            WikiPage(
                page_id="induction-examples",
                title="Induction Examples",
                page_type="concept",
                page_kind="topic",
                module_id="",
                parent_page_id="",
                batch_id="seed",
                status="canonical",
                summary="Examples of induction.",
                aliases=[],
                tags=["concept"],
                related=[],
                source_refs=["induction#section-2"],
                topics=["induction"],
                source_count=1,
                lecture_number=None,
                last_compiled_at=utc_now(),
                body="# Induction Examples\n",
            ),
        ),
        (
            settings.root_dir / "wiki/concepts/topic-a-overview.md",
            WikiPage(
                page_id="topic-a-overview",
                title="Topic A Overview",
                page_type="concept",
                page_kind="topic",
                module_id="",
                parent_page_id="",
                batch_id="seed",
                status="canonical",
                summary="This method always requires normalization.",
                aliases=[],
                tags=["concept"],
                related=[],
                source_refs=["topic-a#section-1"],
                topics=["latent-space"],
                source_count=1,
                lecture_number=None,
                last_compiled_at=utc_now(),
                body="# Topic A Overview\n\nNormalization is always required.\n",
            ),
        ),
        (
            settings.root_dir / "wiki/concepts/topic-b-counterexample.md",
            WikiPage(
                page_id="topic-b-counterexample",
                title="Topic B Counterexample",
                page_type="concept",
                page_kind="topic",
                module_id="",
                parent_page_id="",
                batch_id="seed",
                status="canonical",
                summary="This method is not always required.",
                aliases=[],
                tags=["concept"],
                related=[],
                source_refs=["topic-b#section-1"],
                topics=["latent-space"],
                source_count=1,
                lecture_number=None,
                last_compiled_at=utc_now(),
                body="# Topic B Counterexample\n\nNormalization is not always required.\n",
            ),
        ),
        (
            settings.root_dir / "wiki/concepts/topic-c-notes.md",
            WikiPage(
                page_id="topic-c-notes",
                title="Topic C Notes",
                page_type="concept",
                page_kind="topic",
                module_id="",
                parent_page_id="",
                batch_id="seed",
                status="canonical",
                summary="Additional latent-space notes.",
                aliases=[],
                tags=["concept"],
                related=[],
                source_refs=["topic-c#section-1"],
                topics=["latent-space"],
                source_count=1,
                lecture_number=None,
                last_compiled_at=utc_now(),
                body="# Topic C Notes\n",
            ),
        ),
    ]
    for path, page in pages:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_page(page), encoding="utf-8")

    findings = LintWorkflow(settings).run()
    kinds = {finding.kind for finding in findings}

    assert "missing_related_target" in kinds
    assert "weak_source_coverage" in kinds
    assert "missing_cross_links" in kinds
    assert "stale_page_coverage" in kinds
    assert "possible_contradiction" in kinds
    assert "missing_concept_page" in kinds
    assert "research_gap" in kinds


def test_ingest_requires_provider_with_file_inputs(settings) -> None:
    with pytest.raises(ValueError, match="configured provider with file-input support"):
        IngestWorkflow(settings, provider=None).ingest()
