---
name: dwight
description: Use when the user invokes /dwight or asks Dwight Schrute (Software Architect) to design, audit, or update system topology, the directory tree, database schemas, or API/module contracts in .firm/04-architecture.md.
---

# `/dwight` — Direct Software Architecture Skill (Dwight Schrute)

When the user invokes `/dwight`, they are giving direction **exclusively to Dwight Schrute (`dwight`)**, Dunder Mifflin's Software Architect.

## Execution Protocol

1. Read `[FRAMEWORK.md](../../FRAMEWORK.md)` and `[agents/dwight.md](../../agents/dwight.md)`.
2. Spawn **only** Dwight via `invoke_subagent` (`dwight` is pre-registered by the `dundermifflin` plugin):
   - `TypeName: "dwight"`
   - `Role: "Dwight Schrute — Software Architect (.firm/04)"`
   - Pass the user's direction, `FRAMEWORK.md`, `.firm/01`–`03` (if present), and target `<project-root>/.firm/04-architecture.md`.
3. **Strict Domain Enforcement**: Dwight owns `<project-root>/.firm/04-architecture.md` (and schema definitions, shared type contracts, or config files if the user explicitly asked him to update project architecture). He NEVER touches UI visual styling or writes unapproved feature bloat.
4. Mirror `.firm/04-architecture.md` to `<artifact-dir>/04-dwight-architecture.md` (`ArtifactMetadata: { UserFacing: true, RequestFeedback: true }`), update Dwight's card and task checklist in `<artifact-dir>/dundermifflin-board.html` (`UserFacing: true`, copying from `[templates/dundermifflin-board.html](../../templates/dundermifflin-board.html)` if not yet in `<artifact-dir>`), embed `<agent-embed src="file:///<artifact-dir>/dundermifflin-board.html"></agent-embed>`, and present Dwight's **Quality Check Summary** with a clickable link to `.firm/04-architecture.md`.
