# Initial risk register — 2026-10-16 (unverified assumptions)

| ID | Severity | Threat | Mitigation / owner to assign |
|---|---|---|---|
| R-01 | CRITICAL | Investor payment occurs before driver funds clear | Conservative forecast + shortfall alert + human payout gate; finance owner |
| R-02 | CRITICAL | False two-book reporting / tax exposure | Reconciled single evidence source; accountant/legal approval; finance owner |
| R-03 | CRITICAL | Cross-tenant driver or financial data leak | Scoped auth, tenant-bound queries, isolation tests; security owner |
| R-04 | HIGH | Planfix permissions/MCP overreach | Read-only audit, least privilege, tool allowlist and write approval |
| R-05 | HIGH | Missing driver statements represented as zero | Explicit UNKNOWN state and freshness alerts |
| R-06 | HIGH | Webhook retry duplicates money/obligations | Source-key dedup journal and idempotency tests |
| R-07 | HIGH | AI executes unauthorized action | Separate execution gates, no AI-only consent path |
| R-08 | HIGH | Outdated 1C/Planfix integration or license terms | Pin versions, vendor/API audit, substitute adapter |
| R-09 | HIGH | Payout contract details misunderstood | Contract-by-contract discovery and counsel |
| R-10 | HIGH | Sandbox reaches live money services | Separate credentials/accounts and fault-injection controls |
| R-11 | MEDIUM | Source latency makes dashboard look real-time | Timestamp and staleness watermark |
| R-12 | MEDIUM | Commercial-model switch changes historical bills | Effective dates, preview, audit, regression suite |
| R-13 | MEDIUM | Vendor outages block operating processes | Manual fallback, queues and DR drill |
| R-14 | MEDIUM | Planfix licenses for 500 drivers exceed business case | Office seats vs separate driver app economics |
| R-15 | HIGH | Vehicle safety status incorrectly cleared | Human QA and dispatch connector control |
| R-16 | HIGH | Customer-specific customisations fork codebase | Contract-driven configuration and ADR review |

No owner or mitigation completion is implied.

