# Session 1: Emergence and Naming

**Status**: Original design session  
**Topics**: How it started, building the roster, naming, design philosophy

---

## The Brief

This post documents the real-time design process behind Mark My Words — a multi-agent writing system built to help me produce better, more intentional blog content. The system was not designed in advance. It emerged through a conversation, decision by decision, until it had a name, a roster, a workflow, and a philosophy.

The post should capture that emergence. Not the final architecture. The thinking behind it.

---

## How It Started

It started with a simple problem: I needed a name for an editor agent. Something short, memorable, and different from "Editor."

From that small constraint, ten names became twenty. From twenty, one landed: **Caret** — the typographic editing symbol `^`. It felt right because it was niche, editorial, and had a double meaning.

That instinct — find the name with the most layers — became the design principle for everything that followed.

---

## Building the Roster

Once Caret existed, the question became: what else does a writer need?

The first answer was a writing room. Not one agent doing everything, but a room of specialists — each covering a distinct discipline that would otherwise live only in the writer's head or get skipped under time pressure.

The roster built itself through a series of honest questions:

**What roles am I missing?** The first pass had a writer, an editor, a brand agent, a critique agent, and a researcher. The gaps that emerged: a publisher, a headline agent, an audience proxy, an archivist, a scheduler. Each gap revealed something the writer unconsciously depends on but rarely makes explicit.

**Should I merge or keep separate?** Echo (Audience) and Devil (Critique) looked like the same role. They weren't. Devil challenges the writer — adversarial, inward-facing. Echo challenges the connection to the reader — empathetic, outward-facing. One asks "is this good writing?" The other asks "will this land?" Merging them would have lost that distinction.

**What did I already have?** Seven GitHub Copilot prompts from a prior implementation — an accusation audit, a brand voice guide, a content writer, a brand strategist, an SEO auditor, a blog portfolio auditor, and a visual brand validator. These weren't starting from scratch. They were proven logic that needed a new home.

---

## The Names

Every agent got a name through the same filter: short, memorable, layered. The naming process itself became part of the design.

| Agent | Name | Why It Works |
|---|---|---|
| Writer + Orchestrator | Caret | Typographic editing symbol `^` |
| Brand + Voice | Mark | Hallmark, benchmark, the brand agent marks the work |
| Strategist | Compass | Sets direction before anyone moves |
| Critique | Devil | Devil's advocate — adversarial by design |
| Researcher | Turing | Decodes hidden structure, finds signal in noise |
| Audience | Echo | Reflects the reader's voice back |
| Publisher | Press | The printing press, the act of committing |
| Archivist | Index | The index at the back of every serious book |
| Scheduler | Cadence | The rhythm of consistent publishing |
| Visual Brand | Prism | Splits the brand into its component parts |

The system name came last. Playing with the agent names as raw material — Caret, Mark, Press, Index — led to typographic heritage, then to the idiom "Mark My Words." It was already there, hiding in the roster. Three letters became the shorthand: **MMW**.

---

## Key Design Decisions

### File-based shared memory

Agents don't pass state through conversation. They read files and write files. Each piece gets a folder. Each agent writes to that folder. The next agent reads what the last one left.

This was a deliberate choice: stateless, inspectable, recoverable. If anything breaks mid-workflow, the files tell you exactly where things stopped. No black box.

### The codename

Every piece gets a codename derived from the brief — descriptive, lowercase, hyphenated, 2-3 words. Not random or evocative. The codename should tell you what the piece is about without opening any files. `writers-room-build`. `brand-pivot-retro`. The archivist can scan them without context.

### Compass before Turing

The strategist runs before the researcher. Research without strategic direction is unfocused. Compass sets the frame — piece type, editorial angle, research priorities — then Turing works within it. Getting this order wrong wastes Turing's most valuable output.

### Index as the first gate

Before any agent does creative work, the archivist checks whether this piece overlaps with something already published. Three outcomes: abandon, differentiate the angle, or proceed knowingly. Duplicate content is a problem that's much easier to catch at the brief stage than after a draft exists.

### The Caret/Mark feedback loop

Mark doesn't just flag problems. It informs the next draft directly. The loop: Caret drafts, Mark reviews, Caret reads the review and revises, Mark re-checks. Maximum two iterations before the circuit breaker fires and surfaces the outstanding issues to the user.

### The research gate

Caret will not start a draft without explicitly confirming that research.md exists and is non-empty. This is not a soft suggestion. If the research isn't there, nothing runs. The other agents are only as good as the ground they stand on.

### Prism owns the image prompt

The GitHub Actions automation previously had Gemini generate its own image prompt. Prism replaces that. Prism reads the finished piece and brand guidelines, then produces a single plain-paragraph prompt for Gemini Image Pro — grounded in the content, consistent with the "Calm Signal" aesthetic. The automation just reads the file. No parsing required.

---

## The Most Important Feature

Co-edit mode was identified as the most human part of the system — the moment the writer's voice actually enters the draft.

The design is intentional: when co-edit is triggered, Caret surfaces the exact lines that need attention, with the current text and the specific issue. Then it steps back. The user edits the draft file directly. Caret waits. No suggestions, no rewrites, no hovering.

When the user signals completion, Caret reads the edited file, integrates any remaining issues it can handle autonomously, produces the next versioned draft, and then reports exactly what it changed beyond the user's edits. If the user's edit contains a banned word, Caret flags it — but does not delete it. The user's voice overrides the brand rules when there is a conflict.

The principle that guided this: the system serves the writer's voice. Everything else is infrastructure.

---

## The Brand Pivot

The system was designed alongside a brand pivot. The prior identity was a multi-cloud engineering brand — srvrlss.dev, Technical Outcome Leader, GCP/AWS/Azure. That identity is not wrong. It's just not current.

The new identity: AI Enthusiast, builder-in-public, honest learner. The audience stays the same — CTOs, engineers, technical leaders. The content shifts: AI agents, building in public, retrospectives, failure and recovery.

Microsoft is origin story, not current identity. The old blog is archive, not content to migrate. srvrlss.dev is a prior chapter. This blog is a fresh start.

Every agent in Mark My Words had its brand references updated before the system was finalized.

---

## What This Post Should Be

This is not a tutorial. It is not a "here are the five steps to build an agent system" post.

It is an honest account of a design process — the questions asked, the decisions made, the things that emerged that weren't planned. The fact that the system name was hiding in the roster all along. The fact that Echo and Devil looked like the same agent until they weren't. The fact that co-edit mode became the most important feature not because of technical complexity but because of what it represents: the writer's voice is the point.

The reader should finish this post with two things: a clear understanding of what Mark My Words is, and a felt sense of how it came to exist. Not the architecture. The thinking.

---

## Suggested Angles for Compass

- **The emergence angle**: Systems designed through conversation rather than specification. What that reveals about how good tools are actually built.
- **The naming angle**: Why naming matters in system design. The names encode the philosophy. Caret is not "Writer." Turing is not "Researcher." The difference matters.
- **The voice angle**: Why co-edit mode is the most important feature in a writing system. What it says about the relationship between automation and authorship.
- **The builder-in-public angle**: The system itself is the first post it will help write. That recursion is worth examining.

---

## Suggested Research Directions for Turing

- Prior art on multi-agent writing systems and editorial workflows
- The history of the writer's room as a creative structure (TV writers' rooms, editorial boards, newsrooms)
- Research on AI-assisted writing and where human voice gets lost
- The accusation audit methodology (borrowed from negotiation practice — Chris Voss, Never Split the Difference)
- Type 1 / Type 2 decision framework (Amazon / Jeff Bezos)
- The "Empty Chair" as a design principle in product and content
- llms.txt as an emerging standard for AI-readable content

---

## Tone Notes for Caret

- First person throughout — this is a personal account, not a technical specification
- Reflective-vulnerable blended with urgently excited
- The system is not finished. It is version one. Say that.
- The design decisions are not perfect. Surface the tradeoffs.
- Do not write this as a success story. Write it as a process story.
- A single-sentence paragraph is a signature move. Use it.
- Close with a question that invites the reader into the conversation — not a summary of what was covered.
