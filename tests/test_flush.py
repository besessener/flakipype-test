import time
import unittest

from sandbox.flush import Buffer


class FlushTest(unittest.TestCase):
    def test_flushed_items_reach_the_sink(self) -> None:
        buffer = Buffer()
        buffer.add("event")

        buffer.flush_later()
        time.sleep(0.05)

        self.assertEqual(buffer.sink, ["event"])


if __name__ == "__main__":
    unittest.main()
