# Contributor onboarding: reference checklist

## Inspect
Identify prerequisites, setup, configuration examples and first useful task.

## Choose
Prioritize a clean runnable example and actionable troubleshooting.

## Verify
Try setup in a clean environment and record blockers.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
