# Container engineering: reference checklist

## Inspect
Use minimal trusted base images, multi-stage builds, non-root users and explicit runtime configuration.

## Choose
Keep secrets out of layers and build args; pin versions according to update policy.

## Verify
Build and run locally, check health and image contents.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
