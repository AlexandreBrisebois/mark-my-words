# Project Agent — Claude Project Sync Tools

The **Project Agent** is a standalone Claude agent designed to manage synchronization between your local workspace and a Claude Project. It provides a simple, slash-command interface for initializing your environment and pushing/pulling files.

All synchronization is rooted in the **project/** directory at the root of your workspace.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r scripts/claude-project-tools/requirements.txt
   ```

2. **Initialize the Agent**:
   Run the following command in your Claude session to set up your sessionKey and link your local folder to a Claude Project:
   ```
   /project:init
   ```
   Follow the interactive prompts to retrieve your `sessionKey` from your browser.

## Commands

The Project Agent responds to the following commands:

### `/project:init`
Guided setup to link your workspace to a Claude Project. It creates the required `.claude/config.json` and ensures the local `project/` directory is ready.

### `/project:push [files...]`
Uploads files from your local `project/` directory to the Claude Project. 
- If no files are specified, the agent will attempt to push all files in the `project/` folder.
- Example: `/project:push test.txt`

### `/project:pull [files...]`
Downloads files from the Claude Project to your local `project/` directory.
- Example: `/project:pull code-review.md`

## CLI Usage

While the Agent is the primary interface, you can also run the underlying scripts directly from your terminal:

```bash
# Push files (paths relative to the 'project/' root)
python3 scripts/claude-project-tools/project_sync.py push project/test.txt

# Pull files
python3 scripts/claude-project-tools/project_sync.py pull test.txt
```

---

> [!CAUTION]
> **Authentication Security**: The `.claude/config.json` contains your `sessionKey`, which grants full access to your Claude account. This file should **never** be committed to Git. The init script adds this to your `.gitignore` automatically.
