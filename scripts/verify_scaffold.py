"""Deterministic local check for canonical source files and safety terms."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    ".github/workflows/ci.yml",
    "pyproject.toml",
    "docs/00-project/PROJECT_CHARTER.md",
    "docs/00-project/DECISION_LOG.md",
    "docs/01-discovery/PLANFIX_AUDIT.md",
    "docs/02-product/PRD.md",
    "docs/02-product/BUSINESS_WORKFLOWS.md",
    "docs/03-architecture/ARCHITECTURE.md",
    "docs/03-architecture/COMMERCIAL_CONFIG.md",
    "docs/04-finance/BUSINESS_PLANS_REAL_REPORTING.md",
    "docs/04-finance/APPROVED_WORDING_RU.md",
    "docs/04-finance/CASH_FORECAST.md",
    "docs/05-integrations/PLANFIX_INTEGRATION.md",
    "docs/06-governance/SECURITY_AND_APPROVALS.md",
    "docs/07-delivery/BACKLOG.md",
    "docs/07-delivery/ACCEPTANCE_GATES.md",
    "docs/08-business/PARTNER_PROPOSAL.md",
    "docs/09-future/OWN_TAXI_CRM_LATER.md",
    "docs/10-runbooks/RESUME.md",
    "tests/test_finance.py",
    "tests/test_journal.py",
    "tests/test_commercial.py",
    "tests/test_planning.py",
    "tests/test_sandbox_data.py",
    "scripts/generate_sandbox_data.py",
    "src/taxi_platform/sandbox_data.py",
    "docs/01-discovery/PLANFIX_SANDBOX_LAB.md",
    "docs/01-discovery/STAKEHOLDER_BOUNDARY.md",
    "docs/02-product/WF-001_DAILY_CASH_AND_INVESTOR_PAYOUT.md",
    "docs/07-delivery/IMPLEMENTATION_PLAYBOOK.md",
]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        for path in missing:
            print(f"MISSING: {path}")
        return 1
    charter = (ROOT / "docs/00-project/PROJECT_CHARTER.md").read_text(encoding="utf-8")
    reporting = (ROOT / "docs/04-finance/BUSINESS_PLANS_REAL_REPORTING.md").read_text(
        encoding="utf-8"
    )
    quote = (ROOT / "docs/04-finance/APPROVED_WORDING_RU.md").read_text(
        encoding="utf-8"
    )
    if "Planfix-first" not in charter or "Starter" not in reporting:
        print("MISSING: required product invariants")
        return 1
    if "Никаких скрытых книг" not in quote or "Двойную бухгалтерию" not in quote:
        print("MISSING: approved verbatim quote markers")
        return 1
    print(f"Foundation file gate PASS: {len(REQUIRED)} files; no live integration implied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
