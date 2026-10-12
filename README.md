# flakipype-test

A sandbox whose only job is to be flaky in known ways, so that
[flakipype](https://github.com/besessener/flakipype) can be tested end to end
(scan, investigate, fix, draft pull request, verification, timer) without
touching a real project. Nothing here is real code; please do not send fixes
by hand, except the pending pull request for the "Fixed" case.

## Cases

Each case is its own workflow, so one case's failures never hide another
case's passes.

| Workflow | Job › step | How it fails | Expected verdict | Fixable |
| --- | --- | --- | --- | --- |
| Timing race | `test` › Run the export tests | `tests/test_export.py` sleeps 50 ms for a background export that takes 20 or 80 ms | `flaky_test` | yes: wait for the export (`export.wait()`) instead of sleeping |
| Random order | `test` › Run the report tests | `test_the_report_lists_failures` reads the report file that the other test writes; unlucky runs run the tests in reverse order | `flaky_test` | yes: the test writes its own report |
| Network | `fixtures` › Download the test fixtures from the mirror | `scripts/download-fixtures.sh` downloads without a retry; the mirror answers 503 once on unlucky runs | `flaky_infrastructure` | yes: `curl --retry 3 --retry-all-errors` |
| Real bug | `test` › Run the price tests | The commit "Round prices down to whole cents" truncates instead of rounding: 2027 instead of 2028, on every run | `real_bug` | no (the fix is a code decision) |
| Fixed | `test` › Run the flush tests | Was flaky like the timing race until the pull request "Wait for the flush instead of sleeping" was merged | `fixed` | no: already fixed |
| Configuration | `label` › Mark the repository as checked | `gh label create` needs `issues: write`, the workflow grants only `contents: read`: HTTP 403 on every run | `configuration` | yes, with a `.github/` warning |

## The pinned bad luck

`sandbox/environment.py` decides which runs are unlucky: odd run numbers on
their first attempt. So each flaky case fails in about half of its runs, and
the rerun passes. It stands in for a slow or busy runner and is not part of
any bug; a fix that edits it is wrong.

The workflow **Rerun once** reruns the failed jobs of every first attempt
once, as a person would. That gives the scan its proof:

- flaky cases fail on attempt 1 and pass on attempt 2 ("passed on rerun");
- the real bug and the configuration case fail again ("still fails after a
  rerun", which is broken, not flaky).

## Schedule and cost

The cases run on every push to `main`, by hand (`workflow_dispatch`) and on a
schedule: every 30 minutes, staggered, and the configuration case every 3
hours. Each run takes seconds. The repository is public, so its Actions
minutes are free. GitHub disables schedules after 60 days without activity in
the repository; a push or enabling the workflows again restarts them.

## Using it

```bash
flakipype scan --repo besessener/flakipype-test
flakipype investigate --repo besessener/flakipype-test
flakipype run          # ask mode in the chat, auto mode from the timer
```

Compare the verdicts with the table above. In auto mode flakipype opens draft
pull requests here and starts verification reruns; that is what this
repository is for. Close the pull requests after checking them.
