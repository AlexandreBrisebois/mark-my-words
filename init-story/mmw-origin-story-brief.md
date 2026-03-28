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

