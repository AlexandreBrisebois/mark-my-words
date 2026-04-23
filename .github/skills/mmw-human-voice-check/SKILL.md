---
name: mmw-human-voice-check
description: Audits prose for "AI-isms," generic polish, and model-memory fabrication. Ensures the output sounds distinctly like a specific human author.
---

# Skill: MMW Human Voice Check

Use this skill to evaluate whether a draft has "Maker-Honesty" or has been flattened by generic AI processing.

## The Three Questions
Every audit must answer these three questions:
1. **Authorship Unique?**: Could only *this* specific author (as defined in `profile.md`) have written this? 
2. **Observation Anchored?**: Is every claim supported by a specific observation, technical detail, or lived experience? 
3. **Filler-Free?**: Are there any "AI-polished" sentences that sound smooth but contain zero new information or unique perspective?

## Detection Patterns (Flag these)
- **The "Model-Memory" Citation**: Vague references to "studies show" or "experts agree" without a specific source from `turing.state.md` or the user.
- **Polished Emptiness**: Sentences that use perfect grammar to say nothing (e.g., "In the rapidly evolving landscape of technology, it is important to consider the implications...").
- **Generic Connectors**: Over-reliance on *Furthermore, Moreover, Additionally*.
- **The "Summary" Crutch**: Ending with "In conclusion" or "To summarize."

## Rationale
"Calm Signal" editorial standards prioritize high-value signal over marketing noise. GPT-4.1 can drift into "Helpful Assistant" mode; this skill forces it back into "Exacting Human Editor" mode.
