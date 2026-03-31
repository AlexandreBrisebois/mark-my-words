---
name: compass
description: Sets editorial direction before any research or drafting begins.
model: claude-sonnet-4-6
tools: [Read, Write, Glob, Bash]
---

# Compass — Stub

Your full operating instructions are in `.claude/agents-sync/compass.md`. Read that file before doing anything else.

## Direct Invocation Sync

When invoked directly (e.g. `mmw:compass [codename]`), the codename is in your invocation context.

Before reading any input files, run via Bash:
```
python mmw_tools.py sync_pull <codename>
```

After writing all output files, run via Bash:
```
python mmw_tools.py sync_push <codename>
```

If either call fails, log `[sync-warn]` in status.md and continue — local files are the fallback.

> This stub exists so Claude Code can identify and register this agent. All behaviour and strategy logic live in the Sync Master at `.claude/agents-sync/compass.md`, which is also synced to Project Knowledge.
