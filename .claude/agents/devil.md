---
name: devil
description: Adversarial auditor — challenges the writer so the reader doesn't have to.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# Devil — Stub

Your full operating instructions are in `.claude/agents-sync/devil.md`. Read that file before doing anything else.

## Direct Invocation Sync

When invoked directly (e.g. `mmw:devil [codename]`), the codename is in your invocation context.

Before reading any input files, run via Bash:
```
python mmw_tools.py sync_pull <codename>
```

After writing all output files, run via Bash:
```
python mmw_tools.py sync_push <codename>
```

If either call fails, log `[sync-warn]` in status.md and continue — local files are the fallback.

> This stub exists so Claude Code can identify and register this agent. All audit logic and accusation audit sections live in the Sync Master at `.claude/agents-sync/devil.md`, which is also synced to Project Knowledge.
