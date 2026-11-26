# Prompt engineering: reference checklist

## Inspect
Define objective, constraints, examples, output schema and untrusted input boundaries.

## Choose
Prefer clear task instructions and measurable acceptance criteria over magical wording.

## Verify
Evaluate baseline and revised prompts on held-out cases.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
