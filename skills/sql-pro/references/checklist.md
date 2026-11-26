# SQL engineering: reference checklist

## Inspect
Use parameterized queries, transactions, constraints, explain plans and appropriate indexes.

## Choose
Optimize based on plans and actual workload; avoid interpolated input.

## Verify
Test query correctness and compare plans in a safe database.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
