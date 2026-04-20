from __future__ import annotations

import knowledge_wiki.cli as cli

from .conftest import write_notebook, write_text_pdf


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


def test_cli_init_logs_progress_to_stderr(tmp_path, capsys) -> None:
    root = tmp_path / "knowledge-wiki"

    exit_code = cli.main(["--root", str(root), "init"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Initialized knowledge wiki scaffold" in captured.out
    assert "[kwiki:init] Starting in" in captured.err
    assert "[kwiki:init] Ensuring repository scaffold exists." in captured.err
    assert "[kwiki:init] Completed in" in captured.err
    assert root.joinpath(".obsidian/app.json").exists()
    assert root.joinpath(".obsidian/core-plugins.json").exists()
    assert root.joinpath("raw/assets/.gitkeep").exists()


def test_cli_ingest_course_logs_progress_to_stderr(
    settings, scripted_provider, monkeypatch, capsys
) -> None:
    _build_course_tree(settings)
    monkeypatch.setattr(cli, "build_provider", lambda settings, purpose="qa": scripted_provider)

    exit_code = cli.main(
        [
            "--root",
            str(settings.root_dir),
            "ingest-course",
            str(settings.raw_dir / "Y1S1" / "CS1231S"),
        ]
    )

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Module: y1s1-cs1231s" in captured.out
    assert "Layout: layout-y1s1-cs1231s-" in captured.out
    assert "[kwiki:ingest-course] Configured ingest provider" in captured.err
    assert (
        "[kwiki:ingest-course] Discovering supported files under raw/Y1S1/CS1231S." in captured.err
    )
    assert "[kwiki:ingest-course] Found 4 usable file(s) and 0 skipped file(s)." in captured.err
    assert "concurrency=" in captured.err
    assert "Saved evidence" in captured.err
    assert "[kwiki:ingest-course] Planning layout from 4 evidence artifact(s)." in captured.err
    assert "[kwiki:ingest-course] Drafting 2 page(s) for layout review." in captured.err
    assert "[kwiki:ingest-course] Completed in" in captured.err


def test_cli_show_layout_renders_readable_summary(
    settings, scripted_provider, monkeypatch, capsys
) -> None:
    _build_course_tree(settings)
    monkeypatch.setattr(cli, "build_provider", lambda settings, purpose="qa": scripted_provider)

    cli.main(
        [
            "--root",
            str(settings.root_dir),
            "ingest-course",
            str(settings.raw_dir / "Y1S1" / "CS1231S"),
        ]
    )
    captured = capsys.readouterr()
    layout_line = next(line for line in captured.out.splitlines() if line.startswith("Layout: "))
    layout_id = layout_line.split()[1]

    exit_code = cli.main(["--root", str(settings.root_dir), "show-layout", layout_id])

    shown = capsys.readouterr()
    assert exit_code == 0
    assert "# CS1231S Layout Review" in shown.out
    assert "## Page Plan" in shown.out
    assert "`core-concepts` [topic]" in shown.out


def test_cli_help_omits_legacy_draft_review_commands() -> None:
    parser = cli.build_parser()

    help_text = parser.format_help()

    assert "drafts" not in help_text
    assert "show-draft" not in help_text
    assert "approve-draft" not in help_text
    assert "reject-draft" not in help_text
    assert "revise-draft" not in help_text


def test_cli_revise_page_updates_canonical_markdown(
    settings, scripted_provider, monkeypatch, capsys
) -> None:
    _build_course_tree(settings)
    monkeypatch.setattr(cli, "build_provider", lambda settings, purpose="qa": scripted_provider)

    cli.main(
        [
            "--root",
            str(settings.root_dir),
            "ingest-course",
            str(settings.raw_dir / "Y1S1" / "CS1231S"),
        ]
    )
    layout_out = capsys.readouterr()
    layout_id = next(
        line.split()[1] for line in layout_out.out.splitlines() if line.startswith("Layout: ")
    )

    cli.main(["--root", str(settings.root_dir), "approve-layout", layout_id])
    capsys.readouterr()

    topic_path = "wiki/courses/y1s1/cs1231s/topics/core-concepts.md"
    exit_code = cli.main(
        [
            "--root",
            str(settings.root_dir),
            "revise-page",
            topic_path,
            "--feedback",
            "Tighten the explanation and make the evidence callout clearer.",
        ]
    )

    captured = capsys.readouterr()
    assert exit_code == 0
    assert f"Revised {topic_path} [Core Concepts]" in captured.out
    assert "Applied reviewer feedback" in settings.root_dir.joinpath(topic_path).read_text(
        encoding="utf-8"
    )


def test_cli_query_can_save_suggested_synthesis(
    settings, scripted_provider, monkeypatch, capsys
) -> None:
    _build_course_tree(settings)
    monkeypatch.setattr(cli, "build_provider", lambda settings, purpose="qa": scripted_provider)

    cli.main(
        [
            "--root",
            str(settings.root_dir),
            "ingest-course",
            str(settings.raw_dir / "Y1S1" / "CS1231S"),
        ]
    )
    layout_out = capsys.readouterr()
    layout_id = next(
        line.split()[1] for line in layout_out.out.splitlines() if line.startswith("Layout: ")
    )

    cli.main(["--root", str(settings.root_dir), "approve-layout", layout_id])
    capsys.readouterr()

    exit_code = cli.main(
        [
            "--root",
            str(settings.root_dir),
            "query",
            "How do proofs and induction show up in this course?",
            "--save-synthesis",
        ]
    )

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Suggested synthesis page:" in captured.out
    assert "- Saved: wiki/syntheses/reusable-query-insight.md" in captured.out
    assert settings.root_dir.joinpath("wiki/syntheses/reusable-query-insight.md").exists()
