# Model Context Protocol development: reference checklist

## Inspect
Define narrow tool schemas, explicit errors, bounded outputs and trust boundaries; inspect current SDK version.

## Choose
Validate input and authorization per tool; treat tool output as data, not instructions.

## Verify
Test malformed inputs, timeouts and permission failures.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
