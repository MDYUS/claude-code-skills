# TypeScript development: reference checklist

## Inspect
Use strict types, discriminated unions, unknown at external boundaries and runtime schema validation.

## Choose
Avoid any and unsafe assertions; distinguish compile-time narrowing from runtime checks.

## Verify
Run tsc and test malformed external input.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
