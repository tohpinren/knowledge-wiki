from __future__ import annotations

from html.parser import HTMLParser

from ..models import ExtractedSource, SourceManifest
from .base import SourceAdapter, build_single_section, resolve_source_path


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        cleaned = data.strip()
        if cleaned:
            self.chunks.append(cleaned)


class HTMLSourceAdapter(SourceAdapter):
    kind = "html"

    def extract(self, manifest: SourceManifest, *, root_dir) -> ExtractedSource:
        path = resolve_source_path(manifest, root_dir=root_dir)
        parser = _HTMLTextExtractor()
        parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
        text = "\n".join(parser.chunks)
        return ExtractedSource(
            manifest=manifest,
            title=manifest.title,
            text=text.strip(),
            sections=build_single_section(text, heading="HTML Document"),
        )
