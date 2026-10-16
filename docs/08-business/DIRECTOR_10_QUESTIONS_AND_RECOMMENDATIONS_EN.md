# Taxi Operator: 10 Questions and 10 Practical Recommendations

**Status:** Proposal for the fleet director | 2026-10-17 | To be validated with the customer

**Context:** About 500 cars, many owned by investors, and an existing Planfix installation. Our purpose is to reduce daily operational strain without requiring a CRM change. The ten questions below are **hypotheses**, not claims that we have audited the customer's business.

| # | Question to the director | What we propose |
|---|---|---|
| 1 | Is it hard to see, for each vehicle, its investor-owner, current driver and contractual obligations in one place? | Link Planfix directories for vehicles, drivers, investors and contracts with access restricted by role. |
| 2 | Do hiring and driver-document checks require repeated calls, manual follow-ups and missing information? | Set up an onboarding checklist in Planfix, named approvers and automatic reminders. |
| 3 | Do vehicle handovers, returns, keys, mileage and damage sometimes create arguments or gaps in documentation? | Make the Planfix handover/return workflow require a checklist, photos or evidence references and an accountable confirmation. |
| 4 | Is it difficult to know how much a driver earned, how much was handed in as cash, how much was received electronically, and what is actually available? | Track EARNED, CONFIRMED, RECEIVED and CLEARED separately; use source-backed finance reconciliation and Planfix exceptions. |
| 5 | Do late cash hand-ins, missing reports and disputed settlements create too much manual collection work? | Auto-create one traceable Planfix case per driver and period, assign an owner, deadline and escalation; prevent duplicate cases. |
| 6 | Do repairs and vehicle downtime generate unpredictable costs and lost earning days? | Follow report -> estimate -> approval -> repair -> safety check -> return to service, with vehicle-level cost/downtime tracking. |
| 7 | Are insurance, taxes, service, parts and other expenses sometimes entered after the fact or without complete evidence? | Require prompt, vehicle-specific cost registration, evidence, owner and source timestamp; alert on missing receipts or renewals. |
| 8 | Do investor payouts on the 10th force management to rely on drivers' promises or pay before cash has really arrived? | Establish a rolling payout-eligibility cutoff at D-14 calendar days, daily/weekly cash remittances, reconciliation and a hard no-advance guard. Protect taxes, insurance, repairs, unpaid bills and reserves before calculating a payout. |
| 9 | Is it difficult to verify invoices, payments and statutory reports without putting inaccurate entries into the official books? | Isolated synthetic Planfix lab for experiments; separate controlled real-data preflight; accountant approval before authorized accounting/statutory action. Never file simulated data. |
| 10 | Does getting the current status of 500 vehicles mean calling staff and comparing several reports? | Give the director a source-aware Planfix dashboard: cars working/off road, overdue tasks, driver debts, collected money, expenses, investor payout capacity, and Taxi-versus-Service performance. |

## The offer

**Keep Planfix as the operating front-end** and improve what people already use. Only add a narrowly scoped financial validation/forecast component where Planfix itself cannot guarantee trustworthy money calculations, retry safety or approval integrity. The director should spend time on exceptions, not hunting data.

**First proof:** ask the director to mark each question YES / PARTLY / NO; select the two most costly problems. Read-only map their Planfix; rehearse 10 synthetic cases, then 500; demonstrate a driver cash exception, a vehicle expense, and D-14 payout warning in an isolated Planfix lab. Compare recorded baseline with evidence, and request separate authorization for a real-data pilot.

**Safety/contract boundary:** an entry in Planfix is not a bank receipt; uncollected driver balances are not payout cash. The D-14 cutoff is for contractually eligible rolling settlement periods, not a method of hiding month-end transactions. Unexpected costs after cutoff still reduce payout eligibility. If the investor contract guarantees an unconditional payment on the 10th, it cannot be delayed unilaterally: the operator must arrange lawful funding or negotiate signed revised terms. Existing statutory accounting dates and filing obligations remain unchanged.

**Migration only on evidence:** if critical workflows demonstrably cannot be made safe and economical using Planfix plus extensions, compare assembled alternatives (Odoo, ERPNext, Bitrix24, composable tooling) and purpose-built Taxi modules. Do not propose a cutover without fit-gap evidence, full cost and a reversible migration plan.

**Present prototype:** offline foundation and synthetic scenario tests only. No production Planfix, bank, payout or government filing connection exists.
