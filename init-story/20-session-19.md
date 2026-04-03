## Session 19 — The Great Simplification: From Agents to Skills (add to the story)

The multi-agent system was a masterclass in automation, but it carried a hidden cost: **orchestration bloat**. As the system grew, so did the context windows, the token usage, and the latency. We had built a high-fidelity editorial office, but to use it, the writer had to manage a complex flow and navigate a rigid file-based memory (`writers-room/`).

The design question: how do we keep the specialized personas (Compass, Mark, Devil) without the "infrastructure tax"?

The answer was a definitive pivot to **GitHub Copilot Skills**. We moved away from automated orchestration and returned to a conversation-centric, flexible model.

### Why this design achieves the goal

**Human-in-the-Loop Orchestration**
Instead of a "Caret" agent deciding who runs next, the writer is the orchestrator. You call the skill you need, when you need it: `@mmw /compass` for strategy, `@mmw /mark` for brand guidance. This eliminates the "orchestrator overhead" and gives the writer absolute control over the creative sequence.

**The "No Infrastructure" Philosophy**
We deleted the `writers-room/` directory and all its nested complexity. MMW is no longer a "system you manage"—it is a suite of tools that follow you. You work in your current directory, and the skills anchor themselves to your draft.

**Cumulative Insights (The 00-Series)**
The shared file-based memory was replaced by **Persistent Context**. Each skill now maintains its own `00_<skill>.md` file in the working directory. These files act as "skill-specific memory," ensuring that Compass remembers your strategy and Mark remembers your voice without requiring a massive unified status file.

### Why it matters (for the story)

This transition is a story of "Aesthetic & Cognitive Minimalist." It recognizes that AI is at its best when it enhances the human writer, not when it attempts to replace the editorial flow with an automated pipeline. 

We didn't lose the "Writers' Room." We just turned it into a high-performance toolkit. The personas are as sharp as ever, but they are now unencumbered by the machinery that was originally designed to support them.

### Additional angle for Compass

- **The simplification angle**: The difference between a "system" and a "toolkit." A system requires maintenance; a toolkit requires mastery. By moving to Skills, we reduced the "infrastructure to value" ratio to the absolute minimum.

- **The piece-centric angle**: By moving from `writers-room/` to a single-piece-per-directory focus, we anchored the AI to the writer's actual context, not a project management schema. The "working directory" is the only context that matters.

---