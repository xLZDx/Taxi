# Product Requirements Document — Taxi Automation Platform

Status: DRAFT v0.1, based on customer-discovery discussion; not validated against production Planfix.

## Stakeholders
Operator/CEO (accountable for taxi business), fleet/garage manager, driver relations, accountant, compliance/legal, investors (read-only views where allowed), technology provider (platform operator, not taxi controller).

## Required first-party capabilities
- FR-001 Per-tenant Planfix discovery and integration inventory without destructive modification.
- FR-002 Driver, vehicle, contract, documents, settlement and incident objects mapped to existing Planfix data where possible.
- FR-003 Ingest sources with timestamps, provenance, idempotent source-event IDs and sync health.
- FR-004 Separate accrual/earned amounts, settlement confirmed, receivables, cash collected and available bank liquidity.
- FR-005 Automated reconciliation, exception queues, owner assignment and audit history.
- FR-006 Daily forecast of investor obligations due on the 10th; confidence bands and shortfall warnings.
- FR-007 Business Plans & Real Reporting in the Starter baseline: forecasts, actuals, internal P&L/cash flow and legally reconcilable statutory extracts.
- FR-008 Track repair request -> diagnosis -> quote -> approval -> work -> QA -> service return, downtime impact.
- FR-009 Driver safety/compliance document expirations; control access and notifications.
- FR-010 Isolated sandbox for synthetic financial stress cases; hard block on production payments.
- FR-011 Configurable commercial model independent from access entitlements and operational rules, with effective dates and audit.
- FR-012 Human approvals for payouts, accounting postings, statutory filings, unsafe-vehicle overrides and privileged configuration changes.
- FR-013 Deterministic operations/notifications when AI or Planfix is unavailable; queued retry/reconciliation.
- FR-014 Strict tenant isolation and minimum-necessary driver/investor disclosure.
- FR-015 Planfix MCP/REST integration via controlled adapter, not direct administrative AI access.
- FR-016 KPI dashboard with source freshness, reconciliation coverage, forecast error, overdue incidents, vehicle downtime and savings methodology.

## Exclusions from pilot
Own taxi CRM; own dispatch engine or payment processor; autonomous payouts; direct real-time GPS storage in Planfix; changing legal books; law-specific tax rules without expert review.

## Non-functional acceptance
Fail-closed tenant boundary, deterministically deduplicated incoming events, immutable correction trail (append reversal/correction not silent overwrite), bounded retries, replay-safe workflows, explainable calculations, accessibility and role-tested views, no secrets in Git. Availability/latency/service levels await contract.

## Success definition
By the pilot gate, daily cash position for source-covered vehicles is reconciled with source timestamps and exception owners; investor payout coverage alert demonstrably precedes a seeded shortfall; Plan vs Actual explains every discrepancy; a live/sandbox boundary test passes.

