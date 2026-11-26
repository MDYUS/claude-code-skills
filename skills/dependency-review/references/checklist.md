# Dependency review: reference checklist

## Inspect
Inspect manifests, lockfiles and authoritative vulnerability advisories.

## Choose
Prefer smallest compatible fixes; assess reachability and avoid blind major upgrades.

## Verify
Run clean install and regression checks; document unresolved advisories.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
