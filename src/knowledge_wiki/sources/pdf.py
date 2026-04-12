from __future__ import annotations

import re
from pathlib import Path

from ..models import ExtractedSource, SourceManifest, SourceSection
from .base import SourceAdapter, resolve_source_path

MAX_REGEX_FALLBACK_PDF_BYTES = 20 * 1024 * 1024

STREAM_RE = re.compile(r"stream\r?\n(.*?)\r?\nendstream", re.DOTALL)
TEXT_RE = re.compile(r"\(([^()]*(?:\\.[^()]*)*)\)\s*Tj")
TEXT_ARRAY_RE = re.compile(r"\[(.*?)\]\s*TJ", re.DOTALL)
TEXT_ARRAY_STRING_RE = re.compile(r"\(([^()]*(?:\\.[^()]*)*)\)")


class PDFSourceAdapter(SourceAdapter):
    kind = "pdf"

    def extract(self, manifest: SourceManifest, *, root_dir: Path) -> ExtractedSource:
        path = resolve_source_path(manifest, root_dir=root_dir)
        text = _extract_pdf_text(path).strip()
        if not text:
            raise ValueError(f"No extractable text found in PDF: {path}")
        return ExtractedSource(
            manifest=manifest,
            title=manifest.title,
            text=text,
            sections=[
                SourceSection(
                    section_id="page-1",
                    heading="Page 1",
                    text=text,
                )
            ],
        )


def _extract_pdf_text(path: Path) -> str:
    reader_class = _load_pdf_reader()
    if reader_class is None:
        return _fallback_extract_pdf_text(path)

    reader = reader_class(str(path))
    page_text = [page.extract_text() or "" for page in reader.pages]
    return "\n\n".join(chunk.strip() for chunk in page_text if chunk.strip())


def _load_pdf_reader():
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        return None
    return PdfReader


def _fallback_extract_pdf_text(path: Path) -> str:
    file_size = path.stat().st_size
    if file_size > MAX_REGEX_FALLBACK_PDF_BYTES:
        raise ValueError(
            "Local PDF fallback requires pypdf for large PDFs. "
            f"Refusing regex extraction for {path} ({file_size} bytes)."
        )
    raw = path.read_bytes().decode("latin-1", errors="ignore")
    chunks: list[str] = []
    for stream_match in STREAM_RE.finditer(raw):
        stream = stream_match.group(1)
        chunks.extend(_decode_pdf_string(match.group(1)) for match in TEXT_RE.finditer(stream))
        for array_match in TEXT_ARRAY_RE.finditer(stream):
            chunks.extend(
                _decode_pdf_string(inner.group(1))
                for inner in TEXT_ARRAY_STRING_RE.finditer(array_match.group(1))
            )
    return " ".join(part.strip() for part in chunks if part.strip())


def _decode_pdf_string(value: str) -> str:
    value = re.sub(r"\\([0-7]{3})", lambda match: chr(int(match.group(1), 8)), value)
    value = value.replace("\\(", "(").replace("\\)", ")")
    value = value.replace("\\n", " ").replace("\\r", " ")
    value = value.replace("\\t", " ")
    value = value.replace("\\\\", "\\")
    return value
