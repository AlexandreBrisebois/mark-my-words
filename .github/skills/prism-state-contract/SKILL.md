---
name: prism-state-contract
description: Mandatory state handling for the Visual Auditor. Manages snapshots and production assets.
---

# Prism State Contract

Use this skill to manage the "Latest Truth" and production artifacts.

## 1. Stateless Snapshot (`prism.state.md`)
Always **OVERWRITE** the entire file with the current audit results. No historical logs.
Include:
- **Input Context**: Which draft and strategy were used.
- **Visual Thesis**: The distilled "Meaning" of the visual.
- **The Verdict**: (CLEAR / BLOCKED / POLISH).
- **Audit Findings**: High-signal bullet points from the structural audit.
- **Latest Prompt**: The exact prompt generated for history.

## 2. Production Asset (`{slug}.image-prompt.md`)
Generate a separate, clean file for the user/production pipeline.
- **Naming**: Use the `{slug}` extracted from the draft or working directory.
- **Content**: Exactly one plain-text paragraph. No markdown. No headers.

## 3. Slug Extraction
- Identify the project `{slug}` from the primary draft file (e.g., `ai-patterns.draft.md` -> `ai-patterns`).
- If no draft exists, use the working directory name or `brief.md`.

## 4. Chat Dashboard
Every run must end with a high-signal summary in the chat:
1. **The Verdict**: (CLEAR / BLOCKED / POLISH)
2. **Visual Thesis**: 1-sentence elevator pitch.
3. **Squint Test**: Pass/Fail on hierarchy.
4. **Actionable Move**: The single most impactful structural or visual change required.

## Rationale
Consistency is the foundation of the MMW relay. By separating the *Auditor's Logic* (state) from the *Production Asset* (prompt), we ensure technical cleanliness.
