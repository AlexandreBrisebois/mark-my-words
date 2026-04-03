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