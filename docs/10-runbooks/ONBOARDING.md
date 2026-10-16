# Read-only Planfix and finance source onboarding

1. Confirm written scope, data processor/controller role, operating legal entity, access expiring date, owner and escalation contact.
2. Prefer read-only scoped user/token for inventory; share secrets only via approved secret manager.
3. Inventory object definitions and mapping samples with redaction; get consent for driver PII and finance evidence.
4. Configure synthetic sandbox tenant and test integration separately.
5. Record source event IDs, timestamps, time zones, dedup logic, API limits and failure classification.
6. Establish manual-only default; enable narrowly scoped writes after acceptance.
7. Rotate credentials and revoke audit access at end of discovery.

