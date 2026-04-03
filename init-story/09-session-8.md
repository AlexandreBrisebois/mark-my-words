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