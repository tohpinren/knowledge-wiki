from __future__ import annotations

import json
from collections import defaultdict

from ..config import Settings
from .pages import extract_related_refs, iter_page_paths, read_page


def regenerate_wiki_index(settings: Settings) -> None:
    grouped: dict[str, list[tuple[str, str, dict[str, object]]]] = defaultdict(list)
    for path in iter_page_paths(settings.wiki_dir):
        try:
            page = read_page(path)
        except Exception:
            continue
        relative_path = path.relative_to(settings.wiki_dir).as_posix()
        grouped[page.page_type].append((page.title, relative_path, _page_index_metadata(page)))

    lines = ["# Wiki Index", ""]
    if not grouped:
        lines.append("No canonical wiki pages have been published yet.")
    else:
        for page_type in ("concept", "course", "project", "synthesis"):
            items = grouped.get(page_type, [])
            if not items:
                continue
            lines.append(f"## {page_type.title()}s")
            lines.append("")
            for title, relative_path, metadata in sorted(
                items, key=lambda item: (item[0].lower(), item[1])
            ):
                rendered = " :: ".join(
                    f"{key}={_render_index_scalar(value)}" for key, value in metadata.items()
                )
                lines.append(f"- [{title}]({relative_path}) :: {rendered}")
            lines.append("")

    settings.wiki_dir.joinpath("index.md").write_text(
        "\n".join(lines).rstrip() + "\n", encoding="utf-8"
    )


def _page_index_metadata(page) -> dict[str, object]:
    return {
        "type": page.page_type,
        "kind": page.page_kind or "",
        "module": page.module_id or "",
        "parent": page.parent_page_id or "",
        "lecture": page.lecture_number,
        "source_count": page.source_count,
        "topics": list(page.topics),
        "related_count": len(extract_related_refs(page)),
        "updated": page.last_compiled_at,
        "summary": page.summary,
    }


def _render_index_scalar(value: object) -> str:
    if isinstance(value, list):
        return json.dumps([str(item) for item in value], ensure_ascii=True)
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=True)
