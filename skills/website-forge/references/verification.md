# Evidence-based website verification

## Before testing
Identify available tools and the actual commands in package manifests or project docs. Run only in an authorized local/test environment. Never use real customer data or trigger real emails, charges, publication or destructive operations without approval.

## Execute
1. Install dependencies using the project's package manager and lockfile when permitted. Record versions and any network or credential blockers.
2. Run relevant lint, typecheck, tests and production build. Record exact exit codes. If a check does not exist, do not mark it passed.
3. Start the application and use a real browser to visit each required route. Capture console errors, failed requests and screenshots. Test navigation, CTAs, form validation, keyboard interaction, loading/empty/error/success states and other critical journeys.
4. Test representative widths such as 360, 768, 1024 and 1440 CSS pixels; inspect screenshots and overflow. Verify touch usability, zoom, focus, contrast and reduced motion. Automated accessibility checks alone do not prove WCAG compliance.
5. Verify SEO metadata and internal links on rendered pages, HTTP statuses and sitemap/robots consistency where deployed. Check asset requests, layout shifts and meaningful performance metrics with available tools. Never invent Lighthouse scores.
6. Fix confirmed defects and repeat the failing checks plus relevant regression checks. Avoid unrelated rewrites. Inspect final diff for secrets, unintended generated files and scope changes.

## Report
| Check | Status | Evidence |
|---|---|---|
| Production build | PASS / FAIL / BLOCKED | Actual command and exit code |
| Primary routes | PASS / FAIL / BLOCKED | URLs and observations |
| Mobile layout | PASS / FAIL / BLOCKED | Viewports and screenshots |
| Critical user flow | PASS / FAIL / BLOCKED | Test case and result |
| External service | PASS / FAIL / BLOCKED | Sandbox result or missing credential |
| SEO and accessibility | PASS / FAIL / BLOCKED | Specific inspected checks |

PASS means the stated check actually ran and succeeded. FAIL means it ran and failed. BLOCKED means the tool, environment, credentials or prerequisites were unavailable. A successful build does not prove visual quality or functional completeness.
