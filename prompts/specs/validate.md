# mmw_validate.py — Build Validation Script Spec

This spec defines a `mmw_validate.py` script that automates the mechanical pre-flight checks after a build. It replaces the error-prone manual file inspection in the Validation section of `mmw-build-prompt.md`.

Run from the project root:
```
python mmw_validate.py
```

Exits 0 if all checks pass. Exits 1 and prints a failure summary if any check fails.

---

## Checks

### 1. Required files exist and are non-empty

Verify each of the following paths exists and has non-zero byte size:

**Seed files:**
- `writers-room/brand/guidelines.md`
- `writers-room/index/post-index.md`
- `writers-room/cadence/calendar.md`
- `writers-room/research/notes.md`

**Agent files** (all 10):
- `.claude/agents/caret.md`
- `.claude/agents/mark.md`
- `.claude/agents/compass.md`
- `.claude/agents/devil.md`
- `.claude/agents/turing.md`
- `.claude/agents/echo.md`
- `.claude/agents/press.md`
- `.claude/agents/prism.md`
- `.claude/agents/index.md`
- `.claude/agents/cadence.md`

**Skill files** (all 12):
- `.claude/skills/mmw/SKILL.md`
- `.claude/skills/mmw-turing/SKILL.md`
- `.claude/skills/mmw-devil/SKILL.md`
- `.claude/skills/mmw-echo/SKILL.md`
- `.claude/skills/mmw-press/SKILL.md`
- `.claude/skills/mmw-prism/SKILL.md`
- `.claude/skills/mmw-compass/SKILL.md`
- `.claude/skills/mmw-mark/SKILL.md`
- `.claude/skills/mmw-cadence/SKILL.md`
- `.claude/skills/mmw-index/SKILL.md`
- `.claude/skills/mmw-bearings/SKILL.md`
- `.claude/skills/mmw-proof/SKILL.md`

### 2. Agent frontmatter `tools:` is a YAML inline sequence

For each agent file, parse the YAML frontmatter and confirm the `tools` field:
- Is present
- Is a list (not a plain string)
- When re-serialized, renders with `[` and `]` brackets

If `tools` is a plain string (e.g., `tools: Read, Write`), flag it as a failure. A plain string silently disables tool scoping with no runtime error.

### 3. Agent frontmatter `model:` is present

For each agent file, confirm `model: claude-sonnet-4-6` is present in the frontmatter.

### 4. SLUG_SENTINEL consistency

Read `.claude/agents/caret.md` and `.claude/agents/press.md`. Both must contain the exact string `- Slug: (written by Press)`. If either is missing or differs, report the mismatch.

---

## Output format

On success:
```
mmw validate: all checks passed (10 agents, 12 skills, 4 seed files)
```

On failure:
```
mmw validate: FAILED

  [MISSING] .claude/agents/prism.md
  [TOOLS NOT LIST] .claude/agents/mark.md — tools field is a plain string
  [SLUG MISMATCH] press.md does not contain the expected SLUG_SENTINEL

Fix the above before tracing workflow paths manually.
```

---

## Implementation notes

- Use PyYAML to parse frontmatter (split on `---` delimiters, parse the first block).
- All paths are relative to the directory where the script is invoked (project root).
- The script does not run a live workflow — it only inspects files.
