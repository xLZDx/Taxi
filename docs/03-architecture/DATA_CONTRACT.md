# Canonical data contracts and ownership

Proposed keys: tenant_id; source_system; source_event_id; external_object_id; occurred_at; received_at; business_date and timezone; status; evidence_ref; currency; version. Read APIs require a tenant context and proper authorization.

## Financial state
- EARNED: reported/estimated economic activity, not money received.
- CONFIRMED: verified contractual receivable or settlement, still not cash.
- RECEIVED: proven payment receipt with receipt/bank/cash evidence.
- CLEARED: bank-cleared, unrestricted cash (subject to other reserved liabilities).
- ADJUSTMENT: auditable correction/reversal referring to original event.
Different accounting recognition dates and fiscal basis must be reconciled rather than suppressed.

## Minimum objects
- Tenant, user, role, entitlements, commercial contract effective version.
- Driver and vehicle (Planfix identity mapping); rental/investor agreement (authorized contract source).
- Shift, earning statement, confirmed settlement, expected receipt, collected receipt, clearing event.
- Obligation (investor/date/amount), other liabilities, hold/restricted cash and reserve policy.
- Reconciliation exception (reason, source, owner, deadline, status).
- Repair job, vehicle availability, compliance document, incident, audit record.
- Plan scenario, forecast version and assumption set.

## Money and time
Always use Decimal in code and explicit ISO currency; never floating point for money. Preserve original period/source timezone; the pilot local zone is presumed Europe/Chisinau only until validated. Store instants in UTC, business cutoffs with tenant timezone. No negative received amounts masquerading as chargebacks: represent explicit reversal events. Use source hashes and separate original/corrected values.

## Plan-versus-actual trace
Every total should permit drilldown to the underlying event IDs, correction chain, mapping rule and accounting view basis. A regulator-facing extract must never use simulated forecasts as factual taxable activity.

