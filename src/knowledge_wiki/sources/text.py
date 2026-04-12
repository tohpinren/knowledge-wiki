from __future__ import annotations

from ..models import ExtractedSource, SourceManifest
from .base import SourceAdapter, build_single_section, infer_title_from_markdown, read_text_file, resolve_source_path, split_markdown_sections


class TextSourceAdapter(SourceAdapter):
    kind = "text"

    def extract(self, manifest: SourceManifest, *, root_dir) -> ExtractedSource:
        path = resolve_source_path(manifest, root_dir=root_dir)
        text = read_text_file(path)
        title = infer_title_from_markdown(text, fallback=manifest.title)
        sections = split_markdown_sections(text) if "#" in text else build_single_section(text, heading="Document")
        return ExtractedSource(
            manifest=manifest,
            title=title,
            text=text.strip(),
            sections=sections,
        )
