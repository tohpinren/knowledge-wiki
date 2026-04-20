from __future__ import annotations

from knowledge_wiki.models import WikiPage
from knowledge_wiki.wiki.pages import read_page, write_page
from knowledge_wiki.workflows import IngestWorkflow, QueryWorkflow, ReviewWorkflow

from .conftest import write_notebook, write_text_pdf


def _seed_existing_page(settings) -> None:
    page = WikiPage(
        page_id="proof-techniques",
        title="Proof Techniques",
        page_type="concept",
        page_kind="topic",
        module_id="",
        parent_page_id="",
        batch_id="seed",
        status="canonical",
        summary="Reusable proof strategies across modules.",
        aliases=[],
        tags=["concept"],
        related=[],
        source_refs=["seed-proof#section-1"],
        last_compiled_at="2026-04-06T00:00:00+00:00",
        body="# Proof Techniques\n\nProof by induction appears often [source:seed-proof#section-1]\n",
    )
    write_page(settings.root_dir / "wiki/concepts/proof-techniques.md", page)


def _build_course_tree(settings) -> None:
    course_root = settings.raw_dir / "Y1S1" / "CS1231S"
    (course_root / "lectures").mkdir(parents=True)
    (course_root / "tutorials").mkdir()

    (course_root / "lectures" / "week1.md").write_text(
        "# Week 1\n\nLogic and proofs.", encoding="utf-8"
    )
    (course_root / "lectures" / "week2.html").write_text(
        "<h1>Week 2</h1><p>Induction and recurrence.</p>", encoding="utf-8"
    )
    write_text_pdf(course_root / "lectures" / "slides.pdf", "Sets, relations, and proofs.")
    write_notebook(course_root / "tutorials" / "tutorial1.ipynb")


def _publish_course(settings, scripted_provider) -> None:
    _build_course_tree(settings)
    ingest_result = IngestWorkflow(settings, provider=scripted_provider).ingest_course(
        settings.raw_dir / "Y1S1" / "CS1231S"
    )
    review = ReviewWorkflow(settings)
    review.approve_layout(ingest_result.layout_review.layout_id)


def test_query_uses_published_course_pages_with_citations_and_cross_links(
    settings, scripted_provider
) -> None:
    _seed_existing_page(settings)
    _publish_course(settings, scripted_provider)

    topic_page = read_page(settings.root_dir / "wiki/courses/y1s1/cs1231s/topics/core-concepts.md")
    answer = QueryWorkflow(settings).answer("How do proofs and induction show up in this course?")

    assert "proof-techniques" in topic_page.related
    assert answer.raw_fallback_used is False
    assert len(answer.hits) >= 1
    assert "[source:" in answer.answer_markdown
    assert any(hit.path.startswith("wiki/courses/y1s1/cs1231s/") for hit in answer.hits)
    assert answer.suggested_synthesis is not None
    assert answer.suggested_synthesis.path.startswith("wiki/syntheses/")


def test_query_save_synthesis_writes_canonical_page_and_updates_index(
    settings, scripted_provider
) -> None:
    _seed_existing_page(settings)
    _publish_course(settings, scripted_provider)

    workflow = QueryWorkflow(settings, provider=scripted_provider)
    answer = workflow.answer("How do proofs and induction show up in this course?")

    assert answer.suggested_synthesis is not None

    saved_path, created = workflow.save_synthesis(answer.suggested_synthesis)

    assert created is True
    assert saved_path == "wiki/syntheses/reusable-query-insight.md"
    saved_page = read_page(settings.root_dir / saved_path)
    assert saved_page.page_type == "synthesis"
    assert saved_page.page_kind == "synthesis"
    assert saved_page.status == "canonical"
    assert saved_page.source_refs
    assert "Reusable Query Insight" in settings.wiki_dir.joinpath("index.md").read_text(
        encoding="utf-8"
    )
