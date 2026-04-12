from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

ProviderPurpose = Literal["ingest", "qa"]


@dataclass(slots=True)
class Settings:
    root_dir: Path
    raw_dir: Path
    wiki_dir: Path
    system_dir: Path
    manifests_dir: Path
    source_manifest_dir: Path
    module_manifest_dir: Path
    reviews_dir: Path
    drafts_dir: Path
    layouts_dir: Path
    evidence_dir: Path
    graph_dir: Path
    metrics_dir: Path
    ingest_metrics_dir: Path
    cache_dir: Path
    file_env: dict[str, str] = field(default_factory=dict, repr=False)
    provider_name: str = "openai_compatible"
    model_name: str = "gpt-5.4-mini"
    ingest_provider_name: str = "gemini"
    ingest_model_name: str = "gemini-2.5-flash-lite"
    qa_provider_name: str = "gemini"
    qa_model_name: str = "gemini-2.5-flash"
    ingest_concurrency: int = 4
    ingest_timeout_ms: int = 120000
    qa_timeout_ms: int = 60000
    openai_base_url: str = "https://api.openai.com/v1"
    openai_api_key_env: str = "OPENAI_API_KEY"
    gemini_api_key_env: str = "GEMINI_API_KEY"
    max_retrieval_hits: int = 5

    @classmethod
    def from_root(cls, root_dir: str | Path | None = None) -> "Settings":
        root = Path(root_dir or ".").resolve()
        file_env = _load_env_file(root / ".env")
        return cls(
            root_dir=root,
            raw_dir=root / "raw",
            wiki_dir=root / "wiki",
            system_dir=root / "system",
            manifests_dir=root / "system" / "manifests",
            source_manifest_dir=root / "system" / "manifests" / "sources",
            module_manifest_dir=root / "system" / "manifests" / "modules",
            reviews_dir=root / "system" / "reviews",
            drafts_dir=root / "system" / "reviews" / "drafts",
            layouts_dir=root / "system" / "reviews" / "layouts",
            evidence_dir=root / "system" / "evidence",
            graph_dir=root / "system" / "graph",
            metrics_dir=root / "system" / "metrics",
            ingest_metrics_dir=root / "system" / "metrics" / "ingest",
            cache_dir=root / "system" / "cache",
            file_env=file_env,
            provider_name=_env_value("KWIKI_PROVIDER", file_env, default="openai_compatible"),
            model_name=_env_value("KWIKI_MODEL", file_env, default="gpt-5.4-mini"),
            ingest_provider_name=_env_with_fallback("KWIKI_INGEST_PROVIDER", "KWIKI_PROVIDER", file_env=file_env, default="gemini"),
            ingest_model_name=_env_with_fallback("KWIKI_INGEST_MODEL", "KWIKI_MODEL", file_env=file_env, default="gemini-2.5-flash-lite"),
            qa_provider_name=_env_with_fallback("KWIKI_QA_PROVIDER", "KWIKI_PROVIDER", file_env=file_env, default="gemini"),
            qa_model_name=_env_with_fallback("KWIKI_QA_MODEL", "KWIKI_MODEL", file_env=file_env, default="gemini-2.5-flash"),
            ingest_concurrency=_parse_positive_int(_env_value("KWIKI_INGEST_CONCURRENCY", file_env, default="4"), default=4),
            ingest_timeout_ms=_parse_positive_int(_env_value("KWIKI_INGEST_TIMEOUT_MS", file_env, default="120000"), default=120000),
            qa_timeout_ms=_parse_positive_int(_env_value("KWIKI_QA_TIMEOUT_MS", file_env, default="60000"), default=60000),
            openai_base_url=_env_value("KWIKI_OPENAI_BASE_URL", file_env, default="https://api.openai.com/v1"),
            openai_api_key_env=_env_value("KWIKI_OPENAI_KEY_ENV", file_env, default="OPENAI_API_KEY"),
            gemini_api_key_env=_env_value("KWIKI_GEMINI_KEY_ENV", file_env, default="GEMINI_API_KEY"),
        )

    def ensure_layout(self) -> None:
        directories = [
            self.raw_dir,
            self.wiki_dir,
            self.wiki_dir / "concepts",
            self.wiki_dir / "courses",
            self.wiki_dir / "projects",
            self.wiki_dir / "syntheses",
            self.system_dir,
            self.manifests_dir,
            self.source_manifest_dir,
            self.module_manifest_dir,
            self.reviews_dir,
            self.drafts_dir,
            self.layouts_dir,
            self.evidence_dir,
            self.graph_dir,
            self.metrics_dir,
            self.ingest_metrics_dir,
            self.cache_dir,
        ]
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

    @property
    def openai_api_key(self) -> str | None:
        return os.environ.get(self.openai_api_key_env) or self.file_env.get(self.openai_api_key_env)

    @property
    def gemini_api_key(self) -> str | None:
        return os.environ.get(self.gemini_api_key_env) or self.file_env.get(self.gemini_api_key_env)

    def provider_name_for(self, purpose: ProviderPurpose) -> str:
        if purpose == "ingest":
            return self.ingest_provider_name
        return self.qa_provider_name

    def model_name_for(self, purpose: ProviderPurpose) -> str:
        if purpose == "ingest":
            return self.ingest_model_name
        return self.qa_model_name

    def timeout_ms_for(self, purpose: ProviderPurpose) -> int:
        if purpose == "ingest":
            return self.ingest_timeout_ms
        return self.qa_timeout_ms


def _load_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", maxsplit=1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key:
            values[key] = value
    return values


def _env_value(key: str, file_env: dict[str, str], *, default: str) -> str:
    value = os.environ.get(key)
    if value:
        return value
    value = file_env.get(key)
    if value:
        return value
    return default


def _env_with_fallback(primary: str, fallback: str, *, file_env: dict[str, str], default: str) -> str:
    value = _env_value(primary, file_env, default="")
    if value:
        return value
    value = _env_value(fallback, file_env, default="")
    if value:
        return value
    return default


def _parse_positive_int(value: str | None, *, default: int) -> int:
    if not value:
        return default
    try:
        parsed = int(value)
    except ValueError:
        return default
    return max(1, parsed)
