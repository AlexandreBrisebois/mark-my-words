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