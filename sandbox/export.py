"""Exports rows in the background, like a job queue would."""

import threading
import time

from sandbox.environment import unlucky


class Export:
    def __init__(self, rows: list[str]) -> None:
        self.result: int | None = None
        self._thread = threading.Thread(target=self._run, args=(rows,))
        self._thread.start()

    def _run(self, rows: list[str]) -> None:
        time.sleep(0.08 if unlucky() else 0.02)
        self.result = len(rows)

    def wait(self, timeout: float = 5.0) -> int | None:
        self._thread.join(timeout)
        return self.result


def start_export(rows: list[str]) -> Export:
    return Export(rows)
