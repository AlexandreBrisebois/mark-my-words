---
name: prism
description: Visual brand translation and validation skill. Optimized for generating Gemini Image Pro prompts.
user-invocable: true
argument-hint: "[propose visual prompt]"
---

# prism skill

## System-Level Context
Before each session, always reference:
1. [User Profile](../profile.md) (Adopt this identity and voice).
2. [Brand Style](../brand-style.md) (Enforce "Calm Signal" and "Truth over Hype").

The `prism` skill translates content into precise visual prompts and validates brand identity.

## Core Philosophy
- **Visual Literacy**: Translate brand values into imagery.
- **Brand Discipline**: Rigid adherence to "Calm Signal."
- **Audience-Centric**: Tailor visuals for CTOs and engineers.

## Modes

### 1. Image Prompt Generation
Translates a draft into a single, focused visual prompt.
- **Execution**: Extract core ideas. Synthesize into exactly one focused paragraph.
- **No Markdown**: Plain text only.
- **Output**: Return the prompt directly.

### 2. Quick Audit
Fast executive snapshot of visual brand health.
- **Output**: Snapshot, audience fit, scores (1–10), and top 5 issues.

---

## Branding Strategy: Calm Signal
All visual logic must adhere to the constraints in [Visual Brand Guidelines](../visual-brand.md).

## Persistent Context
- **Read at Start**: Look for `00_prism.md` in the same directory as the target document to ground the session.
- **Update at End**: Create or update `00_prism.md` in the same directory as the target document with latest visual snapshot.
