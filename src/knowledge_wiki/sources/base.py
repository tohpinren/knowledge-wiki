from __future__ import annotations

import re
from abc import ABC, abstractmethod
from pathlib import Path

from ..models import ExtractedSource, SourceManifest, SourceSection

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


class SourceAdapter(ABC):
    kind = "base"

    @abstractmethod
    def extract(self, manifest: SourceManifest, *, root_dir: Path) -> ExtractedSource:
        raise NotImplementedError


class SourceRegistry:
    def __init__(self, adapters: list[SourceAdapter]) -> None:
        self._adapters = {adapter.kind: adapter for adapter in adapters}

    def for_kind(self, kind: str) -> SourceAdapter:
        if kind not in self._adapters:
            raise ValueError(f"No source adapter registered for kind: {kind}")
        return self._adapters[kind]

    @property
    def kinds(self) -> set[str]:
        return set(self._adapters)


def resolve_source_path(manifest: SourceManifest, *, root_dir: Path) -> Path:
    path = root_dir / manifest.file_path
    if not path.exists():
        raise FileNotFoundError(f"Source file does not exist: {path}")
    return path


def read_text_file(path: Path) -> str:
    for encoding in ("utf-8", "utf-16", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="ignore")


def infer_title_from_markdown(text: str, *, fallback: str) -> str:
    for line in text.splitlines():
        match = HEADING_RE.match(line.strip())
        if match and len(match.group(1)) == 1:
            return match.group(2).strip()
    return fallback


def split_markdown_sections(text: str, *, default_heading: str = "Overview") -> list[SourceSection]:
    sections: list[SourceSection] = []
    current_heading = default_heading
    current_lines: list[str] = []
    counter = 1

    def flush() -> None:
        nonlocal counter, current_lines
        body = "\n".join(current_lines).strip()
        if not body:
            return
        sections.append(
            SourceSection(
                section_id=f"section-{counter}",
                heading=current_heading,
                text=body,
            )
        )
        counter += 1
        current_lines = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        match = HEADING_RE.match(line.strip())
        if match:
            flush()
            current_heading = match.group(2).strip()
            continue
        current_lines.append(line)
    flush()

    if not sections:
        stripped = text.strip()
        sections.append(
            SourceSection(
                section_id="section-1",
                heading=default_heading,
                text=stripped or default_heading,
            )
        )
    return sections


def build_single_section(
    text: str, *, heading: str = "Overview", section_id: str = "section-1"
) -> list[SourceSection]:
    stripped = text.strip()
    return [SourceSection(section_id=section_id, heading=heading, text=stripped or heading)]
