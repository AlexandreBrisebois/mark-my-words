---
name: mmw
description: Launch the Mark My Words writing system. Spawns Caret as orchestrator for a new piece or resumes an existing one by codename.
argument-hint: [topic or codename]
---

Spawn the `caret` subagent defined in `.claude/agents/caret.md`, passing `$ARGUMENTS` as the user's topic, brief, or codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw [topic or codename]" and do nothing further.
