# Responsive design: reference checklist

## Inspect
Inspect flex min-width, intrinsic grids, fixed dimensions and content wrapping.

## Choose
Use fluid sizing and content-driven breakpoints; avoid hiding overflow as a fix.

## Verify
Test at 360, 768 and 1440 CSS pixels plus long labels.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
