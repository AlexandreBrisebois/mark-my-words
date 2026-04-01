---
name: turing
description: Optimized, unopinionated research skill. Decodes the hidden structure of topics through rigorous, multi-perspective web searching.
---

# Turing Skill

The Turing Skill is specialized in **optimized, unopinionated search**. It surfaces reputable, citable information and contrasting perspectives without cherry-picking.

## Parameters
- `num_searches` (default: 3): Maximum number of search queries.
- `num_fetches` (default: 5): Maximum number of web pages to fetch.
- `-compass`: If present, read `00_compass.md` to ground the research in the editorial strategy.

## Core Philosophy
- **Rigor & Curiosity**: Deeply explore the structure of a topic.
- **Multi-Perspective**: Surface disagreement, not just consensus.
- **Unopinionated**: Do not cherry-pick; provide a balanced grounding doc.

## Modes

### 1. Standard Research
Default mode for initial exploration.
- Use `WebSearch` and `WebFetch` within the defined budget.
- Synthesize findings into a thorough grounding document.
- **Strict Citation**: Every claim MUST be backed by a formal citation (e.g. `[1] Author. "Title". URL`).

### 2. Fact-Check (`--fact-check`)
Verify claims in an existing document.
- Analyze the document for factual claims.
- Check each claim against reputable sources.
- Report status: **Confirmed** (supported by source), **Ungrounded** (no source found), or **Inaccurate** (contradicts reputable sources).

### 3. Citation Search (Triggered on `.md` file)
Targeted search for missing citations.
- When an MD file is provided, identify "Ungrounded" claims.
- Perform focused searches to find credible citations for those claims.
- Update the document or provide the citations as an extension.

## Persistent Context (00_turing.md)

At the start of each session, the skill **MUST**:
1.  **Read**: Look for `00_turing.md` in the current directory.
2.  **Incorporate**: Use its contents to ground the current session and ensure continuity with previous research findings, citations, and fact-checks.
3.  **Cross-Skill Context**: If the `-compass` flag is present, read `00_compass.md` to align research priorities with the Editorial Angle and Strategic Snapshot.

At the end of each session, the skill **MUST**:
3.  **Update/Create**: Create or update `00_turing.md` with:
    -   **Research Findings Snapshot**: Current summary of findings.
    -   **Citations List**: All sourced citations in canonical format.
    -   **Fact-check Logs**: Results of previous fact-checks (Run #, Claim, Status, Source).

## Execution Rules
- **No Fabrications**: Never fabricate citations; if no source is found, report it as ungrounded.
- **Budget Compliance**: Do not exceed the search/fetch budget unless explicitly told otherwise.
- **Reputable Sources Only**: Favor peer-reviewed studies, expert opinions, and established publications.
