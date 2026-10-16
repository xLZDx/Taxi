# Planfix adapter integration contract

Priority: read-only configuration audit of the existing customer account. No OAuth token, webhook secret or customer payload in source control.

## Adapter operations (target interface)
- discover_object_types, fields, mappings, users/roles and relevant workflows (subject to API visibility).
- list_changes with stable cursor and bounded pagination.
- upsert_task / add_comment only with explicit authorized service identity and idempotency, after sandbox test.
- receive_webhook: validate signature/secret or provider verification method as documented, capture raw redacted event hash, deduplicate, queue, acknowledge.
- query_completion: status and evidence of asynchronous Planfix write; a 202 response is not guaranteed completion.
- report_sync_state: last success, source lag, failures, retry queue and mapping version.

## Boundaries
Planfix owns workflow task/owner/status data. It is not the authoritative bank balance, payment processor, fiscal return or GPS timeseries store. High-volume GPS goes through separate telemetry service. MCP agent access must be scoped by user/role; no shared admin agent.

## Reliability
Verify API version, scope model, daily rate limits and batch sizes against the account plan and current docs before choosing quotas. Use rate-limited shared queue, exponential jittered retry for transient faults, dead-letter queue and reconciliation after outage. Backfill requests must not overwrite newer changes.

## Rollout
Read-only discovery -> synthetic Planfix account contract tests -> separate limited write integration -> monitor and reconcile -> approved phased live rollout. Fallback to manual tasks when API unavailable.

## References
- https://help.planfix.com/restapidocs/
- https://planfix.com/help/Planfix_MCP
- https://github.com/planfix/planfix-1c

