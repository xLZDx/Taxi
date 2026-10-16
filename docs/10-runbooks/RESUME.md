# Taxi — Resume / handover

Date: 2026-10-16. Repository: https://github.com/xLZDx/Taxi ; intended Windows path: D:\Repo\Taxi.
Stage: initial design + domain prototype; not production or integrated. This scaffold does not demonstrate actual Planfix access or business permission.

## Current decisions
Planfix-first. One multi-tenant codebase; independent commercial model/access tier; Starter minimum subscription; Business Plans & Real Reporting always available. Operator controls the taxi business. Focus investor payment due on the 10th despite post-month driver report lag. 20% internal task schedule buffer; risk-based liquidity reserve. Synthetic sandbox separate. Native CRM deferred.

## Next action
1. Gain approved read-only view of existing customer Planfix, not secrets in chat/Git.
2. Map current accounting/dispatch/settlement source and actual investor payout contract.
3. Record initial baselines and prioritise backlog TAXI-001..TAXI-017.
4. Make real connector and persistence choices only after threat-model and contract review.
5. Run exact-head code/doc validation in approved environment and create a reviewed PR; no production action implied.

## Current risks
No Planfix audit, incomplete commercial/legal agreements, no live/source telemetry, no customer KPI baseline, no real webhook contracts, no production CI evidence. Current source tests verify prototypes only.

## Local workstation
Personal DC v2.2 is the intended operator-controlled route to D:\Repo\Taxi. If connector is unavailable, do not claim writes to Windows. Synchronize approved GitHub changes only after checking local Git status, untracked files and branch to prevent overwrite.

