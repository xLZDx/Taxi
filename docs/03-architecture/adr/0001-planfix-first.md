# ADR-0001: Extend existing Planfix before replacement

Accepted 2026-10-16.
Context: customer already uses Planfix, actual setup not yet inspected.
Decision: conduct least-privilege read-only audit; keep useful objects and automations, configure missing native capabilities, add controlled adapters/external finance logic only when needed.
Consequences: faster pilot and lower migration risk; SaaS/API/rate limits and license dependence. Track alternative stack and exit path without building a replacement CRM in phase 1.

