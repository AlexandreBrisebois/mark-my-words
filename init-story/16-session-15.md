## Session 15 — Strategic Context Management: The /clear Protocol (add to the story)

As the multi-agent system matured and the pieces grew more complex, a new constraint surfaced: the "input tax" of the long-running Caret session. Every turn in a long writing project carried the token weight of every previous turn. The more we wrote, the more expensive it became to think.

The design problem: how do we keep the orchestrator's window lean without losing the thread of the project?

The answer was the **Strategic Context Reset Protocol** — a deliberate use of the `/clear` command at high-signal transition points, paired with a robust re-entry path via `mmw:bearings`.

### Why this design achieves the goal

**Token-Efficient Reasoning**

By recommending a `/clear` at four strategic boundaries, we effectively reset the model's "memory bill" to zero. The previous phase's scaffolding — raw research data, iterative line-edits, or complex critique logic — is removed from the active window. This forces the model to focus purely on the next task using the persisted state on disk as its only source of truth.

**The "Stateless" Design Payoff**

MMW was built from the start to be stateless, with everything from piece status to draft history living in the filesystem. This iteration proved the value of that choice. Because the `status.md` and `brief.md` are the canonical memory, the conversation history is disposable. Clearing it doesn't break the logic; it purifies it.

**Strategic Reset Points**

We identified four "Clean Handoff" moments where the previous context becomes technical debt:
1. **The Research-to-Draft Boundary** (post-Turing): Once research is on disk, the raw search history is noise.
2. **The Draft-to-Review Boundary** (post-Phase 3): The draft is the new source of truth.
3. **The Branding-to-Critique Boundary** (post-Mark loop): Critics should see the polished text with fresh eyes, not biased by the history of line-edits.
4. **The Creative-to-Technical Boundary** (post-Revision): SEO and image prompt generation are deterministic tasks that don't need creative backstory.

**The Re-entry Path: mmw:bearings**

A `/clear` is only safe if you can find your way back. We standardized `mmw:bearings [codename]` as the re-entry command. It reads `status.md`, reports the current state, and restores the next-step prompt. It makes the transition from a "dirty" long session to a "clean" focused session feels like a single continuous motion.

### Why it matters (for the story)

This iteration represents a shift from "agentic persistence" to "agentic focus." We moved from trying to keep a single agent in context for an entire project to treating the context window as a ephemeral workspace.

It proves that in a sophisticated multi-agent system, the file system is the only memory that matters. The context window is not a journal; it's a workbench. When you're done with one toolset, you clear the bench for the next.

### Additional angle for Compass

- **The workbench angle**: The difference between a conversation and a workflow. A conversation needs memory; a workflow needs focus. By using `/clear` strategically, we treat the LLM context not as a historical record of our chat, but as a clean workbench for the task at hand. Token efficiency isn't just about saving money; it's about increasing the signal-to-noise ratio of the reasoning.

---