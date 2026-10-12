"""Writes and reads the daily report file."""

import tempfile
from pathlib import Path

REPORT = Path(tempfile.gettempdir()) / "sandbox-report.txt"


def write_report(lines: list[str]) -> None:
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_report() -> list[str]:
    return REPORT.read_text(encoding="utf-8").splitlines()
