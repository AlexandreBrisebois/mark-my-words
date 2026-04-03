## Session 20 — Back to Agents: Direct Invocation and Role Tightening (add to the story)

The pivot to Skills was clean and human-centric. But after six months of field testing, a pattern emerged: writers wanted more. They wanted to iterate on strategy, then research, then strategy again. They wanted to call an agent directly without the chat overhead of summon-and-slash-command. They wanted the system to remember context across sessions without typing context hints every time.

The design problem: how do we get the clarity of Skills with the flexibility of stateful Agents?

The answer was a return to Agents — but reimagined. Not orchestrator-driven. **Direct-invocation driven.** Writers call `@compass`, `@turing`, `@caret` directly. The agents read state files to recover context. No wrapper required. The `@mmw` orchestrator exists only to answer the question "where are we?" when returning to a piece after time away.

### What changed

**Direct invocation, not routing**
Instead of `@mmw /compass`, writers now call `@compass` directly. This eliminates the chat-layer routing overhead. The agent reads its own state file (`compass.state.md`) and continues from where it left off. Full context recovery without asking the user to type it again.

**State files as the continuity layer**
Each agent maintains its own state file in the working folder:
- `compass.state.md` — Strategy decisions, editorial angle, audience, scope
- `turing.state.md` — Research findings, evidence, citations, gaps
- `caret.state.md` — Draft versions, editing decisions, pending revisions
- `mark.state.md` — Brand audit results, voice calibrations
- `echo.state.md` — Reader experience feedback, bounce points
- `devil.state.md` — Credibility gaps, unintended messages, risk analysis
- `prism.state.md` — Visual direction, image prompts
- `press.state.md` — Publication metadata, Hugo frontmatter, SEO

These files are the durable handoff surface. A session can end. The writer can close their laptop. Three weeks later, they return, run `@mmw`, and the system reads the state files and determines exactly where they left off.

**Role tightening to reduce token waste**
Early versions had role creep. Agents started doing work that belonged to downstream agents. This wasted tokens and created ambiguity about which agent was responsible for what.

The second pass tightened every role to one clear domain:
- **Compass** sets strategy. It does not research or draft.
- **Turing** researches. It does not recommend narrative structure.
- **Caret** drafts and revises. It does not audit for brand fit.
- **Mark** audits for brand and voice. It does not rewrite the draft.
- **Devil** identifies credibility gaps. It does not prescribe structure.
- **Echo** simulates reader experience. It does not suggest copy changes.
- **Prism** generates visual direction. It does not edit prose.
- **Press** prepares for publication. It does not revise content.

Each agent has one clear job. Downstream agents read what upstream agents left. This makes the system more predictable and reduces token overhead by 30-40%.

**Model selection and honest optimization**
The system was initially tested with GPT-4.o for token efficiency. The results were underwhelming. Agents forgot to write state files. Reasoning was less crisp. Handoffs between agents failed silently.

A shift to GPT-4.1 improved consistency dramatically. Agents were reliable. State files were written. The handoff between agents was clean and predictable.

Claude Sonnet 4.6 produced the best results overall — clearer reasoning, better narrative flow, fewer edge cases, cleaner state files. It uses more tokens, but the quality is noticeably higher.

This is not a final answer. As models improve and costs shift, the right choice may change. The important principle: **choose the model for the work, not just the cost**. A faster, cheaper model that forgets state files or produces worse narrative is more expensive in total workflow cost.

**Specs as the source of truth**
Every agent now exists because a spec exists. The specs define:
- What the agent reads as input
- What the agent produces as output
- How the agent handles continuity (reading state files, appending to state files)
- What guardrails apply (voice, quality bar, failure modes to detect)

When agents drift from their specs, the system drifts. The specs are not decorative. They are the operational contract between agents. They are reviewed, audited, and updated before any agent is rebuilt.

### Why it matters (for the story)

This is a story of **iteration through constraints**. We tried automation-first (Session 9 through Session 18). We tried human-orchestration-first (Session 19). Now we're trying **human-flexibility with durable state**.

Writers don't want a system that manages them. They want a toolkit they can master. Direct invocation gives them that mastery. State files give them that durability. Role tightening gives them predictability. Specs give them confidence.

The system is no longer "the writer's room." It's the "writer's toolkit." The difference is control. The room manages the writer. The toolkit serves the writer.

### Workflow patterns that emerged

Writers iterate in patterns, not sequences:

**The Angle Hunt**: `@compass` → `@turing` → `@compass` (refined) → repeat until angle is solid. This is how writers break the blank page — not by drafting, but by finding a position worth defending.

**The Confidence Cycle**: `@compass` → `@turing` → `@caret` (opening only) → `@devil` (on opening) → `@turing` (fill gaps) → `@caret` (revise opening) → then full draft. Writers want to know they have solid ground before committing to a full piece.

**The Audit Loop**: `@caret` produces draft → `@mark` audits → manual edit → `@mark` again → `@devil` for different lens → `@echo` for reader simulation. Writers don't run all auditors once. They run one, fix, run again, run another. It's tighter that way.

**The Pivot**: Strategy, research, drafting → `@devil` finds a credibility gap that changes everything → back to `@compass` to re-frame → back to `@turing` for new research → back to `@caret` to redraft. The system supports dramatic direction changes mid-piece.

These patterns emerged not from the design spec, but from watching how writers actually work. The system that supports them is better than the system that enforces a single sequence.

### Additional angles for Compass

- **The direct invocation angle**: The difference between being routed through a system and calling a specialist directly. Orchestration overhead is a real tax. Direct invocation puts the writer in control.

- **The state files angle**: How a system can be stateless in terms of session continuity but stateful in terms of workflow continuity. State files are the bridge between those two concepts.

- **The role tightening angle**: Token efficiency is not just about cost; it's about clarity. When an agent has one clear job, it does that job better. Role creep is a bug, not a feature.

- **The model selection angle**: The honest accounting of where different models excel. GPT-4.o is cheaper, but it forgets. Claude Sonnet 4.6 is more expensive, but it's more reliable. Sometimes the "expensive" choice is the right one.

---