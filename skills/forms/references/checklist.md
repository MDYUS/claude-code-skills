# Robust forms: reference checklist

## Inspect
Map validation, pending, duplicate submission, failure and success states.

## Choose
Enforce validation server-side as well as client-side; retain input after recoverable errors.

## Verify
Test empty, malformed, duplicate and network-failure submissions.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
