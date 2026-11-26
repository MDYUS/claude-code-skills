# Next.js development: reference checklist

## Inspect
Identify router and version; separate server and client boundaries, caching and environment variables.

## Choose
Keep secrets server-side and verify framework-specific APIs against installed version.

## Verify
Run production build and test dynamic routes and unauthorized access.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
