# Tool Scoping — Authoritative Reference

This file is the single source of truth for agent tool scoping. When an agent's permitted tools change, update this table and rerun Step B for that agent only.

**Tool names are case-sensitive** and must match Claude Code's registered names exactly: `Read`, `Write`, `Edit`, `Agent`, `Glob`, `Bash`, `WebSearch`, `WebFetch`. A mistyped tool name will silently fail to scope access — no error is raised.

The `tools` value in each agent's YAML frontmatter must be a YAML inline sequence (bracketed, comma-separated). Example: `tools: [Read, Write, Edit]`. A plain string (`tools: Read, Write`) will not be parsed as a list and silently disables tool scoping.

## Agent Tool Scoping Table

| Agent | `tools` frontmatter value |
|---|---|
| Caret | Read, Write, Edit, Agent, Glob, Bash |
| Mark | Read, Write |
| Compass | Read, Write, Glob |
| Devil | Read, Write |
| Turing | Read, Write, WebSearch, WebFetch, Glob, Bash |
| Echo | Read, Write |
| Press | Read, Write, Edit, Glob, Bash |
| Prism | Read, Write, Glob |
| Index | Read, Write, Glob, Bash |
| Cadence | Read, Write, Bash |

**Tool scoping is enforced by Claude Code via the frontmatter — not by prose instructions inside the file body.** Do not rely on written instructions alone to restrict tool access.

Add `Bash` to any agent that calls `mmw_tools.py` (see Step B in the build prompt).
