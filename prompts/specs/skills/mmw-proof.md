---
name: mmw-proof
description: Declare an mmw piece final. Runs pre-flight checks and, if all pass, writes final.md and publishes to writers-room/published/. This is always a deliberate human decision — no agent calls this automatically.
argument-hint: [codename]
---

Invoke Caret inline (do not spawn a subagent). Execute the Phase 11 pre-flight directly for the piece named by `$ARGUMENTS`:

1. Run `python scripts/mmw_tools.py preflight $ARGUMENTS` — returns `{"ready": true/false, "failures": [...]}`.
2. If `ready` is false: surface each item in `failures` to the user and stop.
3. If `ready` is true: run `python scripts/mmw_tools.py publish $ARGUMENTS` — atomically writes final.md, published/[slug].md, and published/[slug]-image-prompt.md and updates status.md.
4. Write `Mode: archive-update` to `status.md` (via `python scripts/mmw_tools.py status_write $ARGUMENTS '{"mode": "archive-update"}'`).
5. Spawn Index and Cadence in parallel.

If `$ARGUMENTS` is empty: scan `status.md` files in `writers-room/pieces/` for any piece containing `Next step: Ready for mmw:proof`, list them, and ask the user to confirm which one to proof. Never assume.
