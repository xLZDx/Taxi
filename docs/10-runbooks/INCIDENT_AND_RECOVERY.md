# Incident response / recovery (draft)

SEV-1: cross-tenant data exposure, wrongful payout, safety-critical dispatch action or financial data corruption. Stop automated writes; preserve evidence, page accountable human. SEV-2: Planfix/bank source unavailable or missing reconciliation; visible data-staleness warning and manual exception process.

Preflight: snapshot exact deployment/queue cursor, limit write scope; verify secrets and tenant isolation. On failure: block non-idempotent side effects; persist inbound events, turn off automation, use manual process. Recovery: replay with source-event dedup, reconcile authoritative statements and approvals, compare target vs source, document corrective action. No deletion of immutable evidence. Postmortem includes timeline, blast radius, recurrence prevention and acceptance-test change.

