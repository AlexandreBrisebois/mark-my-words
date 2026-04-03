## Session 6 — Where Does the Prompt Live? (add to the story)

After four audits and a collaborative pass, the system was ready to build.
Which raised a question that hadn't been asked yet: where does the build
prompt actually live in the repo?

The file was sitting at the root of `mark-my-words/`. That works for a
session. It doesn't work for a year.

The question was framed as a long-lived repo problem: the prompt needs
to be findable, version-controlled, and distinct from the artifacts it
generates. The build prompt creates `CLAUDE.md`, `ARCHITECTURE.md`,
`.claude/agents/`, and `writers-room/`. If the prompt that generates
those things sits alongside them at root, the source is indistinguishable
from the output.

The answer: `prompts/mmw-claude-code-prompt.md`.

Not `docs/`. Not `specs/`. `prompts/` — because the file is an instruction
to an AI system, and that should be legible from the directory name alone.
The same way `.claude/agents/` signals agent configuration and
`writers-room/` signals content, `prompts/` signals intent: these files
tell the system what to build.

The root is reserved for what MMW produces. `prompts/` holds what makes
MMW reproducible.

### The principle behind it

A build artifact and its source should not share a namespace. The prompt
is source. `CLAUDE.md` is output. Putting them in the same directory is
the same mistake as checking generated code into the same folder as the
generator — it works until you need to rebuild from scratch and can't
tell which files are safe to delete.

The decision is also a commitment: this repo will outlast any single
build of MMW. The prompt stays. The agents can be regenerated. The
directory structure makes that clear by design.

### Additional angle for Compass

- **The source/output separation angle**: In software, you separate source
  from build artifacts. The same discipline applies to prompt systems.
  The file that generates the agents is not the same kind of thing as
  the agents it generates — and the directory structure should say so.

---