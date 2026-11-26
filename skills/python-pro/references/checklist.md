# Python development: reference checklist

## Inspect
Use explicit types at interfaces, context managers, pathlib, bounded concurrency and structured exceptions.

## Choose
Prefer standard library and simple data structures; choose async only for compatible I/O workloads.

## Verify
Run existing Python tests, type checks and boundary cases.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
