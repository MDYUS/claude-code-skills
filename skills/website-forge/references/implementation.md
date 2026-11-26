# Functional implementation checklist

## Scope and architecture
- Record routes with purpose, required content and CTA destination. Keep shared navigation and footer consistent; ensure current navigation state where useful.
- Check actual runtime/package manager and lockfile. Preserve project conventions. For new projects document selected stack and why.
- Implement business rules before decorative enhancements. Use semantic HTML, explicit component interfaces and reliable state handling. Prefer small coherent modules over one giant generated file.

## Marketing sites
- Landing: value proposition, proof only when supplied, relevant offerings, CTA, contact path.
- Service pages: actual service scope, useful examples, process and appropriate enquiry action.
- Portfolio: real project assets and descriptions; use placeholders explicitly only if necessary.
- Contact: accessible labels, client and server validation, pending state, safe submission and real confirmation only after success. Never display a fake success alert for an unconnected form.
- External links: correct targets, no invented social links or contact information. Provide meaningful 404 and navigation recovery where supported.

## Web applications
- Define roles, resource ownership, persistence, route protection, and authorization rules. Test negative access paths. Never rely only on frontend hiding for access control.
- Use trusted auth libraries and verified SDKs; do not implement custom crypto. Keep tokens and secrets out of client bundles, logs and version control.
- Handle validation, retries, concurrency and idempotency for consequential writes. Use parameterized queries and transactions as appropriate. Keep migrations reversible when feasible; never run destructive migrations without authorization.
- Payments: use authorized provider sandbox first, server-verified webhook signatures, safe idempotency, explicit charge confirmation. Do not process a real charge as a test.
- AI integrations: use authorized providers and actual APIs; expose costs, pending/failure states and limitations; never simulate successful generation as real.

## SEO and deployment
- Unique descriptive titles and useful content; canonical, sitemap and redirects must agree with actual public URL structure. If domain unknown, configure via environment and document remaining work.
- Schema must reflect visible verified content. Do not add invented ratings or FAQ rich-result guarantees. Protect private pages with authentication, not just noindex.
- Provide environment template, local start/build/test commands and deployment instructions suitable for the stack. Do not choose a static-only host for a server-dependent app without an appropriate backend.
