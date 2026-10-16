# Safe Windows sync helper: no deletion, forced updates or overwrite of dirty worktree.
param(
    [string] $Target = "D:\Repo\Taxi",
    [string] $Branch = "setup/taxi-foundation-20261016"
)
$ErrorActionPreference = "Stop"
$Remote = "https://github.com/xLZDx/Taxi.git"
$Parent = Split-Path -Parent $Target
if (-not (Test-Path $Parent)) { throw "Parent directory not found: $Parent" }

if (-not (Test-Path $Target)) {
    git clone --branch $Branch --single-branch $Remote $Target
    if ($LASTEXITCODE -ne 0) { throw "Clone failed" }
    Write-Host "Cloned $Branch at $Target"
    return
}
if (-not (Test-Path (Join-Path $Target ".git"))) {
    throw "Target exists but is not a Git checkout: $Target. Manual inspection required."
}
$ActualRemote = (git -C $Target remote get-url origin).Trim()
if ($LASTEXITCODE -ne 0 -or $ActualRemote -notmatch "xLZDx/Taxi(\.git)?$") {
    throw "Unexpected origin remote: $ActualRemote"
}
$Dirty = git -C $Target status --porcelain
if ($LASTEXITCODE -ne 0 -or $Dirty) { throw "Dirty checkout: no fetch/switch performed" }
git -C $Target fetch origin $Branch
if ($LASTEXITCODE -ne 0) { throw "Fetch failed" }
git -C $Target switch $Branch
if ($LASTEXITCODE -ne 0) { throw "Checkout failed; inspect branch state manually" }
Write-Host "Branch ready. Confirm git status/log before local work."
