"""Synthetic-money contract tests; these are not accounting certification."""

from datetime import date
from decimal import Decimal

import pytest

from taxi_platform.domain import Money
from taxi_platform.forecast import ExpectedReceipt, assess_payout


def mdl(amount: str) -> Money:
    return Money(Decimal(amount), "MDL")


def test_outstanding_investor_payment_only_cleared_cash_is_actual() -> None:
    result = assess_payout(
        payout_due_on=date(2026, 11, 10),
        cleared_cash=mdl("12000"),
        restricted_cash=mdl("2000"),
        protected_obligations=mdl("1000"),
        payout_amount=mdl("15000"),
        expected_receipts=(
            ExpectedReceipt(date(2026, 11, 9), mdl("8000")),
            ExpectedReceipt(date(2026, 11, 11), mdl("6000")),
        ),
    )
    assert result.actual_available == Decimal("9000")
    assert result.actual_shortfall == Decimal("6000")
    assert result.projected_available == Decimal("17000")
    assert result.projected_shortfall == 0
    assert result.payout_due_on.day == 10


def test_future_expected_cash_does_not_fix_cash_shortfall() -> None:
    result = assess_payout(
        payout_due_on=date(2026, 11, 10),
        cleared_cash=mdl("1000"),
        restricted_cash=mdl("0"),
        protected_obligations=mdl("0"),
        payout_amount=mdl("5000"),
        expected_receipts=(ExpectedReceipt(date(2026, 11, 11), mdl("50000")),),
    )
    assert result.actual_shortfall == Decimal("4000")
    assert result.projected_shortfall == Decimal("4000")


def test_currency_mix_is_rejected() -> None:
    with pytest.raises(ValueError, match="Currency mismatch"):
        assess_payout(
            payout_due_on=date(2026, 11, 10),
            cleared_cash=mdl("100"),
            restricted_cash=Money(Decimal("0"), "EUR"),
            protected_obligations=mdl("0"),
            payout_amount=mdl("0"),
        )


def test_money_cannot_be_negative_float_or_nonfinite() -> None:
    with pytest.raises(ValueError):
        Money(Decimal("-1"), "MDL")
    with pytest.raises(ValueError):
        Money(1.0, "MDL")
    with pytest.raises(ValueError):
        Money(Decimal("NaN"), "MDL")
