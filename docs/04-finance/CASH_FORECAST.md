# Cash forecast and investor payout control — first pilot slice

## Problem
Payout obligation falls on the 10th, while drivers may report or settle 7–14 days after month-end. A retrospective monthly close cannot ensure liquidity. We need a daily forward cash-position forecast and disciplined exception management.

## Distinct pools
1. Earned (provisional), 2. Contractually confirmed due, 3. Collected with evidence, 4. Cleared and unrestricted cash, 5. Restricted/held cash, 6. Other known obligations, 7. Investor due per contracts. No estimate is counted as bank-cleared cash.

## At each daily cutoff
- Import source periods with freshness stamps and idempotency keys.
- Reconcile driver statements and receipts to cash/bank/PSP evidence. Unknown reports remain UNKNOWN.
- Compute confirmed current unrestricted liquidity and due liabilities.
- Forecast near-term receipts by observed timing distribution, with low/base/high scenarios; report confidence and coverage.
- Evaluate payout due by the 10th and a lower-tail liquidity shortfall risk; create Planfix exceptions.
- Finance owner proposes approved financing, collection follow-up or negotiated contract action if a shortfall exists.
- Human approval before outgoing payout; capture bank receipt and close reconciliation.

## Indicators
- Available liquidity (cleared unrestricted minus prior protected obligations and holds).
- Known payout obligation amount and date; shortfall if projected safe cash < obligation.
- Confirmed receivables and unknown receivables by driver/source.
- Collection-lag percentiles, bank clearing time, failure rate, stale source count.
- Plan vs actual error at 1/3/7/14-day horizons.

## Never claim
'Real-time cash certainty' without live bank/source feeds; 'safe to pay' based solely on predicted earnings; tax-liability reductions from hidden operations.

