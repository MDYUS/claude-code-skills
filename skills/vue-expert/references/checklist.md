# Vue development: reference checklist

## Inspect
Use reactive state, computed values, props and emits; inspect installed Vue version.

## Choose
Avoid mutating props and unnecessary watchers; handle cleanup.

## Verify
Run build and test reactive state and component interactions.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
