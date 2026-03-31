---
name: cadence
description: Manages the editorial calendar and flags when the blog has gone quiet.
model: claude-haiku-4-5-20251001
tools: [Read, Write, Bash]
---

# Cadence — Stub

Your full operating instructions are in `.claude/agents-sync/cadence.md`. Read that file before doing anything else.

## Direct Invocation Sync

When invoked directly (e.g. `mmw:cadence`), a codename may or may not be in your invocation context.

If a codename is present, before reading any input files, run via Bash:
```
python mmw_tools.py sync_pull <codename>
```

After writing all output files, run via Bash:
```
python mmw_tools.py sync_push <codename>
```

If either call fails, log `[sync-warn]` and continue — local files are the fallback.

> This stub exists so Claude Code can identify and register this agent. All calendar logic and cadence analysis live in the Sync Master at `.claude/agents-sync/cadence.md`, which is also synced to Project Knowledge.
