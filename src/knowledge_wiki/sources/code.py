from __future__ import annotations

from ..models import ExtractedSource, SourceManifest
from .base import SourceAdapter, build_single_section, read_text_file, resolve_source_path


class CodeSourceAdapter(SourceAdapter):
    kind = "code"

    def extract(self, manifest: SourceManifest, *, root_dir) -> ExtractedSource:
        path = resolve_source_path(manifest, root_dir=root_dir)
        text = read_text_file(path)
        return ExtractedSource(
            manifest=manifest,
            title=manifest.title,
            text=text.strip(),
            sections=build_single_section(text, heading="Source", section_id="source-1"),
        )
