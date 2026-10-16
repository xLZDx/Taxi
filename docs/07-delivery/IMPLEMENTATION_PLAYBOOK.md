# Taxi implementation playbook — pilot S0/S1

**Status:** implementation design for the independent technology provider/investor; not a customer-approved deployment. **Owner of taxi operations:** the taxi fleet director. **Scope:** one fleet with approximately 500 cars, including a few cars owned by the technology partner. There is no assumption of shared ownership of the taxi company.

## The outcome we will actually sell
Today the fleet director sees last month's numbers late. The pilot should give the director a trustworthy daily answer: "How much was earned? How much is verified? How much has really arrived? Will there be enough cleared, unencumbered money to pay investors on the 10th? What do my employees need to resolve today?" Standard exceptions should move automatically through Planfix to an accountable person, with AI limited to advice.

## Work packages with owner and a falsifiable result

| Work package | Delivery activity | Acceptance evidence / next owner |
|---|---|---|
| S0-01 | Set up a separately registered Planfix trial/eligible partner lab | Operator-controlled screenshot of lab URL and tenant identity; never production |
| S0-02 | Map drivers as contacts, vehicles as directories, exceptions as tasks | Sample records and reference IDs, authorized lab only |
| S0-03 | Generate 500 deterministic synthetic drivers/cars and simulated settlements | CSV + JSON count, no PII, matching IDs; code can regenerate files |
| S0-04 | Configure statuses, templates, filters and automations in lab | Screen-recorded ten-case demonstration with task owners |
| S0-05 | Read-only workshop with real fleet director | Signed source systems/roles/data map; no live mutation |
| S1-01 | Offline ingest of ride/settlement and cash/bank export | Traceable event IDs and correct UNKNOWN vs 0 distinction |
| S1-02 | Match earned, confirmed, received and cleared | Reconciliation exception list with evidence and no double counting |
| S1-03 | Forecast payout due on the 10th | Low/base/high plus safe cash coverage and source freshness |
| S1-04 | Send bounded Planfix exceptions into lab | One task per exception, retry safe, no admin-token agent |
| S1-05 | Show owner dashboard for Plan vs Actual | Every amount drills down to valid source evidence |
| S1-06 | Rehearse disconnected Planfix and delayed bank feed | Manual escalation continues; no hidden success |
| S1-07 | Test design with operator/accountant, then approve limited pilot | Signed acceptance and separate go-live permission |

## Concrete Planfix test-lab design
- **Contacts**: driver reference, identifier and simulated assignment; never create 500 paying Planfix employees for a demo.
- **Directory "Vehicles"**: synthetic VEH IDs, assigned driver, current status, permit/maintenance dates.
- **Object "Settlement exception"**: data period, driver/vehicle refs, expected/confirmed/received values, last source timestamp, discrepancy reason, task owner, SLA, approval state.
- **Object "Repair ticket"**: vehicle ref, reported fault, safety classification, estimate, service status, agreed deadline.
- **Dashboard**: source freshness; missing driver reports; unreceived confirmed cash; available cleared funds; 10th payout coverage; vehicles unavailable; overdue unresolved tasks.
- **Task automations**: missing report -> finance controller; unresolved > agreed cutoff -> director escalation; source unavailable -> do NOT mark reconciled.
- **Existing production Planfix**: inspect first and map to whatever types and fields are already in use; these names are lab suggestions, not instructions to overwrite the client's configuration.

## First end-to-end walkthrough (fully synthetic)
1. Generate a model of 500 vehicles/500 associated drivers (one-to-one **simulation assumption**, not fleet fact).
2. Import synthetic contacts and vehicle directory entries into the **separate Planfix test account**. Only after matching field templates, import the scenario tasks.
3. Choose one driver with a confirmed settlement but no cleared cash, one whose driver statement is still missing, and one whose receipt cleared on time.
4. Simulated nightly ingest detects the difference; task is assigned with a 20% **internal** time buffer, not a change to payment due date.
5. Forecast warns ahead of the payout due on the 10th; report shows actual available cash separately from predicted receipts.
6. Controller resolves evidence; sensitive payments remain manual in this phase.
7. Change commercial_model from subscription to partnership in a sandbox fixture and show that no operational settlement or cash result changes.

## Required customer-side input before a real pilot
Read-only authorized Planfix access; earnings/dispatch source; actual bank/cash statement export; anonymized driver settlement sample; exact investor contract and payout rule; accountant's statutory mapping; names of responsible staff; allowed periods/retention; sign-off on data access. No confidential files are requested in this repository.

## Order and timing
First, offline lab and product proof using synthetic data; second, operator read-only audit; third, approved sandbox API integration; fourth, signed limited real pilot. Dates and 20% task contingency are planning inputs, not a guarantee. Do not activate real customer webhooks, finance postings or bank payouts without distinct approval.

## Gate for calling the first workflow "working"
A clean exact-head CI, successful replay/idempotency and tenant-isolation tests; Planfix lab task workflow proven against synthetic exceptions; report/forecast split checked by a finance domain reviewer; customer sign-off. Current repo tests prove only the standalone domain prototype, not Planfix actions.
