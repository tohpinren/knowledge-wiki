from __future__ import annotations

from .config import Settings
from .utils import utc_now

BOOTSTRAP_FILES = {
    "raw/README.md": "# Raw Sources\n\nStore immutable source material here.\n",
    "raw/assets/.gitkeep": "",
    "wiki/README.md": "# Wiki\n\nCanonical markdown knowledge pages live here.\n",
    "wiki/index.md": "# Wiki Index\n\nNo canonical wiki pages have been published yet.\n",
    ".obsidian/app.json": (
        "{\n"
        '  "attachmentFolderPath": "raw/assets",\n'
        '  "alwaysUpdateLinks": true,\n'
        '  "newLinkFormat": "relative",\n'
        '  "promptDelete": false,\n'
        '  "readableLineLength": false,\n'
        '  "showLineNumber": true,\n'
        '  "showUnsupportedFiles": true,\n'
        '  "useMarkdownLinks": true\n'
        "}\n"
    ),
    ".obsidian/core-plugins.json": (
        "[\n"
        '  "file-explorer",\n'
        '  "search",\n'
        '  "outline",\n'
        '  "backlink",\n'
        '  "page-preview",\n'
        '  "graph"\n'
        "]\n"
    ),
    ".obsidian/appearance.json": "{}\n",
    ".obsidian/graph.json": (
        "{\n"
        '  "search": "path:wiki",\n'
        '  "showAttachments": false,\n'
        '  "showTags": false,\n'
        '  "showOrphans": true,\n'
        '  "collapse-filter": false,\n'
        '  "collapse-color-groups": false,\n'
        '  "collapse-display": false,\n'
        '  "groups": []\n'
        "}\n"
    ),
    "system/README.md": (
        "# System\n\n"
        "Operational metadata for the knowledge wiki lives here. This directory mixes canonical policy files "
        "with generated runtime state, so only a small subset should be tracked in git.\n"
    ),
    "system/AGENTS.md": (
        "# Knowledge Wiki Agent Rules\n\n"
        "1. Prefer compiled wiki pages over raw sources when answering questions.\n"
        "2. Query by reading `wiki/index.md` first, then opening the relevant wiki pages.\n"
        "3. Do not write directly to canonical wiki pages outside the review workflow, except for an explicit saved synthesis.\n"
        "4. Every synthesized section should carry stable source tokens.\n"
        "5. Publishing canonical pages must update the wiki index, graph, and system log together.\n"
    ),
    "system/index.md": (
        "# System Index\n\n"
        "## Course Batches\n\n"
        "- Total: 0\n"
        "- Awaiting planning: 0\n"
        "- Layout pending: 0\n"
        "- Layout approved: 0\n"
        "- Drafts pending: 0\n"
        "- Published: 0\n\n"
        "## Source Manifests\n\n"
        "- Total: 0\n"
        "- Registered: 0\n"
        "- Drafted: 0\n"
        "- Published: 0\n\n"
        "## Evidence Artifacts\n\n"
        "- Total: 0\n\n"
        "## Layout Reviews\n\n"
        "- Pending: 0\n"
        "- Approved: 0\n"
        "- Rejected: 0\n\n"
        "## Generated Publish Plans\n\n"
        "- Pending: 0\n"
        "- Approved: 0\n"
        "- Rejected: 0\n\n"
        "## Knowledge Graph\n\n"
        "- Nodes: 0\n"
        "- Edges: 0\n"
    ),
    "system/log.md": f"# Update Log\n\n- {utc_now()} bootstrap: repository scaffold created.\n",
    "system/manifests/README.md": "# Source Manifests\n\nEach raw source is tracked by one JSON manifest.\n",
    "system/manifests/modules/README.md": "# Module Manifests\n\nEach course ingest batch writes one module manifest here.\n",
    "system/evidence/README.md": "# Evidence Artifacts\n\nPer-file evidence summaries for course ingest live here.\n",
    "system/graph/README.md": "# Knowledge Graph\n\nInternal graph artifacts used for query expansion and lint live here.\n",
    "system/metrics/README.md": "# Metrics\n\nStructured operational metrics and usage accounting live here.\n",
    "system/metrics/ingest/README.md": "# Ingest Metrics\n\nPer-batch ingest token and cost accounting lives here.\n",
    "system/reviews/README.md": (
        "# Reviews\n\n"
        "Layout reviews live under `reviews/layouts/`.\n\n"
        "Internal generated publish plans live under `reviews/drafts/`. "
        "They are workflow state, not a user-facing review queue.\n"
    ),
    "system/reviews/layouts/README.md": "# Layout Reviews\n\nEach course ingest batch writes one layout review artifact here.\n",
    "system/cache/.gitignore": "*\n!.gitignore\n",
}


def bootstrap_repository(settings: Settings) -> None:
    settings.ensure_layout()
    for relative_path, content in BOOTSTRAP_FILES.items():
        path = settings.root_dir / relative_path
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
