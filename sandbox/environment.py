"""The pinned bad luck of the sandbox: which runs get a slow or busy runner.

Odd-numbered runs are unlucky on their first attempt and lucky when rerun, so every case
fails about half its runs and passes on rerun. This is the simulated environment, not the bug:
fixes belong in the code and tests of each case, never here.
"""

import os


def unlucky() -> bool:
    attempt = int(os.environ.get("GITHUB_RUN_ATTEMPT", "1"))
    run = int(os.environ.get("GITHUB_RUN_NUMBER", "0"))
    return attempt == 1 and run % 2 == 1
