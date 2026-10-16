# Acceptance and proof gates

- G0 FOUNDATION: repo integrity, docs references, CI runner, no secrets, lint/unit tests on exact head. This is an engineering-only gate.
- G1 DISCOVERY: signed Planfix state inventory; authoritative sources, contract due date and permissions verified. NO live mutations.
- G2 FINANCIAL TRUTH: all distinctions earned/confirmed/received/cleared and missing-data UNKNOWN; reconciliation explains every simulated discrepancy.
- G3 SAFETY: tenant boundary, idempotency, duplicate webhooks, STOP/rollback/manual fallback, approval gates, sandbox-live segregation, source freshness.
- G4 PILOT: performance within agreed quotas, signed operator/accountant acceptance; incident/restore drills and forward payout forecast independently reviewed.
- G5 RELEASE: security, legal, deployment and migration approval required; green code tests alone do NOT authorize production, payment, filing or push.

Proof record for each gate: exact commit, tests run, test output digest, scenario fixtures, reviewers and explicitly NOT_RUN parts. No unsupported PASS claims.

