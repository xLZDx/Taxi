# ADR-0005: Experimental validation and controlled statutory release

Status: **Accepted product direction (2026-10-17); implementation and jurisdictional rules pending discovery**.
Related decisions: ADR-0002 (one auditable financial truth), ADR-0004 (isolated sandbox and human approval).

## Context and terminology

The operator described two business/reporting lanes: an experimental lane to check invoices, payments, timing and integrations, followed by an approved release to the official/statutory reporting lane. This is **not two sets of books**.

Business lines (e.g., **Taxi** and **Vehicle Service**) are separate analytical dimensions within an authorized legal entity, not separate accounting truths or necessarily separate legal entities. Each fact is tagged with `tenant_id`, `legal_entity_id`, `business_line_id`, source identity and evidence. Shared costs may be allocated only using recorded, approved rules. Reports may be by business line or consolidated by legal entity as applicable.

## Decision: two operational lanes, one reconciled source of truth

**Lane A: EXPERIMENTAL / VALIDATION**
- A separate Planfix development account and integration sandbox use **synthetic or properly de-identified data** to exercise workflow, imports, rule changes, reconciliation, timing, negative cases and user interface.
- No live payment credentials, taxpayer submission credentials or production posting endpoint may be reachable from this sandbox; sandbox records are permanently non-postable/non-fileable.
- **Real invoices and payments** require a distinct, permissioned **pre-submission review/staging workspace** within the controlled production data boundary. There, validations run in preview/dry-run mode against authentic source records **without posting or filing**. This workspace is not the open development sandbox.
- A passing experiment never constitutes evidence that a real payment occurred or that an invoice is genuine.

**Lane B: OFFICIAL / STATUTORY**
- Authoritative, evidence-backed real records are fetched from the approved source (bank, accounting platform, contract, signed document or authorized transaction source) and validated again in the controlled environment.
- After policy-defined accountant/controller review and any additional director/legal approval, an immutable, versioned **release package** is authorized for posting in the existing accounting system and/or inclusion in a statutory report.
- A separate authorized production action sends the relevant report/document through the company's **official channels**, where required and supported; not every invoice or payment is individually submitted to a regulator.
- Each posting/export/submission has a recorded result and acknowledgement/reference, or an explicit rejection and owner-assigned remediation. No claim of filing success before acknowledgement.

```text
                     Source evidence (invoices, receipts, bank, Planfix)
                                        |
                      +-----------------+----------------+
                      |                                  |
            EXPERIMENTAL LAB                    CONTROLLED REAL-DATA REVIEW
          synthetic/de-identified              authentic drafts / dry-run checks
          no posting / no filing               deadline + duplicate + reconciliation
                      |                                  |
                 TEST RESULTS                      HUMAN APPROVAL GATE
                      |                                  |
          Feedback into validators              Re-read source + revalidate
              (never source facts)                         |
                                                          v
                                                 OFFICIAL ACCOUNTING
                                                 posting and reconciliation
                                                          |
                                               Authorized statutory channel
                                                          |
                                               Receipt / reject / audit trail
```

## Minimum release conditions

1. Verify tenant/legal-entity and business-line scope, invoice identifiers, counterparties, amounts/currency, dates/period/time zone, contract basis, source provenance and evidence integrity.
2. Perform schema/rule checks (including applicable tax treatment and deadlines), duplicate/idempotency checks, document-to-ledger reconciliation and bank/payment confirmation **only when claiming money was received**. An unpaid but authentic invoice can still be valid.
3. Fail closed on missing or stale sources, unexplained discrepancies, wrong entity, altered evidence, expired deadlines that need accountant escalation or unresolved approvals.
4. Record the reviewer(s), authority, time, source hashes, rule version, reconciliation result, approvals, release-package ID and target channel. Enforce segregation of duties for regulated actions according to customer policy.
5. Post/submit idempotently using source + target + version keys and deduplicated acknowledgements. Corrections and resubmissions preserve prior versions; no silent overwrites.
6. Maintain an explicit workflow with deadlines and alerts before filing dates. A green sandbox test cannot waive accounting or legal review.
7. Provide an AI-free human fallback for validation, approval and authorized submission if Planfix/integrations are unavailable.

## Explicit prohibitions and scope

- No fake second accounting ledger, fabricated income/invoices or undisclosed mismatch between management and statutory data.
- Never promote a synthetic/sandbox invoice, sandbox-generated payment or copied sandbox ID directly into an official ledger or filing.
- Never permit an approval flag to turn unverified test data into a financial fact.
- No autonomous outgoing bank transfers or regulator filings under the present prototype.
- Never assume local statutory formats or government APIs without validation by the operator's accountant and a jurisdiction-specific integration discovery.

## Verification scenarios (to implement; not yet tested)

- A synthetic sandbox invoice marked APPROVED still cannot reach production posting or a regulator.
- A real invoice submitted to review with mismatched amount/currency or legal entity is blocked with a Planfix reconciliation task.
- A valid real unpaid invoice is distinguishable from a bank-confirmed paid invoice; no fake bank receipt.
- The same release-package replay produces one accounting posting/submission reference, not two.
- Missing regulator receipt means PENDING/UNKNOWN, never SUCCESS.
- Taxi and Service reports reconcile to the correctly scoped legal-entity total with documented shared-cost allocations.
- A missed cutoff raises an alert and escalation; it cannot silently backdate a filing.
- Production credentials and personal source records cannot be read from the development sandbox.

## Ownership and implementation plan

Planfix owns task assignment, exception queues and human sign-offs. A dedicated validation/finance component owns rules, provenance, reconciliation, preflight result, immutable release package and deduplication. The existing accounting system of record owns statutory postings; the operator's authorized channel owns submission. Integration details, legal-entity mappings, tax rules, accountant approval policy and supported regulator channels are **discovery deliverables**, not deployed capabilities.
