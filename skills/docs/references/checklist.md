# Developer documentation: reference checklist

## Inspect
Inspect public interfaces, setup commands and environment variable names.

## Choose
Document implemented behavior separately from planned work.

## Verify
Run commands if available and verify relative links.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
