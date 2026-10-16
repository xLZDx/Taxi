# Contribution workflow

1. Read AGENTS.md and canonical product/architecture/acceptance documents.
2. Start from exact clean HEAD on an isolated feature branch; record base and candidate SHA.
3. Update a story, ADR or requirement alongside behavior. Keep interfaces testable.
4. Add tests for idempotency, tenant isolation, fail-closed unknown financial facts, commercial-model invariance and time buffer when applicable.
5. Run pytest, Ruff, scaffold verifier and include exact commands/results in PR.
6. For financial/approval/security changes, request independent code/security review of the complete diff.
7. No production deployment, external AI calls, billing, payments, secrets, destructive migration or force push without explicit separate authorization.
8. Document limits with NOT_RUN or NOT_COVERED, never inferred PASS.

GitHub and repo-facing text is English, except the preserved approved historic verbatim wording.
