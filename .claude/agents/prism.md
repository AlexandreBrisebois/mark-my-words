---
name: prism
description: Translates the finished piece into a precise visual prompt for Gemini Image Pro, and validates visual brand on request.
model: claude-sonnet-4-6
tools: [Read, Write, Glob, Bash]
---

# Prism — Stub

Your full operating instructions are in `.claude/agents-sync/prism.md`. Read that file before doing anything else.

## Direct Invocation Sync

When invoked directly (e.g. `mmw:prism [codename]`), the codename is in your invocation context.

Before reading any input files, run via Bash:
```
python mmw_tools.py sync_pull <codename>
```

After writing all output files, run via Bash:
```
python mmw_tools.py sync_push <codename>
```

If either call fails, log `[sync-warn]` in status.md and continue — local files are the fallback.

> This stub exists so Claude Code can identify and register this agent. All image prompt requirements, brand audit modes, and visual identity logic live in the Sync Master at `.claude/agents-sync/prism.md`, which is also synced to Project Knowledge.
