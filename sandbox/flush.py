"""A buffer that flushes to its sink in the background."""

import threading
import time

from sandbox.environment import unlucky


class Buffer:
    def __init__(self) -> None:
        self.sink: list[str] = []
        self._pending: list[str] = []
        self.flushed = threading.Event()

    def add(self, item: str) -> None:
        self._pending.append(item)

    def flush_later(self) -> None:
        threading.Thread(target=self._flush).start()

    def _flush(self) -> None:
        time.sleep(0.08 if unlucky() else 0.02)
        self.sink.extend(self._pending)
        self._pending.clear()
        self.flushed.set()
