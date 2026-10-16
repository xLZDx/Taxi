# Taxi Automation Platform — Project Charter

Status: PROPOSED / discovery baseline, 2026-10-16. Source: operator discovery discussion. No pilot authorization, actual Planfix inspection or financial-data access has been confirmed.

## Purpose
Deliver a reusable, multi-tenant technology product that reduces manual effort, makes operating cash flow predictable and improves fleet performance for a taxi operator with approximately 500 vehicles. The operator owns and manages its taxi business, employees, vehicles, accounting and relationships with investors. We are a technology and automation provider, not a taxi business co-operator.

## Problem
Driver reports and cash settlements may arrive 1–2 weeks after the month ends, while fleet investor payments are due on the 10th. The operator cannot safely infer cash on hand from accrued revenue, and currently learns too much after the fact. Repairs, vehicle downtime, driver documents, taxes, inspections, incidents, and missing process ownership add delays and cost.

## Product principles
1. Planfix-first: audit and extend the operator's existing Planfix configuration before building replacements.
2. One product, one codebase; business logic invariant across all commercial arrangements.
3. Separate tenant commercial-model and entitlement selectors in admin; start with minimum subscription (Starter).
4. Include Business Plans & Real Reporting in Starter: one auditable data foundation with forecast, actual and legally reconciled statutory views.
5. Forecast the 10th-of-month liquidity before it becomes a shortfall; never equate earned, confirmed, receivable and collected funds.
6. Default 20% schedule contingency for internal tasks; monetary reserves are risk-based and separate.
7. Real/live and synthetic/sandbox domains remain isolated.
8. Humans approve sensitive payouts, postings, regulatory filings and safety decisions.
9. Rules and manual fallback continue to function without AI.
10. Do not initiate an independent taxi-specific CRM in phase 1; hold it as a future option.

## Pilot outcomes (targets to be negotiated)
Measured coverage of data feeds; daily reconciled cash position; investor payout coverage forecast; decrease in unassigned exceptions and repair idle time; documented evidence trail and repeatable onboarding. Numeric savings and pricing are assumptions until a measured baseline.

## Decisions explicitly NOT made
Legal entity, IP ownership and commercial agreement, country-specific tax interpretation, access to live Planfix, selected dispatch/finance providers, funding, customer price, and production go-live.

