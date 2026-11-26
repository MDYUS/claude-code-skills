# Release readiness: reference checklist

## Inspect
Create acceptance matrix for core flows, authorization, data, accessibility, build and recovery.

## Choose
Block release on confirmed critical defects; unknown checks remain unknown.

## Verify
Report PASS, FAIL and BLOCKED with exact evidence.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
