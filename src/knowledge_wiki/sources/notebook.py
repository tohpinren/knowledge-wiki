from __future__ import annotations

import json

from ..models import ExtractedSource, SourceManifest, SourceSection
from .base import SourceAdapter, resolve_source_path


class NotebookSourceAdapter(SourceAdapter):
    kind = "notebook"

    def extract(self, manifest: SourceManifest, *, root_dir) -> ExtractedSource:
        path = resolve_source_path(manifest, root_dir=root_dir)
        payload = json.loads(path.read_text(encoding="utf-8"))
        sections: list[SourceSection] = []
        text_parts: list[str] = []
        counter = 1
        for cell in payload.get("cells", []):
            cell_type = str(cell.get("cell_type", "cell"))
            source = "".join(cell.get("source", []))
            if not source.strip():
                continue
            heading = "Markdown Cell" if cell_type == "markdown" else "Code Cell"
            section_id = f"{cell_type}-{counter}"
            sections.append(
                SourceSection(section_id=section_id, heading=heading, text=source.strip())
            )
            text_parts.append(f"{heading}\n{source.strip()}")
            counter += 1
        text = "\n\n".join(text_parts)
        return ExtractedSource(
            manifest=manifest,
            title=manifest.title,
            text=text.strip(),
            sections=sections
            or [SourceSection(section_id="cell-1", heading="Notebook", text="Empty notebook")],
        )
