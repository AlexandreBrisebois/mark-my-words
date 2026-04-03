# System Spec: Mark My Words Agent Operation

## One-line purpose
Defines the folder-level operating model for the Mark My Words agent system: how agents discover work, persist state, share context, and move a piece from brief to packaged output.

## System identity
The orchestrator is called Mark My Words, or `mmw` for short.

This spec is the workflow contract for the multi-agent system. Individual agent specs define domain behavior, voice, and review standards. This document defines how those agents operate together inside a single working folder.

---

## Scope model

The system operates inside exactly one folder at a time.

- That folder is the complete runtime scope for the piece
- Agents read inputs from that folder
- Agents write outputs and state files to that folder
- Agents do not depend on files outside that folder to continue work on the piece

The folder may begin in either of these states:

- Empty
- Seeded with `brief.md`, which `compass` reads as the initial input

If the folder is empty, `mmw` may accept a user prompt and generate `brief.md` for `compass` to use as the initial strategic input.

---

## File contract

### Draft file

Each piece is represented by a single draft file:

- `{slug}.draft.md`

The slug is the canonical identifier for the piece inside the folder.

### State files

Each agent persists its working memory in a same-folder state file:

- `compass.state.md`
- `turing.state.md`
- `caret.state.md`
- `mark.state.md`
- `echo.state.md`
- `devil.state.md`
- `prism.state.md`
- `press.state.md`
- `mmw.state.md`

The state file is the durable handoff surface for that agent. It is not temporary scratch space.

---

## Persistence rules

Each time an agent runs, it appends to its existing state file.

- If the state file does not exist, the agent creates it
- If the state file already exists, the agent adds a new run entry to the end
- Agents do not replace prior run history as their default behavior
- State files should preserve earlier reasoning, decisions, and results so later runs can recover context

Each appended run should capture the minimum durable context needed for future work:

- What the agent received as input
- What it decided or produced
- What constraints, open questions, or risks remain
- What downstream agent or user action is now unblocked

When useful, agents should include a clearly labeled `Results` section so the user can review saved output quickly without reading the entire run log.

---

## Cross-context-window behavior

Agents cross context windows by reading one another's state files.

This is the core continuity mechanism for the system:

- Agents do not assume prior chat context is available
- Agents recover prior decisions by reading the relevant `.state.md` files in the folder
- Agents use saved state as the authoritative record of previous work on the piece
- Agents may read multiple peer state files when needed to reconstruct the current status of the piece

In practice, the state files act as the shared memory layer for the system.

---

## Orchestrator contract

`mmw` is the workflow orchestrator.

Its responsibilities are:

- Determine the current stage of the piece from the folder contents and state files
- If the folder is empty, convert the user's prompt into `brief.md` before routing to `compass`
- Route work to the next appropriate specialist without requiring human approval between steps
- Report the recommended next action and the current piece status concisely
- Preserve orchestration decisions in `mmw.state.md`
- Avoid asking downstream agents to guess missing upstream context that should already exist in state

`mmw.state.md` is the orchestrator's durable record of:

- Current piece status
- The source prompt used to bootstrap `brief.md`, when applicable
- Completed stages
- Pending stages
- Recommended next action
- Any workflow blockers or deviations

---

## Canonical workflow

The default sequence is:

1. `mmw` bootstraps `brief.md` from a user prompt when the folder is empty
2. `compass` — editorial strategy
3. `turing` — research
4. `caret` — first draft
5. `mark`, `echo`, and `devil` — review passes (any order, repeatable)
6. `prism` — visual direction
7. `press` — publication packaging

When `brief.md` already exists, the bootstrap step is skipped.

### Direct invocability

All agents are directly callable by the user in any order at any time.

`mmw` does not gate access to individual agents. When the user calls a specialist directly, that agent reads its own state file and any upstream state files it depends on to recover context. Specialists do not require `mmw` to run first.

`mmw` is useful when the user wants workflow coordination — determining the current stage, routing the next step, or recovering the overall status of the piece. It is not a required wrapper for specialist access.

### 1. MMW Bootstrap

When the folder is empty, `mmw` is responsible for creating the initial `brief.md` from the user's prompt.

`mmw` should:

- Read the user's prompt
- Convert that prompt into a usable editorial brief
- Write `brief.md` in the working folder
- Record the bootstrap action in `mmw.state.md`
- Route the piece to `compass`

If `brief.md` already exists, `mmw` should not overwrite it by default.

### 2. Compass

`compass` is the entry point.

Its role is to set the strategic direction for the piece.

`compass` should:

- Read `brief.md` when it exists
- Establish the audience, angle, stakes, and scope
- Save that strategic direction to `compass.state.md`
- Give downstream agents enough context to continue without re-deriving the editorial brief

### 3. Turing

`turing` runs after `compass`.

Its role is to use the context saved by `compass` and perform research.

`turing` should:

- Read `compass.state.md`
- Perform the required research, validation, and evidence gathering
- Save findings, references, and unresolved questions to `turing.state.md`

### 4. Caret

`caret` creates the first draft.

It should:

- Read `compass.state.md`
- Read `turing.state.md`
- Produce the initial `{slug}.draft.md`
- Save drafting decisions, open revisions, and output notes to `caret.state.md`

### 5. Mark, Echo, Devil

After the first draft exists, `mark`, `echo`, and `devil` are review agents used by the user.

Their role is not to advance the core sequence automatically, but to evaluate the draft from different perspectives:

- `mark` reviews voice, editorial quality, and brand fit
- `echo` reviews reader experience, friction, and likely bounce points
- `devil` reviews argument risk, credibility gaps, and unintended messages

These review passes may happen in any order and may be repeated.

Each review agent should:

- Read `{slug}.draft.md`
- Read any relevant prior state files when helpful
- Append its findings to its own `.state.md` file

The user can read the saved `Results` from these state files at any time and make manual edits to `{slug}.draft.md`.

### 6. Prism

Once the draft direction is stable, `prism` generates the image prompt.

`prism` should:

- Read the current draft and any relevant review state
- Produce the visual prompt or visual direction for the piece
- Persist that output in `prism.state.md`

### 7. Press

`press` prepares and packages the final draft and image prompt.

`press` should:

- Read the latest `{slug}.draft.md`
- Read `prism.state.md`
- Read other state files when packaging context matters
- Prepare the final publication package
- Persist packaging decisions and output details in `press.state.md`

---

## User interaction model

The user remains in control of the draft throughout the workflow.

- The user may inspect any `.state.md` file at any time
- The user may use saved agent `Results` to review recommendations without rerunning the agent
- The user may edit `{slug}.draft.md` manually between agent runs
- Review agents do not lock the draft or prevent user edits
- The system should treat the current folder contents plus all state files as the source of truth for the latest piece status

---

## Required invariants

- One active piece per folder
- One canonical `{slug}.draft.md` per piece
- One append-only `.state.md` file per agent
- Shared continuity happens through state-file reads, not hidden session memory
- If the folder is empty, `mmw` may create `brief.md` from the user's prompt before `compass` runs
- `compass` is the strategic entry point for a new piece
- `turing` follows `compass`
- `caret` follows `compass` and `turing`
- `prism` follows drafting and review
- `press` is the final packaging stage
- `mmw` maintains orchestration state in `mmw.state.md`

---

## Non-goals

This spec does not define:

- The internal writing style of each agent
- The evaluation rubric inside each review agent
- The exact markdown schema of each run entry
- Multi-folder or multi-piece coordination

Those concerns belong in the individual agent specs or future implementation specs.