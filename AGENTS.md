# Taxi — repository working contract

## Authority
One technology product for external taxi operators. This repository represents a proposal, process inventory and offline prototype, not a deployed or authorized live business service. The operator retains control of taxi operations.

## Working rules
1. Preflight repository root, branch, exact HEAD and dirty/untracked paths before any overwrite.
2. Use read-only calls first for Planfix, 1C, bank, ERP, dispatch, telemetry and Windows PC. Personal DC v2.2 is a preferred client for authorized local workstation operations; if unavailable, report the limitation rather than inventing local writes.
3. No deleting, force pushing, production payment, regulatory filing, account mutation, credential retrieval, deploying or destructive migrations without explicit operator authorization.
4. Do not run external AI reviewers/sub-agents without permission; deterministic tests first. Optional agent prompt files do not start agents.
5. Keep Git contributions and comments in English. The one specifically approved historical original-language quote is maintained in docs/04-finance/APPROVED_WORDING_RU.md unchanged.
6. Keep independent evidence for findings; note exact file:line and reproducible test. Never claim source tests prove customer integration or production correctness.
7. Preserve one codebase and independent tenant commercial model and entitlement tier. Do not weaken tenant isolation or safety gates to get passing tests.
8. Prepare reviews on a separate branch/PR, using normal non-force Git updates only. No automatic PR merge.
9. Real tax/statutory reports require licensed accounting/legal review in the customer jurisdiction; internal and statutory reports must reconcile.
10. No credentials, private driver data, bank details or real source payloads in Git or synthetic fixtures.

## Read first
docs/00-project/CANONICAL_DOCUMENTS.md; docs/02-product/PRD.md; docs/03-architecture/ARCHITECTURE.md; docs/06-governance/SECURITY_AND_APPROVALS.md; docs/07-delivery/ACCEPTANCE_GATES.md.

## Gate order
Discovery -> design -> sandbox implementation -> exact-diff review -> operator-controlled piloting -> separate production approval.
