from __future__ import annotations

import argparse

from .bootstrap import bootstrap_repository
from .config import Settings
from .progress import CliProgressReporter
from .providers import build_provider
from .ui import launch_app
from .workflows import IngestWorkflow, LintWorkflow, QueryWorkflow, ReviewWorkflow


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Knowledge Wiki operator CLI.")
    parser.add_argument("--root", default=".", help="Repository root.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init", help="Create the repository scaffold if missing.")

    register_parser = subparsers.add_parser("register-source", help="Register a source manifest.")
    register_parser.add_argument("path", help="Path to a file or export directory under raw/.")
    register_parser.add_argument(
        "--kind",
        required=True,
        choices=["markdown", "notion", "pdf", "office", "html", "notebook", "code", "text"],
    )
    register_parser.add_argument("--title")
    register_parser.add_argument("--origin", default="manual")
    register_parser.add_argument("--scope", default="general")

    ingest_parser = subparsers.add_parser(
        "ingest", help="Generate wiki updates from registered sources."
    )
    ingest_parser.add_argument("--source-id", action="append", default=[])

    ingest_course_parser = subparsers.add_parser(
        "ingest-course", help="Recursively ingest a course/module directory."
    )
    ingest_course_parser.add_argument("path", help="Path like raw/Y1S1/CS1231S")
    ingest_course_parser.add_argument("--term")
    ingest_course_parser.add_argument("--module-code")

    query_parser = subparsers.add_parser("query", help="Answer a question from the wiki.")
    query_parser.add_argument("question")
    query_parser.add_argument(
        "--save-synthesis",
        action="store_true",
        help="Save the suggested synthesis page if one is generated.",
    )

    layouts_parser = subparsers.add_parser("layouts", help="List layout review artifacts.")
    layouts_parser.add_argument("--state", choices=["pending", "approved", "rejected"])
    layouts_parser.add_argument("--module-id")
    layouts_parser.add_argument("--batch-id")

    show_layout_parser = subparsers.add_parser(
        "show-layout", help="Show a human-readable layout review."
    )
    show_layout_parser.add_argument("layout_id")

    revise_layout_parser = subparsers.add_parser(
        "revise-layout", help="Revise a layout with reviewer feedback."
    )
    revise_layout_parser.add_argument("layout_id")
    revise_layout_parser.add_argument("--feedback", required=True)

    revise_page_parser = subparsers.add_parser(
        "revise-page", help="Revise a published wiki page with reviewer feedback."
    )
    revise_page_parser.add_argument("page")
    revise_page_parser.add_argument("--feedback", required=True)

    approve_layout_parser = subparsers.add_parser(
        "approve-layout", help="Approve a course layout review."
    )
    approve_layout_parser.add_argument("layout_id")

    reject_layout_parser = subparsers.add_parser(
        "reject-layout", help="Reject a course layout review."
    )
    reject_layout_parser.add_argument("layout_id")

    subparsers.add_parser("lint", help="Run semantic and structural lint checks.")

    ui_parser = subparsers.add_parser("ui", help="Launch the Gradio review UI.")
    ui_parser.add_argument("--host", default="127.0.0.1")
    ui_parser.add_argument("--port", default=7860, type=int)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    settings = Settings.from_root(args.root)
    progress = CliProgressReporter(args.command)
    progress.start(str(settings.root_dir))

    try:
        exit_code = _run_command(args, settings, progress.emit)
    except Exception as exc:
        progress.fail(exc)
        raise

    progress.finish()
    return exit_code


def _run_command(args, settings: Settings, progress) -> int:
    if args.command == "init":
        progress("Ensuring repository scaffold exists.")
        bootstrap_repository(settings)
        print(f"Initialized knowledge wiki scaffold at {settings.root_dir}")
        return 0

    if args.command == "register-source":
        workflow = IngestWorkflow(settings, provider=None, progress=progress)
        manifest = workflow.register_source(
            args.path,
            kind=args.kind,
            title=args.title,
            origin=args.origin,
            scope=args.scope,
        )
        print(f"Registered {manifest.source_id} -> {manifest.file_path}")
        return 0

    if args.command == "ingest":
        provider = build_provider(settings, purpose="ingest")
        _report_provider_settings(progress, settings, purpose="ingest", provider=provider)
        workflow = IngestWorkflow(settings, provider=provider, progress=progress)
        proposals = workflow.ingest(source_ids=args.source_id or None)
        if not proposals:
            print("No sources were ingested.")
            return 0
        for proposal in proposals:
            print(f"{proposal.draft_id}: {proposal.target_page} [{proposal.proposal_type}]")
        return 0

    if args.command == "ingest-course":
        provider = build_provider(settings, purpose="ingest")
        _report_provider_settings(progress, settings, purpose="ingest", provider=provider)
        workflow = IngestWorkflow(settings, provider=provider, progress=progress)
        result = workflow.ingest_course(
            args.path,
            term=args.term,
            module_code=args.module_code,
        )
        print(f"Module: {result.module_manifest.module_id}")
        print(f"Batch: {result.module_manifest.batch_id}")
        print(f"Status: {result.module_manifest.status}")
        print(f"Evidence artifacts: {len(result.evidence_artifacts)}")
        if result.layout_review:
            print(
                f"Layout: {result.layout_review.layout_id} [{result.layout_review.approval_state}]"
            )
            print(f"Planned pages: {len(result.draft_proposals)}")
        else:
            print("Layout: not created")
        return 0

    if args.command == "query":
        provider = build_provider(settings, purpose="qa")
        _report_provider_settings(progress, settings, purpose="qa", provider=provider)
        workflow = QueryWorkflow(settings, provider=provider, progress=progress)
        answer = workflow.answer(args.question)
        print(answer.answer_markdown)
        if answer.suggested_synthesis:
            suggestion = answer.suggested_synthesis
            print("\n---\n")
            print("Suggested synthesis page:")
            print(f"- Title: {suggestion.title}")
            print(f"- Path: {suggestion.path}")
            print(f"- Summary: {suggestion.summary}")
            if args.save_synthesis:
                saved_path, created = workflow.save_synthesis(suggestion)
                if created:
                    print(f"- Saved: {saved_path}")
                else:
                    print(f"- Already exists: {saved_path}")
        elif args.save_synthesis:
            print("\nNo synthesis suggestion was generated.")
        return 0

    if args.command == "layouts":
        workflow = ReviewWorkflow(settings, provider=None, progress=progress)
        layouts = workflow.list_layouts(
            state=args.state, module_id=args.module_id, batch_id=args.batch_id
        )
        if not layouts:
            print("No layouts found.")
            return 0
        for layout in layouts:
            print(
                f"{layout.layout_id}: {layout.approval_state} -> {layout.module_id} [{len(layout.pages)} pages]"
            )
        return 0

    if args.command == "show-layout":
        workflow = ReviewWorkflow(settings, provider=None, progress=progress)
        inspection = workflow.inspect_layout(args.layout_id)
        print(inspection["summary_markdown"])
        return 0

    if args.command == "revise-page":
        provider = build_provider(settings, purpose="ingest")
        _report_provider_settings(progress, settings, purpose="ingest", provider=provider)
        workflow = ReviewWorkflow(settings, provider=provider, progress=progress)
        page_path, page = workflow.revise_page(args.page, args.feedback)
        print(f"Revised {page_path} [{page.title}]")
        return 0

    if args.command == "approve-layout":
        workflow = ReviewWorkflow(settings, provider=None, progress=progress)
        layout = workflow.approve_layout(args.layout_id)
        published_count = int(layout.metadata.get("auto_published_draft_count", 0))
        print(f"Approved {layout.layout_id} and published {published_count} page(s)")
        return 0

    if args.command == "reject-layout":
        workflow = ReviewWorkflow(settings, provider=None, progress=progress)
        layout = workflow.reject_layout(args.layout_id)
        print(f"Rejected {layout.layout_id}")
        return 0

    if args.command == "revise-layout":
        provider = build_provider(settings, purpose="ingest")
        _report_provider_settings(progress, settings, purpose="ingest", provider=provider)
        workflow = ReviewWorkflow(settings, provider=provider, progress=progress)
        layout = workflow.revise_layout(args.layout_id, args.feedback)
        print(f"Revised {layout.layout_id}")
        return 0

    if args.command == "lint":
        workflow = LintWorkflow(settings, progress=progress)
        findings = workflow.run()
        print(workflow.render_markdown(findings))
        return 0

    if args.command == "ui":
        progress(f"Launching review UI on http://{args.host}:{args.port}.")
        launch_app(args.root, host=args.host, port=args.port)
        return 0

    raise ValueError(f"Unsupported command: {args.command}")


def _report_provider_settings(progress, settings: Settings, *, purpose: str, provider) -> None:
    provider_name = settings.provider_name_for(purpose)
    model_name = settings.model_name_for(purpose)
    if purpose == "ingest":
        progress(
            f"Configured {purpose} provider {provider_name}/{model_name} with concurrency={settings.ingest_concurrency}."
        )
    else:
        progress(f"Configured {purpose} provider {provider_name}/{model_name}.")
    if provider is None:
        progress(
            f"No initialized client is available for {purpose}; command will use fallback behavior if supported."
        )
