## Session 16 — The Great Reversion: Local-First for Velocity (add to the story)

The "Hybrid Model" with Claude Projects was a clever optimization but, in practice, it introduced a new class of friction: the sync tax. Every push and pull added seconds to the feedback loop. Every discrepancy between the web UI and the local CLI became a potential source of drift.

The design question: is the token savings worth the cognitive load of a disjointed environment?

The answer was a resounding **no**. We reverted the entire architecture to a pure, local-only CLI model.

### Why this design achieves the goal

**Absolute Source of Truth**
The local filesystem is now the only reality. We moved away from "Sync Masters" and "Local Stubs." Every agent in `.claude/agents/` is now a full-fidelity specification, perfectly aligned with the "God-Source" prompts in `prompts/specs/`. There is no "syncing" — there is only execution.

**Zero Latency Workflow**
By removing the `sync_pull` and `sync_push` gates from the `mmw` critical path, we returned to a zero-latency development experience. The system is responsive, predictable, and fully autonomous within the terminal.

**Token Efficiency via Tools, Not Sync**
We realized that the real token savings didn't come from a shared web UI, but from the deterministic Python tools layer. The local agents are lean because they delegate high-token tasks (like history parsing and file indexing) to local scripts, not because they are offloading reasoning to a Claude Project.

### Why it matters (for the story)

This reversion is a story of "Developer Flow." It recognizes that for a technical writer building at the edge, even a few seconds of sync delay is a flow-breaker. The system is at its best when it is unencumbered by external state.

We didn't just go back to where we were. We returned more disciplined — with cleaner specs, better tools, and a firm commitment to the local-first philosophy.

---