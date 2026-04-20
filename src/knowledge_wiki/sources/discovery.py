from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

IGNORE_DIR_NAMES = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    "target",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
}
IGNORE_FILE_NAMES = {".DS_Store"}

CLASSIFICATION_MAP = {
    ".pdf": ("pdf", "document"),
    ".doc": ("office", "document"),
    ".docx": ("office", "document"),
    ".ppt": ("office", "slides"),
    ".pptx": ("office", "slides"),
    ".md": ("markdown", "document"),
    ".rst": ("markdown", "document"),
    ".txt": ("text", "document"),
    ".html": ("html", "web"),
    ".htm": ("html", "web"),
    ".ipynb": ("notebook", "notebook"),
    ".py": ("code", "code"),
    ".java": ("code", "code"),
    ".c": ("code", "code"),
    ".cpp": ("code", "code"),
    ".h": ("code", "code"),
    ".hpp": ("code", "code"),
    ".js": ("code", "code"),
    ".ts": ("code", "code"),
    ".tsx": ("code", "code"),
    ".go": ("code", "code"),
    ".rs": ("code", "code"),
    ".sql": ("code", "code"),
    ".sh": ("code", "code"),
    ".scala": ("code", "code"),
    ".r": ("code", "code"),
    ".m": ("code", "code"),
    ".json": ("code", "config"),
    ".yaml": ("code", "config"),
    ".yml": ("code", "config"),
    ".toml": ("code", "config"),
}


@dataclass(slots=True)
class DiscoveredFile:
    path: Path
    relative_path: Path
    kind: str
    content_class: str
    usable: bool
    skip_reason: str = ""


def discover_course_files(root_path: Path) -> tuple[list[DiscoveredFile], list[DiscoveredFile]]:
    usable: list[DiscoveredFile] = []
    skipped: list[DiscoveredFile] = []

    for root_str, dirnames, filenames in os.walk(root_path):
        current_root = Path(root_str)
        dirnames[:] = [dirname for dirname in dirnames if not _should_ignore_dir(Path(dirname))]
        for filename in sorted(filenames):
            file_path = current_root / filename
            relative_path = file_path.relative_to(root_path)
            discovered = classify_path(file_path, relative_path=relative_path)
            if discovered.usable:
                usable.append(discovered)
            else:
                skipped.append(discovered)

    usable.sort(key=lambda item: item.relative_path.as_posix())
    skipped.sort(key=lambda item: item.relative_path.as_posix())
    return usable, skipped


def classify_path(path: Path, *, relative_path: Path | None = None) -> DiscoveredFile:
    relative = relative_path or path.name
    if path.name in IGNORE_FILE_NAMES or path.name.startswith("."):
        return DiscoveredFile(
            path=path,
            relative_path=Path(relative),
            kind="",
            content_class="",
            usable=False,
            skip_reason="ignored_file",
        )
    suffix = path.suffix.lower()
    if suffix in CLASSIFICATION_MAP:
        kind, content_class = CLASSIFICATION_MAP[suffix]
        return DiscoveredFile(
            path=path,
            relative_path=Path(relative),
            kind=kind,
            content_class=content_class,
            usable=True,
        )
    return DiscoveredFile(
        path=path,
        relative_path=Path(relative),
        kind="",
        content_class="",
        usable=False,
        skip_reason="unsupported_extension",
    )


def _should_ignore_dir(path: Path) -> bool:
    return path.name in IGNORE_DIR_NAMES or path.name.startswith(".")
