# System architecture: reference checklist

## Inspect
Map runtime boundaries, dependencies, data flows, failure modes and constraints.

## Choose
Choose the simplest architecture meeting current requirements; document tradeoffs.

## Verify
Test high-risk assumptions with a small prototype.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
