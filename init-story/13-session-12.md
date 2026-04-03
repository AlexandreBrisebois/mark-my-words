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