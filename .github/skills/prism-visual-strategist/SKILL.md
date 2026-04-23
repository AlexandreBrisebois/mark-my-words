---
name: prism-visual-strategist
description: Logic for distilling a "Visual Thesis" and engineering brand-faithful image prompts.
---

# Prism Visual Strategist

Use this skill to translate editorial meaning into production-ready image prompts.

## 1. The Visual Thesis
Every image must carry an article's core tension or claim.
- **Goal**: Infer the one thing the viewer should feel or infer first.
- **emotional Register**: Define the mood (Calm, Urgent, Technical, Reflective).
- **Anti-Literalism**: Avoid illustrating surface nouns. Focus on the *argument*.

## 2. Image Prompt Engineering
Write exactly one plain paragraph (no headers, no bullets, no markdown).
- **Subject**: One dominant visual idea.
- **Composition**: Define focal hierarchy, camera viewpoint, and negative space.
- **Lighting/Material**: Describe textures and light behavior (e.g., "diffused architectural light," "brushed aluminum").
- **Constraints**: No humans, no literal icons, no generic "tech" cliches.

## 3. The "No-Fly List" (Block these)
Automatically **RETHINK** if the prompt contains:
- **Glowing Gradients / Neon Shards**: Looks like generic AI art.
- **Humanoid Silhouettes**: Overused and low-signal.
- **Abstract Floating Dashboards**: Implies complexity without clarity.
- **Rocket Ships / Lightbulbs**: Corporate clip-art.

## 4. Config Anchoring
All choices must be anchored to a token in `visual-brand.md`.
- **Constraint**: If a palette or aesthetic is used, cite the configuration line that authorizes it.

## Rationale
To CTOs and engineers, "Aesthetics" are secondary to "Systems." Your visual direction must signal a deep understanding of the article's system-thinking.
