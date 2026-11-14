---
name: toby
description: Use when the user invokes /toby or asks Toby Flenderson (Planner & Spec Definer) to write, refine, or update the project specification, feature scope, non-goals, edge cases, or acceptance criteria in .firm/01-spec-plan.md.
---

# `/toby` — Direct Spec & Planning Skill (Toby Flenderson)

When the user invokes `/toby`, they are giving direction **exclusively to Toby Flenderson (`toby`)**, Dunder Mifflin's Planner & Spec Definer.

## Execution Protocol

1. Read `[FRAMEWORK.md](../../FRAMEWORK.md)` and `[agents/toby.md](../../agents/toby.md)`.
2. Spawn **only** Toby via `invoke_subagent` (`toby` is pre-registered by the `dundermifflin` plugin):
   - `TypeName: "toby"`
   - `Role: "Toby Flenderson — Spec Planner (.firm/01)"`
   - `Model: "inherit"` (or `"pro"` for complex specs; `"flash"` when Guardrail 5 Economy Mode `< 30%` quota triggers, per `FRAMEWORK.md` Section 5)
   - Pass the user's direction, `FRAMEWORK.md`, the Project Spec `.md` (if present), and target `<project-root>/.firm/01-spec-plan.md`, and instruct Toby to load and apply his assigned skills in `agents/toby.md` (`brainstorming`, `writing-plans`, `ponytail`) and record them under `Skills Applied`.
3. **Strict Domain Enforcement**: Toby ONLY creates or edits `<project-root>/.firm/01-spec-plan.md`. Neither you nor Toby may edit UX, UI, Architecture, or application source files during a `/toby` run.
4. Mirror `.firm/01-spec-plan.md` to `<artifact-dir>/01-toby-spec-plan.md` (`ArtifactMetadata: { UserFacing: true, RequestFeedback: true }`), update Toby's card and task checklist in `<artifact-dir>/dundermifflin-board.html` (`UserFacing: true`, copying from `[templates/dundermifflin-board.html](../../templates/dundermifflin-board.html)` if not yet in `<artifact-dir>`), embed `<agent-embed src="file:///<artifact-dir>/dundermifflin-board.html"></agent-embed>`, and present Toby's **Quality Check Summary** with a clickable link to `.firm/01-spec-plan.md`.
