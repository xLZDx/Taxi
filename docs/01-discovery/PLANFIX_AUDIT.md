# Existing Planfix audit — read-only first

**State:** NOT RUN. We have not seen the operator's real account, configuration, integrations or legal data. This is an audit plan, not a completed inventory.

## Discover with scoped read-only authorization
1. Account plan, allowed users/roles, service accounts, subscription/API quotas; collect only necessary identifiers.
2. Entity/object types, fields, custom data tags, statuses, templates, contact/company records, directories, reports.
3. Live automations/scenarios: trigger, condition, action, retries, escalation, execution logs, owner and failure handling.
4. Existing integrations: dispatch/aggregators, GPS, bank/PSP, cash register, 1C/ERP, payroll, documents, email/bots, Planfix MCP.
5. Data ownership and authority: where earned revenue, confirmed orders, actual cash, driver receivables, invoices, tax records and final payouts are generated.
6. Access rights: owner vs managers vs drivers vs investors; audit logs, attachment permissions and service-user scope.
7. Monthly workflow: example month-end, driver reporting 1–2 weeks later, cash received by channel, investor payout due 10th.
8. Missing identifiers, duplicate records, stale data, undocumented manual spreadsheets, wrong assumptions in historical reports.
9. Operational processes for driver compliance, roadworthiness, repairs, penalties, incidents, inspections and downtime.
10. Test tenant/account and synthetic scenarios available? Never test financial changes in live objects.

## Deliverables
- Entity and field inventory with source of truth, PII classification and cardinality.
- 20+ workflows mapped to trigger/owner/SLA/escrow/exception plus 20% schedule buffer.
- Integration and permissions matrix, API sample payloads with redaction, rate-limit observations.
- Four-way disposition per requirement: KEEP / CONFIGURE / INTEGRATE / EXTERNAL MODULE.
- Data-quality report, risk register update and pilot estimate.

## Discovery evidence template
| Object/source | Owner | Evidence ref | Last observed | Confidence | Status |
|---|---|---|---|---|---|
| Planfix tasks | UNKNOWN | NONE | N/A | UNVERIFIED | NOT_RUN |
| Cash/bank | UNKNOWN | NONE | N/A | UNVERIFIED | NOT_RUN |
| Driver earning source | UNKNOWN | NONE | N/A | UNVERIFIED | NOT_RUN |

Do not insert real credentials, personal driver data or bank details into Git.

