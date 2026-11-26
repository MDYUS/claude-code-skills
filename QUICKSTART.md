# Install Claude Code Skills

Requires Python 3.9+ and a local project.

```bash
git clone https://github.com/MDYUS/claude-code-skills.git
cd claude-code-skills
python3 scripts/install.py --project /path/to/project --skills debugging seo ship
```

Replace the example path with your own project directory. Omit --skills to install all 50. Use --dry-run to preview. Existing skill directories are not overwritten. Open your project in Claude Code and invoke /debugging or another installed skill. Inspect instructions before use. Other agents may use different skill locations.

## Manual installation

Copy an entire skill directory, including its references, into your project's .claude/skills directory. No extra API key is needed by this installer; your agent may require its own subscription.

## Troubleshooting

If a skill is not visible, check the actual project root, directory name and SKILL.md frontmatter, then reload your agent if needed. Verify current client documentation.