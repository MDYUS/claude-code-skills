# Internationalization: reference checklist

## Inspect
Externalize strings, use locale-aware formatting and plural rules, account for expansion.

## Choose
Avoid concatenating grammar fragments and distinguish locale from language.

## Verify
Test missing translations, locale switching and long content.

## Evidence record
| Check | Baseline | Actual result | Status | Evidence |
|---|---|---|---|---|
| Core requirement | Record before changes | Record after changes | PASS / FAIL / BLOCKED | Command, log or file path |

## Failure handling
If verification fails, preserve the error and isolate the smallest reproducible case. If the environment or permissions are missing, document the exact blocker and the next safe test. Do not infer success from a generated patch.
