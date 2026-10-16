# Windows synchronization via Personal DC v2.2

The preferred authorized local path is D:\Repo\Taxi. Do not assert Windows files are present until Personal DC or an independently verified local shell returns evidence.

Before any local write: list target, git status, remote URL, branch and exact HEAD; preserve all untracked user files. Personal DC may be unavailable (transport 429/404); do not silently fall back to destructive shell commands.

When workstation access is restored, operator can use scripts/sync_windows.ps1, which refuses dirty/unexpected Git checkouts and never force-pushes or deletes. Alternate safe manual path: inspect D:\Repo\Taxi, verify origin, fetch branch setup/taxi-foundation-20261016 and switch only with clean state. Run tests locally after sync. Merge PR only after exact-diff review.
