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