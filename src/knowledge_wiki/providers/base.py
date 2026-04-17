from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from ..models import GenerationResult, GenerationUsage

MODEL_PRICING_USD_PER_1M_TOKENS: dict[tuple[str, str], tuple[float, float]] = {
    ("gemini", "gemini-2.5-flash-lite"): (0.10, 0.40),
    ("gemini", "gemini-2.5-flash"): (0.30, 2.50),
    ("openai_compatible", "gpt-5.4-mini"): (0.25, 2.00),
}


class ProviderError(RuntimeError):
    pass


class LLMProvider(ABC):
    name = "base"
    supports_file_inputs = False
    model = ""

    @abstractmethod
    def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
        raise NotImplementedError

    def generate_with_files(
        self,
        prompt: str,
        *,
        files: list[Path],
        system_prompt: str | None = None,
    ) -> GenerationResult:
        raise ProviderError(f"Provider `{self.name}` does not support file inputs.")

    @property
    def label(self) -> str:
        model = getattr(self, "model", "")
        return f"{self.name}/{model}" if model else self.name


def build_usage(
    *,
    provider: str,
    model: str,
    input_tokens: int | None,
    output_tokens: int | None,
    total_tokens: int | None,
    metadata: dict | None = None,
) -> GenerationUsage | None:
    if input_tokens is None and output_tokens is None and total_tokens is None:
        return None
    normalized_input = max(0, int(input_tokens or 0))
    normalized_output = max(0, int(output_tokens or 0))
    normalized_total = max(0, int(total_tokens or (normalized_input + normalized_output)))

    estimated_input_cost_usd = None
    estimated_output_cost_usd = None
    estimated_total_cost_usd = None
    prices = MODEL_PRICING_USD_PER_1M_TOKENS.get((provider, model))
    if prices is not None:
        input_price, output_price = prices
        estimated_input_cost_usd = _round_cost((normalized_input / 1_000_000) * input_price)
        estimated_output_cost_usd = _round_cost((normalized_output / 1_000_000) * output_price)
        estimated_total_cost_usd = _round_cost(estimated_input_cost_usd + estimated_output_cost_usd)

    return GenerationUsage(
        provider=provider,
        model=model,
        input_tokens=normalized_input,
        output_tokens=normalized_output,
        total_tokens=normalized_total,
        estimated_input_cost_usd=estimated_input_cost_usd,
        estimated_output_cost_usd=estimated_output_cost_usd,
        estimated_total_cost_usd=estimated_total_cost_usd,
        metadata=dict(metadata or {}),
    )


def _round_cost(value: float) -> float:
    return round(value, 8)
