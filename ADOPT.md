# Adopting Mark My Words (MMW)

> [!TIP]
> This guide is for people who want to use MMW for their own writing but branded under their own name and style.

## 1. Installation
1. Clone this repository.
2. Open the folder in VS Code.
3. Ensure you have the **GitHub Copilot** extension installed.

## 2. Personalization (The 5-Minute Rebrand)
MMW separates your personal identity from the editorial core. To make it yours:

### STEP 1: Update Your Profile
Open `skills/github-copilot/profile.md` and update the following:
- `Name`: Your full name.
- `Primary Website/Blog`: Your URL.
- `Primary Topic`: What you usually write about.
- `Origin Story`: A brief background to provide context for the AI.

### STEP 2: Optional Style Adjustment
Open `skills/github-copilot/brand-style.md`. The default is the **"Calm Signal"** aesthetic (Reflective, Expert-Vulnerable, Minimalist). If your brand is different (e.g., "Corporate Professional" or "Excited Entrepreneur"), update the description and language rules here.

## 3. How it Works (Under the Hood)
Each skill (e.g., `@mmw /mark`) is instructed to read `profile.md` and `brand-style.md` at the start of every session. This means:
- The AI adopts your voice without you having to re-prompt it.
- Hugo frontmatter (via `@mmw /press`) uses your name automatically.
- Token usage is optimized because these shared context files are cached by Copilot.

## 4. Run Your First Audit
1. Open a markdown draft.
2. In Copilot Chat, type: `@mmw /mark audit this for me.`
3. Observe how the feedback respects *your* profile and *your* brand rules.

---
**Happy Writing!**
