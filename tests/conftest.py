from __future__ import annotations

import json
import re
import sys
import threading
import time
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from knowledge_wiki.bootstrap import bootstrap_repository
from knowledge_wiki.config import Settings
from knowledge_wiki.models import ExtractedSource, GenerationResult, SourceManifest, SourceSection
from knowledge_wiki.providers.base import LLMProvider, ProviderError
from knowledge_wiki.sources.base import SourceAdapter, SourceRegistry


class ScriptedCourseProvider(LLMProvider):
    name = "scripted-course"
    supports_file_inputs = True

    def __init__(self, *, invalid_layout: bool = False) -> None:
        self.invalid_layout = invalid_layout
        self.calls: list[tuple[str, str | None]] = []
        self.file_calls: list[tuple[str, tuple[str, ...], str | None]] = []

    def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
        self.calls.append((prompt, system_prompt))
        if "SOURCE_SUMMARY_REQUEST" in prompt:
            title = _match_line(prompt, "Title") or "Source"
            return GenerationResult(
                text=f"{title} is a course source that contributes usable evidence."
            )
        if "LAYOUT_PLAN_REQUEST" in prompt:
            if self.invalid_layout:
                return GenerationResult(
                    text='{"pages":[{"title":"Broken","slug":"hub","page_kind":"topic","target_path":"wiki/outside.md","summary":"bad","parent_slug":"","related_page_ids":[],"assigned_source_refs":[],"rationale":"invalid"}]}'
                )
            return GenerationResult(text=self._layout_response(prompt))
        if "DRAFT_PAGE_REQUEST" in prompt:
            return GenerationResult(text=self._draft_response(prompt))
        if "REVISE_PAGE_REQUEST" in prompt:
            return GenerationResult(text=self._revised_page_response(prompt))
        if "SUGGEST_SYNTHESIS_REQUEST" in prompt:
            return GenerationResult(
                text=json.dumps(
                    {
                        "save": True,
                        "title": "Reusable Query Insight",
                        "summary": "A reusable answer synthesized from the compiled wiki.",
                        "body": "# Reusable Query Insight\n\nThis answer is worth saving.",
                    }
                )
            )
        if "Answer the question using only the provided wiki page evidence." in prompt:
            refs = re.findall(r"\[source:([A-Za-z0-9_-]+#[A-Za-z0-9_-]+)\]", prompt)
            citation = f"[source:{refs[0]}]" if refs else ""
            return GenerationResult(
                text=f"## Provider Summary\n\nCompiled answer grounded in the wiki {citation}".strip()
            )
        return GenerationResult(text="Fallback provider response.")

    def generate_with_files(
        self,
        prompt: str,
        *,
        files: list[Path],
        system_prompt: str | None = None,
    ) -> GenerationResult:
        self.file_calls.append((prompt, tuple(str(path) for path in files), system_prompt))
        if "DRAFT_PAGE_REQUEST" in prompt:
            return GenerationResult(text=self._draft_response(prompt))
        if "FILE_EXTRACTION_REQUEST" not in prompt or not files:
            return GenerationResult(
                text='{"title":"Uploaded File","sections":[{"heading":"Overview","text":"Uploaded file content."}]}'
            )

        file_path = files[0]
        title = file_path.stem.replace("-", " ").replace("_", " ").title()
        suffix = file_path.suffix.lower().lstrip(".") or "file"
        extracted_text = _read_provider_fixture_text(file_path)
        payload = {
            "title": title,
            "sections": [
                {
                    "heading": "Overview",
                    "text": extracted_text
                    or f"{title} captures course material extracted from the uploaded {suffix} file.",
                },
                {
                    "heading": "Key Topics",
                    "text": (
                        f"{title} includes concepts, examples, and references suitable for the course wiki."
                        if not extracted_text
                        else f"{title} contains academic material that should be preserved in the course wiki."
                    ),
                },
            ],
        }
        return GenerationResult(text=json.dumps(payload))

    def _layout_response(self, prompt: str) -> str:
        module_root = _match_line(prompt, "Course module root") or "wiki/courses/y1s1/cs1231s"
        refs = re.findall(r"([A-Za-z0-9_-]+#[A-Za-z0-9_-]+)", prompt)
        nearby_section = _extract_section(prompt, "Nearby existing pages:")
        nearby_page_ids = re.findall(r"- ([A-Za-z0-9_-]+) :: ", nearby_section)
        feedback = _extract_feedback(prompt)
        topic_refs = refs[: max(1, min(3, len(refs)))]
        related = nearby_page_ids[:1]
        payload = {
            "pages": [
                {
                    "title": "Core Concepts Revised" if feedback else "Core Concepts",
                    "slug": "core-concepts",
                    "page_kind": "topic",
                    "target_path": f"{module_root}/topics/core-concepts.md",
                    "summary": (
                        f"Core concepts restructured after reviewer feedback: {feedback[:80]}"
                        if feedback
                        else "Core concepts surfaced across the course materials."
                    ),
                    "parent_slug": "hub",
                    "related_page_ids": related,
                    "assigned_source_refs": topic_refs,
                    "rationale": "Capture reusable ideas that appear across the module.",
                },
            ]
        }
        return json.dumps(payload)

    def _draft_response(self, prompt: str) -> str:
        title = _match_line(prompt, "Page title") or "Untitled"
        refs = re.findall(r"([A-Za-z0-9_-]+#[A-Za-z0-9_-]+)", prompt)
        feedback = _extract_feedback(prompt)
        citation = f"[source:{refs[0]}]" if refs else ""
        second = f"[source:{refs[1]}]" if len(refs) > 1 else citation
        revision_block = (
            f"\n## Revision Notes\n\nApplied reviewer feedback: {feedback}\n" if feedback else ""
        )
        return (
            f"## Overview\n\n{title} synthesizes the assigned course evidence {citation}.\n\n"
            f"## Evidence\n\n- Key point grounded in the material {second}\n"
            f"{revision_block}"
        )

    def _revised_page_response(self, prompt: str) -> str:
        title = _match_line(prompt, "Page title") or "Untitled"
        feedback = _extract_feedback(prompt) or "review requested"
        return f"# {title}\n\n## Revised Page\n\nApplied reviewer feedback: {feedback}\n"


class ParallelTrackingProvider(ScriptedCourseProvider):
    def __init__(self) -> None:
        super().__init__()
        self._lock = threading.Lock()
        self.active_file_calls = 0
        self.max_active_file_calls = 0

    def generate_with_files(
        self,
        prompt: str,
        *,
        files: list[Path],
        system_prompt: str | None = None,
    ) -> GenerationResult:
        with self._lock:
            self.active_file_calls += 1
            self.max_active_file_calls = max(self.max_active_file_calls, self.active_file_calls)
        try:
            time.sleep(0.05)
            return super().generate_with_files(prompt, files=files, system_prompt=system_prompt)
        finally:
            with self._lock:
                self.active_file_calls -= 1


class AlwaysFailingFileProvider(ScriptedCourseProvider):
    def generate_with_files(
        self,
        prompt: str,
        *,
        files: list[Path],
        system_prompt: str | None = None,
    ) -> GenerationResult:
        raise ProviderError("Gemini request failed: insufficient_quota")


class SleepingTextAdapter(SourceAdapter):
    kind = "text"

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.active = 0
        self.max_active = 0

    def extract(self, manifest: SourceManifest, *, root_dir: Path) -> ExtractedSource:
        with self._lock:
            self.active += 1
            self.max_active = max(self.max_active, self.active)
        try:
            time.sleep(0.05)
            text = (root_dir / manifest.file_path).read_text(encoding="utf-8")
            return ExtractedSource(
                manifest=manifest,
                title=manifest.title,
                text=text,
                sections=[
                    SourceSection(
                        section_id="section-1",
                        heading="Overview",
                        text=text,
                    )
                ],
            )
        finally:
            with self._lock:
                self.active -= 1


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    root = tmp_path / "knowledge-wiki"
    root.mkdir()
    settings = Settings.from_root(root)
    bootstrap_repository(settings)
    return settings


@pytest.fixture
def scripted_provider() -> ScriptedCourseProvider:
    return ScriptedCourseProvider()


@pytest.fixture
def parallel_tracking_provider() -> ParallelTrackingProvider:
    return ParallelTrackingProvider()


@pytest.fixture
def failing_file_provider() -> AlwaysFailingFileProvider:
    return AlwaysFailingFileProvider()


@pytest.fixture
def sleeping_text_registry() -> tuple[SourceRegistry, SleepingTextAdapter]:
    adapter = SleepingTextAdapter()
    return SourceRegistry([adapter]), adapter


def write_text_pdf(path: Path, text: str) -> None:
    escaped = (
        text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)").replace("\n", "\\n")
    )
    stream = f"BT /F1 12 Tf 72 720 Td ({escaped}) Tj ET"
    objects = [
        "<< /Type /Catalog /Pages 2 0 R >>",
        "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        f"<< /Length {len(stream.encode('latin-1'))} >>\nstream\n{stream}\nendstream",
    ]

    parts = [b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"]
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(sum(len(part) for part in parts))
        parts.append(f"{index} 0 obj\n{obj}\nendobj\n".encode("latin-1"))

    xref_offset = sum(len(part) for part in parts)
    xref = [b"xref\n0 6\n0000000000 65535 f \n"]
    for offset in offsets[1:]:
        xref.append(f"{offset:010d} 00000 n \n".encode("ascii"))
    trailer = f"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode(
        "ascii"
    )
    path.write_bytes(b"".join(parts + xref + [trailer]))


def write_notebook(path: Path) -> None:
    payload = {
        "cells": [
            {
                "cell_type": "markdown",
                "source": ["# Notebook Title\n", "Graphs and proofs connect ideas.\n"],
            },
            {"cell_type": "code", "source": ["def prove():\n", "    return True\n"]},
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.write_text(json.dumps(payload), encoding="utf-8")


def _match_line(prompt: str, label: str) -> str | None:
    pattern = rf"^{re.escape(label)}:\s*(.+)$"
    match = re.search(pattern, prompt, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def _extract_feedback(prompt: str) -> str:
    return _extract_section(prompt, "Reviewer feedback:").replace("\n", " ").strip()


def _extract_section(prompt: str, heading: str) -> str:
    if heading not in prompt:
        return ""
    section = prompt.split(heading, maxsplit=1)[1]
    for terminator in (
        "\n\nExisting layout pages:",
        "\n\nReviewer feedback:",
        "\n\nPlanned sibling pages:",
        "\n\nAssigned evidence:",
        "\n\nNearby published pages:",
        "\n\nUse stable",
        "\n\nRevise the draft accordingly",
    ):
        if terminator in section:
            section = section.split(terminator, maxsplit=1)[0]
            break
    return "\n".join(line.strip() for line in section.strip().splitlines() if line.strip())


def _read_provider_fixture_text(path: Path) -> str:
    if path.suffix.lower() in {
        ".md",
        ".txt",
        ".html",
        ".htm",
        ".py",
        ".java",
        ".c",
        ".cpp",
        ".h",
        ".hpp",
        ".js",
        ".ts",
        ".tsx",
        ".go",
        ".rs",
        ".sql",
        ".sh",
        ".scala",
        ".r",
        ".m",
        ".json",
        ".yaml",
        ".yml",
        ".toml",
        ".ipynb",
    }:
        return path.read_text(encoding="utf-8", errors="ignore").strip()
    return ""
