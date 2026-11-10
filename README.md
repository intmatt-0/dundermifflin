# <img src="assets/logo.svg" width="36" height="36" align="center" /> Dunder Mifflin — Multi-Agent SDD Construction Firm (`dundermifflin`)

A Spec-Driven Development (SDD) multi-agent software construction firm plugin for **Google Antigravity**, modeled after *The Office* sitcom characters. It transforms any project specification Markdown file (`SPEC.md`) into production software through 5 role-isolated specialist subagents, 3 mandatory User Quality-Check Gates, and a live 8-bit pixel-art **Visual Task Progress Board** (`dundermifflin-board.html`).

---

## Crew Roster & Slash Commands

| Pixel Icon | Slash Skill | Character & Subagent ID | Role | Strict Domain Ownership |
| :---: | :--- | :--- | :--- | :--- |
| <img src="assets/michael.svg" width="44" height="44" /> | **`/dundermifflin`** | **Michael Scott** *(Foreman)* | Regional Manager & Orchestrator | Reads your `SPEC.md`, runs Stages 1–3 & Quality-Check Gates 1–3, updates the live Visual Task Progress Board |
| <img src="assets/toby.svg" width="44" height="44" /> | **`/toby`** | **`toby`** *(Toby Flenderson)* | Planner & Spec Definer | `.firm/01-spec-plan.md` only (locks Surface Profile A/B/C, cuts unrequested bloat into Non-Goals, writes `Given/When/Then` criteria) |
| <img src="assets/jim.svg" width="44" height="44" /> | **`/jim`** | **`jim`** *(Jim Halpert)* | UX Designer | `.firm/02-ux-design.md` + UX flow/state behavior only (maps 4-State Matrix: Ideal, Loading, Empty, Error) |
| <img src="assets/andy.svg" width="44" height="44" /> | **`/andy`** | **`andy`** *(Andy Bernard)* | UI Designer | `.firm/03-ui-design.md` + CSS/theme/UI styling files only (typography scale, WCAG tokens, anti-slop rules) |
| <img src="assets/dwight.svg" width="44" height="44" /> | **`/dwight`** | **`dwight`** *(Dwight Schrute)* | Software Architect | `.firm/04-architecture.md` + schema/contract/config files only (locks file tree, strict schemas, Law 4 Ponytail/YAGNI minimalism) |
| <img src="assets/darryl.svg" width="44" height="44" /> | **`/darryl`** | **`darryl`** *(Darryl Philbin)* | Warehouse Lead & Software Engineer | Production code & tests + `.firm/05-build-log.md` (implements strictly from `.firm/01`–`04` with zero `TODO` stubs) |

---

## Features

- **Adaptive Surface Profiles (`FRAMEWORK.md`)**:
  - **Profile A (Full-Stack / UI App)**: Runs all 5 specialists (`Toby → Jim + Andy + Dwight → Darryl`).
  - **Profile B (CLI / Developer Tool)**: Runs `Toby → Jim (CLI UX) + Dwight → Darryl` (skips Andy's visual UI layer).
  - **Profile C (Headless API / Worker / Library)**: Runs `Toby → Dwight → Darryl` (skips UI/UX layers).
- **3 Mandatory User Quality-Check Gates**:
  - **Gate 1**: Review & approve Toby's `.firm/01-spec-plan.md`.
  - **Gate 2**: Review & approve Jim, Andy, and Dwight's `.firm/02`–`04` blueprints.
  - **Gate 3**: Review & approve Darryl's live verification and `.firm/05-build-log.md`.
- **8-Bit Animated Visual Task Progress Board (`templates/dundermifflin-board.html`)**:
  - Embedded custom 5x7 TrueType pixel font (`DunderPixel`), animated 16x16 character sprites, marching pixel progress bars, blinking status LEDs, and interactive stage filters.

---

## Installation

### Option 1: One-Command PowerShell Install
```powershell
git clone https://github.com/intmatt-0/dundermifflin.git
cd dundermifflin
pwsh -ExecutionPolicy Bypass -File ./install.ps1
```

### Option 2: Direct Clone into Antigravity Plugins
```bash
git clone https://github.com/intmatt-0/dundermifflin.git ~/.gemini/config/plugins/dundermifflin
```

---

## Repository Structure

```text
dundermifflin/
├── plugin.json                        # Antigravity plugin manifest
├── FRAMEWORK.md                       # Adaptive Surface Profile router & 5 Anti-Slop Laws
├── install.ps1                        # Cross-machine installer script
├── agents/                            # Pre-registered specialist subagents
│   ├── toby.md
│   ├── jim.md
│   ├── andy.md
│   ├── dwight.md
│   └── darryl.md
├── assets/                            # Animated 16x16 pixel-art SVG sprites
│   ├── logo.svg
│   ├── michael.svg
│   ├── toby.svg
│   ├── jim.svg
│   ├── andy.svg
│   ├── dwight.svg
│   └── darryl.svg
├── skills/                            # Global slash skills (/dundermifflin, /toby, /jim, /andy, /dwight, /darryl)
│   ├── dundermifflin/SKILL.md
│   ├── toby/SKILL.md
│   ├── jim/SKILL.md
│   ├── andy/SKILL.md
│   ├── dwight/SKILL.md
│   └── darryl/SKILL.md
├── templates/
│   └── dundermifflin-board.html       # Self-contained animated pixel-font Visual Task Progress Board
├── docs/
│   ├── dev-firm-design.md             # System architecture & design specification
│   └── dev-firm-plan.md               # Implementation plan
└── scripts/
    ├── test-dundermifflin.ps1         # 22-file contract verification suite
    └── make_pixel_font.py             # Embedded 5x7 TrueType pixel font generator
```
