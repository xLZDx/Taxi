"""Commercial configuration remains independent of core fleet and money logic."""

from dataclasses import dataclass
from datetime import date
from enum import StrEnum


class CommercialModel(StrEnum):
    SUBSCRIPTION = "subscription"
    PARTNERSHIP = "partnership"
    PER_VEHICLE = "per_vehicle"
    COMMISSION = "commission"
    LICENSE = "license"
    FRANCHISE = "franchise"
    HYBRID = "hybrid"


class AccessTier(StrEnum):
    STARTER = "starter"
    FULL_ACCESS = "full_access"


@dataclass(frozen=True, slots=True)
class TenantCommercialConfig:
    tenant_id: str
    model: CommercialModel
    tier: AccessTier
    effective_from: date
    contract_version: str

    def __post_init__(self) -> None:
        if not self.tenant_id or not self.contract_version:
            raise ValueError("Tenant and contract version are required")


BASELINE_ENTITLEMENTS: frozenset[str] = frozenset(
    {"business_plans", "real_reporting", "settlement_reconciliation", "cash_forecast"}
)


def entitlements(tier: AccessTier) -> frozenset[str]:
    if tier is AccessTier.STARTER:
        return BASELINE_ENTITLEMENTS
    if tier is AccessTier.FULL_ACCESS:
        return BASELINE_ENTITLEMENTS | {"extended_ai", "advanced_workflow_reports"}
    raise ValueError("Unsupported access tier")
