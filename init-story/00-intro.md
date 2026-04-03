# Mark My Words Origin Story — Overview

**Status**: Version 1, Updated 2026-04-03  
**Format**: Progressive narrative of system evolution  
**Audience**: CTOs, engineers, AI enthusiasts — builders of systems

---

## Key Learnings (Inverted Pyramid — Most Recent at Top)

**Session 21 Learning**: **Documentation is the handoff.** A system is not finished when it works. It's finished when you can hand it to someone else and they can use it without your help. The final documentation refresh captured not just what MMW is, but how it came to be and why choices matter.

**Session 20 Learning**: **Direct invocation with state files beats both orchestration and chat-layer routing.** Writers want to call agents directly (`@compass`, `@turing`, `@caret`). Context recovery through state files lets them iterate freely. Role tightening to single-domain agents reduced token overhead by 30-40%.

**Session 19 Learning**: **The Great Simplification.** Moved from orchestration-heavy agents to human-orchestrated Skills. The insight: AI is at its best when it enhances the human workflow, not when it tries to replace the editorial flow.

**Session 18 Learning**: **Constraints are a feature.** Token governance (10/10 research budget, targeted reading boundaries) forces better reasoning. An agent with limits thinks harder.

**Session 17 Learning**: **Separation of concerns.** Extract the sync infrastructure into its own agent and its own folder. MMW stays clean; the Project Agent handles synchronization.

**Session 16 Learning**: **Local-first beats cloud-first for velocity.** The hybrid model added latency and complexity. Returning to local-only operation gave back the flow.

**Sessions 13-15 Learning**: **The token math changes everything.** Token optimization, context management, model selection—these are not nice-to-haves. They determine whether the system works at all.

**Sessions 9-12 Learning**: **Specs are the source of truth.** Design through conversation, then audit the design rigorously. Each audit asks a different question. The specs must be reviewed before any agent is built.

**Sessions 2-8 Learning**: **Architecture emerges through conversation.** The best system design comes not from specification, but from the questions asked and decisions made together.

**Session 1 Learning**: **Names encode philosophy.** Short, memorable, layered names guide the entire system design.

---

## How This File Works

This intro file is **your update point**. When you learn something new or the system evolves:

1. **Add the new learning to the top** under "Key Learnings"
2. **Push previous learnings down** as the inverted pyramid grows
3. **Keep the most recent insight at the peak**
4. **Reference the session** that taught the lesson

The other files (individual sessions) remain immutable. The intro is your living document.

---

## File Structure

- **00-intro.md** (this file) — Updated learnings in inverted pyramid format
- **01-emergence.md** — The Brief, How It Started, Building the Roster, The Names
- **02-design.md** — Key Design Decisions, Most Important Feature, Brand Pivot
- **03-compass-brief.md** — Editorial angles for strategy
- **04-turing-brief.md** — Research directions
- **05-caret-brief.md** — Tone notes for drafting
- **06-session-2.md** — Logic Review
- **07-session-3.md** — Pre-Build Audit
- **... through ...**
- **26-session-21.md** — The Full Circle: Specs, Agents, Docs
- **INDEX.md** — Full index and navigation

---

## The Progression Narrative

Read the sessions in order to understand how the system evolved:

**Emergence Phase** (Sessions 1-2): Naming, roster building, logic audit  
**Design Phase** (Sessions 3-8): Specification, external audit, collaborative refinement  
**Build Phase** (Sessions 9-12): Pre-build hardening, agent design, migration  
**Optimization Phase** (Sessions 13-18): Token budgeting, hybrid models, context management, reversion  
**Evolution Phase** (Sessions 19-21): Great simplification, return to agents, direct invocation, documentation

Each session builds on the previous one. The story is about iteration through constraints, not about a perfect design revealed upfront.
