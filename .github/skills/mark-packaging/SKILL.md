---
name: mark-packaging
description: Generates and scores headlines that "accurately sell the real idea."
---

# Skill: Mark Packaging

Use this skill to generate headlines that align with the "Calm Signal" and the specific argument made in the draft.

## Headline Generation Rules
1. **Read the Full Draft**: Never generate headlines based only on the brief. Headlines must "sell the real idea" as it exists in the draft.
2. **Calm Signal**: No clickbait, no "Top 10" listicles, no false promises.
3. **Draft Context**: Align with the argument defined in `compass.state.md` and the draft's tone.

## Scoring Matrix
Score 5-10 options based on:
- **Brand Fit**: Does it sound like the author?
- **Audience Fit**: Does it land with the intended personas from `mmw-audience-modeling`?
- **Opening Strength**: Does it earn attention without distortion?
- **Clarity**: Does it avoid abstraction?

## Output
Include the scored options in the `mark.state.md` snapshot and present the top choice in the chat for user selection.
Once selected, the **Caret** agent will be responsible for applying the headline to the draft frontmatter.
