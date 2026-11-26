# Claude Code Skills Guide — 50 Open-Source Agent Skills

Choose the right skill for debugging, frontend development, technical SEO, security, testing, programming languages and AI engineering. See [Quick start](QUICKSTART.md) for installation and [Workflows](WORKFLOWS.md) for combinations.

## Which skill should I use?

| Your task | Start with | Follow with |
|---|---|---|
| Bug or unexpected output | [/debugging](skills/debugging/SKILL.md) | /test, /code-review |
| Generic AI website | [/anti-slop](skills/anti-slop/SKILL.md) | /responsive, /accessibility |
| Search indexing issue | [/seo](skills/seo/SKILL.md) | /content-check |
| Authentication or data exposure | [/security](skills/security/SKILL.md) | /privacy, /test |
| Slow code or database | [/performance](skills/performance/SKILL.md) | /postgres-expert |
| Deploy a project | [/ship](skills/ship/SKILL.md) | /deploy, /smoke-test |
| Build AI integrations | [/mcp-developer](skills/mcp-developer/SKILL.md) | /llm-evaluation |
| Reduce context overhead | [/token-save](skills/token-save/SKILL.md) | /handoff |

## Complete skill catalog

### Quality

| Skill | Purpose |
|---|---|
| [/audit](skills/audit/SKILL.md) | Repository audit |
| [/debugging](skills/debugging/SKILL.md) | Root cause debugging |
| [/test](skills/test/SKILL.md) | Regression testing |
| [/code-review](skills/code-review/SKILL.md) | Code review |
| [/fix-all](skills/fix-all/SKILL.md) | Defect remediation |
| [/performance](skills/performance/SKILL.md) | Performance engineering |
| [/playwright-expert](skills/playwright-expert/SKILL.md) | Browser automation |

### Design

| Skill | Purpose |
|---|---|
| [/anti-slop](skills/anti-slop/SKILL.md) | UI design improvement |
| [/responsive](skills/responsive/SKILL.md) | Responsive design |
| [/accessibility](skills/accessibility/SKILL.md) | Accessible interfaces |
| [/forms](skills/forms/SKILL.md) | Robust forms |
| [/i18n](skills/i18n/SKILL.md) | Internationalization |

### Growth

| Skill | Purpose |
|---|---|
| [/seo](skills/seo/SKILL.md) | Technical SEO |
| [/content-check](skills/content-check/SKILL.md) | Content quality |

### Safety

| Skill | Purpose |
|---|---|
| [/security](skills/security/SKILL.md) | Defensive security |
| [/privacy](skills/privacy/SKILL.md) | Privacy engineering |
| [/dependency-review](skills/dependency-review/SKILL.md) | Dependency review |
| [/incident](skills/incident/SKILL.md) | Incident triage |

### Workflow

| Skill | Purpose |
|---|---|
| [/token-save](skills/token-save/SKILL.md) | Context efficiency |
| [/handoff](skills/handoff/SKILL.md) | Agent handoff |
| [/docs](skills/docs/SKILL.md) | Developer documentation |
| [/onboarding](skills/onboarding/SKILL.md) | Contributor onboarding |
| [/git-hygiene](skills/git-hygiene/SKILL.md) | Safe Git workflow |
| [/cost-review](skills/cost-review/SKILL.md) | Cost optimization |

### Engineering

| Skill | Purpose |
|---|---|
| [/api-contract](skills/api-contract/SKILL.md) | API contracts |
| [/database-migration](skills/database-migration/SKILL.md) | Schema migration |
| [/architecture](skills/architecture/SKILL.md) | System architecture |
| [/refactor](skills/refactor/SKILL.md) | Safe refactoring |
| [/observability](skills/observability/SKILL.md) | Observability |

### Release

| Skill | Purpose |
|---|---|
| [/deploy](skills/deploy/SKILL.md) | Deployment planning |
| [/ship](skills/ship/SKILL.md) | Release readiness |
| [/release-notes](skills/release-notes/SKILL.md) | Release notes |
| [/smoke-test](skills/smoke-test/SKILL.md) | Smoke testing |

### Languages

| Skill | Purpose |
|---|---|
| [/python-pro](skills/python-pro/SKILL.md) | Python development |
| [/typescript-pro](skills/typescript-pro/SKILL.md) | TypeScript development |
| [/javascript-pro](skills/javascript-pro/SKILL.md) | JavaScript development |
| [/sql-pro](skills/sql-pro/SKILL.md) | SQL engineering |

### Frameworks

| Skill | Purpose |
|---|---|
| [/react-expert](skills/react-expert/SKILL.md) | React development |
| [/nextjs-expert](skills/nextjs-expert/SKILL.md) | Next.js development |
| [/angular-expert](skills/angular-expert/SKILL.md) | Angular development |
| [/vue-expert](skills/vue-expert/SKILL.md) | Vue development |
| [/fastapi-expert](skills/fastapi-expert/SKILL.md) | FastAPI development |
| [/django-expert](skills/django-expert/SKILL.md) | Django development |

### Infrastructure

| Skill | Purpose |
|---|---|
| [/postgres-expert](skills/postgres-expert/SKILL.md) | PostgreSQL engineering |
| [/docker-expert](skills/docker-expert/SKILL.md) | Container engineering |
| [/ci-cd](skills/ci-cd/SKILL.md) | Continuous integration |

### AI

| Skill | Purpose |
|---|---|
| [/mcp-developer](skills/mcp-developer/SKILL.md) | Model Context Protocol development |
| [/rag-engineer](skills/rag-engineer/SKILL.md) | Retrieval augmented generation |
| [/llm-evaluation](skills/llm-evaluation/SKILL.md) | LLM evaluation |
| [/prompt-engineering](skills/prompt-engineering/SKILL.md) | Prompt engineering |

## Example prompts

- `/debugging Reproduce this checkout failure before changing code.`
- `/anti-slop Improve this landing page without replacing our branding.`
- `/seo Inspect redirects, canonicals and sitemap consistency.`
- `/typescript-pro Validate API inputs and remove unsafe assertions.`
- `/ship Produce an evidence-based readiness matrix; do not deploy.`

Skills are instructions, not guaranteed improvements or automated scanners. Real agent effectiveness requires evaluation.