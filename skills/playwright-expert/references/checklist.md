# Browser automation: reference checklist

## Inspect
Use role-based locators, explicit assertions, isolated contexts and deterministic fixtures.

## Choose
Avoid fixed sleeps; wait for observable application state.

## Verify
Run core journeys and capture traces on failure.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
