from __future__ import annotations

import json
import re
from typing import Any


FRONTMATTER_DELIMITER = "---"
NUMBER_RE = re.compile(r"-?\d+(\.\d+)?")


def split_frontmatter(document: str) -> tuple[dict[str, Any], str]:
    if not document.startswith(f"{FRONTMATTER_DELIMITER}\n"):
        return {}, document

    lines = document.splitlines()
    end_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == FRONTMATTER_DELIMITER:
            end_index = index
            break
    if end_index is None:
        raise ValueError("Unterminated frontmatter block.")

    frontmatter_lines = lines[1:end_index]
    body = "\n".join(lines[end_index + 1 :]).lstrip("\n")
    return parse_frontmatter_lines(frontmatter_lines), body


def parse_frontmatter_lines(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.startswith("  - "):
            if current_key is None:
                raise ValueError("List item found before a key in frontmatter.")
            data.setdefault(current_key, []).append(_parse_scalar(line[4:].strip()))
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key = key.strip()
        value = value.strip()
        if not value:
            data[key] = []
            current_key = key
        else:
            data[key] = _parse_scalar(value)
            current_key = None

    return data


def render_frontmatter(data: dict[str, Any]) -> str:
    lines = [FRONTMATTER_DELIMITER]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {_render_scalar(item)}")
            continue
        lines.append(f"{key}: {_render_scalar(value)}")
    lines.append(FRONTMATTER_DELIMITER)
    return "\n".join(lines)


def _parse_scalar(raw: str) -> Any:
    if raw in {"null", "~"}:
        return None
    if raw == "true":
        return True
    if raw == "false":
        return False
    if raw.startswith('"') or raw.startswith("[") or raw.startswith("{"):
        return json.loads(raw)
    if NUMBER_RE.fullmatch(raw):
        return float(raw) if "." in raw else int(raw)
    return raw


def _render_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=True)
