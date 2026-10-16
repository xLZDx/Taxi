# Architecture — Planfix-first, integration-safe, multi-tenant

Status: target design; no actual deployment.

~~~text
Dispatch / Aggregators / GPS / Banks / Cash / Accounting
            | trusted, scoped adapters
            v
   Integration Gateway (identity, mapping, queues,
   retry, dedup, source timestamps, reconciliation)
            |
       +----+--------------------+
       |                         |
       v                         v
Cash/Finance Intelligence     Planfix Adapter
Business Plans &              (REST / webhook / MCP)
Real Reporting                       |
       |                              v
       +----------------------- Planfix workflows
       |                              |
       v                              v
Admin dashboard / alerting     Tasks, owners, approvals
       |
Commercial Engine + independent Entitlements
       |
Tenant isolation + provenance + audit throughout
~~~

## Bounded contexts
- Integration: connector interface, auth scopes, ingestion journal, immutable external-ID mapping, bounded retry, DLQ.
- Finance: money facts, event corrections, forecasts, risk bands, plan/actual/statutory reconciliation views.
- Operations: Planfix process mapping, driver/fleet/repair/compliance workflows and service status.
- Commercial: account contracts, subscription/commission/partnership rules, price plans and effective dates.
- Entitlements: Starter/Full, feature permissions and enforcement, independent of commercial ownership.
- Governance: identities, tenant boundaries, roles, approvals, audit, evidence and sandbox/live separation.

## Invariants
1. Source-of-truth boundaries are explicit; neither Planfix tasks nor MCP responses equal accounting postings.
2. Every financial fact has source, captured_at, effective_at, currency, tenant, idempotency key, status and evidence.
3. Missing or stale source creates UNKNOWN, not a synthetic zero or a green dashboard.
4. A webhook retry cannot double-post money, duplicate receivables or trigger a second payout.
5. Technical revenue share and passenger/driver/investor cash are separate ledgers/domains.
6. A tenant commercial-model switch cannot rewrite past operational events or move between tenants.
7. AI is optionally assistive; no hidden control path bypasses approval.
8. Vehicle telemetry high-volume stream stays out of Planfix; only aggregated metrics and exceptions reach Planfix.
9. Sandbox uses synthetic/de-identified data and separate credentials, queues and payment endpoints.
10. Tax rules, privacy law and investor obligations are subject to local legal/accounting review.

## Technology baseline
Python 3.12+ pure-standard-library domain prototype; pytest + Ruff in CI; no database, web server, payment SDK or live connector yet. Choose persistent stack only after discovery and threat model. The code in this scaffold demonstrates invariants, not feature completion.

