# LLM evaluation: reference checklist

## Inspect
Define task rubric, held-out cases, baseline, repeatability and model/version metadata.

## Choose
Use representative failures and blind comparisons when feasible; avoid tuning on test sets.

## Verify
Record per-case outputs, scores and uncertainty.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
