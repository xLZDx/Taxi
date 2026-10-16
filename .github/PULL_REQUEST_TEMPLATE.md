# Scope
Story IDs, base SHA, candidate SHA, reasons and changes.

# Risk map
Tenant | Finance truth | Planfix side effects | Approval | Sandbox/live | Privacy | Commercial config.

# Evidence
- [ ] Ruff, pytest and scaffold verifier; exact command/results attached
- [ ] Idempotency/tenancy/financial correctness cases run (if affected)
- [ ] Secrets and real personal/financial fixtures absent
- [ ] Docs/ADR/backlog/RESUME updated
- [ ] Failure/rollback and unauthorized-action paths covered
- [ ] No push to production or privileged side effects

# Limitations / gates
Explicit NOT_RUN tests, open risks, required independent review and approvals. Code approval never means go-live.
