# Continuous integration: reference checklist

## Inspect
Separate build, test and deployment; use least privilege tokens and trusted dependencies.

## Choose
Avoid unsafe untrusted PR execution with secrets; keep deployments gated.

## Verify
Verify workflow syntax and inspect actual job results.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
