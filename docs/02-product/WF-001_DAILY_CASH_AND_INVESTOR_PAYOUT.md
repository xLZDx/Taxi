# WF-001: Daily driver-to-cash reconciliation and investor payment risk

## Roles
- **Fleet director**: owns and acts on operations, collections, payouts and commercial/contractual decisions.
- **Driver settlement specialist**: requests missing reports and explains disputed amounts.
- **Accountant/controller**: verifies amounts, source documents, bank receipts and cash proof.
- **Investor**: recipient under existing contract; cannot assume all fleet data access.
- **Technology partner**: operates software/integrations under contracted permissions; does not order taxi payouts.

## Sources and authoritative facts
1. Ride/dispatched work generates **EARNED** (may be provisional).
2. Signed platform/driver statement and contract logic generate **CONFIRMED** receivable/settlement.
3. Cash receipt or bank credit generates **RECEIVED**.
4. Bank availability / cash custody evidence generates **CLEARED** and separately available cash.
5. Existing investor contract generates obligation amount, payee, legal entity, date (usually the 10th) and allowed adjustments.
6. Repairs, taxes, salaries, card processing reserves and other liabilities reduce what is safe to pay; classifications need authorized accountant.

A missing statement is **UNKNOWN**, not zero. A customer payout due date cannot be moved because the software needs more time.

## Trigger -> condition -> action
| Trigger | Condition | Automated action | Human owner |
|---|---|---|---|
| New ride statement | Source ID unseen | Store evidence, upsert accrual state, update expected lag | Controller reviews discrepancies |
| Driver report expected | Report missing at internal cutoff | Create Planfix task "Statement missing" with source age and deadline | Driver settlements lead |
| Receipt exported | Receipt matches driver/period and signed source | Update received amount, initiate clearing verification | Accountant |
| Source feed unavailable | Last success exceeds agreed SLA | Mark STALE/UNKNOWN; no false zero or green result | Integration on-call |
| Reconciliation mismatch | Difference > agreed threshold, or orphan cash entry | Create exactly one deduplicated exception task | Controller |
| Daily projection | Safe amount < investor due on 10th under low scenario | Notify director early with evidence and options, no outgoing payment | Director |
| Statement corrected | Referenced original and authorized adjustment | Recompute versioned actual and forecast; maintain previous evidence | Accountant |
| Payout requested | Contract due and draft approved | Generate human-review packet, never auto-transfer money | Director/accountant |

## Proposed Planfix task lifecycle
NEW -> SOURCE_PENDING -> NEEDS_RECONCILIATION -> VERIFIED -> READY_FOR_REVIEW -> CLOSED.
Any state -> ESCALATED if external clock risk, missing evidence or counterparty disagreement. CLOSED requires proof and approval; reopening creates a traceable action. These are target lab statuses only; map to actual Planfix workflow after read-only audit.

## Planned alert schedule
Business deadline: 10th calendar day according to actual contract/time zone and banking cutoffs. Proposed internal checkpoints: 7th day, 9th day, morning of 10th, plus daily low-case projections earlier in the month. The first threshold must be tuned to the distribution of delayed reports; a 20% contingency increases time budget for internal work only, not contractual deadlines.

## Scenario-based acceptance (synthetic)
- D-01: Report late by 14 days -> UNKNOWN receivable and early missing-source task, not fictitious zero.
- D-02: Confirmed MDL 20,000; received MDL 14,000; outstanding MDL 6,000 (illustrative and contract-dependent).
- D-03: Projected MDL 30,000 arriving on 11th cannot cover payout due on 10th.
- D-04: Replayed webhook generates one financial event and one Planfix exception, not duplicate payout.
- D-05: Cancelled settlement creates explicit reversal; no silent mutation of earlier period.
- D-06: Bank source stale -> status UNVERIFIED and human follow-up.
- D-07: Same tenant under subscription and partnership yields identical operational cash values.
- D-08: Tenant B cannot inspect Tenant A driver data.
- D-09: Sandbox payment action is impossible, even for administrator or AI client.
- D-10: Accounting export reconciles management actual vs legally mandated presentation without manipulating facts.

## KPIs
Daily freshness by source, statement coverage, confirmed vs received gap, cleared cash, expected receipt-lag distribution, projected coverage of investor obligation, warning lead time, overdue exceptions, time spent per reconciliation. Record a 4+ week measured baseline before claiming a specific ROI.
