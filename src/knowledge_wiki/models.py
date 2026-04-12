from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


ALLOWED_SOURCE_KINDS = {
    "markdown",
    "notion",
    "pdf",
    "office",
    "html",
    "notebook",
    "code",
    "text",
}
ALLOWED_PAGE_TYPES = {"concept", "course", "project", "synthesis"}
ALLOWED_PAGE_STATUS = {"draft", "canonical"}
ALLOWED_PROPOSAL_TYPES = {"create_page", "patch_page"}
ALLOWED_APPROVAL_STATES = {"pending", "approved", "rejected"}
ALLOWED_PAGE_KINDS = {"hub", "inventory", "topic", "artifact", "synthesis", "source"}


@dataclass(slots=True)
class SourceManifest:
    source_id: str
    title: str
    kind: str
    origin: str
    scope: str
    file_path: str
    checksum: str
    ingest_status: str
    created_at: str
    updated_at: str
    module_id: str = ""
    batch_id: str = ""
    module_relpath: str = ""
    content_class: str = ""
    extract_status: str = ""
    skip_reason: str = ""
    extractor_metadata: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        required = {
            "source_id": self.source_id,
            "title": self.title,
            "kind": self.kind,
            "origin": self.origin,
            "scope": self.scope,
            "file_path": self.file_path,
            "checksum": self.checksum,
            "ingest_status": self.ingest_status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        missing = [name for name, value in required.items() if not str(value).strip()]
        if missing:
            raise ValueError(f"Source manifest missing required fields: {', '.join(missing)}")
        if self.kind not in ALLOWED_SOURCE_KINDS:
            raise ValueError(f"Unsupported source kind: {self.kind}")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return {
            "source_id": self.source_id,
            "title": self.title,
            "kind": self.kind,
            "origin": self.origin,
            "scope": self.scope,
            "file_path": self.file_path,
            "checksum": self.checksum,
            "ingest_status": self.ingest_status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "module_id": self.module_id,
            "batch_id": self.batch_id,
            "module_relpath": self.module_relpath,
            "content_class": self.content_class,
            "extract_status": self.extract_status,
            "skip_reason": self.skip_reason,
            "extractor_metadata": self.extractor_metadata,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "SourceManifest":
        manifest = cls(
            source_id=str(payload["source_id"]),
            title=str(payload["title"]),
            kind=str(payload["kind"]),
            origin=str(payload["origin"]),
            scope=str(payload["scope"]),
            file_path=str(payload["file_path"]),
            checksum=str(payload["checksum"]),
            ingest_status=str(payload["ingest_status"]),
            created_at=str(payload["created_at"]),
            updated_at=str(payload["updated_at"]),
            module_id=str(payload.get("module_id", "")),
            batch_id=str(payload.get("batch_id", "")),
            module_relpath=str(payload.get("module_relpath", "")),
            content_class=str(payload.get("content_class", "")),
            extract_status=str(payload.get("extract_status", "")),
            skip_reason=str(payload.get("skip_reason", "")),
            extractor_metadata=dict(payload.get("extractor_metadata", {})),
            metadata=dict(payload.get("metadata", {})),
        )
        manifest.validate()
        return manifest


@dataclass(slots=True)
class ModuleManifest:
    module_id: str
    term: str
    module_code: str
    root_path: str
    batch_id: str
    status: str
    discovered_files: int
    usable_files: int
    skipped_files: int
    layout_review_state: str
    draft_review_state: str
    created_at: str
    updated_at: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        required = {
            "module_id": self.module_id,
            "term": self.term,
            "module_code": self.module_code,
            "root_path": self.root_path,
            "batch_id": self.batch_id,
            "status": self.status,
            "layout_review_state": self.layout_review_state,
            "draft_review_state": self.draft_review_state,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        missing = [name for name, value in required.items() if not str(value).strip()]
        if missing:
            raise ValueError(f"Module manifest missing required fields: {', '.join(missing)}")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return {
            "module_id": self.module_id,
            "term": self.term,
            "module_code": self.module_code,
            "root_path": self.root_path,
            "batch_id": self.batch_id,
            "status": self.status,
            "discovered_files": self.discovered_files,
            "usable_files": self.usable_files,
            "skipped_files": self.skipped_files,
            "layout_review_state": self.layout_review_state,
            "draft_review_state": self.draft_review_state,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ModuleManifest":
        manifest = cls(
            module_id=str(payload["module_id"]),
            term=str(payload["term"]),
            module_code=str(payload["module_code"]),
            root_path=str(payload["root_path"]),
            batch_id=str(payload["batch_id"]),
            status=str(payload["status"]),
            discovered_files=int(payload["discovered_files"]),
            usable_files=int(payload["usable_files"]),
            skipped_files=int(payload["skipped_files"]),
            layout_review_state=str(payload["layout_review_state"]),
            draft_review_state=str(payload["draft_review_state"]),
            created_at=str(payload["created_at"]),
            updated_at=str(payload["updated_at"]),
            metadata=dict(payload.get("metadata", {})),
        )
        manifest.validate()
        return manifest


@dataclass(slots=True)
class SourceSection:
    section_id: str
    heading: str
    text: str


@dataclass(slots=True)
class ExtractedSource:
    manifest: SourceManifest
    title: str
    text: str
    sections: list[SourceSection]


@dataclass(slots=True)
class EvidenceArtifact:
    evidence_id: str
    source_id: str
    module_id: str
    batch_id: str
    source_path: str
    source_refs: list[str]
    summary: str
    key_topics: list[str]
    content_class: str
    extractor: str
    created_at: str
    updated_at: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        required = {
            "evidence_id": self.evidence_id,
            "source_id": self.source_id,
            "module_id": self.module_id,
            "batch_id": self.batch_id,
            "source_path": self.source_path,
            "summary": self.summary,
            "content_class": self.content_class,
            "extractor": self.extractor,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        missing = [name for name, value in required.items() if not str(value).strip()]
        if missing:
            raise ValueError(f"Evidence artifact missing required fields: {', '.join(missing)}")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return {
            "evidence_id": self.evidence_id,
            "source_id": self.source_id,
            "module_id": self.module_id,
            "batch_id": self.batch_id,
            "source_path": self.source_path,
            "source_refs": self.source_refs,
            "summary": self.summary,
            "key_topics": self.key_topics,
            "content_class": self.content_class,
            "extractor": self.extractor,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "EvidenceArtifact":
        artifact = cls(
            evidence_id=str(payload["evidence_id"]),
            source_id=str(payload["source_id"]),
            module_id=str(payload["module_id"]),
            batch_id=str(payload["batch_id"]),
            source_path=str(payload["source_path"]),
            source_refs=[str(item) for item in payload.get("source_refs", [])],
            summary=str(payload["summary"]),
            key_topics=[str(item) for item in payload.get("key_topics", [])],
            content_class=str(payload["content_class"]),
            extractor=str(payload["extractor"]),
            created_at=str(payload["created_at"]),
            updated_at=str(payload["updated_at"]),
            metadata=dict(payload.get("metadata", {})),
        )
        artifact.validate()
        return artifact


@dataclass(slots=True)
class LayoutPagePlan:
    title: str
    slug: str
    page_kind: str
    target_path: str
    summary: str
    parent_slug: str
    related_page_ids: list[str]
    assigned_source_refs: list[str]
    rationale: str = ""

    def validate(self) -> None:
        required = {
            "title": self.title,
            "slug": self.slug,
            "page_kind": self.page_kind,
            "target_path": self.target_path,
            "summary": self.summary,
        }
        missing = [name for name, value in required.items() if not str(value).strip()]
        if missing:
            raise ValueError(f"Layout page plan missing required fields: {', '.join(missing)}")
        if self.page_kind not in {"hub", "inventory", "topic", "artifact"}:
            raise ValueError(f"Unsupported layout page kind: {self.page_kind}")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return {
            "title": self.title,
            "slug": self.slug,
            "page_kind": self.page_kind,
            "target_path": self.target_path,
            "summary": self.summary,
            "parent_slug": self.parent_slug,
            "related_page_ids": self.related_page_ids,
            "assigned_source_refs": self.assigned_source_refs,
            "rationale": self.rationale,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "LayoutPagePlan":
        plan = cls(
            title=str(payload["title"]),
            slug=str(payload["slug"]),
            page_kind=str(payload["page_kind"]),
            target_path=str(payload["target_path"]),
            summary=str(payload["summary"]),
            parent_slug=str(payload.get("parent_slug", "")),
            related_page_ids=[str(item) for item in payload.get("related_page_ids", [])],
            assigned_source_refs=[str(item) for item in payload.get("assigned_source_refs", [])],
            rationale=str(payload.get("rationale", "")),
        )
        plan.validate()
        return plan


@dataclass(slots=True)
class LayoutReview:
    layout_id: str
    module_id: str
    batch_id: str
    approval_state: str
    pages: list[LayoutPagePlan]
    created_at: str
    updated_at: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        required = {
            "layout_id": self.layout_id,
            "module_id": self.module_id,
            "batch_id": self.batch_id,
            "approval_state": self.approval_state,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        missing = [name for name, value in required.items() if not str(value).strip()]
        if missing:
            raise ValueError(f"Layout review missing required fields: {', '.join(missing)}")
        if self.approval_state not in ALLOWED_APPROVAL_STATES:
            raise ValueError(f"Unsupported approval state: {self.approval_state}")
        if not self.pages:
            raise ValueError("Layout review must include at least one planned page.")
        for page in self.pages:
            page.validate()

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return {
            "layout_id": self.layout_id,
            "module_id": self.module_id,
            "batch_id": self.batch_id,
            "approval_state": self.approval_state,
            "pages": [page.to_dict() for page in self.pages],
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "LayoutReview":
        review = cls(
            layout_id=str(payload["layout_id"]),
            module_id=str(payload["module_id"]),
            batch_id=str(payload["batch_id"]),
            approval_state=str(payload["approval_state"]),
            pages=[LayoutPagePlan.from_dict(item) for item in payload.get("pages", [])],
            created_at=str(payload["created_at"]),
            updated_at=str(payload["updated_at"]),
            metadata=dict(payload.get("metadata", {})),
        )
        review.validate()
        return review


@dataclass(slots=True)
class WikiPage:
    page_id: str
    title: str
    page_type: str
    status: str
    summary: str
    aliases: list[str]
    tags: list[str]
    related: list[str]
    source_refs: list[str]
    last_compiled_at: str
    body: str
    topics: list[str] = field(default_factory=list)
    source_count: int = 0
    lecture_number: int | None = None
    page_kind: str = ""
    module_id: str = ""
    parent_page_id: str = ""
    batch_id: str = ""

    def validate(self) -> None:
        required = {
            "page_id": self.page_id,
            "title": self.title,
            "page_type": self.page_type,
            "status": self.status,
            "summary": self.summary,
            "last_compiled_at": self.last_compiled_at,
        }
        missing = [name for name, value in required.items() if not str(value).strip()]
        if missing:
            raise ValueError(f"Wiki page missing required fields: {', '.join(missing)}")
        if self.page_type not in ALLOWED_PAGE_TYPES:
            raise ValueError(f"Unsupported page type: {self.page_type}")
        if self.status not in ALLOWED_PAGE_STATUS:
            raise ValueError(f"Unsupported page status: {self.status}")
        if self.page_kind and self.page_kind not in ALLOWED_PAGE_KINDS:
            raise ValueError(f"Unsupported page kind: {self.page_kind}")
        if self.source_count < 0:
            raise ValueError("source_count must be non-negative.")

    def frontmatter(self) -> dict[str, Any]:
        self.validate()
        return {
            "page_id": self.page_id,
            "title": self.title,
            "page_type": self.page_type,
            "page_kind": self.page_kind,
            "module_id": self.module_id,
            "parent_page_id": self.parent_page_id,
            "batch_id": self.batch_id,
            "status": self.status,
            "summary": self.summary,
            "aliases": self.aliases,
            "tags": self.tags,
            "related": self.related,
            "source_refs": self.source_refs,
            "topics": self.topics,
            "source_count": self.source_count,
            "lecture_number": self.lecture_number,
            "last_compiled_at": self.last_compiled_at,
        }

    @classmethod
    def from_parts(cls, frontmatter: dict[str, Any], body: str) -> "WikiPage":
        page = cls(
            page_id=str(frontmatter["page_id"]),
            title=str(frontmatter["title"]),
            page_type=str(frontmatter["page_type"]),
            page_kind=str(frontmatter.get("page_kind", "")),
            module_id=str(frontmatter.get("module_id", "")),
            parent_page_id=str(frontmatter.get("parent_page_id", "")),
            batch_id=str(frontmatter.get("batch_id", "")),
            status=str(frontmatter["status"]),
            summary=str(frontmatter["summary"]),
            aliases=[str(item) for item in frontmatter.get("aliases", [])],
            tags=[str(item) for item in frontmatter.get("tags", [])],
            related=[str(item) for item in frontmatter.get("related", [])],
            source_refs=[str(item) for item in frontmatter.get("source_refs", [])],
            topics=[str(item) for item in frontmatter.get("topics", [])],
            source_count=int(frontmatter.get("source_count", len(frontmatter.get("source_refs", [])))),
            lecture_number=(
                int(frontmatter["lecture_number"])
                if frontmatter.get("lecture_number") not in ("", None)
                else None
            ),
            last_compiled_at=str(frontmatter["last_compiled_at"]),
            body=body.strip() + "\n",
        )
        page.validate()
        return page


@dataclass(slots=True)
class CatalogEntry:
    path: str
    page_id: str
    title: str
    page_type: str
    summary: str
    text: str
    related: list[str]
    source_refs: list[str]
    last_compiled_at: str = ""
    topics: list[str] = field(default_factory=list)
    source_count: int = 0
    lecture_number: int | None = None
    module_id: str = ""
    page_kind: str = ""
    parent_page_id: str = ""


@dataclass(slots=True)
class RetrievalHit:
    path: str
    page_id: str
    title: str
    score: float
    snippet: str
    source_refs: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "page_id": self.page_id,
            "title": self.title,
            "score": self.score,
            "snippet": self.snippet,
            "source_refs": self.source_refs,
        }


@dataclass(slots=True)
class DraftProposal:
    draft_id: str
    target_page: str
    proposal_type: str
    rationale: str
    evidence_set: list[str]
    proposed_markdown: str
    approval_state: str
    created_at: str
    updated_at: str
    module_id: str = ""
    batch_id: str = ""
    page_kind: str = ""
    parent_page_id: str = ""
    assigned_source_refs: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        required = {
            "draft_id": self.draft_id,
            "target_page": self.target_page,
            "proposal_type": self.proposal_type,
            "rationale": self.rationale,
            "proposed_markdown": self.proposed_markdown,
            "approval_state": self.approval_state,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        missing = [name for name, value in required.items() if not str(value).strip()]
        if missing:
            raise ValueError(f"Draft proposal missing required fields: {', '.join(missing)}")
        if self.proposal_type not in ALLOWED_PROPOSAL_TYPES:
            raise ValueError(f"Unsupported proposal type: {self.proposal_type}")
        if self.approval_state not in ALLOWED_APPROVAL_STATES:
            raise ValueError(f"Unsupported approval state: {self.approval_state}")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return {
            "draft_id": self.draft_id,
            "target_page": self.target_page,
            "proposal_type": self.proposal_type,
            "rationale": self.rationale,
            "evidence_set": self.evidence_set,
            "proposed_markdown": self.proposed_markdown,
            "approval_state": self.approval_state,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "module_id": self.module_id,
            "batch_id": self.batch_id,
            "page_kind": self.page_kind,
            "parent_page_id": self.parent_page_id,
            "assigned_source_refs": self.assigned_source_refs,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "DraftProposal":
        proposal = cls(
            draft_id=str(payload["draft_id"]),
            target_page=str(payload["target_page"]),
            proposal_type=str(payload["proposal_type"]),
            rationale=str(payload["rationale"]),
            evidence_set=[str(item) for item in payload.get("evidence_set", [])],
            proposed_markdown=str(payload["proposed_markdown"]),
            approval_state=str(payload["approval_state"]),
            created_at=str(payload["created_at"]),
            updated_at=str(payload["updated_at"]),
            module_id=str(payload.get("module_id", "")),
            batch_id=str(payload.get("batch_id", "")),
            page_kind=str(payload.get("page_kind", "")),
            parent_page_id=str(payload.get("parent_page_id", "")),
            assigned_source_refs=[str(item) for item in payload.get("assigned_source_refs", [])],
            metadata=dict(payload.get("metadata", {})),
        )
        proposal.validate()
        return proposal


@dataclass(slots=True)
class CourseIngestResult:
    module_manifest: ModuleManifest
    evidence_artifacts: list[EvidenceArtifact]
    layout_review: LayoutReview | None
    draft_proposals: list[DraftProposal]


@dataclass(slots=True)
class GenerationResult:
    text: str
    raw_response: dict[str, Any] = field(default_factory=dict)
    usage: "GenerationUsage | None" = None


@dataclass(slots=True)
class GenerationUsage:
    provider: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    estimated_input_cost_usd: float | None = None
    estimated_output_cost_usd: float | None = None
    estimated_total_cost_usd: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "estimated_input_cost_usd": self.estimated_input_cost_usd,
            "estimated_output_cost_usd": self.estimated_output_cost_usd,
            "estimated_total_cost_usd": self.estimated_total_cost_usd,
            "metadata": self.metadata,
        }


@dataclass(slots=True)
class QueryAnswer:
    question: str
    answer_markdown: str
    hits: list[RetrievalHit]
    raw_fallback_used: bool = False
    citations: list[str] = field(default_factory=list)
    draft_id: str | None = None
    suggested_synthesis: SynthesisSuggestion | None = None


@dataclass(slots=True)
class SynthesisSuggestion:
    title: str
    path: str
    summary: str
    body: str
    citations: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "path": self.path,
            "summary": self.summary,
            "body": self.body,
            "citations": self.citations,
        }


@dataclass(slots=True)
class LintFinding:
    kind: str
    severity: str
    message: str
    path: str | None = None
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "severity": self.severity,
            "message": self.message,
            "path": self.path,
            "details": self.details,
        }
