# Regression testing: reference checklist

## Inspect
Use deterministic fixtures and behavior-level assertions; cover boundaries and negative paths.

## Choose
Choose the lowest test layer that proves the requirement; mock only external boundaries.

## Verify
Run targeted and relevant broader tests and record exit codes.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
