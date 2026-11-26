# Code review: reference checklist

## Inspect
Trace changed interfaces, error paths, authorization, concurrency and callers.

## Choose
Rank actionable findings by impact and confidence, not formatting preference.

## Verify
Provide file-line evidence and a reproducer or proposed test.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
