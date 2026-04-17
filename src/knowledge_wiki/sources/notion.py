from __future__ import annotations

from pathlib import Path

from ..models import ExtractedSource, SourceManifest
from .base import (
    SourceAdapter,
    infer_title_from_markdown,
    resolve_source_path,
    split_markdown_sections,
)


class NotionSourceAdapter(SourceAdapter):
    kind = "notion"

    def extract(self, manifest: SourceManifest, *, root_dir: Path) -> ExtractedSource:
        path = resolve_source_path(manifest, root_dir=root_dir)
        if path.is_dir():
            markdown_files = sorted(path.rglob("*.md"))
            text = "\n\n".join(file.read_text(encoding="utf-8") for file in markdown_files)
        else:
            text = path.read_text(encoding="utf-8")
        title = infer_title_from_markdown(text, fallback=manifest.title)
        return ExtractedSource(
            manifest=manifest,
            title=title,
            text=text.strip(),
            sections=split_markdown_sections(text, default_heading="Notion Export"),
        )
