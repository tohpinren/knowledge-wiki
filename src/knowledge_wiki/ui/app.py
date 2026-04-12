from __future__ import annotations

from ..config import Settings
from ..providers import build_provider
from ..workflows import LintWorkflow, QueryWorkflow, ReviewWorkflow


def build_app(root_dir: str | None = None):
    try:
        import gradio as gr
    except ImportError as exc:
        raise RuntimeError("Gradio is not installed. Install with `pip install .[ui]`.") from exc

    settings = Settings.from_root(root_dir)
    qa_provider = build_provider(settings, purpose="qa")
    ingest_provider = build_provider(settings, purpose="ingest")
    query_workflow = QueryWorkflow(settings, provider=qa_provider)
    review_workflow = ReviewWorkflow(settings, provider=ingest_provider)
    lint_workflow = LintWorkflow(settings)

    def layout_choices() -> list[str]:
        return [
            layout.layout_id
            for layout in review_workflow.list_layouts()
            if layout.approval_state == "pending"
        ]

    def page_choices() -> list[tuple[str, str]]:
        return [
            (entry["choice_label"], entry["path"])
            for entry in review_workflow.list_pages()
        ]

    def run_query(question: str):
        answer = query_workflow.answer(question)
        suggestion = answer.suggested_synthesis.to_dict() if answer.suggested_synthesis else {}
        suggestion_body = answer.suggested_synthesis.body if answer.suggested_synthesis else ""
        return answer.answer_markdown, [hit.to_dict() for hit in answer.hits], suggestion, suggestion_body

    def inspect_layout(layout_id: str):
        if not layout_id:
            return "", [], {}
        inspection = review_workflow.inspect_layout(layout_id)
        return inspection["summary_markdown"], inspection["page_rows"], inspection["raw_payload"]

    def inspect_page(page_path: str):
        if not page_path:
            return "", [], {}, ""
        inspection = review_workflow.inspect_page(page_path)
        return (
            inspection["summary_markdown"],
            inspection["evidence_rows"],
            inspection["raw_payload"],
            inspection["proposed_markdown"],
        )

    def approve_layout(layout_id: str):
        if not layout_id:
            return (
                "Select a layout first.",
                gr.update(choices=layout_choices()),
                gr.update(choices=page_choices()),
            )
        try:
            layout = review_workflow.approve_layout(layout_id)
        except Exception as exc:
            return (
                f"Error: {exc}",
                gr.update(choices=layout_choices()),
                gr.update(choices=page_choices()),
            )
        return (
            f"Approved `{layout.layout_id}` and published "
            f"{int(layout.metadata.get('auto_published_draft_count', 0))} page(s).",
            gr.update(choices=layout_choices(), value=None),
            gr.update(choices=page_choices(), value=None),
        )

    def reject_layout(layout_id: str):
        if not layout_id:
            return (
                "Select a layout first.",
                gr.update(choices=layout_choices()),
                gr.update(choices=page_choices()),
            )
        try:
            layout = review_workflow.reject_layout(layout_id)
        except Exception as exc:
            return (
                f"Error: {exc}",
                gr.update(choices=layout_choices()),
                gr.update(choices=page_choices()),
            )
        return (
            f"Rejected `{layout.layout_id}`.",
            gr.update(choices=layout_choices(), value=layout.layout_id),
            gr.update(choices=page_choices(), value=None),
        )

    def revise_layout(layout_id: str, feedback: str):
        if not layout_id:
            return (
                "Select a layout first.",
                gr.update(choices=layout_choices()),
                gr.update(choices=page_choices()),
                "",
                [],
                {},
                feedback,
            )
        if not feedback.strip():
            return (
                "Enter revision feedback first.",
                gr.update(choices=layout_choices()),
                gr.update(choices=page_choices()),
                "",
                [],
                {},
                feedback,
            )
        try:
            layout = review_workflow.revise_layout(layout_id, feedback)
        except Exception as exc:
            return (
                f"Error: {exc}",
                gr.update(choices=layout_choices()),
                gr.update(choices=page_choices()),
                "",
                [],
                {},
                feedback,
            )
        inspection = review_workflow.inspect_layout(layout.layout_id)
        return (
            f"Revised `{layout.layout_id}`.",
            gr.update(choices=layout_choices(), value=layout.layout_id),
            gr.update(choices=page_choices(), value=None),
            inspection["summary_markdown"],
            inspection["page_rows"],
            inspection["raw_payload"],
            "",
        )

    def revise_page(page_path: str, feedback: str):
        if not page_path:
            return "Select a page first.", gr.update(choices=page_choices()), "", [], {}, "", feedback
        if not feedback.strip():
            return "Enter revision feedback first.", gr.update(choices=page_choices()), "", [], {}, "", feedback
        try:
            revised_path, page = review_workflow.revise_page(page_path, feedback)
        except Exception as exc:
            return f"Error: {exc}", gr.update(choices=page_choices()), "", [], {}, "", feedback
        inspection = review_workflow.inspect_page(revised_path)
        return (
            f"Revised `{revised_path}` [{page.title}].",
            gr.update(choices=page_choices(), value=revised_path),
            inspection["summary_markdown"],
            inspection["evidence_rows"],
            inspection["raw_payload"],
            inspection["proposed_markdown"],
            "",
        )

    def run_lint():
        findings = lint_workflow.run()
        return lint_workflow.render_markdown(findings), [finding.to_dict() for finding in findings]

    with gr.Blocks(title="Knowledge Wiki") as app:
        gr.Markdown("# Knowledge Wiki")
        with gr.Tab("Query"):
            question = gr.Textbox(label="Question", lines=4, placeholder="How does normalization compare across my database and ML notes?")
            query_button = gr.Button("Ask")
            answer_markdown = gr.Markdown(label="Answer")
            evidence_json = gr.JSON(label="Evidence")
            suggestion_json = gr.JSON(label="Suggested synthesis")
            suggestion_body = gr.Textbox(label="Suggested synthesis body", lines=12)

        with gr.Tab("Layout Review"):
            pending_layouts = gr.Dropdown(label="Pending layouts", choices=layout_choices())
            refresh_layouts = gr.Button("Refresh layouts")
            layout_summary = gr.Markdown(label="Layout summary")
            layout_pages = gr.Dataframe(
                headers=["Slug", "Title", "Kind", "Parent", "Refs", "Sources", "Related"],
                datatype=["str", "str", "str", "str", "number", "str", "str"],
                interactive=False,
                wrap=True,
                label="Layout pages",
            )
            layout_json = gr.JSON(label="Raw layout payload")
            layout_feedback = gr.Textbox(label="Revision feedback", lines=4, placeholder="Ask for a different layout or hierarchy.")
            revise_layout_button = gr.Button("Revise layout")
            approve_layout_button = gr.Button("Approve layout")
            reject_layout_button = gr.Button("Reject layout")
            layout_status = gr.Textbox(label="Status")

        with gr.Tab("Pages"):
            published_pages = gr.Dropdown(label="Published pages", choices=page_choices())
            refresh_pages = gr.Button("Refresh pages")
            page_summary = gr.Markdown(label="Page summary")
            page_evidence = gr.Dataframe(
                headers=["Source Ref", "Title", "Path", "Summary"],
                datatype=["str", "str", "str", "str"],
                interactive=False,
                wrap=True,
                label="Page evidence",
            )
            page_json = gr.JSON(label="Raw page payload")
            page_preview = gr.Textbox(label="Current markdown", lines=18)
            page_feedback = gr.Textbox(
                label="Revision feedback",
                lines=4,
                placeholder="Ask for a rewrite or refinement of the published page.",
            )
            revise_page_button = gr.Button("Revise page")
            page_status = gr.Textbox(label="Status")

        with gr.Tab("Lint"):
            lint_button = gr.Button("Run lint")
            lint_markdown = gr.Markdown(label="Findings")
            lint_json = gr.JSON(label="Structured findings")

        query_button.click(
            run_query,
            inputs=[question],
            outputs=[answer_markdown, evidence_json, suggestion_json, suggestion_body],
        )
        pending_layouts.change(
            inspect_layout,
            inputs=[pending_layouts],
            outputs=[layout_summary, layout_pages, layout_json],
        )
        refresh_layouts.click(lambda: gr.update(choices=layout_choices()), outputs=[pending_layouts])
        revise_layout_button.click(
            revise_layout,
            inputs=[pending_layouts, layout_feedback],
            outputs=[layout_status, pending_layouts, published_pages, layout_summary, layout_pages, layout_json, layout_feedback],
        )
        approve_layout_button.click(
            approve_layout,
            inputs=[pending_layouts],
            outputs=[layout_status, pending_layouts, published_pages],
        )
        reject_layout_button.click(
            reject_layout,
            inputs=[pending_layouts],
            outputs=[layout_status, pending_layouts, published_pages],
        )
        published_pages.change(
            inspect_page,
            inputs=[published_pages],
            outputs=[page_summary, page_evidence, page_json, page_preview],
        )
        refresh_pages.click(lambda: gr.update(choices=page_choices()), outputs=[published_pages])
        revise_page_button.click(
            revise_page,
            inputs=[published_pages, page_feedback],
            outputs=[page_status, published_pages, page_summary, page_evidence, page_json, page_preview, page_feedback],
        )
        lint_button.click(run_lint, outputs=[lint_markdown, lint_json])

    return app


def launch_app(root_dir: str | None = None, *, host: str = "127.0.0.1", port: int = 7860) -> None:
    app = build_app(root_dir)
    app.launch(server_name=host, server_port=port, inbrowser=False, share=False)
