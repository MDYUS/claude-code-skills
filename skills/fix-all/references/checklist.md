# Defect remediation: reference checklist

## Inspect
Build a prioritized issue ledger and preserve unrelated working-tree edits.

## Choose
Fix critical risks first, use minimal patches, and stop when scope changes materially.

## Verify
Map each patch to a regression check.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
