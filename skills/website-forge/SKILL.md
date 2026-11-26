---
name: website-forge
description: Build complete, distinctive, production-oriented websites and web applications from natural-language briefs. Use for text-to-website development, new sites, full-stack web apps, landing pages, ecommerce, portfolios and redesigns when polished UI, functional flows, accessibility, SEO and real verification are required.
---
# Website Forge — text to complete website

Convert the user's brief into working source code, not a screenshot, design-only mockup, or generic template. Optimize for the customer's task, the brand and the actual content. Preserve existing working features and user changes.

## 1. Understand and plan
- Inspect the repository, framework version, routes, dependencies, existing components and design references before editing. Never overwrite unrelated work or switch frameworks unnecessarily.
- Extract audience, business goal, conversion action, page inventory, brand assets, content, required integrations and deployment constraints from the brief. Ask only for facts that block progress; otherwise make reversible assumptions and disclose them.
- Produce a compact route/feature map with acceptance criteria. For a marketing site, include relevant service/product pages, navigation, contact journey and error states; for apps, map roles, authentication, persistence and critical workflows. Do not add irrelevant pages just to appear complete.
- Select one coherent visual concept, define type scale, palette, spacing, layout rhythm and image direction before building. Read [design system](references/design.md) for the anti-slop rules.

## 2. Build the real thing
- Use the existing stack. For a greenfield content site prefer semantic HTML/CSS/JS or a suitable static framework; choose a full-stack framework only when requirements justify it. Use installed dependencies and verify version-specific APIs. No heavy dependencies solely for decorative effects.
- Build shared layout, navigation and footer, then complete each required route with original, context-specific content. Make all primary CTAs work. Implement loading, empty, validation, error and success states wherever relevant.
- Build server-side flows when needed. Validate input at boundaries, enforce authorization on the server, use safe database queries and keep secrets server-side. Use an example environment file without credentials. No fake login, checkout, submission, testimonials, analytics or data persistence. If credentials are missing, implement and document the integration boundary; mark live verification blocked.
- Use user-owned/licensed imagery or authorized image tools when available. Give every image a purpose, correct crops and meaningful alt text. Never use fabricated portfolio photos as real projects. No invented reviews, achievements, client logos, awards or business contact details. Clearly label placeholders and demo data.
- Read [implementation checklist](references/implementation.md) for page and backend details.

## 3. Reject AI slop through design review
- Avoid the default purple-gradient/glass-card aesthetic, repetitive equal-size grids, giant empty heroes, pill overload, random blobs, excessive shadows, emoji-as-icons, meaningless jargon and stock imagery used as filler. These are warning signs, not blanket bans when explicitly justified by the brand.
- Use a recognizable visual hierarchy and intentional composition. Favor actual product or service imagery, useful copy, coherent typography and consistent controls. Avoid wrapping every paragraph in a card.
- Use motion only to guide attention, communicate state or reinforce the brand. Respect reduced-motion preferences; avoid scroll hijacking, autoplay audio and unnecessary 3D. Never claim an animation works until observed in a browser.
- Match references in structure, hierarchy and behavior where authorized, without copying proprietary assets or misrepresenting affiliation.

## 4. SEO, accessibility, speed
- Use semantic landmarks, meaningful headings, descriptive links, keyboard-accessible controls, visible focus, sufficient contrast and accessible form errors. Use native controls where possible.
- For public indexable pages, produce unique title and description, canonical URL only when the actual domain is known, logical internal links, appropriate robots and sitemap, Open Graph metadata, and truthful structured data when relevant. Keep private routes non-indexable; do not mistake robots.txt for access control. No keyword stuffing or ranking guarantees.
- Reserve image dimensions, use responsive sources, lazy-load below-the-fold imagery, optimize fonts, minimize blocking scripts and unnecessary client JS. Avoid invisible text, layout shifts and mobile overflow. Measure rather than invent performance scores.

## 5. Execute verification — do not merely promise it
Read [verification protocol](references/verification.md). Discover actual project commands and run relevant lint/typecheck/build/tests. Use browser tools or Playwright if available to visit real routes and exercise primary tasks. Capture screenshots at desktop and mobile sizes; inspect console errors, network failures, overflow and interactions. Correct defects and repeat checks. If tools are missing, state exactly what was not tested. Never fabricate screenshots, output, benchmark values, accessibility conformance or deploy URLs.

## 6. Deliver
Provide the working source in the requested format or repository, setup steps, environment variable names, route inventory and concise evidence matrix: PASS / FAIL / BLOCKED. List assumptions, missing credentials, unresolved defects and the next safe step. Do not deploy, publish, purchase, or modify production resources without authorization. Do not claim completion for an unimplemented flow or unrun test.

## Example invocation
`/website-forge Build a premium construction company website for Chennai with service pages, project gallery, enquiry form, mobile navigation, local SEO and a professional editorial design. Use our supplied brand and project photos. Build and test the working source.`
