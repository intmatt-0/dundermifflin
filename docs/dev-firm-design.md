# Design Doc: `dundermifflin` Software Construction Firm Plugin

## 1. Intent & Why

Your software construction firm is now **Dunder Mifflin (`dundermifflin`)**. Instead of one generic AI reading your Project Spec `.md` and producing "AI slop," **Michael Scott** (`/dundermifflin`, the Regional Manager / Foreman) reads your **Project Spec `.md`** alongside the firm's adaptive **`FRAMEWORK.md`** and dispatches five specialized employees from *The Office* (`toby`, `jim`, `andy`, `dwight`, `darryl`).

You can either:
1. Run **`/dundermifflin`** at the start of a project to run the full Spec-Driven Development (SDD) pipeline with **Quality Check Gates 1–3** and a live **Visual Task Progress Board** (`dundermifflin-board.html`).
2. Or call any individual employee directly via their slash skill (**`/toby`**, **`/jim`**, **`/andy`**, **`/dwight`**, **`/darryl`**) to give targeted direction—only that character wakes up and edits only their owned blueprint and domain files.

---

## 2. The Dunder Mifflin Roster & Slash Skills

| Slash Skill | Character & Subagent ID | Role in the Firm | Blueprint Owned | Domain Files Owned When Called Directly |
| :--- | :--- | :--- | :--- | :--- |
| **`/dundermifflin`** | **Michael Scott** (Foreman) | **Regional Manager** — Orchestrates the 5 specialists, updates the Visual Task Progress Board, and enforces Quality Checks 1–3 | All `.firm/01`–`05` (via subagents) | Never edits product code directly |
| **`/toby`** | **`toby`** (Toby Flenderson) | **Planner & Spec Definer** — Scope compliance, cuts bloat (`Non-Goals`), testable acceptance criteria, trust boundaries | `.firm/01-spec-plan.md` | `.firm/01-spec-plan.md` only |
| **`/jim`** | **`jim`** (Jim Halpert) | **UX Designer** — User journeys, navigation hierarchy, 4-state matrix (Ideal, Loading, Empty, Error), keyboard/CLI/API ergonomics | `.firm/02-ux-design.md` | `.firm/02-ux-design.md` + UX flow/state behavior only |
| **`/andy`** | **`andy`** (Andy Bernard) | **UI Designer** — Visual persona, typography scale, semantic color tokens, spacing grid, component visuals (zero AI slop) | `.firm/03-ui-design.md` | `.firm/03-ui-design.md` + CSS/theme/token/UI styling files only |
| **`/dwight`** | **`dwight`** (Dwight Schrute) | **Software Architect** — System topology, exact file tree, data schemas, API contracts, YAGNI/Ponytail minimalism | `.firm/04-architecture.md` | `.firm/04-architecture.md` + schema/contract/config files only |
| **`/darryl`** | **`darryl`** (Darryl Philbin) | **Software Engineer** — Warehouse Lead who builds & verifies production code strictly from `.firm/01`–`04` (zero `TODO` stubs) | `.firm/05-build-log.md` | Production source/test files + `.firm/05-build-log.md` |

---

## 3. Visual Task Progress & Pixel-Art Character Icons

1. **Sidebar Subagent Tracking**: Every `invoke_subagent` call passes the character's full name and role in `Role` (e.g., `"Toby Flenderson — Spec Planner (.firm/01)"`, `"Jim Halpert — UX Designer (.firm/02)"`, `"Andy Bernard — UI Designer (.firm/03)"`, `"Dwight Schrute — Software Architect (.firm/04)"`, `"Darryl Philbin — Software Engineer (.firm/05)"`) so they appear clearly in the Antigravity **Subagents** sidebar panel.
2. **Custom 16x16 Pixel-Art Icons**: Crisp SVG pixel-art portraits (`shape-rendering="crispEdges"`) for **Michael**, **Toby**, **Jim**, **Andy**, **Dwight**, and **Darryl** live in `assets/` and are embedded directly inside the Visual Task Progress Board.
3. **Interactive Visual Task Progress Board (`dundermifflin-board.html`)**:
   - Stored as a reusable template at `~/.gemini/config/plugins/dundermifflin/templates/dundermifflin-board.html`.
   - Whenever `/dundermifflin` or an individual character skill (`/toby`, `/jim`, `/andy`, `/dwight`, `/darryl`) runs, it copies/updates `dundermifflin-board.html` in the conversation's artifact directory (`UserFacing: true`) and embeds it inline via `<agent-embed>`.
   - Displays:
     - **Whole-Firm Progress Bar** (`0%`–`100%`), current Stage, Surface Profile badge (`Profile A / B / C`), and Quality Check gate status.
     - **Per-Agent Cards** with each character's pixel-art portrait, role badge, `/slash` command tag, individual progress bar (`0%`–`100%`), live status pill (`IDLE`, `WORKING`, `QUALITY CHECK`, `APPROVED`), and task checklist items.

---

## 4. Plugin Directory Structure

```text
~/.gemini/config/plugins/dundermifflin/
├── plugin.json                         # Plugin manifest (name: dundermifflin)
├── README.md                           # User-facing documentation
├── FRAMEWORK.md                        # Master Adaptive Construction Playbook & Anti-Slop Laws
├── assets/
│   ├── logo.svg                        # Dunder Mifflin pixel logo (Michael Scott)
│   ├── michael.svg                     # Michael Scott 16x16 pixel icon
│   ├── toby.svg                        # Toby Flenderson 16x16 pixel icon
│   ├── jim.svg                         # Jim Halpert 16x16 pixel icon
│   ├── andy.svg                        # Andy Bernard 16x16 pixel icon
│   ├── dwight.svg                      # Dwight Schrute 16x16 pixel icon
│   └── darryl.svg                      # Darryl Philbin 16x16 pixel icon
├── templates/
│   └── dundermifflin-board.html        # Interactive Generative UI Visual Task Progress Board
├── agents/
│   ├── toby.md                         # Pre-registered Toby subagent
│   ├── jim.md                          # Pre-registered Jim subagent
│   ├── andy.md                         # Pre-registered Andy subagent
│   ├── dwight.md                       # Pre-registered Dwight subagent
│   └── darryl.md                       # Pre-registered Darryl subagent
└── skills/
    ├── dundermifflin/SKILL.md          # /dundermifflin — Michael Scott Foreman orchestrator
    ├── toby/SKILL.md                   # /toby — Direct Spec & Planning skill
    ├── jim/SKILL.md                    # /jim — Direct UX Design skill
    ├── andy/SKILL.md                   # /andy — Direct UI Design skill
    ├── dwight/SKILL.md                 # /dwight — Direct Software Architecture skill
    └── darryl/SKILL.md                 # /darryl — Direct Software Engineering skill
```
