---
name: mmw-turing
description: Run a research pass on an active mmw piece. Spawns Turing directly, bypassing Caret.
argument-hint: [codename]
---

Spawn the `turing` subagent defined in `.claude/agents/turing.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-turing [codename]" and do nothing further.
