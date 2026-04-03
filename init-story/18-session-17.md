## Session 17 — The Standalone Project Agent: Infrastructure Decoupled (add to the story)

The work done on the sync layer wasn't lost. It was just in the wrong place. We realized that the ability to link a local folder to a Claude Project is a universal utility, not an MMW feature.

The design decision: extract the sync logic, generalize it, and rebirthe it as a standalone **Project Agent**.

### What was built

We moved the sync tools to `scripts/claude-project-tools/` and created a new, dedicated agent: **Project**. It responds to three simple commands:
- `/project:init` — Links the workspace and creates the session context.
- `/project:push` — Uploads the contents of a local `project/` directory to the cloud.
- `/project:pull` — Downloads the cloud state back to the local `project/` directory.

### Why it matters (for the story)

This is a story of "Separation of Concerns." By moving the sync infrastructure into its own agent and its own folder, we decoupled the "Writing Room" (MMW) from the "Sync Layer" (Project Agent). 

MMW stays clean, focused purely on the craft of writing. The Project Agent stays focused on the mechanics of workspace synchronization. If the sync logic ever needs to change — or if we want to use it for a different project entirely — we can do so without touching a single line of MMW logic.

It proves that the best systems aren't monolithic; they are a collection of specialized tools that know how to stay out of each other's way.

---