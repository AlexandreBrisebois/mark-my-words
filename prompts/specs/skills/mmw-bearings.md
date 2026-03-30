---
name: mmw-bearings
description: Get a session orientation report for an active mmw piece — what has been done, current draft, outstanding work, and proposed next step.
argument-hint: [codename]
---

Invoke Caret inline (do not spawn a subagent). Read `writers-room/pieces/$ARGUMENTS/status.md` and the agent run log, then produce a concise orientation report:

```
Bearings: [codename]
Description: [one-line description from status.md]

Done:
  [x] [each completed agent run from the log]

Current draft: [latest draft-vN.md]
Outstanding: [summary of what is not yet done]

Next step: [proposed next action]
  [C] Continue  [S] Stop
```

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-bearings [codename]" and do nothing further. Always pause after the report — never auto-advance.
