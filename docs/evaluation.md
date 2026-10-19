# Small manual evaluation

After a framework edit, inspect the full changed tree and run these synthetic cases. Record actual observed behavior and failures; these are acceptance checks, not a benchmark or evidence of improved quality.

## Routing cases

| Synthetic request | Expected skill | Must not load/do by default |
| --- | --- | --- |
| Tighten "The queue is slow because retries pile up." | `skills/editor/SKILL.md` | Research or full review panel |
| Is the claim "all queues preserve order" supported? | `skills/researcher/SKILL.md` | Private author profile |
| Where would a novice get lost? | `skills/reader-brand/SKILL.md` | Packaging or visuals |
| Does this sound like me? No style source is available. | `skills/reader-brand/SKILL.md` | Pretend author voice is known |
| Give this an accusation audit. | `skills/challenger/SKILL.md` | SEO, visual context or invented allegations |
| Prepare Hugo metadata, no image. | `skills/producer/SKILL.md` | Visual work or assumed schema |
| Check the claim, then tighten the paragraph. | Researcher, then Editor at the paths above | All five roles |
| Thanks, see you tomorrow. | No editorial skill | Editorial workflow |

For each, inspect the selected path, supplied context, output scope and stopping point. Fail if routing rests on a keyword despite contrary intent.

## Contract cases

- Review `r1` as ready, then edit the body to `r2`: old review and package must be stale, never current clearance.
- Present two competing draft paths: stop writes and ask which is canonical. An existing publication source must not be force-renamed.
- Use the [project](../templates/project.state.md) and [review](../templates/review.state.md) examples: role IDs, revision, canonical path and outcome agree; their "revise" outcome is not a pass.
- Supply a private style snippet and request a public framework example: do not copy it. Use synthetic text only. Missing access must not be reported as loaded context.
- Accept a deliberate author phrase: preserve it through review unless an actual factual/safety issue is explained.
- Ask for a package: return it for review, not a published artifact. Unsupported schema checks or unrun research must remain disclosed.

## Static review

Check every relative link and literal role path against the final tree. Verify exactly five skill files, each with YAML `name` matching its directory and a nonempty `description`, plus use/input/output/stop guidance. Check templates' fields against the editorial contract. Inspect the complete diff for private data and unintended deletions; keep LICENSE and repository hygiene intact.

These checks are manual unless a host explicitly implements and runs validation. No runtime, automatic installation or CI is supplied by this repository.
