# Repository audit: reference checklist

## Inspect
Map entry points, manifests and critical user journeys; distinguish reproducible failures from static suspicions.

## Choose
Record path, line, severity, reproduction and confidence. Prioritize data loss and broken core flows.

## Verify
Run existing checks and reproduce at least one suspected defect.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
