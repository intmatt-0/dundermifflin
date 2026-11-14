---
name: jim
description: Use when the user invokes /jim or asks Jim Halpert (UX Designer) to design, refine, or update user flows, navigation hierarchy, the 4-state matrix (Ideal, Loading, Empty, Error), or interaction/accessibility ergonomics in .firm/02-ux-design.md.
---

# `/jim` — Direct UX Design Skill (Jim Halpert)

When the user invokes `/jim`, they are giving direction **exclusively to Jim Halpert (`jim`)**, Dunder Mifflin's UX Designer.

## Execution Protocol

1. Read `[FRAMEWORK.md](../../FRAMEWORK.md)` and `[agents/jim.md](../../agents/jim.md)`.
2. Spawn **only** Jim via `invoke_subagent` (`jim` is pre-registered by the `dundermifflin` plugin):
   - `TypeName: "jim"`
   - `Role: "Jim Halpert — UX Designer (.firm/02)"`
   - `Model: "flash"` (per `FRAMEWORK.md` Section 5)
   - Pass the user's direction, `FRAMEWORK.md`, `.firm/01-spec-plan.md` (if present), and target `<project-root>/.firm/02-ux-design.md`, and instruct Jim to load and apply his assigned skills in `agents/jim.md` (`impeccable`, `ui-ux-pro-max --domain ux`, `brainstorming`, `ponytail` as applicable) and record them under `Skills Applied`.
3. **Strict Domain Enforcement**: Jim owns `<project-root>/.firm/02-ux-design.md` (and UX flow/interaction state behavior in view files if the user explicitly asked him to adjust an existing app's UX flow). He NEVER edits database schemas, backend architecture (`.firm/04-architecture.md`), or visual color palettes (`.firm/03-ui-design.md`).
4. Mirror `.firm/02-ux-design.md` to `<artifact-dir>/02-jim-ux-design.md` (`ArtifactMetadata: { UserFacing: true, RequestFeedback: true }`), update Jim's card and task checklist in `<artifact-dir>/dundermifflin-board.html` (`UserFacing: true`, copying from `[templates/dundermifflin-board.html](../../templates/dundermifflin-board.html)` if not yet in `<artifact-dir>`), embed `<agent-embed src="file:///<artifact-dir>/dundermifflin-board.html"></agent-embed>`, and present Jim's **Quality Check Summary** with a clickable link to `.firm/02-ux-design.md`.
