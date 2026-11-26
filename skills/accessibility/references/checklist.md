# Accessible interfaces: reference checklist

## Inspect
Use native semantics, accessible names, focus order, contrast and reduced motion.

## Choose
Prefer native controls over custom ARIA widgets.

## Verify
Check keyboard flows, zoom and error announcements; distinguish manual from automated checks.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
