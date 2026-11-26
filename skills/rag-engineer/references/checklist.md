# Retrieval augmented generation: reference checklist

## Inspect
Separate ingestion, chunking, indexing, retrieval, reranking and grounded generation.

## Choose
Measure retrieval quality before tuning prompts; enforce document-level access.

## Verify
Use labeled questions, citation checks and adversarial document tests.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
