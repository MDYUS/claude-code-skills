# Incident triage: reference checklist

## Inspect
Establish timeline, observed impact, affected systems and reversible containment.

## Choose
Preserve evidence and get approval for disruptive operations.

## Verify
Confirm restoration and document unresolved indicators without exposing secrets.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
