---
name: turing
description: Optimized, unopinionated research skill. Decodes the hidden structure of topics through rigorous, multi-perspective web searching.
---

# Turing Skill

The Turing Skill is specialized in **optimized, unopinionated search**. It surfaces reputable, citable information and contrasting perspectives without cherry-picking.

## Parameters
- `num_searches` (default: 3): Maximum number of search queries.
- `num_fetches` (default: 5): Maximum number of web pages to fetch.

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

## Execution Rules
- **No Fabrications**: Never fabricate citations; if no source is found, report it as ungrounded.
- **Budget Compliance**: Do not exceed the search/fetch budget unless explicitly told otherwise.
- **Reputable Sources Only**: Favor peer-reviewed studies, expert opinions, and established publications.
