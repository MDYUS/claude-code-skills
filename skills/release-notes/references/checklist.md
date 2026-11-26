# Release notes: reference checklist

## Inspect
Inspect actual commits and public changes, group fixes and breaking changes.

## Choose
Focus on user-facing impact and migration instructions; avoid invented release claims.

## Verify
Trace each note to a real change.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
