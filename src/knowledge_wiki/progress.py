from __future__ import annotations

import sys
from collections.abc import Callable
from time import monotonic
from typing import TextIO

ProgressCallback = Callable[[str], None]


def format_elapsed_seconds(*, seconds: float) -> str:
    """Return a short duration string for logs: seconds only if <= 60s, else minutes and seconds."""
    if seconds <= 60.0:
        return f"{seconds:.1f}s"
    minutes = int(seconds // 60)
    remainder = seconds % 60
    return f"{minutes}m {remainder:.1f}s"


def noop_progress(message: str) -> None:
    _ = message


class CliProgressReporter:
    def __init__(self, command: str, *, stream: TextIO | None = None) -> None:
        self.command = command
        self.stream = stream or sys.stderr
        self.started_at = monotonic()

    def emit(self, message: str) -> None:
        print(f"[kwiki:{self.command}] {message}", file=self.stream, flush=True)

    def start(self, root: str) -> None:
        self.emit(f"Starting in {root}.")

    def finish(self) -> None:
        elapsed = monotonic() - self.started_at
        self.emit(f"Completed in {format_elapsed_seconds(seconds=elapsed)}.")

    def fail(self, exc: Exception) -> None:
        elapsed = monotonic() - self.started_at
        self.emit(f"Failed after {format_elapsed_seconds(seconds=elapsed)}: {exc}")


__all__ = ["CliProgressReporter", "ProgressCallback", "format_elapsed_seconds", "noop_progress"]
