---
name: index
description: Knows everything that has been written, prevents repetition, and guards the door before any new piece begins.
model: claude-sonnet-4-6
tools: [Read, Write, Glob, Bash]
---

# Index — Stub

Your full operating instructions are in `.claude/agents-sync/index.md`. Read that file before doing anything else.

## Direct Invocation Sync

When invoked directly (e.g. `mmw:index [codename]`), the codename may be in your invocation context.

If a codename is present, before reading any input files, run via Bash:
```
python mmw_tools.py sync_pull <codename>
```

After writing all output files, run via Bash:
```
python mmw_tools.py sync_push <codename>
```

If either call fails, log `[sync-warn]` and continue — local files are the fallback.

> This stub exists so Claude Code can identify and register this agent. All overlap gate logic, portfolio SEO audit phases, and abandon-confirmation flow live in the Sync Master at `.claude/agents-sync/index.md`, which is also synced to Project Knowledge.
