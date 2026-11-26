# Schema migration: reference checklist

## Inspect
Inspect constraints, indexes, locks and compatibility; plan expand-migrate-contract.

## Choose
Prefer additive changes and batched backfills; approve irreversible operations separately.

## Verify
Rehearse on disposable representative data and verify constraints and recovery.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
