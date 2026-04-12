from __future__ import annotations

from pathlib import Path
from typing import Any

from ..models import GenerationResult
from .base import LLMProvider, ProviderError, build_usage

try:
    from google import genai
except ImportError:  # pragma: no cover - exercised when dependency is not installed
    genai = None


class GeminiProvider(LLMProvider):
    name = "gemini"
    supports_file_inputs = True

    def __init__(self, *, api_key: str | None, model: str, timeout_ms: int = 60000) -> None:
        self.api_key = api_key
        self.model = model
        self.timeout_ms = timeout_ms

    def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
        client = self._require_client()
        try:
            response = client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=_gemini_config(system_prompt, json_mode=_wants_json_response(prompt)),
            )
        except Exception as exc:  # pragma: no cover - vendor exception shape is external
            raise _gemini_error(exc) from exc
        raw = _gemini_raw(response)
        return GenerationResult(
            text=_gemini_text(response),
            raw_response=raw,
            usage=_gemini_usage(raw, provider=self.name, model=self.model),
        )

    def generate_with_files(
        self,
        prompt: str,
        *,
        files: list[Path],
        system_prompt: str | None = None,
    ) -> GenerationResult:
        client = self._require_client()
        if not files:
            raise ProviderError("At least one file is required for file-input generation.")

        uploaded_files: list[Any] = []
        try:
            for path in files:
                uploaded_files.append(client.files.upload(file=str(path)))
            contents: list[Any] = []
            if prompt.strip():
                contents.append(prompt)
            contents.extend(uploaded_files)
            response = client.models.generate_content(
                model=self.model,
                contents=contents,
                config=_gemini_config(system_prompt, json_mode=_wants_json_response(prompt)),
            )
        except Exception as exc:  # pragma: no cover - vendor exception shape is external
            raise _gemini_error(exc) from exc
        finally:
            for uploaded in uploaded_files:
                name = getattr(uploaded, "name", "")
                if not name:
                    continue
                try:
                    client.files.delete(name=name)
                except Exception:
                    continue
        raw = _gemini_raw(response)
        return GenerationResult(
            text=_gemini_text(response),
            raw_response=raw,
            usage=_gemini_usage(raw, provider=self.name, model=self.model),
        )

    def _require_client(self):
        if genai is None:
            raise ProviderError("Gemini support requires the `google-genai` package to be installed.")
        if not self.api_key:
            raise ProviderError("Gemini provider requires a GEMINI_API_KEY.")
        kwargs = {"api_key": self.api_key}
        genai_types = getattr(genai, "types", None)
        if genai_types is not None:
            kwargs["http_options"] = genai_types.HttpOptions(timeout=self.timeout_ms)
        return genai.Client(**kwargs)


def _gemini_config(system_prompt: str | None, *, json_mode: bool = False) -> dict[str, Any] | None:
    config: dict[str, Any] = {}
    if system_prompt:
        config["system_instruction"] = system_prompt
    if json_mode:
        config["response_mime_type"] = "application/json"
    return config or None


def _wants_json_response(prompt: str) -> bool:
    lowered = prompt.lower()
    return "return json only" in lowered or "schema:" in lowered


def _gemini_text(response: Any) -> str:
    text = getattr(response, "text", "")
    if isinstance(text, str) and text.strip():
        return text.strip()
    candidates = getattr(response, "candidates", None) or []
    texts: list[str] = []
    for candidate in candidates:
        content = getattr(candidate, "content", None)
        parts = getattr(content, "parts", None) or []
        for part in parts:
            value = getattr(part, "text", None)
            if isinstance(value, str) and value.strip():
                texts.append(value.strip())
    return "\n\n".join(texts).strip()


def _gemini_raw(response: Any) -> dict[str, Any]:
    model_dump = getattr(response, "model_dump", None)
    if callable(model_dump):
        try:
            payload = model_dump(mode="json", exclude_none=True)
        except TypeError:
            payload = model_dump()
        if isinstance(payload, dict):
            return payload
    return {}


def _gemini_error(exc: Exception) -> ProviderError:
    message = str(exc).strip() or exc.__class__.__name__
    return ProviderError(f"Gemini request failed: {message}")


def _gemini_usage(raw: dict[str, Any], *, provider: str, model: str):
    usage = raw.get("usage_metadata") or raw.get("usageMetadata")
    if not isinstance(usage, dict):
        return None
    input_tokens = usage.get("prompt_token_count", usage.get("promptTokenCount"))
    output_tokens = usage.get("candidates_token_count", usage.get("candidatesTokenCount"))
    total_tokens = usage.get("total_token_count", usage.get("totalTokenCount"))
    metadata: dict[str, Any] = {}
    thoughts = usage.get("thoughts_token_count", usage.get("thoughtsTokenCount"))
    if thoughts is not None:
        metadata["thoughts_token_count"] = thoughts
    cached = usage.get("cached_content_token_count", usage.get("cachedContentTokenCount"))
    if cached is not None:
        metadata["cached_content_token_count"] = cached
    return build_usage(
        provider=provider,
        model=model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        metadata=metadata,
    )
