from datetime import date
from decimal import Decimal

from taxi_platform.commercial import (
    AccessTier,
    CommercialModel,
    TenantCommercialConfig,
    entitlements,
)
from taxi_platform.domain import Money
from taxi_platform.forecast import assess_payout


def test_business_plans_and_reporting_always_in_starter() -> None:
    assert {"business_plans", "real_reporting", "cash_forecast"}.issubset(
        entitlements(AccessTier.STARTER)
    )
    assert entitlements(AccessTier.STARTER).issubset(entitlements(AccessTier.FULL_ACCESS))


def test_commercial_model_does_not_change_operational_cash_math() -> None:
    observed = set()
    for model in CommercialModel:
        config = TenantCommercialConfig(
            tenant_id="synthetic", model=model, tier=AccessTier.STARTER,
            effective_from=date(2026, 10, 16), contract_version="draft-v1"
        )
        assert config.model is model
        forecast = assess_payout(
            payout_due_on=date(2026, 11, 10),
            cleared_cash=Money(Decimal("9000"), "MDL"),
            restricted_cash=Money(Decimal("1000"), "MDL"),
            protected_obligations=Money(Decimal("2000"), "MDL"),
            payout_amount=Money(Decimal("8000"), "MDL"),
        )
        observed.add((forecast.actual_shortfall, forecast.actual_available))
    assert observed == {(Decimal("2000"), Decimal("6000"))}
