from __future__ import annotations

from ..config import Settings
from ..models import CatalogEntry
from ..wiki.pages import collect_page_source_refs, extract_related_refs, iter_page_paths, read_page


def build_catalog(settings: Settings) -> list[CatalogEntry]:
    entries: list[CatalogEntry] = []
    for path in iter_page_paths(settings.wiki_dir):
        try:
            page = read_page(path)
        except Exception:
            continue
        entries.append(
            CatalogEntry(
                path=path.relative_to(settings.root_dir).as_posix(),
                page_id=page.page_id,
                title=page.title,
                page_type=page.page_type,
                summary=page.summary,
                text=f"{page.title}\n{page.summary}\n{page.body}",
                related=extract_related_refs(page),
                source_refs=collect_page_source_refs(page),
                last_compiled_at=page.last_compiled_at,
                topics=list(page.topics),
                source_count=page.source_count,
                lecture_number=page.lecture_number,
                module_id=page.module_id,
                page_kind=page.page_kind,
                parent_page_id=page.parent_page_id,
            )
        )
    return entries
