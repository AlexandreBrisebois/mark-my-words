---
name: mmw-mark
description: Run a brand and voice review on the latest draft of an active mmw piece. Spawns Mark directly.
argument-hint: [codename]
---

Spawn the `mark` subagent defined in `.claude/agents/mark.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-mark [codename]" and do nothing further.
