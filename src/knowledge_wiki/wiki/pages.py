from __future__ import annotations

import re
from pathlib import Path

from ..models import WikiPage
from ..utils import ensure_parent, slugify
from .frontmatter import render_frontmatter, split_frontmatter
from .provenance import extract_source_refs

PAGE_TYPE_DIRECTORIES = {
    "concept": "concepts",
    "course": "courses",
    "project": "projects",
    "synthesis": "syntheses",
}
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")


def render_page(page: WikiPage) -> str:
    return f"{render_frontmatter(page.frontmatter())}\n{page.body.strip()}\n"


def write_page(path: Path, page: WikiPage) -> None:
    ensure_parent(path)
    path.write_text(render_page(page), encoding="utf-8")


def read_page(path: Path) -> WikiPage:
    frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
    return WikiPage.from_parts(frontmatter, body)


def iter_page_paths(wiki_dir: Path) -> list[Path]:
    paths: list[Path] = []
    for path in sorted(wiki_dir.rglob("*.md")):
        if path.parent == wiki_dir and path.name in {"README.md", "index.md"}:
            continue
        paths.append(path)
    return paths


def build_page_path(root_dir: Path, *, title: str, page_type: str) -> Path:
    if page_type not in PAGE_TYPE_DIRECTORIES:
        raise ValueError(f"Unsupported page type: {page_type}")
    return root_dir / "wiki" / PAGE_TYPE_DIRECTORIES[page_type] / f"{slugify(title)}.md"


def build_course_page_path(
    root_dir: Path,
    *,
    term: str,
    module_code: str,
    page_kind: str,
    slug: str | None = None,
) -> Path:
    module_root = root_dir / "wiki" / "courses" / slugify(term) / slugify(module_code)
    if page_kind == "hub":
        return module_root / "index.md"
    if page_kind == "inventory":
        return module_root / "inventory.md"
    if page_kind == "topic":
        if not slug:
            raise ValueError("Topic pages require a slug.")
        return module_root / "topics" / f"{slugify(slug)}.md"
    if page_kind == "artifact":
        if not slug:
            raise ValueError("Artifact pages require a slug.")
        return module_root / "artifacts" / f"{slugify(slug)}.md"
    raise ValueError(f"Unsupported course page kind: {page_kind}")


def extract_related_refs(page: WikiPage) -> list[str]:
    refs = list(page.related)
    refs.extend(match.group(1).strip() for match in WIKILINK_RE.finditer(page.body))
    return list(dict.fromkeys(refs))


def collect_page_source_refs(page: WikiPage) -> list[str]:
    refs = list(page.source_refs)
    refs.extend(extract_source_refs(page.body))
    return list(dict.fromkeys(refs))
