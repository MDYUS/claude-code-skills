# React development: reference checklist

## Inspect
Use stable keys, derived state, effect cleanup and accessible components.

## Choose
Avoid effects for pure derivations; memoize only measured bottlenecks.

## Verify
Test loading, error, updates and unmount behavior.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
