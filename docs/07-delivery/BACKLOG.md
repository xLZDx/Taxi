# Prioritized initial backlog (not started)

Status vocabulary: TODO / IN_PROGRESS / DONE / BLOCKED / NOT_COVERED. Nothing in this backlog is done merely because a document mentions it.

| ID | Priority | Story | Minimum acceptance |
|---|---|---|---|
| TAXI-001 | P0 | Inspect Planfix existing objects and workflows | Read-only inventory with evidence & current-state map |
| TAXI-002 | P0 | Create driver/vehicle/external ID map | Source ownership, duplicates and mapping drift documented |
| TAXI-003 | P0 | Map payout contracts due on 10th | Contract rules reviewed by fleet owner/accountant |
| TAXI-004 | P0 | Describe source driver earnings | Full field mapping incl time and fees |
| TAXI-005 | P0 | Describe bank/cash clearing source | Cash, clearing, restrictions distinct |
| TAXI-006 | P0 | Define tenant-bound canonical finance events | Schemas, examples, idempotency keys |
| TAXI-007 | P0 | Implement deterministic ingestion journal | Duplicate/replay test passes |
| TAXI-008 | P0 | Implement period-by-period reconciliation | Exceptions with source evidence, no silent zero |
| TAXI-009 | P0 | Build 10th investor liquidity forecast | Known liabilities, conservative low scenario |
| TAXI-010 | P0 | Planfix alert and human approval workflow | Sandbox end-to-end with missing source |
| TAXI-011 | P0 | Business Plans / Real Reporting basic views | Same evidence, reconciled plan vs actual |
| TAXI-012 | P0 | Synthetic sandbox with isolation | Cannot reach live keys or payouts |
| TAXI-013 | P0 | Multi-tenant authorization | Negative cross-tenant tests |
| TAXI-014 | P0 | Commercial model and tier separation | Same finance result across all models |
| TAXI-015 | P0 | Source freshness and observable errors | Stale feed visible and escalated |
| TAXI-016 | P0 | Security/threat model and compliance review | Approved boundary before production |
| TAXI-017 | P0 | CI tests/lint/docs gate | Push & PR execution once connected |
| TAXI-018 | P1 | Driver docs expiry automation | Lead times + escalation |
| TAXI-019 | P1 | Repairs lifecycle and downtime KPI | Critical unsafe vehicle held |
| TAXI-020 | P1 | Parts requests and purchase approvals | Approval thresholds and audit |
| TAXI-021 | P1 | Fuel anomaly investigations | No automated guilt inference |
| TAXI-022 | P1 | Accident/insurance workflow | Human triage and secure evidence |
| TAXI-023 | P1 | Tax/inspection evidence prep | Draft only, accountant approval |
| TAXI-024 | P1 | Bank-feed outage/replay recovery | Bounded retries and manual fallback |
| TAXI-025 | P1 | Operator executive dashboard | KPI drilldown to evidence |
| TAXI-026 | P1 | Driver portal/bot economics | Permissions and per-seat costs |
| TAXI-027 | P1 | Per-vehicle/commercial billing strategy | Future-dated, no history changes |
| TAXI-028 | P1 | Pilot source quality score | Baseline and exception trend |
| TAXI-029 | P2 | Read-only AI analyst via MCP | No admin identity, no money writes |
| TAXI-030 | P2 | Second/third dispatch integrations | Same adapter interface, no tenant forks |
| TAXI-031 | P2 | Standalone taxi CRM feasibility | Deferred decision with TCO comparison |

