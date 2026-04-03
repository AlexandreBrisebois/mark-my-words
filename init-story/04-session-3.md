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