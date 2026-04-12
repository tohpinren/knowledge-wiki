from __future__ import annotations

import sys
from collections.abc import Callable
from time import monotonic
from typing import TextIO

ProgressCallback = Callable[[str], None]


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
        self.emit(f"Completed in {monotonic() - self.started_at:.1f}s.")

    def fail(self, exc: Exception) -> None:
        self.emit(f"Failed after {monotonic() - self.started_at:.1f}s: {exc}")


__all__ = ["CliProgressReporter", "ProgressCallback", "noop_progress"]
