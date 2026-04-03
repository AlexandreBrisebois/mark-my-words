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