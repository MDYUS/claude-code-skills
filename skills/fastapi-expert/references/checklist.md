# FastAPI development: reference checklist

## Inspect
Use typed request models, dependency injection, explicit authorization and documented errors.

## Choose
Do not block async handlers with slow synchronous I/O; validate boundary inputs.

## Verify
Test routes, validation errors and unauthorized requests.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
