# ADR-0004: Isolated sandbox with human approval gates

Accepted 2026-10-16.
Decision: synthetic financial stress testing in separate environment with no live payment keys, callbacks or account identities. Sensitive actions (payouts, regulated filings, accounting posts, roadworthiness exceptions) require authorized human workflow. Deterministic manual process persists if AI fails.
Consequences: added environment cost, safer demonstrations and auditable go-live.

