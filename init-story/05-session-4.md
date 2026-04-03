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