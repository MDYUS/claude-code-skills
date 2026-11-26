# Privacy engineering: reference checklist

## Inspect
Map data purpose, storage, retention, access, deletion and external transfers.

## Choose
Minimize data collection and default to least access.

## Verify
Use synthetic records to test redaction and deletion; do not claim legal compliance.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
