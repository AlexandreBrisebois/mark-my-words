# Adopting Mark My Words (MMW)

> [!TIP]
> This guide is for people who want to use MMW for their own writing but branded under their own name and style.

## 1. Installation
1. Clone this repository.
2. Open the folder in VS Code.
3. Ensure you have the **GitHub Copilot** extension installed.
4. (Optional) If you prefer agents, confirm `copilot/agents/` is enabled; if you prefer skills, confirm `copilot/skills/` is enabled.

## 2. Choose your mode
- Option A: Agents (`copilot/agents/`). If you want the full, bundled behavior in one `@mmw` persona.
- Option B: Skills (`copilot/skills/`). If you prefer slash commands (`@mmw /mark`, `@mmw /devil`).
- Optional: keep both, then delete the folder you are not using to avoid ambiguity.

## 3. Personalization (The 5-Minute Rebrand)
MMW separates your personal identity from the editorial core. To make it yours, edit your profile + brand templates in your chosen mode.

### Option A: Agents
Open and edit these files:
- `copilot/agents/configurations/profile.md`
- `copilot/agents/configurations/brand-style.md`
- `copilot/agents/configurations/READABILITY.md`
- `copilot/agents/configurations/visual-brand.md`

### Option B: Skills
Open and edit these files:
- `copilot/skills/profile.md`
- `copilot/skills/brand-style.md`
- `copilot/skills/READABILITY.md`
- `copilot/skills/visual-brand.md`

Point edits:
- `Name`: your full name
- `Primary Website/Blog`: your URL
- `Primary Topic`: your content focus
- `Origin Story`: your brief author background
- `Voice + Tone`: your brand personality (e.g., Calm Signal, Corporate Professional, Excited Entrepreneur)

## 4. How it Works (Under the Hood)
- Shared profile/style files are loaded at each run; updates apply instantly.
- Agent mode (`@mmw`): the `copilot/agents` bundle resolves its `configurations/` path for auditing, copyediting, etc.
- Skill mode (`@mmw /<skill>`): named skills resolve from `copilot/skills/` and read shared resource files.
- Readability audits (`mark`, `devil`, `echo`) use `READABILITY.md` standards.
- Visual and brand checks (`press`, `prism`) use `visual-brand.md` and `brand-style.md`.

## 5. Run Your First Audit
1. Open a markdown draft.
2. In Copilot Chat:
   - Agents example: `@mmw audit this draft for clarity and voice` (or `@mmw /mark audit this for me` if your setup supports slash command fallback).
   - Skills example: `@mmw /mark audit this for me` or `@mmw /devil find weak claims`.
3. Review feedback and optionally edit the source files in `copilot/agents` or `copilot/skills` to refine tone and rules.
4. If you have both directories, delete the one you are not using to avoid duplicate behavior:
   - `rm -rf copilot/agents` or `rm -rf copilot/skills`.

---
> **Migration note:** If you previously used `skills/github-copilot/*`, switch to the current `copilot/agents/*` or `copilot/skills/*` paths.

**Happy Writing!**
