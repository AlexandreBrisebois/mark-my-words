# MMW Input Primer
# How Mark My Words Came to Be

**Trigger**: `MMW write a post about building Mark My Words`
**Suggested codename**: `writers-room-build`
**Piece type**: Builder-in-public retrospective + technical design post
**Audience**: CTOs, engineers, AI enthusiasts — people who build things
and think in systems

---

## The Brief

This post documents the real-time design process behind Mark My Words
— a multi-agent writing system built to help me produce better, more
intentional blog content. The system was not designed in advance. It
emerged through a conversation, decision by decision, until it had a
name, a roster, a workflow, and a philosophy.

The post should capture that emergence. Not the final architecture.
The thinking behind it.

---

## How It Started

It started with a simple problem: I needed a name for an editor agent.
Something short, memorable, and different from "Editor."

From that small constraint, ten names became twenty. From twenty,
one landed: **Caret** — the typographic editing symbol `^`. It felt
right because it was niche, editorial, and had a double meaning.
That instinct — find the name with the most layers — became the
design principle for everything that followed.

---

## Building the Roster

Once Caret existed, the question became: what else does a writer need?

The first answer was a writing room. Not one agent doing everything,
but a room of specialists — each covering a distinct discipline that
would otherwise live only in the writer's head or get skipped under
time pressure.

The roster built itself through a series of honest questions:

**What roles am I missing?** The first pass had a writer, an editor,
a brand agent, a critique agent, and a researcher. The gaps that
emerged: a publisher, a headline agent, an audience proxy, an archivist,
a scheduler. Each gap revealed something the writer unconsciously
depends on but rarely makes explicit.

**Should I merge or keep separate?** Echo (Audience) and Devil
(Critique) looked like the same role. They weren't. Devil challenges
the writer — adversarial, inward-facing. Echo challenges the
connection to the reader — empathetic, outward-facing. One asks
"is this good writing?" The other asks "will this land?" Merging
them would have lost that distinction.

**What did I already have?** Seven GitHub Copilot prompts from a
prior implementation — an accusation audit, a brand voice guide,
a content writer, a brand strategist, an SEO auditor, a blog
portfolio auditor, and a visual brand validator. These weren't
starting from scratch. They were proven logic that needed a new home.

---

## The Names

Every agent got a name through the same filter: short, memorable,
layered. The naming process itself became part of the design.

| Agent | Name | Why It Works |
|---|---|---|
| Writer + Orchestrator | Caret | Typographic editing symbol `^` |
| Brand + Voice | Mark | Hallmark, benchmark, the brand agent marks the work |
| Strategist | Compass | Sets direction before anyone moves |
| Critique | Devil | Devil's advocate — adversarial by design |
| Researcher | Turing | Decodes hidden structure, finds signal in noise |
| Audience | Echo | Reflects the reader's voice back |
| Publisher | Press | The printing press, the act of committing |
| Archivist | Index | The index at the back of every serious book |
| Scheduler | Cadence | The rhythm of consistent publishing |
| Visual Brand | Prism | Splits the brand into its component parts |

The system name came last. Playing with the agent names as raw
material — Caret, Mark, Press, Index — led to typographic heritage,
then to the idiom "Mark My Words." It was already there, hiding in
the roster. Three letters became the shorthand: **MMW**.

---

## Key Design Decisions

### File-based shared memory
Agents don't pass state through conversation. They read files and
write files. Each piece gets a folder. Each agent writes to that
folder. The next agent reads what the last one left.

This was a deliberate choice: stateless, inspectable, recoverable.
If anything breaks mid-workflow, the files tell you exactly where
things stopped. No black box.

### The codename
Every piece gets a codename derived from the brief — descriptive,
lowercase, hyphenated, 2-3 words. Not random or evocative. The
codename should tell you what the piece is about without opening
any files. `writers-room-build`. `brand-pivot-retro`. The archivist
can scan them without context.

### Compass before Turing
The strategist runs before the researcher. Research without strategic
direction is unfocused. Compass sets the frame — piece type, editorial
angle, research priorities — then Turing works within it. Getting
this order wrong wastes Turing's most valuable output.

### Index as the first gate
Before any agent does creative work, the archivist checks whether
this piece overlaps with something already published. Three outcomes:
abandon, differentiate the angle, or proceed knowingly. Duplicate
content is a problem that's much easier to catch at the brief stage
than after a draft exists.

### The Caret/Mark feedback loop
Mark doesn't just flag problems. It informs the next draft directly.
The loop: Caret drafts, Mark reviews, Caret reads the review and
revises, Mark re-checks. Maximum two iterations before the circuit
breaker fires and surfaces the outstanding issues to the user.

### The research gate
Caret will not start a draft without explicitly confirming that
research.md exists and is non-empty. This is not a soft suggestion.
If the research isn't there, nothing runs. The other agents are only
as good as the ground they stand on.

### Prism owns the image prompt
The GitHub Actions automation previously had Gemini generate its own
image prompt. Prism replaces that. Prism reads the finished piece and
brand guidelines, then produces a single plain-paragraph prompt for
Gemini Image Pro — grounded in the content, consistent with the
"Calm Signal" aesthetic. The automation just reads the file.
No parsing required.

---

## The Most Important Feature

Co-edit mode was identified as the most human part of the system —
the moment the writer's voice actually enters the draft.

The design is intentional: when co-edit is triggered, Caret surfaces
the exact lines that need attention, with the current text and the
specific issue. Then it steps back. The user edits the draft file
directly. Caret waits. No suggestions, no rewrites, no hovering.

When the user signals completion, Caret reads the edited file,
integrates any remaining issues it can handle autonomously, produces
the next versioned draft, and then reports exactly what it changed
beyond the user's edits. If the user's edit contains a banned word,
Caret flags it — but does not delete it. The user's voice overrides
the brand rules when there is a conflict.

The principle that guided this: the system serves the writer's voice.
Everything else is infrastructure.

---

## The Brand Pivot

The system was designed alongside a brand pivot. The prior identity
was a multi-cloud engineering brand — srvrlss.dev, Technical Outcome
Leader, GCP/AWS/Azure. That identity is not wrong. It's just not
current.

The new identity: AI Enthusiast, builder-in-public, honest learner.
The audience stays the same — CTOs, engineers, technical leaders.
The content shifts: AI agents, building in public, retrospectives,
failure and recovery.

Microsoft is origin story, not current identity. The old blog is
archive, not content to migrate. srvrlss.dev is a prior chapter.
This blog is a fresh start.

Every agent in Mark My Words had its brand references updated
before the system was finalized.

---

## What This Post Should Be

This is not a tutorial. It is not a "here are the five steps to
build an agent system" post.

It is a honest account of a design process — the questions asked,
the decisions made, the things that emerged that weren't planned.
The fact that the system name was hiding in the roster all along.
The fact that Echo and Devil looked like the same agent until they
weren't. The fact that co-edit mode became the most important feature
not because of technical complexity but because of what it represents:
the writer's voice is the point.

The reader should finish this post with two things: a clear
understanding of what Mark My Words is, and a felt sense of how
it came to exist. Not the architecture. The thinking.

---

## Suggested Angles for Compass

- **The emergence angle**: Systems designed through conversation
  rather than specification. What that reveals about how good tools
  are actually built.
- **The naming angle**: Why naming matters in system design. The names
  encode the philosophy. Caret is not "Writer." Turing is not
  "Researcher." The difference matters.
- **The voice angle**: Why co-edit mode is the most important feature
  in a writing system. What it says about the relationship between
  automation and authorship.
- **The builder-in-public angle**: The system itself is the first
  post it will help write. That recursion is worth examining.

---

## Suggested Research Directions for Turing

- Prior art on multi-agent writing systems and editorial workflows
- The history of the writer's room as a creative structure
  (TV writers' rooms, editorial boards, newsrooms)
- Research on AI-assisted writing and where human voice gets lost
- The accusation audit methodology (borrowed from negotiation practice
  — Chris Voss, Never Split the Difference)
- Type 1 / Type 2 decision framework (Amazon / Jeff Bezos)
- The "Empty Chair" as a design principle in product and content
- llms.txt as an emerging standard for AI-readable content

---

## Tone Notes for Caret

- First person throughout — this is a personal account, not a
  technical specification
- Reflective-vulnerable blended with urgently excited
- The system is not finished. It is version one. Say that.
- The design decisions are not perfect. Surface the tradeoffs.
- Do not write this as a success story. Write it as a process story.
- A single-sentence paragraph is a signature move. Use it.
- Close with a question that invites the reader into the conversation —
  not a summary of what was covered.

---

## Session 2 — Logic Review (add to the story)

Before the architecture refactoring began, the monolithic build prompt
(`mmw-claude-code-prompt.md`) went through a deliberate logic review.
Not a polish pass. A surgical audit: find what would break when Claude
Code actually builds this out.

Five issues were found and fixed. Two were critical.

### What was found

**Version ambiguity on critique and audience files.** The workflow
diagram used `critique-vN.md` and `audience-vN.md`, implying versioning.
The prose hardcoded `critique-v1.md` and `audience-v1.md`. On a re-run
after revisions, the file would be silently overwritten — no history,
no trace. The fix: the version number is now explicitly derived from
the draft reviewed. If Devil audits `draft-v2.md`, it writes
`critique-v2.md`. The convention was already implied in one place.
It just needed to be consistent everywhere.

**Press was missing the Edit tool.** Press is responsible for writing
the slug into `status.md` after producing `seo.md`. The instructions
said to use the Edit tool. The tool scoping table didn't grant it.
Without Edit, Press would have to read the entire `status.md`,
reconstruct it, and overwrite it with Write — a fragile operation
that could corrupt the file. One word added to the frontmatter table
fixed it. The kind of bug that only surfaces when you read the spec
and the tool list side by side.

**Index and Cadence weren't receiving the codename at Phase 11.**
Every other parallel spawn in the workflow had an explicit instruction
to pass the active codename to the subagent. The Phase 11 spawn of
Index and Cadence didn't. Without it, Index would have to scan all
piece folders to find the right one — and could update the wrong entry.
The fix was one sentence, matching the pattern already established
for Devil/Echo and Press/Prism.

**Co-edit had no session recovery path.** Co-edit completion is
signaled by `MMW:done` in chat. If the session ended before the user
typed it, `status.md` had no record that a co-edit was in progress.
On resume, Caret would read `status.md`, see the last completed
action, and advance — skipping the co-edit entirely. The fix: before
waiting for `MMW:done`, Caret now writes a state marker to `status.md`.
On resume, if that marker is present, Caret re-surfaces the co-edit
prompt rather than moving forward.

### Why it matters (for the story)

None of these issues were visible from a high-level read of the prompt.
They only surfaced when the spec and the tool list were read in parallel
— the way a compiler reads source and type signatures at the same time.

The review happened before the architecture split. That sequence
matters: first verify the logic is sound, then restructure for
maintainability. Refactoring a broken system just makes the bugs
harder to find.

The same discipline that caught these issues — reading the system as
a system, not as prose — is what the architecture refactoring was
designed to make permanent.

### Additional angle for Compass

- **The review angle**: Why you audit a system before you refactor it.
  The logic errors in the monolith were small. After the split, they
  would have been distributed across ten files. Finding them first
  was the right order of operations.

---

## Session 3 — Pre-Build Audit (add to the story)

The monolith had been reviewed once. Then, before handing it to Claude
Code to build, it was reviewed again. Same file. Different question.

The first review asked: *does the logic hold?* The second asked:
*what will break when an agent actually tries to execute this?*

Eight issues. None catastrophic. All invisible until you read the spec
the way an agent would — linearly, literally, without assumed context.

### What was found and fixed

**The status.md log was out of order.** The example schema showed
`Mark → headlines.md` before `Caret → draft-v1.md`. The workflow is
the opposite: Caret drafts first, Mark generates headlines from the
draft. An agent resuming mid-workflow from `status.md` would have
misread its own position. One line swap.

**Press had no instruction on how to write the slug.** The spec said
Press writes the slug to `status.md`. It didn't say *how*. On a rerun
after a title change, a naive agent would append a second `Slug:` line
rather than replace the existing one — corrupting the field that Caret
reads in Phase 11. The fix added three words: *using the Edit tool,
in place.*

**`research/notes.md` was missing from the scaffold.** Turing reads
this file at the start of every research pass. The directory tree in
Step A listed `research/` with no file inside it. Step F, several
sections later, described creating the file. An agent building from
Step A alone would produce an incomplete scaffold and Turing would
fail on first run.

**Caret was missing `Grep` from its tool list.** Caret's Phase 11
pre-flight verifies field values inside files — confirming `Slug:`
exists in `status.md`, checking it matches the value in `seo.md`.
`Glob` finds files. `Grep` finds content. Without it, Caret would have
to read entire files and parse them manually — fragile, slow, and
unnecessary.

**`MMW:done` needed a clarification.** The co-edit completion signal
is a chat message. The first piece MMW writes is about MMW itself —
and the draft would reference `MMW:done` as an example. The original
note said the signal "cannot appear in prose being edited." That's
wrong for a meta-post. The fix was precise: Caret listens for the
signal in the conversation only, never in file content.

**Phase 0 was missing a conditional.** The Overlap Check section
instructed Index to read `brief.md` — with no condition. The agent
roster said don't read `brief.md` if no codename was passed. An agent
invoked directly via `MMW:index` would try to read a file that didn't
exist in context and fail. The conditional now lives in Phase 0, not
just in the roster.

**Turing's handoff targets were wrong.** The roster listed Mark as a
handoff target alongside Caret. Turing does not invoke Mark. Turing
returns to Caret. Caret then spawns Mark for Phase 4. One misread of
this line and an agent implementation would route directly from Turing
to Mark — bypassing Caret, breaking the orchestration model entirely.

**Phase 11 had no directory existence check.** The handoff writes to
`posts/drafts/[slug].md` using the Write tool. If the scaffold was
partially built and the directory was missing, the Write tool would
error with no guidance. A pre-flight row was added alongside the
existing checks for `seo.md`, `image-prompt.txt`, and the draft.

### Why it matters (for the story)

The second review found things the first missed. Not because the first
was careless — because the two reviews asked different questions.

The first review was a logic audit: does the workflow make sense?
The second was an execution audit: will an agent, reading this linearly,
do the right thing?

The gap between those two questions is where prompt bugs live. A system
can be logically correct and still fail because the agent reads section
A without the context from section F. Because the tool list and the
prose instructions are two separate documents that have to agree.
Because "in place" is a meaningful constraint that prose alone won't
enforce.

The system was reviewed twice before a single file was built. That
sequence — design, audit, audit again, then build — is itself a design
decision worth naming.

### Additional angle for Compass

- **The two audits angle**: The difference between a logic review and
  an execution review. One asks if the system makes sense. The other
  asks if an agent can follow it. Both are necessary. Neither replaces
  the other.

---

## Session 4 — External Audit (add to the story)

The monolith had been reviewed twice by its author. Then it was handed
to a fresh reviewer — no prior context, no memory of the design
decisions, reading the spec the way Claude Code would read it on first
invocation.

Eleven issues surfaced. One was dismissed immediately. The other ten
were real.

### What was different about this pass

The previous audits asked whether the logic was correct. This one asked
a harder question: *what does an agent need that the spec assumes it
already has?*

That framing found things the prior passes missed — not because the
logic was wrong, but because the spec had invisible dependencies.
Capabilities assumed but never granted. Paths described but never
qualified. Failure modes defined for the happy path but not for the
partial failure.

### What was found and fixed

**Caret was missing the `Agent` tool.** Caret is the orchestrator. It
spawns every subagent in the system. The tool scoping table granted it
`Read, Write, Edit`. Without `Agent`, it cannot spawn anything. The
entire orchestration model was broken before the first subagent was
called. One word in the tools table.

**Caret and Index were missing `Glob`.** Caret needs to find the
highest-numbered `draft-vN.md` in a piece folder. Index needs to
enumerate all piece folders. `Read` can open a file. It cannot list a
directory. `Glob` was added to both — and to Press and Prism, which
have the same requirement when locating the latest draft.

**No rule for resuming an existing piece.** `MMW writers-room-build`
and `MMW write a post about the writer's room` look identical to an
agent with no disambiguation rule. The first is a resume. The second is
a new piece that might generate the same codename and overwrite existing
work. A codename disambiguation rule was added: check the pieces folder
first, match before generating, never overwrite without confirmation.

**The loop iteration count could be lost across sessions.** The
circuit breaker fires after two iterations. The count lives in
`status.md`. The spec told Caret to update `status.md` after every
action — but never explicitly said to write the loop counter before
pausing for user input. On session resume, the count would default to
zero. The instruction was made explicit: write the counter to
`status.md` before every loop pause.

**Parallel subagent partial failure had no recovery path.** The spec
said verify both output files after a parallel spawn. It didn't say
what to do if one succeeded and one failed. An agent with no
instruction would either proceed with incomplete data or halt silently.
An explicit failure rule was added: report which agent failed, surface
the re-run command, never proceed with a partial parallel result.

**`MMW:proof` with no matching pieces had no defined response.** The
zero-match case — user omits the codename, scan finds nothing awaiting
proof — was simply absent. The agent would return nothing or behave
unpredictably. An explicit message was added.

**The slug pre-flight check was incomplete.** The handoff reads the
slug from `status.md`. The pre-flight verified the slug was present.
It didn't verify it matched the slug in `seo.md`. A mismatch — from a
Press re-run that updated one file but not the other — would pass the
check and produce a post at the wrong path. A consistency comparison
was added to the pre-flight table.

**`brand/guidelines.md` was an ambiguous path.** Prism's inputs listed
`brand/guidelines.md`. The actual file lives at
`writers-room/brand/guidelines.md`. A subagent doesn't inherit a
working directory assumption. Every occurrence was replaced with the
fully qualified project-relative path.

**`visual/audit-log.md` was orphaned infrastructure.** The scaffold
created the file. No agent was assigned to write to it. It would be
created empty and stay empty. Removed from the scaffold rather than
assigned a purpose it wasn't designed for.

**`research/` global folder had no defined behavior.** Turing's
responsibilities only covered piece-specific `research.md`. The global
`research/` directory in the scaffold had no writing agent and no seed
file. Instead of removing it, the gap became a feature: Turing now
appends reusable cross-piece findings to `writers-room/research/notes.md`
after every research pass, reads it at the start of the next to avoid
duplicating prior work, and prunes entries older than 90 days before
appending. The directory went from dead infrastructure to persistent
institutional memory.

### Why it matters (for the story)

Three audits. Each one asked a different question.

The first audit asked: does the logic hold?
The second asked: will an agent follow this correctly, step by step?
The third asked: does the agent have what it needs to do what the spec requires?

The third question is the one most prompt engineers skip. It's easy to
write a spec that is logically correct, procedurally clear, and
completely unbuildable — because the agent was never given the tools,
the paths were never fully qualified, or the failure modes were only
defined for the cases you expected.

The gap between "the spec makes sense" and "an agent can execute this"
is where most prompt systems quietly fail.

### Additional angle for Compass

- **The capability gap angle**: The difference between specifying
  behavior and specifying capability. A spec can describe exactly what
  an agent should do and still fail — because it never granted the tool
  that makes the action possible. Behavior and capability are two
  separate documents that have to agree.

## Session 5 — Collaborative Audit (add to the story)

The system had been reviewed three times. Then it was reviewed a fourth
time — differently.

Not a batch read followed by a report. A conversation. Each issue surfaced
one at a time. Each fix proposed, discussed, and either accepted, rejected,
or redirected before moving to the next. The author in the loop for every
decision.

Nine issues were found. One was dismissed on closer inspection. One was
overridden by the author with a better answer. One surfaced a design
correction that had been wrong from the beginning.

### What was different about this pass

The previous audits surfaced issues in lists. This one surfaced them in
sequence — which meant each fix was ratified before the next issue was
raised. No batch of changes applied without review. No assumptions made
about what the author wanted.

That difference matters for the story. The prior sessions were solo
analysis. This one was collaborative design. The same discipline, applied
in a different mode.

### What was found and fixed

**Phase 11 had no mechanism for the file copy.** Caret's tool list was
`Read, Write, Edit, Agent, Glob`. The spec said to copy `final.md` to
`posts/drafts/[slug].md`. There is no copy tool. The fix was a design
decision: replace "copy" with an explicit read-then-write instruction.
Caret reads `final.md` and writes its full content to the destination
path using the Write tool. No Bash access required. The tool list didn't
need to change — just the language describing what to do with the tools
it already had.

**Mark's workflow position was wrong.** The original order placed Mark
after Turing and before the first draft — generating headlines from
`brief.md` and `research.md`. The author corrected this: headlines must
be grounded in the actual draft. A headline generated before the draft
exists may have nothing to do with what the piece becomes. Mark moved to
Phase 4, after Caret's first draft. Mark now reads `draft-vN.md` only.
Brief removed from its inputs entirely.

The two modes Mark operates in were also clarified and separated:
- **Headline generation**: reads `draft-vN.md`, produces `headlines.md`
- **Brand review**: reads `draft-vN.md`, produces `brand-notes-vN.md`

Neither mode reads `brief.md`. Neither reads `research.md`. The draft
is the ground truth. Everything else is noise.

**Press's slug instruction was implicit.** The Outputs section said Press
writes the slug to `status.md`. The Responsibilities section never said
it. An agent building the Press prompt from the roster would produce an
agent that only writes `seo.md`. The slug write would be silently skipped.
One explicit bullet added to Responsibilities. The Outputs line trimmed
to avoid duplication.

**`research/notes.md` was missing from Step F.** The seed file was
described — header row, table format — but not explicitly called out as
a file to create during scaffold. The directory would be created. The file
wouldn't. Turing's first research pass reads this file before doing
anything. A missing file is a failed first run. Step F now names all
three seed files explicitly, with a clear instruction that all three must
exist before any agent runs.

**`visual/` was orphaned.** The scaffold included the directory. No agent
wrote to it. No agent read from it. The author's call: remove it. No
purpose assigned, no directory created.

**Turing gained the ability to go deeper.** This was the one addition
that wasn't a bug fix. After completing `research.md`, Turing now
evaluates whether any topics warrant a second, focused pass. If so — or
if the user requests it — Turing surfaces three candidates, pauses, and
waits for the user to pick one, steer with a prompt, or skip. The deeper
pass appends to `research.md` under a clearly marked section. One deep
dive per piece. If skipped, the candidates are recorded so the information
isn't lost.

The design principle behind this: research is not a single-pass operation.
The first pass establishes the ground. The second pass goes where the
first pass revealed something worth pursuing. Turing should know the
difference and say so.

### Why it matters (for the story)

Four audits. Each one found something the previous missed.

Not because the previous passes were careless. Because each pass asked
a different question, from a different position:

- *Does the logic hold?*
- *Will an agent follow this correctly?*
- *Does the agent have what it needs?*
- *Is every decision the right one — and does the author agree?*

The fourth question is the one you can only answer in conversation. The
prior audits produced corrections. This one produced decisions. The
distinction matters because a correction can be applied without the
author. A decision cannot.

The system that went into the build was not the system that came out of
the first design session. It was the system that survived four rounds of
questioning — each from a different angle, each by someone reading it
as if they were about to execute it.

### Additional angle for Compass

- **The decision audit angle**: The difference between a corrections pass
  and a decisions pass. Corrections fix what is wrong. Decisions ratify
  what is right — and sometimes discover that what looked right was wrong
  for a reason that only surfaces when the author is present to say so.

---

## Session 6 — Where Does the Prompt Live? (add to the story)

After four audits and a collaborative pass, the system was ready to build.
Which raised a question that hadn't been asked yet: where does the build
prompt actually live in the repo?

The file was sitting at the root of `mark-my-words/`. That works for a
session. It doesn't work for a year.

The question was framed as a long-lived repo problem: the prompt needs
to be findable, version-controlled, and distinct from the artifacts it
generates. The build prompt creates `CLAUDE.md`, `ARCHITECTURE.md`,
`.claude/agents/`, and `writers-room/`. If the prompt that generates
those things sits alongside them at root, the source is indistinguishable
from the output.

The answer: `prompts/mmw-claude-code-prompt.md`.

Not `docs/`. Not `specs/`. `prompts/` — because the file is an instruction
to an AI system, and that should be legible from the directory name alone.
The same way `.claude/agents/` signals agent configuration and
`writers-room/` signals content, `prompts/` signals intent: these files
tell the system what to build.

The root is reserved for what MMW produces. `prompts/` holds what makes
MMW reproducible.

### The principle behind it

A build artifact and its source should not share a namespace. The prompt
is source. `CLAUDE.md` is output. Putting them in the same directory is
the same mistake as checking generated code into the same folder as the
generator — it works until you need to rebuild from scratch and can't
tell which files are safe to delete.

The decision is also a commitment: this repo will outlast any single
build of MMW. The prompt stays. The agents can be regenerated. The
directory structure makes that clear by design.

### Additional angle for Compass

- **The source/output separation angle**: In software, you separate source
  from build artifacts. The same discipline applies to prompt systems.
  The file that generates the agents is not the same kind of thing as
  the agents it generates — and the directory structure should say so.

---

## Session 7 — Prompt Architecture (add to the story)

After the agents were designed, a new problem emerged: the build prompt
was getting long. ~1,400 lines. One file doing two different jobs —
build-time instructions and runtime behavior — with no separation
between them.

The question asked: *should it be broken down into specs and an
orchestrating prompt, like in software development?*

The answer was yes. But the more important insight was the follow-on:
not just splitting build from runtime, but giving **each agent its own
spec file**. The same way a software project has one file per service,
not one file for the whole system.

### What was built

```
prompts/
├── mmw-build-prompt.md         ← thin orchestrator: reads specs, builds artifacts
└── specs/
    ├── flow.md                 ← canonical workflow, phases, protocols, file schema
    ├── agent-caret.md
    ├── agent-mark.md
    ├── agent-compass.md
    ├── agent-devil.md
    ├── agent-turing.md
    ├── agent-echo.md
    ├── agent-press.md
    ├── agent-prism.md
    ├── agent-index.md
    └── agent-cadence.md
```

### Why it matters (for the story)

The split revealed a structural insight: the original monolith had two
sources of truth fighting each other. The phase specs lived in the build
prompt, but the same logic needed to live in the generated agent files.
No single file was authoritative.

The new structure has a clear contract:
- `flow.md` owns the workflow. Phases, gates, protocols. Change it once,
  rebuild what depends on it.
- Each `agent-X.md` owns only that agent's behavior. Personality,
  responsibilities, inputs, outputs, rules.
- The build prompt owns nothing except the order of operations.

The analogy that surfaced: this is the same reason software projects
have service specs, interface contracts, and a deployment script — not
one enormous README that is also the code.

### The recursion worth noting

The first thing MMW will write is a post about building MMW. The prompt
architecture is now part of that story — not just the agent roster and
naming, but the decision to treat a prompt system with the same
structural discipline as a software project.

That decision was made in a conversation, not in advance. Same as
everything else in this system.

### Additional angle for Compass

- **The architecture angle**: What prompt engineering and software
  architecture have in common. The moment you recognize that a prompt
  is not just instructions but a system with its own coupling,
  separation of concerns, and single-responsibility principle — that's
  the moment the discipline changes.

---

## Session 9 — Pre-Build Spec Hardening (add to the story)

The architecture was reviewed. The specs were clean. The build prompt
was approved.

Then it was handed to a dedicated reviewer — a Claude Agent Designer
with no prior context on this system — and asked one question: *what
can go wrong when an agent actually executes this?*

Not a logic audit. Not a capability check. A failure audit. The
reviewer read every spec with one lens: where will a real agent, in
a live session, produce an outcome the author didn't intend?

Twelve issues. Two were design decisions. The rest were fixes.

### What was different about this pass

The previous passes audited the system from the inside — someone who
understood the design intent reading the specs to find gaps. This pass
audited from the outside. The reviewer had no assumptions about what
the author meant. Every ambiguity was flagged. Every implicit contract
was surfaced.

That difference found a different class of issue: not missing
instructions, but missing guardrails. The specs told agents what to
do. They didn't always tell agents what to do when things went wrong.

### What was found and fixed

**Index had no signal to Caret on Abandon.** The spec said if the
user selected Abandon, Caret would delete the piece folder. Index
is the agent running at Phase 0. Caret spawned Index and waited.
Index had no mechanism to tell Caret what the user had decided. No
flag, no field, no convention. Caret would return from Index, read
status.md, and see no instruction to clean up. The folder would
persist. The fix: Index writes `Abandon: confirmed` to status.md.
Caret checks for this flag on return and deletes the folder.

**The Caret/Mark loop had no HOLD branch.** Mark issues three
verdicts: PASS, REVISE, HOLD. The loop defined exit conditions for
PASS and iteration count. HOLD — the verdict that means the issue is
structural, not a revision problem — was simply not handled. An agent
receiving HOLD after iteration one would have no instruction. The fix
adds an explicit HOLD branch: exit the loop immediately, surface the
structural issue to the user with three options.

**Press's slug sync would fail on first run.** Press uses the Edit
tool to write the slug into status.md. Edit requires an exact string
match. The spec never guaranteed that the string existed. On first
run, if the placeholder wasn't there, the Edit would fail silently.
The fix is in two parts: Caret's status.md template now includes
`- Slug: (written by Press)` as a guaranteed placeholder. If Press
fails anyway, it redoes both writes from scratch — seo.md first,
then the slug field — rather than managing stale state.

**Co-edit session resume read the wrong brand notes.** If a session
ended mid-co-edit, Caret would resume by re-surfacing the flagged
lines. To do that, it needs to read the most recent Mark review. The
spec didn't specify which file. On a piece with multiple loop
iterations, Caret might have reconstructed the flagged lines from an
older review. The fix is one sentence: on co-edit resume, read the
highest-numbered brand-notes-vN.md in the piece folder.

**Partial parallel results left status.md stale.** If Devil succeeded
and Echo failed, Caret would log Devil's completion before verifying
Echo. On resume, status.md would show Devil as done and no record of
Echo's failure. The agent would not know which agent to re-run. The
fix: before spawning any parallel pair, Caret writes a partial marker
to status.md. Each agent's entry is updated only after its output is
verified. If a session ends mid-parallel, the marker persists and
tells Caret exactly where to resume.

**Index re-ran the overlap gate at Phase 11.** The Phase 0 overlap
gate and the Phase 11 archive update both spawn Index with a codename.
Index had no way to distinguish the two contexts — it would run the
full overlap check on a piece that was already finished. The fix:
Caret writes `Mode: archive-update` to status.md before spawning
Index at Phase 11. Index reads this flag first and skips the overlap
gate entirely.

**Turing's 90-day pruning had no date source.** The spec said to
prune research notes older than 90 days. Turing has no Bash tool. No
way to compute today's date. The pruning logic was correct — it just
couldn't execute. The fix: Turing, Press, Cadence, and Index all
gained Bash access. Turing uses `date +%Y-%m-%d` for pruning. Press
uses it to generate the Hugo front matter ISO timestamp. Cadence
uses it to compute suggested publish dates. Index uses it for
freshness decay audits.

### Two decisions, not bugs

**The image prompt file was renamed.** `image-prompt.txt` became
`image-prompt.md`. The original `.txt` extension and the post-write
character verification rule both existed to protect against markdown
corrupting a plain-text file consumed by GitHub Actions. The author's
decision: Gemini handles markdown fine. The restriction was
unnecessary. The verification rule was removed. The format guidance
— one focused paragraph, no headers, no bullets, no code fences —
stayed, because that's about prompt quality, not file safety.

**Abandon was redesigned end to end.** The reviewer flagged that a
single `[A]` keystroke could delete a piece folder with no
confirmation. The author agreed and went further: the `[A]` option
now requires typing the exact codename before anything is deleted.
Slug collisions — a different problem entirely — were separated out:
Caret retries codename generation up to three times before asking
the user to provide one. Abandon is never surfaced for a mechanical
name collision. And when overlap is real, Index now produces a
structured report first: a summary of what the new piece intends to
cover, a TL;DR of each overlapping post, exactly where the overlap
is, and a recommendation for whether the new content would be better
served as an update. A fourth option — `[U] Update` — was added
alongside Abandon, Differentiate, and Proceed.

### One new feature

**`MMW:bearings`** — session orientation. Type it at the start of
any session to get a concise recap of a piece's current state: what
agents have run, what's outstanding, and a proposed next step. It
never auto-advances. It always ends with a pause.

The name came from the system's own vocabulary. Compass sets
direction. Bearings tells you where you are. The feature was missing
from the original design — not because it wasn't useful, but because
it wasn't needed until the system had enough complexity that re-entry
required orientation.

### Why it matters (for the story)

Six audits. Each one found something the previous missed. This one
found what happens when everything is almost right: the issues are
smaller, more specific, and more dangerous — because they're easy to
overlook.

A missing HOLD branch isn't a logic error. The logic is correct. The
branch just wasn't defined. A partial parallel marker isn't a
capability gap. The capability exists. The recovery path wasn't
specified. These are spec confidence issues — the gap between
*correct behavior described* and *every behavior accounted for*.

The system that went into the build was not the system that came out
of the first design session. It was the system that survived six
rounds of questioning, each from a different angle, each with a
different lens.

The build prompt is now ready to run.

### Additional angle for Compass

- **The failure audit angle**: The difference between auditing for
  correctness and auditing for failure. A correctness audit asks
  whether the system does the right thing when everything goes as
  planned. A failure audit asks what the system does when something
  doesn't. Both are necessary. The failure audit is harder — because
  you have to imagine every way a live agent will diverge from the
  spec.

---

## Session 8 — Pre-Build Agent Design Audit (add to the story)

The architecture was split. The specs were written. The build prompt
was ready to run.

Then it was audited again — but this time the object of review had
changed. Previous audits read the monolith: one file, one workflow,
one pass. This audit read the system: ten spec files, a build prompt,
and a global settings file. Eleven artifacts that had to agree with
each other.

The question was no longer *does the spec make sense?* It was: *does
the system have what it needs to run at all?*

### What was different about this pass

Prior audits found logic errors, missing conditionals, wrong tool
assignments, orphaned infrastructure. This one found a different class
of problem: **systemic gaps** — issues that couldn't be seen by
reading any single file, only by reading all of them in relation to
each other.

Three categories emerged: configuration, tool scoping, and behavioral
ambiguity.

### What was found

**The global tool allow list was nearly empty.** `settings.local.json`
permitted only `WebSearch`. Nothing else. Every other tool — `Read`,
`Write`, `Edit`, `Glob`, `WebFetch`, `Agent` — would prompt for user
approval on every invocation. In an automated multi-agent workflow,
that means a permission dialog between every file read, every file
write, and every subagent spawn. The orchestration model doesn't
survive that. One file, seven tools added.

**Caret had `Grep` in its tool list with no use case.** Every spec
was read. No phase, no responsibility, no protocol referenced `Grep`
for Caret. `Glob` finds files. `Read` opens them. `Grep` was an
artifact from an earlier draft of the system — never removed, never
assigned a purpose. An agent granted a tool it has no instruction to
use will reach for it in ambiguous situations. `Grep` was removed from
Caret's frontmatter and from the build prompt's tool table.

**Turing was missing `Glob`.** Turing maintains a global research
notes file, reads prior entries before each research pass, and prunes
stale findings. These operations require file discovery — knowing what
exists before reading it. `Read` requires a known path. `Glob` finds
paths. `Glob` was added to Turing's spec and to the build prompt.

**Three behavioral patterns assumed state the system couldn't guarantee.**
The prior collaborative audit had flagged them as design risks. This
pass confirmed they were structural:

- The `MMW:proof` gate was a passive convention. Nothing prompted
  the user to type it. After Press and Prism completed, the workflow
  would simply stop — waiting silently for a signal the user might
  not know to send. The fix: Caret actively surfaces the proof prompt
  after Phase 9+10 complete, presenting both options explicitly.

- When invoked directly, agents scanned for the highest-numbered
  `draft-vN.md` via `Glob`. That's an expensive, ambiguous operation
  when `status.md` already contains a `Current draft:` field.
  Direct-invocation agents now read that field first — one Read
  instead of a directory scan plus sort.

- Co-edit session recovery wrote a state marker to `status.md` and
  waited passively for the user to resume. On a new session, nothing
  re-surfaced the co-edit prompt. The fix applies the same pattern
  as the proof gate: Caret writes the marker and presents an
  explicit prompt, which it re-surfaces on any resume where the
  marker is present.

### Why it matters (for the story)

Five audits. Each found things the others missed. Not because the
prior passes were careless — because the system being audited kept
changing. When the monolith became ten files, a new class of bug
became possible: gaps between files. The settings file and the spec
files are different documents. They have to agree. Reading one doesn't
tell you whether the other is consistent.

This pass was the first one that couldn't be done by reading a single
document. It required holding the whole system in view at once —
which is, in some ways, exactly what the architecture refactoring was
designed to make possible.

### Additional angle for Compass

- **The cross-file consistency angle**: When a system is one file, the
  bugs are in the logic. When a system is ten files, the bugs are in
  the gaps between them. The audit discipline has to change when the
  unit of review changes from a document to a system.

---

## Session 10 — Pre-Build Spec Hardening, Round 2 (add to the story)

The system had survived eight audits. The build prompt was clean. The
specs were consistent. Then, before the first `MMW` trigger was typed,
one more pass.

Same question as before: *what can go wrong when an agent actually
executes this?* Different answer: the problems this time were smaller,
more specific, and mostly at the boundary between files — not inside
any single spec, but in the contracts between them.

Seven issues. Two were already fine on inspection. Five were real.

### What was different about this pass

The reviewer had read the full system: build prompt, all ten spec
files, and `flow.md`. The pass combined two modes that previous
sessions had kept separate — a deep best-practices check across the
full design, and a targeted failure audit on specific boundaries.

The issues found were not logic errors. They were gap errors: places
where two files described the same thing differently, or where a file
described behavior that required a capability it hadn't been given.

### What was found and fixed

**Tool tables still disagreed with specs for four agents.** Cadence,
Index, Press, and Turing all required Bash in their specs — for date
computation, pruning, and freshness audits. This had been identified
and discussed in a prior session. The fix had been applied to the
specs. It had not been applied to the build prompt's tool table,
which is the authoritative source for frontmatter generation. The
table still showed those four agents without Bash. One edit. Four
rows updated.

**Caret couldn't execute the Abandon flow.** Index confirms deletion
with the user, writes `Abandon: confirmed` to `status.md`, and
returns. Caret reads the flag and deletes the folder. Caret's tool
list is `Read, Write, Edit, Agent, Glob`. No Bash. No deletion.
The flag would be written. The folder would not be removed.

The fix redraws the responsibility boundary. Index already has Bash.
Index already has the user confirmation step. Index now does the
deletion itself — immediately after the codename is confirmed — and
reports directly to the user. Caret is removed from the deletion
path entirely. If Caret somehow reads `Abandon: confirmed` in
`status.md`, it reports that Index already handled it and stops.
The folder is gone before Caret returns.

**The Hugo path dependency in Phase 11.** Phase 11 wrote `final.md`
to `posts/drafts/[slug].md` — a path that mirrored Hugo's content
structure. This created a hard coupling to a specific publishing
environment. MMW is a writing system, not a Hugo deployment tool.

The fix: a new `writers-room/published/` folder. Final drafts land
there. The author brings them to Hugo — or anywhere else — manually.
The file is ready. The destination is the author's decision.

This change cascades through four files: the scaffold in the build
prompt, `flow.md`'s Phase 11 line and success criteria, Caret's
output list and pre-flight check and handoff step 4, and Press's
`draft: true` note. The `## Environment` block in Press — which
referenced the Hugo blog root — was removed entirely. Press has no
reason to know where your Hugo site lives.

**The Success Criteria were loaded at agent runtime.** `flow.md` is
the canonical runtime reference — agents read it during active
workflows. The 26-step Success Criteria section at the bottom was
build-time validation material that had no reason to be there. Every
agent that read `flow.md` was loading it into their context window.

The fix: Success Criteria moved from `flow.md` into the build prompt's
`## Validation` section, where it belongs. `flow.md` now carries a
one-line pointer. Leaner at runtime, still traceable at build time.

**A stalled parallel agent left no recovery guidance.** The `[partial]`
marker in `status.md` correctly identifies which agent failed to
complete. But if a user returned to a session hours later and saw
`[partial] Echo → pending`, there was no indication of whether Echo
was still running or had timed out. The CLAUDE.md instructions now
include an explicit recovery note: if `[partial]` is present with no
recent activity, the agent likely timed out — use `MMW:echo` (or the
relevant shortcut) to retry.

### Why it matters (for the story)

The system that goes into the build is not the system that came out
of any single session. It is the system that survived ten rounds of
questioning — each from a different position, each with a different
lens, each finding something the previous pass missed.

Not because earlier passes were careless. Because the system kept
getting more complete, and more complete systems surface a different
class of problem. Early audits found missing logic. Middle audits
found capability gaps. Late audits find boundary conditions — the
contracts between files that no single file can verify on its own.

The last problems to find are always at the edges. That's true in
software. It's true in prompt systems. It's true here.

### Additional angle for Compass

- **The boundary condition angle**: Early bugs live inside a single
  file. Late bugs live between files. The final audits before a build
  are not checking whether each file is correct — they're checking
  whether the files agree with each other. That's a different skill
  than writing a spec. It's closer to integration testing.

---

## Session 11 — Inlining the Migration (add to the story)

The build prompt had one step that wasn't like the others. Every other
instruction pointed inward — read a spec, build an artifact, write to
the repo. One step pointed outward: read seven GitHub Copilot prompt
files from a path on the author's machine and migrate their logic into
the agent specs.

That dependency was a problem waiting to surface. A different machine,
a moved file, a renamed directory — any of these would silently break
the build. The spec would run fine until the moment it needed those
files, and then stop with no clear guidance.

The fix was straightforward. The migration was a one-time operation.
The logic from those seven files now lives in the specs directly.

### What was done

Seven source files, each migrated to its target agent spec:

| Source | Target | What was added |
|---|---|---|
| `brand-voice.instructions.md` | Mark | Voice characteristics table, emotional registers, cadence rules, identity guardrails, "What NOT to Do", Human Voice Check |
| `brand-strategy.prompt.md` | Compass | Outcome Narrative Guardrail — full framing language |
| `content-writer.prompt.md` | Caret | Story arc detail, core writing rules, cross-domain metaphor framework, channel templates, bad→good narrative example |
| `accusation-audit.prompt.md` | Devil | Accusation audit definition, when-to-run guidance, audit format instruction |
| `seo-audit.prompt.md` | Press | Full Phase 1–5 SEO audit methodology: technical, E-E-A-T, semantic intent, multi-persona, synthesis + constraints |
| `seo-blog-audit.prompt.md` | Index | Full Phase 1–7 portfolio audit detail: inventory, cannibalization, topical gaps, internal linking, freshness, three-lens synthesis, three-horizon action plan + constraints |
| `visual-brand-validator-dual-mode.prompt.md` | Prism | Full Quick Audit and Strategic Audit output structures, input format, response requirements, audience framing |

---

## Session 12 — Writer Control: Iteration Without Limits (add to the story)

The system had been built. The workflow was running. Then a writer asked
a question the spec had never considered: *what if I'm not done?*

The Caret/Mark creative loop had a hard limit: two iterations, then a
circuit breaker. The logic was sound. Two rounds of feedback is usually
enough. But "usually" is not a design principle. A writer mid-piece,
chasing something that isn't there yet, doesn't want a system that
decides for them when they've iterated enough.

The circuit breaker came out. The user-driven exit went in.

### What changed in Phase 5

The 2-iteration cap and the circuit breaker section were removed
entirely. In their place: a single exit mechanism. After every Mark
review — including PASS — the loop pauses and asks:

```
[C] Co-edit
[R] Revise
[N] Move to critique — send this draft to Devil and Echo for review
```

All three options are available regardless of Mark's verdict. PASS no
longer auto-exits. The writer chooses when they're done. One iteration,
ten iterations — the system doesn't decide.

The `Loop iterations: N of 2` field was dropped from `status.md`. There
is nothing to count.

### What changed in Phase 8.5

The brand re-alignment check had the same problem in a different form.
After Mark reviewed a revised draft, the only paths were: fix it once,
or skip it. No way back to the creative loop. A writer who made
substantial revisions in Phase 8 — real revisions, the kind that change
the piece — had no mechanism to do another full pass with Mark before
publishing.

Two changes.

First: `[R] Quick fix` became `[A] Apply`. Same behavior — Caret applies
Mark's feedback directly. Clearer name.

Second: after Caret applies changes (via co-edit or Apply), and after a
PASS verdict, the system now asks:

```
[L] Back to creative mode — keep working with Mark before publishing
[P] Proceed to publish
```

`[L]` re-enters Phase 5 on the latest draft. The writer gets the full
loop — as many iterations as they want — before the piece goes to press.

### Why it matters (for the story)

The circuit breaker was designed as a safeguard. It prevented the system
from running forever. What it also prevented was a writer from finishing.

The right safeguard is not a hard limit. It's a pause and a question.
The system should know when to stop running on its own. The writer should
decide when the work is done.

Phase 5 now pauses after every Mark review and asks. The writer answers.
That's the whole mechanism.

The system serves the writer's voice. That principle showed up in co-edit
mode, where the user owns the keyboard and Caret waits. It shows up here
too — in the decision not to cap iteration, and in the option to return
to creative mode from anywhere in the post-draft workflow.

### Additional angle for Compass

- **The iteration angle**: A system that decides when you've iterated
  enough is a system that doesn't trust the writer. The right design is
  a pause and a question — not a limit and a circuit breaker.

---

Brand pivot applied throughout: `srvrlss.dev` → `alexandrebrisebois.github.io`,
`Technical Outcome Leader` → `builder-in-public`, `multi-cloud engineer` →
`AI agent builder`. The audience stayed the same. The framing changed.

The `## Migration source` field in each spec was kept as a historical note.
It no longer creates a dependency. It just records where the logic came from.

The Context section and migration table were removed from the build prompt.
The build prompt no longer references any path outside the repo.

### Why it matters (for the story)

The migration step was designed as a bridge — a way to carry proven
logic from an old system into a new one without losing it. That's the
right instinct. The problem is that bridges require both sides to stay
standing.

The moment the logic is proven and the bridge has served its purpose,
the right move is to pull it down. Inline the content. Remove the
external dependency. Let the build stand on its own.

This is the same reason software projects don't ship with references
to the developer's local machine in their configuration. The path
that works today is the path that breaks the next time someone else
runs the build.

The specs are now self-contained. The build is idempotent. Running it
twice produces the same result. Running it on a different machine
produces the same result. The migration is complete — and invisible,
which is how a completed migration should feel.

### Additional angle for Compass

- **The bridge removal angle**: A migration step is a bridge. Bridges
  are temporary. The moment the logic has crossed, the bridge becomes
  a liability. Inline the content, remove the external dependency,
  let the system stand on its own. A build that requires files outside
  its own repo is a build that will eventually fail on someone else's
  machine — probably at the worst possible moment.

---

## Iteration 3 — Editorial Workflow Discipline

This section documents the third major iteration of MMW: a set of
ten changes that gave the system two distinct, purpose-built flows
rather than one flow that tried to serve all cases.

### The Research

The design question going in was: what do professional editorial
workflows actually look like, and what has MMW been getting wrong?

The answer was a familiar pattern in software design: the system
had been conflating two fundamentally different working modes.
Auto flow should be about token budget discipline — minimize cost,
maximize throughput, no unnecessary pauses. Manual flow should be
about maximum creative control — every decision point is an
opportunity for the human writer to redirect, refine, or take back
the keyboard. A system that treats both the same way serves neither.

This framing came from studying how professional editorial workflows
handle the moment before expensive work begins. The classic version
is the editorial commissioning meeting: before a journalist spends
three weeks on a story, the editor asks "is this the right story?"
That question costs almost nothing. Skipping it can cost everything.

### The Key Insights

**Commissioning gate as the moment before the expensive path begins**

The most valuable change in this iteration is the commissioning gate
at Phase 1.5. After Compass sets direction but before Turing starts
research, Caret pauses and shows the angle. Three options: approve,
redirect, or skip research entirely.

The insight is the placement. Redirecting an angle after Turing has
already run costs tokens and context. Redirecting it in ten seconds
before Turing starts costs nothing. The gate exists at the exact
moment where the redirect is cheapest.

In auto mode, the gate doesn't exist. Auto flow doesn't need creative
control — it needs throughput. The commissioning gate is manual-only
because the cost it prevents (unnecessary research) is only relevant
when someone is watching.

**Mark's desk mode / copy mode split**

The original Mark spec treated every review as the same review.
A structural voice failure — "this doesn't sound like you, it
sounds like a consulting deck" — and a banned word violation both
produced the same REVISE verdict and the same loop pause.

The split recognizes that these are different concerns requiring
different attention:

- Desk mode (pass 1, manual only): Voice check. Is this piece
  distinctly yours? Could only this author have written it? Structural
  register, story arc integrity, the Human Voice Check. This is a
  deep read that requires judgment.

- Copy mode (all subsequent passes, auto mode, Phase 8.5): Polish
  pass. Banned words, pronoun rules, cadence. Deterministic. Fast.
  The writer never sees "DESK MODE" or "COPY MODE" — they see
  "Voice check — is this piece distinctly yours?" or "Polish pass —
  banned words, rhythm, pronouns." Implementation detail, not UI.

The framing distinction matters: structural voice is an editorial
question. Mechanical compliance is a copyediting question. They
belong in different conversations.

**Echo personas as named reader contracts**

The original Echo spec had one reader: a vague "skeptical, time-poor
CTO." Useful shorthand, but it obscured a real split in the audience.

The two named personas — The Executive and The Builder — are not
demographic segments. They are reading postures with distinct bounce
triggers:

- The Executive reads for credibility signal and strategic takeaway.
  Bounces at jargon without payoff, no insight in the first scroll.

- The Builder reads for "did they actually build it? What can I use?"
  Bounces at vague claims, hype without substance, missing specifics.

A piece that serves The Executive might lose The Builder in the
second paragraph. A piece that serves The Builder might read as too
tactical for The Executive. Knowing this forces an explicit choice:
is the brief targeting one persona, or trying to earn both? Echo
now surfaces that question explicitly (question 6 in the audience
check: "does this piece serve both personas, or make a deliberate
choice?").

**`--auto --quick` as a draft elaborator**

The fast path (`mmw --auto --quick`) was designed for deadline
pressure and short-form content. But its most useful framing turned
out to be something else: a blank-page antidote.

Starting from nothing feels slow. Starting from a rough complete
draft — even an imperfect one — feels like editing, which is faster
and less resistant. The auto-quick path produces a cheap complete
draft that becomes the starting artifact for a full manual run.
Workflow: `mmw --auto --quick [topic]` → then `mmw [codename]` to
continue in manual mode. The full pipeline picks up from draft-v1.md.

**Turing fact-check as the missing link between research and draft fidelity**

The original system had no mechanism to verify that what Caret
wrote was consistent with what Turing found. Caret reads research.md
before drafting — but a long research document and a long draft
create ample room for a claim to slip through ungrounded or slightly
wrong.

The fact-check sub-mode (`mmw:turing [codename] --fact-check`) closes
this loop. Turing reads research.md and the latest draft, then
categorizes every factual claim: Confirmed (in research.md), Ungrounded
(not in research.md — needs citation or removal), or Inaccurate
(contradicts research.md). The `--find-citation` extension handles
the resolution path for ungrounded claims: targeted search, append
result.

This runs opt-in, manual only, gated on Devil flagging credibility
concerns. The design assumption is that most posts don't need it.
But when credibility is the concern — when Devil is saying "this
claim doesn't hold up" — having a structured path to verify
each claim against the research is more valuable than a general
revision pass.

### The Design Decisions That Didn't Make the Cut

**Why Cadence gets no new logic**: Cadence already writes calendar.md.
Compass now reads it. The insight — publishing frequency and topic
concentration should inform editorial direction — didn't require
changing Cadence at all. It just required pointing Compass at the
file that was already there.

**Why Devil is unchanged**: Devil's four-section output (Publish
Verdict, Challenge Questions, Persona Reactions, Structural Assessment)
already maps cleanly to the Phase 8 triage structure. The triage is
Caret's synthesis of Devil's output, not a new Devil behavior.
Changing Devil would have been change for its own sake.

**Why the co-edit protocol is unchanged**: Co-edit is the most
important feature in the system — the moment the human writer's
voice enters the draft. The rule is: don't touch what's working.
Any change to co-edit would require careful testing against the
core guarantee (Caret never rewrites what the user wrote without
flagging). Not worth the risk in this iteration.

### What This Iteration Was Really About

The deeper pattern across all ten changes: MMW was a single flow
pretending to be flexible. It now has two explicit modes with
different cost profiles, different pause structures, and different
agent subsets — and a fast path that exists primarily as a draft
elaborator rather than a publication shortcut.

The commissioning gate, the Mark mode split, the Echo persona
structure, and the Phase 8 triage all point at the same principle:
every decision point should have exactly the information needed
to make that decision well, and no more. The commissioning gate
shows angle + cadence context — not the full research plan. The
Mark pass 1 shows voice — not word-level violations. The Phase 8
triage shows severity — not an undifferentiated wall of critique.

The system got more useful not by adding capability, but by
being more precise about what each moment in the pipeline is for.

---

## Session 13 — Token Optimization: Python Tools Layer (add to the story)

This session addressed a different kind of system design question: not
what the agents do, but what they should never have to do in the first
place.

The framing was token efficiency. Every agent call costs context.
Some of that context carries genuine reasoning — drafting, evaluating,
synthesizing. But a significant portion was occupied by mechanical
operations: scanning for the highest-numbered draft file, parsing
fields out of status.md, appending formatted rows to markdown tables,
checking whether six pre-flight conditions were met. Operations a
five-line Python script could execute in milliseconds, being handled
by a language model that costs tokens to think about them.

The session identified which operations fell into that category and
built a Python tools layer to handle them — `mmw_tools.py`, a single
stdlib-only script at the project root, callable via Bash by any
agent with Bash access.

### What was built

Ten deterministic tools extracted from agent responsibilities:

- **`draft_version`**: Returns the path to the latest or next draft
  file for a codename. Replaces the repeated directory scan that
  every draft-producing phase was doing independently.

- **`status_read` / `status_write` / `status_log`**: Atomic reads
  and writes for `status.md` fields and log entries. Caret was
  updating status.md in prose after every phase — reading the full
  file into context, making an edit, writing it back. Now a single
  Bash call with a JSON payload.

- **`overlap_check`**: TF-IDF lexical scoring of the brief against
  post-index entries. Returns the top-5 candidate overlaps with
  scores and shared keywords. Index receives a shortlist and makes
  the editorial judgment — not a full table scan in context.

- **`research_prune`**: Date-based pruning of research notes older
  than 90 days. Turing was doing this with a Bash date call + file
  read + parse + rewrite in prompt. Now one tool call, one result.

- **`preflight`**: Six Phase 11 checks (seo.md exists, slug
  populated, slugs match, image-prompt.md exists, draft exists,
  published/ directory exists) collapsed into one Bash call that
  returns `{"ready": true/false, "failures": [...]}`.

- **`publish`**: Atomically writes final.md, published/[slug].md,
  and published/[slug]-image-prompt.md, and updates status.md.
  Five file operations that were happening in prose, now one call.

- **`slug_validate`**: Parses the slug from both status.md and
  seo.md and compares them. Eliminates a subtle failure mode where
  a language model misreads or truncates a slug string during
  the comparison.

- **`index_update`** / **`calendar_log`**: Appends correctly
  formatted rows to post-index.md and calendar.md respectively.
  Table formatting and metadata extraction moved out of agent context.

The tools return JSON to stdout and exit non-zero with a descriptive
error to stderr on failure. Agents parse the result and surface
failures directly. No prose interpretation required.

### What the build prompt now says

The build prompt was updated to instruct each agent to call the
appropriate tool instead of performing the operation in prose.
Caret gained Bash access (it previously had none) to support
status.md management and the publish/preflight operations.
The mmw:proof skill was updated to call `preflight` then `publish`
rather than executing six manual checks and five file writes inline.

The tools don't exist at agent-build time — they're built first,
then the build prompt references them. The agent specs don't change.
Only the build prompt changes, instructing the builder agent to
wire the tool calls into the agent files it creates.

### Why it matters (for the story)

There's a principle in system design: every layer of a system should
do only what that layer is suited for. A language model is suited for
judgment, synthesis, and generation. It is not suited for counting
files, parsing dates, or checking whether six conditions are all true.

The original MMW design was correct about agent specialization —
Caret orchestrates, Turing researches, Mark evaluates voice. But it
hadn't drawn the line between "what requires LLM reasoning" and "what
is just computation." The agents were handling both in the same context
window, paying token cost for operations that had nothing to do with
their core function.

The Python tools layer is the equivalent of moving infrastructure
work out of application code. The application (the agent) stays
focused on its purpose. The infrastructure (file management, state
tracking, validation) runs cheaply beneath it.

The key insight from the overlap_check design: the tool doesn't
decide whether an overlap is editorially significant. It can't —
that requires judgment about angle, differentiation, and portfolio
strategy. What the tool can do is answer the mechanical question:
"which existing entries share keywords with this brief?" Index
receives a shortlist and reasons from there. The separation is clean
because the question is clean.

The same logic applies to preflight. The tool doesn't decide whether
to proceed — it just reports which conditions aren't met. The agent
decides what to surface to the user. Computation and judgment remain
in their respective layers.

### Additional angle for Compass

- **The right layer for the right work**: Systems get slow and
  expensive when layers do work that belongs elsewhere. Token cost
  in a multi-agent pipeline is a forcing function for this discipline.
  When you can see what each operation costs, it becomes obvious
  which operations are in the wrong layer.

- **Determinism as a feature**: The tools are boring by design.
  `draft_version` always returns the same answer given the same
  directory state. `preflight` always checks the same six conditions.
  That determinism is the point — these operations should not vary
  by model, by context, or by phrasing. Moving them out of the LLM
  layer removes an entire class of non-deterministic failure.

---

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

## Session 17 — The Standalone Project Agent: Infrastructure Decoupled (add to the story)

The work done on the sync layer wasn't lost. It was just in the wrong place. We realized that the ability to link a local folder to a Claude Project is a universal utility, not an MMW feature.

The design decision: extract the sync logic, generalize it, and rebirthe it as a standalone **Project Agent**.

### What was built

We moved the sync tools to `scripts/claude-project-tools/` and created a new, dedicated agent: **Project**. It responds to three simple commands:
- `/project:init` — Links the workspace and creates the session context.
- `/project:push` — Uploads the contents of a local `project/` directory to the cloud.
- `/project:pull` — Downloads the cloud state back to the local `project/` directory.

### Why it matters (for the story)

This is a story of "Separation of Concerns." By moving the sync infrastructure into its own agent and its own folder, we decoupled the "Writing Room" (MMW) from the "Sync Layer" (Project Agent). 

MMW stays clean, focused purely on the craft of writing. The Project Agent stays focused on the mechanics of workspace synchronization. If the sync logic ever needs to change — or if we want to use it for a different project entirely — we can do so without touching a single line of MMW logic.

It proves that the best systems aren't monolithic; they are a collection of specialized tools that know how to stay out of each other's way.
