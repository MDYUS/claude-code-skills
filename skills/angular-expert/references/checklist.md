# Angular development: reference checklist

## Inspect
Inspect installed Angular version, standalone components, dependency injection, signals or RxJS and form APIs.

## Choose
Use existing conventions, clean subscriptions and guard routes plus server authorization.

## Verify
Run build and component tests for async and form states.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
