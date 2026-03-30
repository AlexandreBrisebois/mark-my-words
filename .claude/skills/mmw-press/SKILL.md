---
name: mmw-press
description: Run an SEO audit and generate Hugo front matter for the latest draft of an active mmw piece. Spawns Press directly.
argument-hint: [codename]
---

Spawn the `press` subagent defined in `.claude/agents/press.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-press [codename]" and do nothing further.
