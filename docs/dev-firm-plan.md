# `dundermifflin` Plugin & Visual Progress Board Implementation Plan

**Goal:** Package the `dundermifflin` plugin at `C:/Users/Lenovo/.gemini/config/plugins/dundermifflin/` with 6 pixel-art Office character icons, an interactive HTML Visual Task Progress Board (`dundermifflin-board.html`), 5 pre-registered character subagents (`toby`, `jim`, `andy`, `dwight`, `darryl`), and 6 slash skills (`/dundermifflin`, `/toby`, `/jim`, `/andy`, `/dwight`, `/darryl`).

**Spec:** `C:/Users/Lenovo/.gemini/antigravity/brain/940969f1-7de6-4fc9-83cc-939d9202c499/dev-firm-design.md`

---

### Task 1: Pixel-Art Character Icons & Visual Task Progress Board (`assets/*.svg` + `templates/dundermifflin-board.html`)

- [ ] Create `assets/michael.svg`, `assets/toby.svg`, `assets/jim.svg`, `assets/andy.svg`, `assets/dwight.svg`, `assets/darryl.svg`, and `assets/logo.svg` in `C:/Users/Lenovo/.gemini/config/plugins/dundermifflin/assets/`.
- [ ] Create `C:/Users/Lenovo/.gemini/config/plugins/dundermifflin/templates/dundermifflin-board.html` following `generative_ui` rules (allowlisted Tailwind script, semantic CSS variables `--card`, `--foreground`, `--muted-foreground`, `--border`, minimum `12px`/`text-xs` typography, no viewport height classes, embedded pixel-art SVGs, whole-firm progress bar, per-agent progress cards, and editable `window.DUNDER_MIFFLIN_STATE` JSON state object).
- [ ] Copy `dundermifflin-board.html` into the current conversation's artifact directory (`C:/Users/Lenovo/.gemini/antigravity/brain/940969f1-7de6-4fc9-83cc-939d9202c499/dundermifflin-board.html`) with `UserFacing: true` so the user can view and interact with it immediately.

### Task 2: Plugin Manifest, `FRAMEWORK.md`, & 5 Character Agent Prompts (`agents/*.md`)

- [ ] Create `C:/Users/Lenovo/.gemini/config/plugins/dundermifflin/plugin.json` and `README.md`.
- [ ] Create `C:/Users/Lenovo/.gemini/config/plugins/dundermifflin/FRAMEWORK.md` mapping the 5 Office characters (`toby`, `jim`, `andy`, `dwight`, `darryl`) to the Surface Adaptation Matrix, Anti-Slop Laws 1–5, `.firm/01`–`05` blueprints, and Visual Progress Board updates.
- [ ] Create `agents/toby.md`, `agents/jim.md`, `agents/andy.md`, `agents/dwight.md`, and `agents/darryl.md` with strict role boundaries, domain file ownership rules (for when called directly via `/toby`, `/jim`, `/andy`, `/dwight`, `/darryl`), and `.firm/01`–`05` output templates.

### Task 3: The 6 Slash Skills (`/dundermifflin`, `/toby`, `/jim`, `/andy`, `/dwight`, `/darryl`) & Verification

- [ ] Create `skills/dundermifflin/SKILL.md` (Michael Scott Foreman orchestrator that dispatches `toby`, `jim`, `andy`, `dwight`, `darryl`, updates `dundermifflin-board.html`, and enforces Quality Checks 1–3).
- [ ] Create `skills/toby/SKILL.md`, `skills/jim/SKILL.md`, `skills/andy/SKILL.md`, `skills/dwight/SKILL.md`, and `skills/darryl/SKILL.md` so calling `/jim <direction>` (or any character) dispatches ONLY that character subagent to edit ONLY their owned `.firm/` blueprint and domain files, updates that character's card on `dundermifflin-board.html`, and reports a Quality Check summary.
- [ ] Remove legacy `C:/Users/Lenovo/.gemini/config/skills/dev-firm/` directory and run `test-dundermifflin.ps1` to verify all files, frontmatters, pixel icons, visual board, and plugin registration via `GetAllPlugins`.
