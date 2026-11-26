# UI design improvement: reference checklist

## Inspect
Establish hierarchy, typography, spacing, restrained colors, brand assets and interaction states.

## Choose
Use coherent tokens and task-driven layouts instead of generic cards and gratuitous effects.

## Verify
Compare screenshots at mobile and desktop sizes; inspect focus and error states.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
