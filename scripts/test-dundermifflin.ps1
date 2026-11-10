$ErrorActionPreference = "Stop"
$pluginDir = "C:/Users/Lenovo/.gemini/config/plugins/dundermifflin"

$requiredFiles = @(
  "plugin.json",
  "README.md",
  "FRAMEWORK.md",
  "assets/logo.svg",
  "assets/michael.svg",
  "assets/toby.svg",
  "assets/jim.svg",
  "assets/andy.svg",
  "assets/dwight.svg",
  "assets/darryl.svg",
  "templates/dundermifflin-board.html",
  "agents/toby.md",
  "agents/jim.md",
  "agents/andy.md",
  "agents/dwight.md",
  "agents/darryl.md",
  "skills/dundermifflin/SKILL.md",
  "skills/toby/SKILL.md",
  "skills/jim/SKILL.md",
  "skills/andy/SKILL.md",
  "skills/dwight/SKILL.md",
  "skills/darryl/SKILL.md"
)

foreach ($f in $requiredFiles) {
  $p = "$pluginDir/$f"
  if (-not (Test-Path $p)) { throw "Missing file in dundermifflin plugin: $f" }
}

$board = Get-Content "$pluginDir/templates/dundermifflin-board.html" -Raw
foreach ($char in @("michael", "toby", "jim", "andy", "dwight", "darryl", "DUNDER_MIFFLIN_STATE")) {
  if ($board -notmatch $char) { throw "dundermifflin-board.html missing: $char" }
}

foreach ($s in @("dundermifflin", "toby", "jim", "andy", "dwight", "darryl")) {
  $sc = Get-Content "$pluginDir/skills/$s/SKILL.md" -Raw
  if ($sc -notmatch "(?m)^name:\s*$s\s*$") { throw "Skill $s missing name: $s" }
  if ($sc -notmatch "(?m)^description:\s*Use when") { throw "Skill $s description must start with 'Use when'" }
}

Write-Host "DUNDER MIFFLIN VERIFICATION: ALL 22 FILES & CONTRACTS PASS"
