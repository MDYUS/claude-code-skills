# Context efficiency: reference checklist

## Inspect
Use targeted search, bounded file reads, a concise evidence ledger and current observations.

## Choose
Read callers and invariants when required; correctness outranks token savings.

## Verify
Measure usage only when actual token metrics exist.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
