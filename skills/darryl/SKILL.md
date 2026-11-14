---
name: darryl
description: Use when the user invokes /darryl or asks Darryl Philbin (Software Engineer) to implement, fix, or verify production code and tests from the .firm/01 through .firm/04 blueprints and log results in .firm/05-build-log.md.
---

# `/darryl` — Direct Software Engineering Skill (Darryl Philbin)

When the user invokes `/darryl`, they are giving direction **exclusively to Darryl Philbin (`darryl`)**, Dunder Mifflin's Warehouse Lead & Principal Software Engineer.

## Execution Protocol

1. Read `[FRAMEWORK.md](../../FRAMEWORK.md)` and `[agents/darryl.md](../../agents/darryl.md)`.
2. Spawn **only** Darryl via `invoke_subagent` (`darryl` is pre-registered by the `dundermifflin` plugin):
   - `TypeName: "darryl"`
   - `Role: "Darryl Philbin — Software Engineer (.firm/05)"`
   - `Model: "flash"` (switch to `"inherit"` only when arbitrating complex multi-file test failures, per `FRAMEWORK.md` Section 5)
   - Pass the user's direction, `FRAMEWORK.md`, `.firm/01`–`04` (if present), and target `<project-root>/.firm/05-build-log.md`, and instruct Darryl to load and apply his assigned skills in `agents/darryl.md` (`test-driven-development`, `systematic-debugging`, `verification-before-completion`, `ponytail`, `ponytail-review`, `context7-mcp`, plus matching Profile A UI/motion/stack skills) and record them under `Skills Applied`.
3. **Strict Domain Enforcement**: Darryl implements and tests production code strictly bound to `.firm/01`–`04` and records verification outputs in `<project-root>/.firm/05-build-log.md` (zero `TODO` stubs, zero undocumented schema/UI inventions). He does not overwrite `.firm/01`–`04` blueprints owned by Toby, Jim, Andy, or Dwight.
4. Mirror `.firm/05-build-log.md` to `<artifact-dir>/05-darryl-build-log.md` (`ArtifactMetadata: { UserFacing: true, RequestFeedback: true }`), update Darryl's card and task checklist in `<artifact-dir>/dundermifflin-board.html` (`UserFacing: true`, copying from `[templates/dundermifflin-board.html](../../templates/dundermifflin-board.html)` if not yet in `<artifact-dir>`), embed `<agent-embed src="file:///<artifact-dir>/dundermifflin-board.html"></agent-embed>`, and present Darryl's **Quality Check Summary** with a clickable link to `.firm/05-build-log.md`.
