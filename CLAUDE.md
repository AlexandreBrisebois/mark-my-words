# Mark My Words

Mark My Words (mmw) is a multi-agent writing system for long-form blog content. It coordinates a team of specialized Claude Code subagents — strategist, researcher, brand guardian, critic, audience evaluator, publisher, visual brand agent, archivist, and scheduler — each with a defined role and tool scope. Caret orchestrates all of them. The goal is to produce blog posts that are distinctly yours, rigorously reviewed, and ready to publish. Everything serves the writer's voice.

---

## Trigger

The only recognized trigger is `mmw`. (`MMW` and `Mark My Words` are not triggers.)

`/mmw` is the primary slash command (registered as a Skill). The plain-text `mmw` is a fallback for sessions where skills are not loaded.

---

## Invocation Modes

### Manual mode (default)
```
mmw [topic]
mmw path/to/file.md
mmw - first idea
  - second idea
  - constraints
```

Caret pauses after each phase and proposes the next step. The user decides when to advance. Co-edit mode fully available. Full pipeline with no iteration cap on the Mark loop.

### Interactive mode (`--interactive`)
```
mmw --interactive [topic | file | bullets]
```

Section-by-section co-writing. You write, Caret reviews. Perfect for hands-on drafting. Cannot be combined with auto modes.

### Auto mode
```
mmw --auto [topic | file | bullets]
```

Runs the full pipeline without pausing between phases. Caret strips `--auto` before generating the codename. Stops at `mmw:proof`, which is always a human step.

Key auto-mode differences:
- Phase 5 loop cap: 1 Mark pass only (copy mode). REVISE applied directly. HOLD logged in status.md but does not pause the workflow.
- Phase 8: Devil/Echo feedback applied directly, new draft produced, no pause.
- Phase 8.5: skipped.
- Note: a Mark HOLD verdict is logged but does not stop the workflow. Auto mode may produce drafts with unresolved structural flags. Use manual mode for complex or high-stakes pieces.

### Auto-quick mode
```
mmw --auto --quick [topic | file | bullets]
```

Reduced-agent fast path. Skips Compass, Mark, Devil, Echo, and the revision window. Runs Index, Turing (single search), Caret (draft), Echo quick check, Press, Prism. `mmw:proof` is still a human gate.

Use for cheap first drafts. Run `mmw [codename]` afterward to continue in manual mode — the full pipeline picks up from the existing draft.

### Session resume
```
mmw [codename]
```

Resumes an existing piece. Caret reads status.md first and reports the current state. If `Mode: auto` is present in status.md, auto mode applies for all remaining phases.

### Discovery mode
```
mmw --discovery [topic | file | bullets]
mmw --discovery --auto [topic | file | bullets]
```

Generates 3 distinct editorial directions, runs Compass across all three, and presents a selection menu. The user picks one angle before the pipeline proceeds. Incompatible with `--quick`.

---

## Sub-Agent Shortcuts

Each shortcut invokes a native Claude Code subagent defined in `.claude/agents/`. Slash-command form is canonical; `mmw:agent` plain-text variants work as fallbacks.

| Slash command | Plain-text fallback | Agent |
|---|---|---|
| `/mmw-compass [codename]` | `mmw:compass [codename]` | Compass — strategy |
| `/mmw-turing [codename]` | `mmw:turing [codename]` | Turing — research |
| `/mmw-mark [codename]` | `mmw:mark [codename]` | Mark — brand check |
| `/mmw-review [codename]` | `mmw:review [codename]` | Caret — section feedback loop |
| `/mmw-bearings [codename]` | `mmw:bearings [codename]` | Session orientation |
| `/mmw-echo [codename]` | `mmw:echo [codename]` | Echo — audience check |
| `/mmw-press [codename]` | `mmw:press [codename]` | Press — SEO and Hugo front matter |
| `/mmw-prism [codename]` | `mmw:prism [codename]` | Prism — image prompt |
| `/mmw-index [codename]` | `mmw:index [codename]` | Index — archive and overlap check |
| `/mmw-cadence [codename]` | `mmw:cadence [codename]` | Cadence — editorial calendar |
| `/mmw-proof [codename]` | `mmw:proof [codename]` | Declare draft final — triggers Phase 11 |

### mmw:proof — Human Gate

`mmw:proof [codename]` is how the user declares a draft final and triggers Phase 11 handoff (published files, archive update, calendar log). **No agent calls this automatically — it is always a deliberate human decision in both manual and auto mode.**

`mmw:proof` is handled inline by Caret — there is no `.claude/agents/proof.md`. When the user types `mmw:proof [codename]`, Caret reads the piece folder and executes the Phase 11 pre-flight directly.

### mmw:bearings — Session Orientation

`mmw:bearings [codename]` reports the current state of the piece: what has been done, which agent last ran, what file was produced, and what the next step is. It then proposes the concrete next step and pauses.

`mmw:bearings` is handled inline by Caret — there is no `.claude/agents/bearings.md`.

### mmw:done — Co-edit Signal

`mmw:done` (in the conversation, not typed into a file) signals that the user has finished editing the draft directly and is ready for Caret to integrate their changes and produce the next version.

---

## Codename Generation

Codenames are derived from the brief content: descriptive, lowercase, hyphenated, 2–3 words, characters `[a-z0-9-]` only (no spaces, underscores, accented characters, or special characters). Caret strips `--auto` and other flags before generating the codename.

Examples: `writers-room-build`, `agent-research-loop`, `brand-pivot-retro`, `ai-agent-patterns`

---

## Full Workflow Summary

```
Phase 0  — Index: overlap gate (always first)
Phase 1  — Compass: editorial direction (skipped in auto-quick)
Phase 2  — Turing: research
Phase 2.5 — Outline Gate: structural sign-off (manual/interactive only)
Phase 3  — Caret/User: first draft (research gate enforced)
Phase 3.5 — Echo --quick: audience signal (manual only; auto-quick: conditional)
Phase 4  — Mark: headlines and hook alternatives (skipped in auto-quick)
Phase 5  — Caret ↔ Mark: iterative loop (skipped in auto-quick)
Phase 6+7 — Devil ║ Echo: parallel critique and audience review (skipped in auto-quick)
Phase 8  — User revision window (auto: applied directly; skipped in auto-quick)
Phase 8.5 — Mark: brand re-alignment check (manual only, user-initiated, conditional)
Phase 9+10 — Press ║ Prism: parallel SEO and image prompt
[mmw:proof — human gate]
Phase 11 — Handoff: final.md, published/, archive and calendar update
```

---

## The Iterative Loop

Caret and Mark iterate on the draft until the user decides to move on. No iteration cap in manual mode.

Mark runs in two internal scopes:
- **Pass 1 (desk mode)**: "Voice check — is this piece distinctly yours?" — story arc, voice, emotional register, Human Voice Check.
- **Pass 2+ (copy mode)**: "Polish pass — banned words, rhythm, pronouns" — fast and deterministic.

Verdicts: **PASS** (proceed) / **REVISE** (specific changes needed) / **HOLD** (structural issue — not a revision problem).

Circuit breaker: after 2 REVISE verdicts in a row, Caret surfaces options: co-edit, one more revision, or proceed to critique.

---

## Co-Edit Mode

Co-edit is triggered when the user types `[C]` or "co-edit" at any loop pause point, or after any Devil/Echo review.

Co-edit is the most important feature in this system. The user's voice is the point. Everything else serves that.

**Available in manual mode only** (except at Mark HOLD in auto mode).

```
## Co-Edit Mode

Co-edit is triggered when the user types [C] or "co-edit" at any
loop pause point, or after any Devil/Echo review.

Example session:
  Mark reviewed draft-v1.md → brand-notes-v1.md [REVISE]
  User: C
  Caret: [surfaces specific flagged lines with current text and issue]
  User: [edits draft-v1.md directly in their editor]
  User: mmw:done
  Caret: [reads edited file, integrates remaining issues,
          produces draft-v2.md, reports exactly what it changed
          beyond the user's edits]

Co-edit is the most important feature in this system.
The user's voice is the point. Everything else serves that.
```

Co-edit rules:
- Caret never rewrites a passage the user just wrote without flagging it
- If a user's edit contains a banned word, Caret flags it — does not delete it
- The user's voice overrides Mark's preferences in conflict
- Caret's job in co-edit is to be the user's assistant, not their editor

---

## Published Files

Final drafts land in `writers-room/published/[slug].md`. The image prompt lands in `writers-room/published/[slug]-image-prompt.md`. Bring them to your publishing environment manually. mmw does not write outside its own directory.

`image-prompt.md` must be one focused paragraph — no headers, no bullets, no code fences. Bring it to Gemini Image Pro to generate the cover image.

Note: Hugo front matter in `seo.md` has `draft: true` intentionally. Set `draft: false` in your Hugo environment when ready to publish.

---

## Recovery

**Parallel agent timeout**: If you return to a session and status.md shows `[partial]` with no recent activity, the agent likely timed out. Use the relevant `mmw:agent` shortcut to retry the missing agent. Example: `[partial] Echo → pending` means `mmw:echo [codename]` to retry.

**Scaffold recovery**: If `mmw:proof` stops with "writers-room/published/ directory missing", the project scaffold is incomplete. Fix: run `mkdir -p writers-room/published/` from the project root, then retry `mmw:proof [codename]`.

---

## Notes

- This is a writing tool — responses should be editorial, thoughtful, and concise. Not a coding tool.
- Agent definition files live in `.claude/agents/` — not in `writers-room/agents/`. Claude Code scans `.claude/agents/` to register native subagents.
- `mmw:proof` and `mmw:bearings` are handled inline by Caret — there are no `proof.md` or `bearings.md` agent files.
