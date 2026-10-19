# Editorial contract v2

## Authority and scope

Host safety and permissions always apply. For editorial choices, follow current user intent and protected author choices, then authorized private configuration, then this contract and role guidance. Configuration cannot grant permissions. Preserve mission/About content unless explicitly asked to revise it.

Identify the requested outcome, audience and stopping condition. Ask only the question that materially changes the work; a complete brief can skip discovery. Default to one focused pass and a targeted revision if useful. Set a bounded scope/budget before broad research or multi-role work. Stop when the outcome is met, a decision/access/evidence blocker needs the author, or further polishing would only swap equivalent wording. Disclose incomplete work and unmeasured results honestly.

## One canonical draft

Only the designated Editor changes the canonical body. Reviewers propose changes separately. The author retains wording and risk decisions; reviewers do not acquire veto power over taste.

New drafts use `{slug}.draft.md`. Existing publication sources remain canonical at their exact paths, without forced renaming or synchronized copies. If competing drafts exist and the canonical source is unclear, stop writes and ask.

When durable state helps, use the private [project template](../templates/project.state.md). Record the canonical path and actual Git/blob/content hash, or an explicit increasing revision such as `r1`. Never invent a hash. Advance the revision on every body edit, including author edits. Without storage, label the artifact/revision in conversation and disclose that it is not persisted.

## Reviews and evidence

Use the private [review template](../templates/review.state.md) for durable reviews. Record role, canonical path, reviewed revision, scope, findings, author dispositions and outcome:
- `ready`: the stated scope is satisfied on that exact revision.
- `revise`: concrete changes are proposed.
- `blocked`: missing evidence/access/decision or a material unresolved problem.
- `not-needed`: deliberately skipped, with a reason; not a pass.

Only `ready` with a matching current revision is current clearance. Missing or mismatched revisions are stale. Every body edit makes prior reviews stale; recheck affected findings and new claims before issuing fresh scoped clearance. Preserve accepted/rejected findings and protected choices. File existence is never clearance.

Distinguish external facts, author recollections, opinions and inferences. Do not fabricate experience, quotes, metrics, sources or certainty. Citations must support the exact claim. Keep contrary evidence and uncertainty visible; personal recollections need attribution, not invented web citations.

## Privacy and publication

Follow [configuration loading](configuration.md). Keep real drafts, reviews, identity, voice samples, private mappings and source conversations out of public files, fixtures, commits, issues and PRs. Reading private content is not permission to publish it.

Packaging preserves the canonical body. Create a separate package only when requested, with its source revision recorded and `draft: true` where supported. A package becomes stale after a body edit. Use the destination's actual schema. Visuals are optional.

Readiness never authorizes publishing, external sending, uploading, merging or deploying. Those actions require the host's normal authorization.
