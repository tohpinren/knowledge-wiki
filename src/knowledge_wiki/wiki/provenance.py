from __future__ import annotations

import re


SOURCE_REF_RE = re.compile(r"\[source:([A-Za-z0-9_-]+#[A-Za-z0-9_-]+)\]")


def build_source_ref(source_id: str, section_id: str) -> str:
    return f"{source_id}#{section_id}"


def render_citation(source_id: str, section_id: str) -> str:
    return f"[source:{build_source_ref(source_id, section_id)}]"


def extract_source_refs(text: str) -> list[str]:
    return list(dict.fromkeys(SOURCE_REF_RE.findall(text)))
