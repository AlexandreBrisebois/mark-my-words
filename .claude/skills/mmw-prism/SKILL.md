---
name: mmw-prism
description: Generate a Gemini Image Pro prompt for the latest draft of an active mmw piece. Spawns Prism directly.
argument-hint: [codename]
---

Spawn the `prism` subagent defined in `.claude/agents/prism.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-prism [codename]" and do nothing further.
