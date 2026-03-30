---
name: mmw-compass
description: Run a strategic direction pass on an active mmw piece, or generate next post ideas if no codename is provided. Spawns Compass directly.
argument-hint: [codename]
---

Spawn the `compass` subagent defined in `.claude/agents/compass.md`, passing `$ARGUMENTS` as the active piece codename (or empty for a next-post-ideas pass).
