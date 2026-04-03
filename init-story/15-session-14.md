## Session 14 — The Hybrid Model: Claude Projects + API (add to the story)

The system was efficient, but it was still expensive. Every time an agent read the codebase to gain context, the meter ran. API tokens are a consumption tax on reasoning. As the project grew, that tax began to scale.

The design question: how do we shift the heavy computational burden — context loading, expansive brainstorming, and long-form generation — away from the metered API?

The answer was an elegant architectural pivot: moving the thin-stub setup to a hybrid model. We shift the thinking to the flat-rate Claude Pro subscription via Claude Projects, while keeping the doing local.

### Why this design achieves the goal

**Token Efficiency and Cost Control**

By keeping the heavy processing in the web UI (Claude Projects), we shield the budget from the runaway API costs that happen when local agents continuously read and re-read a large codebase. API tokens are strictly reserved for necessary system work: executing targeted tasks locally, running automated fixes, and validating code.

We are buying leverage.

**The Bidirectional Sync Loop**

The linchpin is a thin-stub setup in `.claude/agents/`. The agents pull the latest state via `mmw_tools.py sync_pull` before acting and push updates with `sync_push` after completing a task. It prevents drift.

When working in the Claude Project, the Web UI has the absolute latest context. When an agent acts locally, it forces a sync to ensure it doesn't overwrite the web session's progress. It guarantees a single source of truth across environments.

**Separation of Concerns**

The authoritative prompt instructions live in `.claude/agents-sync/`. Because these sync up to Project Knowledge, the web UI Claude and the local CLI agents share the exact same structural rules and persona definitions.

We don't have to train them twice.

### Where we need to be careful

While the design is solid, there are failure points to watch for.

Project Knowledge consumes the available context window even in the web UI. If the `sync_push` script starts throwing entire build directories or compiled assets into the Project, the web sessions will exhaust their limits fast. We must keep the synchronized footprint lean.

Merge collisions are the other risk. If a file is tweaked locally while Claude is simultaneously generating an artifact for that same file in the web UI, the next sync might overwrite work. The logic needs to handle — or at least warn on — version conflicts.

We have built a continuous loop between local execution and remote reasoning.

### Why it matters (for the story)

This iteration transforms the system from a cost center into a sustainable writing partner. It recognizes that reasoning is cheap in a flat-rate UI but expensive at the edge. The system is at its best when it uses the web for the heavy lifting and the local environment for high-fidelity execution.

This is the bridge between the convenience of a web interface and the power of local automation.

### Additional angle for Compass

- **The hybrid model angle**: The difference between using an API for everything and using it for the right things. The constraint of the token meter pushed us to find a better architectural split. We didn't just save money; we built a more resilient sync loop between our thinking space and our building space.

---