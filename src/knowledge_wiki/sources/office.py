from __future__ import annotations

import subprocess

from ..models import ExtractedSource, SourceManifest
from .base import SourceAdapter, build_single_section, resolve_source_path


class OfficeSourceAdapter(SourceAdapter):
    kind = "office"

    def extract(self, manifest: SourceManifest, *, root_dir) -> ExtractedSource:
        path = resolve_source_path(manifest, root_dir=root_dir)
        text = extract_office_text(path)
        if not text.strip():
            raise ValueError(f"No extractable text found in office document: {path}")
        return ExtractedSource(
            manifest=manifest,
            title=manifest.title,
            text=text.strip(),
            sections=build_single_section(text, heading="Office Document"),
        )


def extract_office_text(path) -> str:
    textutil = _run_textutil(path)
    if textutil.strip():
        return textutil
    metadata = _run_mdls(path)
    if metadata.strip() and metadata.strip() != "(null)":
        return metadata.strip().strip('"')
    return ""


def _run_textutil(path) -> str:
    result = subprocess.run(
        ["/usr/bin/textutil", "-convert", "txt", "-stdout", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        return result.stdout
    return ""


def _run_mdls(path) -> str:
    result = subprocess.run(
        ["/usr/bin/mdls", "-raw", "-name", "kMDItemTextContent", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        return result.stdout
    return ""
