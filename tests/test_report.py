import unittest

from sandbox.report import read_report, write_report


class ReportTest(unittest.TestCase):
    def test_a_report_is_written(self) -> None:
        write_report(["builds: 3", "failed: 1"])

        self.assertEqual(read_report()[0], "builds: 3")

    def test_the_report_lists_failures(self) -> None:
        self.assertIn("failed: 1", read_report())


if __name__ == "__main__":
    unittest.main()
