# Dunder Mifflin (dundermifflin) Plugin Installer for Antigravity
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$userHome = ($HOME -replace '\\', '/')
$targetDir = "$userHome/.gemini/config/plugins/dundermifflin"

Write-Host "Installing Dunder Mifflin plugin to $targetDir ..." -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

$folders = @("agents", "assets", "skills", "templates")
foreach ($folder in $folders) {
    Copy-Item -Recurse -Force "$repoRoot/$folder" "$targetDir/"
}
Copy-Item -Force "$repoRoot/plugin.json" "$targetDir/plugin.json"
Copy-Item -Force "$repoRoot/FRAMEWORK.md" "$targetDir/FRAMEWORK.md"
Copy-Item -Force "$repoRoot/README.md" "$targetDir/README.md"

# Rewrite plugin root path in markdown files for current machine's $HOME
Get-ChildItem -Recurse -File $targetDir -Include "*.md" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $updated = $content -replace 'C:/Users/[^/]+/\.gemini/config/plugins/dundermifflin', $targetDir
    if ($content -ne $updated) {
        Set-Content -Path $_.FullName -Value $updated -NoNewline
    }
}

Write-Host "Dunder Mifflin installed! Available slash skills: /dundermifflin, /toby, /jim, /andy, /dwight, /darryl" -ForegroundColor Green
