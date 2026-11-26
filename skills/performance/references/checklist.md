# Performance engineering: reference checklist

## Inspect
Measure latency distribution, CPU, memory, bundle weight or rendering as appropriate.

## Choose
Optimize measured bottlenecks and preserve caching correctness.

## Verify
Compare identical workloads with sample count and environment.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
