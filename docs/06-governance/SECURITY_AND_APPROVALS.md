# Security and operational approval gates

## Privilege and data
- Tenant isolation enforced at ingress, storage, query and export; tenant_id must come from authenticated context, not caller-controlled request fields.
- Minimum-access service users for Planfix, ERP, accounting and cash feed. No shared administrative credentials for AI.
- Separate live and sandbox credentials/accounts, storage, webhook endpoints and network policy.
- Audit log append-only with actor, purpose, old/new values, source event, approval, timestamp and correlation ID. Protect PII and investor contract terms.
- No raw real driver PII, bank account, credentials, 1C information bases or production API traffic in Git.
- Retention, cross-border transfer and regulatory requirements determined with counsel for the actual jurisdiction.
- Authorized read-only discovery before accessing existing operator systems.

## Protected actions
Requires human review and documented policy: monetary payouts, bank instructions, accounting postings/adjustments, tax filings, critical safety overrides, external data sharing, commercial contract effective model changes and bulk exports. AI may prepare drafts; execution path independently verifies human approval.

## Reliability
Idempotent ingestion and mutation, bounded retry, source-level error surfaces and no silent defaults. Define restart/replay, DLQ manual drain, backup/restore, disaster recovery, and STOP/rollback tests before go-live. A 20% planning buffer does not replace contingency finance capacity.

## Delivery authorization
No production deployment, destructive operations, deletion, forced pushes, paid spend or external AI reviewer invocation without approved decision. Github branch/PR changes are separately reviewed. Approval of source diff is not authorization of deployment, migration or live financial action.

