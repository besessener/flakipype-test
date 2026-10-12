"""Runs one test module in a pinned order: alphabetical, reversed on unlucky runs.

It stands in for a test runner that shuffles test order.
"""

import sys
import unittest

from sandbox.environment import unlucky


def main(module: str) -> int:
    loader = unittest.TestLoader()
    if unlucky():
        loader.sortTestMethodsUsing = lambda first, second: (first < second) - (first > second)
    suite = loader.loadTestsFromName(module)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
