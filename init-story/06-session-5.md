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