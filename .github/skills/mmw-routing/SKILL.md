---
name: mmw-routing
description: Stage Detection & Bootstrapping logic for the MMW orchestrator. Defines the "Living Map" and prerequisite validation.
---

# MMW Routing & Stage Detection

Use this skill to determine the current phase of a piece and identify the next logical step in the editorial relay.

## Stage Detection Matrix

| Condition | Current Phase | Recommended Next |
|---|---|---|
| No `brief.md`, no `compass.state.md` | **Not Started** | Bootstrap `brief.md` → `compass` |
| `brief.md` exists, no `compass.state.md` | **Strategy Pending** | `compass` |
| `compass.state.md` exists, no `turing.state.md` | **Research Pending** | `turing` (or skip to `caret`) |
| `turing.state.md` (or manual research) exists, no `*.draft.md` | **Awaiting Draft** | `caret` |
| `*.draft.md` exists, no auditor states | **Review Pending** | `mark`, `echo`, `devil` |
| Review states exist, no `prism.state.md` | **Visuals Pending** | `prism` |
| `prism.state.md` exists, no `press.state.md` | **Packaging Pending** | `press` |
| `press.state.md` exists | **Packaged** | Final Review / Done |

## Bootstrapping Logic
When the folder is empty:
1.  Read the user's source prompt.
2.  Use `mmw-codename-gen` to generate a canonical slug.
3.  Generate `brief.md` (Hugo frontmatter NOT required).
4.  Record the source prompt in `mmw.state.md`.
5.  Route to `compass`.

## Prerequisite Validation
- **Compass**: Requires `brief.md`.
- **Turing**: Requires `compass.state.md`.
- **Caret**: Requires `compass.state.md`. (Alert if `turing.state.md` is missing but do not block).
- **Reviewers**: Require `{slug}.draft.md`.
- **Prism**: Requires `{slug}.draft.md` and at least one review state.
- **Press**: Requires `{slug}.draft.md` and `prism.state.md`.

## Rationale
The matrix provides a deterministic way to evaluate the "Living Map" without model hallucinations. It ensures the orchestrator always knows where the project stands.
