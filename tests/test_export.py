import time
import unittest

from sandbox.export import start_export


class ExportTest(unittest.TestCase):
    def test_the_export_counts_the_rows(self) -> None:
        export = start_export(["a", "b", "c"])

        time.sleep(0.05)

        self.assertEqual(export.result, 3)


if __name__ == "__main__":
    unittest.main()
