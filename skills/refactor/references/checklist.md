# Safe refactoring: reference checklist

## Inspect
Identify coupling, duplication and invariants; capture public behavior before edits.

## Choose
Make small reversible changes; avoid speculative abstraction.

## Verify
Compare public outputs and tests before and after.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
