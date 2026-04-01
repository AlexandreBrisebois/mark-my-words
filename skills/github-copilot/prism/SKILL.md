---
name: prism
description: Visual brand translation and validation skill. Optimized for generating Gemini Image Pro prompts and auditing brand identity.
---

# Prism Skill

The Prism Skill translates content into precise visual prompts and validates brand identity against established guidelines. It maintains the **Calm Signal** aesthetic and ensures visual discipline across all outputs.

## Parameters
- `mode` (default: `quick`): The audit depth (`quick` or `strategic`).

## Core Philosophy
- **Visual Literacy**: Deep understanding of how imagery communicates brand values.
- **Brand Discipline**: Rigid adherence to the Calm Signal identity over generic aesthetics.
- **Audience-Centric**: Tailoring visual logic for CTOs, business decision makers, and engineers.

## Modes

### 1. Image Prompt Generation
Translates a draft into a single, focused visual prompt for Gemini Image Pro.

- **Inputs**: provided md file
- **Execution**: 
    - Extract the core ideas from the text provided.
    - Synthesize into exactly one focused paragraph.
    - **No markdown formatting** (no headers, bold, bullets, or fences).
- **Output**: **Return the prompt directly as plain text.**

### 2. Quick Audit
Fast executive snapshot of visual brand health.
- **Output**: 
    1. Executive snapshot (5–7 bullets).
    2. Audience fit check (CTO / Business / Engineer).
    3. Scores (1–10): Clarity, Credibility, Differentiation, Memorability, Cohesion.
    4. Top 5 issues to fix first.
    5. Quick wins for this week.

## Branding Strategy: Calm Signal
All visual logic must adhere to the visual brand constraints read from `../visual-brand.md`.

## Execution Rules
- **Directness**: Be specific and practical; avoid generic branding advice.
- **Assumption Clearing**: Explicitly state assumptions when data is missing.
- **Format Rigidity**: For image prompts, return ONLY the paragraph. No preamble or postscript.
