from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from ..models import ExtractedSource, SourceManifest
from .base import SourceAdapter, build_single_section, resolve_source_path


class OfficeSourceAdapter(SourceAdapter):
    kind = "office"

    def extract(self, manifest: SourceManifest, *, root_dir) -> ExtractedSource:
        path = resolve_source_path(manifest, root_dir=root_dir)
        resolved_root = Path(root_dir).resolve()
        try:
            display_path = path.resolve().relative_to(resolved_root)
        except ValueError:
            display_path = path
        text = extract_office_text(path)
        if not text.strip():
            raise ValueError(
                f"No extractable text found in office document: {display_path.as_posix()}"
            )
        return ExtractedSource(
            manifest=manifest,
            title=manifest.title,
            text=text.strip(),
            sections=build_single_section(text, heading="Office Document"),
        )


def extract_office_text(path: Path) -> str:
    textutil = _run_textutil(path)
    if textutil.strip():
        return textutil
    metadata = _run_mdls(path)
    if metadata.strip() and metadata.strip() != "(null)":
        return metadata.strip().strip('"')
    return ""


def _run_textutil(path: Path) -> str:
    if sys.platform != "darwin":
        return ""
    binary = shutil.which("textutil")
    if not binary:
        return ""
    try:
        result = subprocess.run(
            [binary, "-convert", "txt", "-stdout", str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return ""
    if result.returncode == 0:
        return result.stdout
    return ""


def _run_mdls(path: Path) -> str:
    if sys.platform != "darwin":
        return ""
    binary = shutil.which("mdls")
    if not binary:
        return ""
    try:
        result = subprocess.run(
            [binary, "-raw", "-name", "kMDItemTextContent", str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return ""
    if result.returncode == 0:
        return result.stdout
    return ""
