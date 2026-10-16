# Taxi Automation Platform

Planfix-first, multi-tenant automation and financial intelligence for taxi fleet operators. Initial discovery target: an independent taxi operator with approximately 500 vehicles. The taxi operator remains accountable for operations, driver contracts, accounting, compliance and investor payouts. We provide technology and workflow optimization, not taxi operations.

**Status: FOUNDATION / NOT PRODUCTION READY.** No client Planfix, bank, dispatch, 1C or GPS system has been connected. No real data or funds are handled.

## First product slice
Driver economic activity -> confirmed settlement -> money received and cleared -> evidence-linked reconciliation -> 10th-of-month investor payout liquidity forecast -> Planfix exception tasks and approval. Missing driver reports remain unknown, not zero; the 20% scheduling contingency is not a financial cash reserve.

## Product boundaries
- Existing Planfix: configurable tasks, custom objects, process ownership, alerts and human approvals.
- External integration gateway: dispatch, aggregator, cash/bank, accounting and telemetry ingestion; dedup, rate control, audit and retry.
- Business Plans & Real Reporting (included in Starter): plans, forecasts, truthful actuals and legally reconcilable statutory exports from one traceable foundation.
- Commercial model: subscription, partnership, per-vehicle, commission, licensing, franchise and hybrid terms as tenant configuration.
- Access tier: Starter or Full Access, independent of model and of operational ledger.
- Synthetic test environment isolated from live financial endpoints; native Taxi CRM is intentionally deferred.

## Start here
- [Canonical index](docs/00-project/CANONICAL_DOCUMENTS.md)
- [Project charter](docs/00-project/PROJECT_CHARTER.md)
- [Decision log](docs/00-project/DECISION_LOG.md)
- [PRD](docs/02-product/PRD.md)
- [24 workflow scenarios](docs/02-product/BUSINESS_WORKFLOWS.md)
- [Read-only Planfix audit](docs/01-discovery/PLANFIX_AUDIT.md)
- [Cash forecasting design](docs/04-finance/CASH_FORECAST.md)
- [Product/partner proposal](docs/08-business/PARTNER_PROPOSAL.md)
- [Backlog](docs/07-delivery/BACKLOG.md)
- [Resume / open issues](docs/10-runbooks/RESUME.md)

## Local development (Python 3.12+)
~~~powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[dev]"
.\.venv\Scripts\python -m pytest -q
.\.venv\Scripts\python -m ruff check .
.\.venv\Scripts\python scripts\verify_scaffold.py
~~~

The src package is a small dependency-free domain prototype with tests. It is not a cash management service, database, Planfix plug-in or deployable CRM.

## Governance
Read [AGENTS.md](AGENTS.md) before changes. No production connections, financial mutations, deletion, force push, external AI reviewers or paid services without explicit approval. User's Windows workspace target is D:\Repo\Taxi; GitHub commits are not evidence that local files have been synchronized.

License/IP ownership is not yet finalized. **Do not assume an open-source software license** because the repository is public. Third-party reuse must be reviewed separately.
