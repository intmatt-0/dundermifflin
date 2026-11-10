---
name: andy
description: Use when the user invokes /andy or asks Andy Bernard (UI Designer) to design, restyle, or update visual direction, typography, semantic color tokens, spacing grids, or component styling in .firm/03-ui-design.md and UI style files.
---

# `/andy` — Direct UI Design Skill (Andy Bernard)

When the user invokes `/andy`, they are giving direction **exclusively to Andy Bernard (`andy`)**, Dunder Mifflin's UI Designer.

## Execution Protocol

1. Read `[FRAMEWORK.md](../../FRAMEWORK.md)` and `[agents/andy.md](../../agents/andy.md)`.
2. Spawn **only** Andy via `invoke_subagent` (`andy` is pre-registered by the `dundermifflin` plugin):
   - `TypeName: "andy"`
   - `Role: "Andy Bernard — UI Designer (.firm/03)"`
   - Pass the user's direction, `FRAMEWORK.md`, `.firm/01-spec-plan.md` and `.firm/02-ux-design.md` (if present), and target `<project-root>/.firm/03-ui-design.md`.
3. **Strict Domain Enforcement**: Andy owns `<project-root>/.firm/03-ui-design.md` (and CSS/Tailwind/theme token and component styling files if the user explicitly asked him to restyle an existing UI). He NEVER edits backend business logic, database schemas, or product scope.
4. Mirror `.firm/03-ui-design.md` to `<artifact-dir>/03-andy-ui-design.md` (`ArtifactMetadata: { UserFacing: true, RequestFeedback: true }`), update Andy's card and task checklist in `<artifact-dir>/dundermifflin-board.html` (`UserFacing: true`, copying from `[templates/dundermifflin-board.html](../../templates/dundermifflin-board.html)` if not yet in `<artifact-dir>`), embed `<agent-embed src="file:///<artifact-dir>/dundermifflin-board.html"></agent-embed>`, and present Andy's **Quality Check Summary** with a clickable link to `.firm/03-ui-design.md`.
