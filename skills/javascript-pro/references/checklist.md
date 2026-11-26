# JavaScript development: reference checklist

## Inspect
Understand promises, event loop, module boundaries, closures and AbortController.

## Choose
Handle rejection explicitly and cancel stale work; avoid unnecessary global state.

## Verify
Run lint, tests and asynchronous failure scenarios.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
