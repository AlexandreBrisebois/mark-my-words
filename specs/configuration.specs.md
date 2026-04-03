# System Spec: Configurable Author Platform

## One-line purpose
Defines the configuration contract that lets writers adapt the multi-agent writing system by editing shared configuration files instead of rewriting agent logic.

## Why this spec exists

The Mark My Words multi-agent system should be portable.

Writers adopting the platform should be able to change who the writer is, how the writing should sound, how editorial brand should be enforced, how visuals should feel, and how readable the prose must be without editing every agent prompt.

This spec establishes `.github/agents/configurations/` as the stable customization layer for that behavior.

---

## Configuration design goal

The system must be easy to configure and easy to adopt.

That means:

- writers change configuration documents, not agent logic, for normal customization
- agents reference shared configuration files as their source of truth
- the same agent set can be reused across writers, brands, and publications
- author identity, editorial brand, visual brand, and readability rules remain separable concerns
- configuration files stay human-readable so non-engineers can maintain them

---

## Canonical configuration directory

All writer-level shared configuration lives in:

- `.github/agents/configurations/`

This directory is the platform-level configuration surface.

It is intended to be edited by the adopting writer or team.

Agent prompts and specialist specs may reference files in this directory, but should not duplicate their contents unless a local summary is operationally necessary.

## Sample configuration bundle

This spec also includes a sample configuration bundle in:

- `specs/configurations/`

The files in that folder are reference examples for system builders.

They show the intended shape, level of specificity, and operational detail of a valid configuration set.

Those sample files are not the runtime source of truth for agent execution.

They exist so that:

- agent builders can see what a complete configuration package looks like
- adopters have a concrete template to copy or adapt
- the configuration contract remains legible at the spec layer without hard-coding one writer into every specialist spec

---

## Required configuration files

The system currently defines four required shared configuration documents.

Reference examples for each required file exist in `specs/configurations/`.

### 1. `profile.md`

Purpose:

- defines the writer identity
- captures author background, mission, primary topics, and public presence
- gives the system enough context to write in a way that sounds like a real person

This file represents the writer.

It is the primary source for:

- who the author is
- what the author writes about
- why the author writes
- what lived experience or credibility anchors the voice

### 2. `brand-style.md`

Purpose:

- defines the editorial brand system
- establishes voice, tone, language rules, emotional registers, and banned language
- gives review agents a durable standard for brand consistency

This file represents the verbal brand.

It is the primary source for:

- truth-over-hype rules
- tone and voice constraints
- language bans and structural rules
- brand-level editorial checks

### 3. `visual-brand.md`

Purpose:

- defines the visual identity system for generated imagery and visual audits
- establishes palette, mood, abstraction level, and exclusions
- keeps visual output recognizable across pieces and channels

This file represents the visual brand.

It is the primary source for:

- aesthetic direction
- color palette
- image style rules
- forbidden visual patterns

### 4. `READABILITY.md`

Purpose:

- defines the readability standard for drafting and review
- establishes the readability target that content should meet
- gives drafting and auditing agents a shared calibration model

This file represents the readability contract.

It is the primary source for:

- target reading level
- sentence-length expectations
- diction and clarity constraints
- self-audit prompts for simplification

---

## Agent-to-configuration contract

Each specialist agent must consume only the configuration files relevant to its domain.

This keeps the system modular and prevents brand rules, identity rules, and visual rules from becoming entangled.

### `caret`

`caret` is the drafting agent and must always reference:

- `profile.md`
- `brand-style.md`
- `READABILITY.md`

Why:

- `profile.md` tells `caret` who the writer is and what lived perspective the prose should carry
- `brand-style.md` tells `caret` how the prose should sound at the editorial level
- `READABILITY.md` keeps the prose legible, direct, and usable for the intended audience

Required effect:

- drafts should sound like the configured writer, not a generic assistant
- prose should reflect the configured editorial brand
- sentence architecture and diction should stay within the configured readability target

### `mark`

`mark` is the brand and voice reviewer and must always reference:

- `profile.md`
- `brand-style.md`

Why:

- `profile.md` helps `mark` judge whether the draft sounds like the intended author
- `brand-style.md` gives `mark` the explicit editorial rules to enforce

Required effect:

- voice audits should measure fidelity to the configured writer
- editorial reviews should enforce the configured brand without inventing hidden rules

### `prism`

`prism` is the visual strategist and must always reference:

- `visual-brand.md`

Optional supporting context:

- current draft
- relevant brand or editorial context when the article meaning affects visual direction

Why:

- `visual-brand.md` is the source of truth for visual identity and image-prompt constraints

Required effect:

- image prompts should align with the configured visual system
- visual output should remain portable across writers without editing `prism` itself

### Review calibration agents

When readability review is part of the task, agents such as `mark`, `echo`, and `devil` may also reference `READABILITY.md` for calibration.

This is secondary to the `caret` requirement.

The drafting path is where readability must be enforced most directly.

---

## Configuration resolution rules

Agents should resolve shared configuration from the repository-level path:

- `.github/agents/configurations/profile.md`
- `.github/agents/configurations/brand-style.md`
- `.github/agents/configurations/visual-brand.md`
- `.github/agents/configurations/READABILITY.md`

Rules:

- treat these files as canonical shared inputs
- use `specs/configurations/` as the reference model when building or revising agents against this contract
- do not silently substitute unrelated files when one is missing
- if a required configuration file is missing, the agent should say which file is missing and what capability is degraded
- agents may summarize configuration into local state, but the configuration files remain the source of truth

---

## Adoption model

The platform should be adoptable by new writers with minimal prompt editing.

To adapt the system for a new writer or publication:

1. replace the contents of `profile.md` with the new writer identity
2. replace the contents of `brand-style.md` with the new editorial brand
3. replace the contents of `visual-brand.md` with the new visual system
4. adjust `READABILITY.md` if the publication requires a different readability target

The specialist agent prompts should continue to work without structural rewrites.

This separation is a core platform requirement, not an implementation convenience.

---

## Authoring rules for configuration files

Configuration files should be written for maintainability.

They should be:

- explicit rather than poetic
- concrete rather than aspirational
- short enough to scan quickly
- rich enough to be operationally useful to agents
- stable over time, with changes made deliberately

Configuration files should avoid:

- vague brand slogans with no rules behind them
- contradictory voice instructions
- visual descriptions that are purely mood-board language
- readability goals that cannot be operationalized

---

## Platform invariants

- configuration is shared, not duplicated per agent
- author identity is defined in `profile.md`
- editorial brand is defined in `brand-style.md`
- visual brand is defined in `visual-brand.md`
- readability standards are defined in `READABILITY.md`
- `caret` must use profile, brand style, and readability together
- `mark` must use profile and brand style together
- `prism` must use visual brand as its visual source of truth
- adopting writers should be able to customize the platform primarily by editing configuration files

---

## Success criteria

This spec is satisfied when:

- a new writer can adopt the platform by editing configuration documents instead of rewriting agents
- `caret` drafts in the configured writer voice and meets the configured readability bar
- `mark` audits against the configured writer and brand rules
- `prism` produces visuals that follow the configured visual system
- configuration drift is minimized because the shared files are the documented source of truth