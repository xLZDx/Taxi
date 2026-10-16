# Fleet business processes: preliminary workflow catalogue

Suggested generic pattern: event -> evidence/source -> deterministic action -> accountable role -> internal target -> escalation -> auditable close. SLA and owner assignments must be validated by operator. Apply an approximately 20% contingency to planned internal task duration, without extending external or legal deadlines. Money reserve != schedule contingency.

| ID | Process / trigger | System reaction and accountable role | Exception and escalation |
|---|---|---|---|
| WF-01 | Daily ride revenue arrives | Ingest signed/source-identified earning; controller reconciles | Source missing or duplicate -> finance review |
| WF-02 | Driver declares cash collection | Reconcile signed cash handover; cashier confirms | Missing handover -> follow-up before payout cutoff |
| WF-03 | Aggregator payout feed arrives | Match period, driver, fees, bank settlements | Disputed deductions -> reconciliation owner |
| WF-04 | New receivable or overdue driver debt | Age by driver and due date; driver manager tasked | Aging threshold -> finance lead |
| WF-05 | Investor obligation approaches 10th | Forecast safe available cash and payout coverage; CFO reviews | Expected gap -> CEO and options with evidence |
| WF-06 | Month closes but driver reports pending | Track provisional close and evidence queue | Pending source flagged UNKNOWN, never ZERO |
| WF-07 | Cash inflow delayed | Update ETA distribution and risk band | Alert owner; never silently move legal payout date |
| WF-08 | Vehicle fault reported | Safety triage and repair ticket; garage lead | Critical roadworthiness -> block dispatch by authorized connector |
| WF-09 | Repair quote ready | Compare history and parts availability; approve spend | Over cap -> director approval |
| WF-10 | Vehicle idle > planned duration | Identify cause/cost and replacement options | Escalate to fleet manager |
| WF-11 | Scheduled maintenance due | Trigger booking with schedule buffer | Overdue -> prevent release where legally necessary |
| WF-12 | Insurance / permit / license expiration | Notify driver and compliance lead | Due soon -> escalation and controlled hold |
| WF-13 | Driver no-show | Notify operations and propose coverage | Uncovered shifts -> dispatch owner |
| WF-14 | Accident reported | Secure safety response; evidence, insurer, legal tasks | Serious incident -> human escalation immediately |
| WF-15 | Traffic fine received | Match vehicle, driver, timeframe; verify attribution | Dispute -> legal, preserve documents |
| WF-16 | Fuel transaction deviation | Compare telemetry and receipts, create review | Never label fraud before investigation |
| WF-17 | Parts requested | Check approved stock and purchase controls | Low stock / over-price -> procurement |
| WF-18 | Customer complaint / lost property | Open SLA-bound case; assign accountable staff | Safety issue -> priority escalation |
| WF-19 | Government inspection request | Track due date and collect authorized records | Counsel/compliance owner required |
| WF-20 | Tax filing period approaches | Pull verified statutory source records and draft | Accountant signs off before filing |
| WF-21 | Contract onboarding / offboarding | Reconcile deposits, keys, documents, liabilities | Missing evidence -> hold closure |
| WF-22 | AI suggests an operation | Draft analysis and evidence to authorized user | No autonomous payments, filings or postings |
| WF-23 | Source API goes down | Queue and alert; display source freshness badge | Fail safe; replay and reconcile on recovery |
| WF-24 | Pricing/model admin changes | Future-dated audited config change | Two-person review for high-impact terms |

### Payout workflow on the 10th (first implementation)
Day-by-day ingestion -> earned vs confirmed vs collected -> bank-cleared balance -> known obligations and restricted cash -> forecast incoming with probabilities and late-report scenarios -> available cash coverage -> daily alerts -> finance-owned approved payment -> reconciliation and immutable evidence.

The reporting lag is 1–2 weeks in the discovery narrative; do not assume reports are always available before the 10th. Never book a presumed driver payment as cash.

### Example timing guardrail
If internal work normally needs 5 business days, plan 6 business days (20% spare capacity). If the fixed contractual deadline is the 10th, schedule the internal milestone early enough; escalation must not move that deadline.

