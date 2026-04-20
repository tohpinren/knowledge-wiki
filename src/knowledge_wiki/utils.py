from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "from",
    "if",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "their",
    "this",
    "to",
    "was",
    "with",
}


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def timestamp_slug() -> str:
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")


def slugify(value: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower())
    collapsed = re.sub(r"-{2,}", "-", normalized).strip("-")
    return collapsed or "untitled"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8192):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_path(path: Path) -> str:
    if path.is_file():
        return sha256_file(path)

    digest = hashlib.sha256()
    for child in sorted(item for item in path.rglob("*") if item.is_file()):
        digest.update(child.relative_to(path).as_posix().encode("utf-8"))
        with child.open("rb") as handle:
            while chunk := handle.read(8192):
                digest.update(chunk)
    return digest.hexdigest()


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text)]


def top_terms(text: str, *, limit: int = 8) -> list[str]:
    counts = Counter(
        token
        for token in tokenize(text)
        if len(token) > 2 and token not in STOPWORDS and not token.isdigit()
    )
    return [token for token, _ in counts.most_common(limit)]


def compact_text(text: str, *, limit: int = 280) -> str:
    normalized = re.sub(r"\s+", " ", text).strip()
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 3].rstrip() + "..."


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def relative_posix(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def manifest_reason_with_relative_paths(reason: str, *, root_dir: Path) -> str:
    """Rewrite absolute paths under ``root_dir`` to repo-relative paths for portable manifests."""
    if not reason:
        return reason
    root = root_dir.resolve()
    prefix = str(root).rstrip("/") + "/"
    return reason.replace(prefix, "")


def extract_json_object(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if not stripped:
        raise ValueError("Cannot parse JSON from empty text.")
    try:
        return _parse_json_object_candidate(stripped)
    except json.JSONDecodeError:
        start = stripped.find("{")
        end = stripped.rfind("}")
        if start < 0 or end < 0 or end <= start:
            raise ValueError("No JSON object found in provider output.") from None
        return _parse_json_object_candidate(stripped[start : end + 1])


def _parse_json_object_candidate(candidate: str) -> dict[str, Any]:
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        parsed = json.loads(_sanitize_json_candidate(candidate))
    if not isinstance(parsed, dict):
        raise ValueError("Expected a JSON object.")
    return parsed


def _sanitize_json_candidate(candidate: str) -> str:
    valid_escape_chars = {'"', "\\", "/", "b", "f", "n", "r", "t"}
    result: list[str] = []
    in_string = False
    index = 0

    while index < len(candidate):
        char = candidate[index]

        if not in_string:
            result.append(char)
            if char == '"':
                in_string = True
            index += 1
            continue

        if char == '"':
            result.append(char)
            in_string = False
            index += 1
            continue

        if char == "\\":
            next_index = index + 1
            if next_index >= len(candidate):
                result.append("\\\\")
                index += 1
                continue
            next_char = candidate[next_index]
            if next_char in valid_escape_chars or next_char == "u":
                result.append("\\")
                result.append(next_char)
            else:
                result.append("\\\\")
                result.append(next_char)
            index += 2
            continue

        if char == "\n":
            result.append("\\n")
        elif char == "\r":
            result.append("\\r")
        elif char == "\t":
            result.append("\\t")
        else:
            result.append(char)
        index += 1

    return "".join(result)
