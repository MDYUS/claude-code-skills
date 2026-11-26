# Cost optimization: reference checklist

## Inspect
Identify billable units, retry rates, usage volumes, caching and idle resources.

## Choose
Use dated rates, explicit units and total-cost tradeoffs.

## Verify
Compare baseline and scenario costs against actual usage when available.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
