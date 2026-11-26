# Observability: reference checklist

## Inspect
Identify errors, latency, saturation and throughput; use structured events and correlation IDs.

## Choose
Keep metric cardinality bounded and redact sensitive payloads.

## Verify
Exercise success and failure paths and confirm useful signals.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
