## Session 18 — Governance: Hard Limits and Lean Gates (add to the story)

The system was running locally, but "local" doesn't mean "infinite." We realized that even without API sync lag, we were still paying a tax — the tax of bloated context and rogue agent loops. An agent that searches the web twenty times or reads ten historical drafts is an agent that has lost its way.

The design problem: how do we enforce discipline on a system that is designed to be autonomous?

The answer was **Token Governance** — a set of hard architectural limits and "soft gates" that force the system to stay lean.

### What was built

**The 10/10 Research Budget**
Turing, the researcher, was given a hard cap: 10 `WebSearch` queries and 10 `WebFetch` calls per pass. No exceptions. If it can't find the signal in twenty moves, more moves won't help. It forces the model to prioritize high-signal sources over high-volume data.

**Targeted Reading Boundaries**
We moved from "agents read the folder" to "agents read the slice." Mark, Devil, Echo, and Press were explicitly restricted to reading only the `brief.md` and the *current* `draft-vN.md`. They no longer see historical critiques or previous versions. They work only with the context they need to perform their specific role.

**The reset_pending Handshake**
We formalized the `/clear` recommendation into a protocol. Caret now writes `reset_pending: true` into `status.md` at four critical workflow boundaries. When the user resumes via `mmw:bearings`, the system checks for that flag. If a reset hasn't happened, it issues a warning. If it has, it clears the flag and confirms: `✓ Context reset verified (lean session active).`

### Why it matters (for the story)

This is a story of "Constraints as a Feature." We stopped treating the context window as a bottomless resource and started treating it as a transient, high-value workspace. 

The budget isn't just about saving money; it's about forcing better reasoning. An agent that has to work within a 10/10 budget is an agent that thinks harder about its queries. An agent that only sees the current draft is an agent that isn't biased by the ghosts of previous feedback.

We moved from building a system that *can* write to building a system that is *disciplined* about how it writes.

### Additional angle for Compass

- **The governance angle**: The difference between a system that works and a system that is governed. Governance isn't about stopping work; it's about setting the boundaries that make the work better. In a multi-agent system, the strongest tool you have is the ability to say "no more." 

- **The ghost-free drafting angle**: By enforcing targeted reading, we ensure that each agent evaluates the work as it exists *now*, not as it existed in the previous turn. We removed the "historical bias" from the review loop, ensuring that Devil and Echo are always reacting to the latest signal, never the old noise.

---