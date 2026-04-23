---
name: caret-protocol
description: Governs the state contract, handoff dashboard, and non-destructive drafting rules. Use for task management and handoffs.
---

# Skill: Caret Protocol

Use this skill to manage how the agent interacts with the codebase and the user.

## Stateless Snapshot (caret.state.md)
Create or **OVERWRITE** `caret.state.md` with each run.
- **DO NOT** append historical logs.
- **DO** include:
  - **Slug**: [generated-slug]
  - **Status**: [Drafting / Refining / Ready for Review]
  - **Metrics**: Word Count, Reading Time, Grade Level.
  - **Completion %**: [0-100%]
  - **Next Steps**: Explicit tasks for the next run.

## Drafting Rules
- **Non-Destructive**: Always write drafts to `{slug}-draft.md`.
- **Slug Immutability**: The slug remains the primary key for all files.
- **Audit Report (Dashboard)**: Every chat response must include:
  1. Value in Lead (Insight timing).
  2. Practitioner Voice (I/We usage).
  3. The Empty Chair (Audience confirmation).
  4. Elevator Pitch (2 sentences).

## Rationale
The chat dashboard is for humans; the snapshot is for agents. Keep the snapshot clean to prevent model confusion in long sessions.
