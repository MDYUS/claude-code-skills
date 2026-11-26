# Safe Git workflow: reference checklist

## Inspect
Inspect staged and unstaged diffs, untracked files and current branch.

## Choose
Preserve unrelated user work; never reset or force-push without explicit permission.

## Verify
Review staged diff for accidental secrets and generated files.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
