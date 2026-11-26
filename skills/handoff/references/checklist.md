# Agent handoff: reference checklist

## Inspect
Record goal, decisions, affected paths, exact test results and unresolved issues.

## Choose
Prefer durable facts over full transcripts; mark assumptions and stale evidence.

## Verify
Ensure a fresh agent can reproduce the latest check.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
