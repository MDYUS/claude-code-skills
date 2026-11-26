# Technical SEO: reference checklist

## Inspect
Inspect rendered titles, descriptions, canonicals, redirects, robots directives, sitemap and links.

## Choose
Separate crawling, indexing and ranking; use truthful schema matching visible content.

## Verify
Check HTTP status and rendered metadata on representative URLs.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
