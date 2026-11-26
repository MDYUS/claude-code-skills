# Defensive security: reference checklist

## Inspect
Map roles and trust boundaries; inspect server-side object authorization, injection, sessions, CSRF and secrets.

## Choose
Prioritize proven exposure; use parameterized queries and deny-by-default authorization.

## Verify
Use disposable accounts for negative authorization tests; redact sensitive evidence.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
