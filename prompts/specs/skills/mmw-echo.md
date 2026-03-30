---
name: mmw-echo
description: Run an audience check on the latest draft of an active mmw piece. Spawns Echo directly.
argument-hint: [codename]
---

Spawn the `echo` subagent defined in `.claude/agents/echo.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-echo [codename]" and do nothing further.
