from __future__ import annotations

from ..config import ProviderPurpose, Settings
from .base import LLMProvider, ProviderError
from .gemini import GeminiProvider
from .openai_compatible import OpenAICompatibleProvider


def build_provider(settings: Settings, *, purpose: ProviderPurpose = "qa") -> LLMProvider | None:
    provider_name = settings.provider_name_for(purpose)
    model_name = settings.model_name_for(purpose)
    if provider_name == "openai_compatible":
        api_key = settings.openai_api_key
        if not api_key:
            return None
        return OpenAICompatibleProvider(
            api_key=api_key,
            model=model_name,
            base_url=settings.openai_base_url,
            timeout=max(1, settings.timeout_ms_for(purpose) // 1000),
        )
    if provider_name == "gemini":
        api_key = settings.gemini_api_key
        if not api_key:
            return None
        return GeminiProvider(
            api_key=api_key,
            model=model_name,
            timeout_ms=settings.timeout_ms_for(purpose),
        )
    raise ProviderError(f"Unsupported provider `{provider_name}` for {purpose}.")


__all__ = [
    "GeminiProvider",
    "LLMProvider",
    "ProviderError",
    "OpenAICompatibleProvider",
    "build_provider",
]
