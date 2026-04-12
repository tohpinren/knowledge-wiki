from __future__ import annotations

from .code import CodeSourceAdapter
from .base import SourceRegistry
from .discovery import CLASSIFICATION_MAP, DiscoveredFile, discover_course_files
from .html import HTMLSourceAdapter
from .markdown import MarkdownSourceAdapter
from .notion import NotionSourceAdapter
from .notebook import NotebookSourceAdapter
from .office import OfficeSourceAdapter
from .pdf import PDFSourceAdapter
from .text import TextSourceAdapter


def build_source_registry() -> SourceRegistry:
    return SourceRegistry(
        [
            MarkdownSourceAdapter(),
            NotionSourceAdapter(),
            PDFSourceAdapter(),
            OfficeSourceAdapter(),
            HTMLSourceAdapter(),
            NotebookSourceAdapter(),
            CodeSourceAdapter(),
            TextSourceAdapter(),
        ]
    )


__all__ = [
    "CLASSIFICATION_MAP",
    "DiscoveredFile",
    "SourceRegistry",
    "build_source_registry",
    "discover_course_files",
]
