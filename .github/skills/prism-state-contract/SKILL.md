---
name: prism-state-contract
description: Record a scoped prism review against the canonical draft revision.
---

# prism review state

Follow [the editorial contract](../../../docs/editorial-contract.md). Use [the review template](../../../templates/review.state.md) for prism.state.md when persistence is available.

Required fields: canonical_draft, reviewed_revision, role, scope, outcome. Outcomes: ready, revise, blocked, not-needed. Record each concrete finding, triggering passage, proposed move, author disposition, evidence gaps and next action. A skipped scope is not a pass; an old revision is stale.

Do not insert hidden redlines or edit the canonical body. Preserve accepted/rejected decisions when refreshing state. If a visual is useful, provide a separate {slug}.image-prompt.md only when requested. Record whether an actual image was generated; a prompt is not an asset.
