# Smoke testing: reference checklist

## Inspect
Choose critical journeys and safe test accounts; define outcomes before testing.

## Choose
Prioritize login, core operation, persistence and logout where applicable.

## Verify
Record actual results and environment; avoid real transactions.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
