---
name: mmw-devil
description: Run an accusation audit on the latest draft of an active mmw piece. Spawns Devil directly.
argument-hint: [codename]
---

Spawn the `devil` subagent defined in `.claude/agents/devil.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-devil [codename]" and do nothing further.
