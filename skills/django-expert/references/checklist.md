# Django development: reference checklist

## Inspect
Use ORM safely, migrations, middleware, CSRF protection and permission checks.

## Choose
Avoid N+1 queries; use transactions for related writes and secure defaults.

## Verify
Run Django checks and tests for permissions and model constraints.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
