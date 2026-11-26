# PostgreSQL engineering: reference checklist

## Inspect
Inspect query plans, index selectivity, transactions, locks and connection pooling.

## Choose
Measure before adding indexes; keep migrations compatible and minimize lock duration.

## Verify
Use representative disposable data and compare query plans.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
