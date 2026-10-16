"""Conservative cash availability math for a 10th-of-month investor payout.

Projection is advisory. It cannot authorize a payment or statutory report.
"""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from taxi_platform.domain import Money


@dataclass(frozen=True, slots=True)
class ExpectedReceipt:
    expected_available_on: date
    money: Money


@dataclass(frozen=True, slots=True)
class LiquidityAssessment:
    currency: str
    payout_due_on: date
    actual_available: Decimal
    projected_available: Decimal
    payout_amount: Decimal
    actual_shortfall: Decimal
    projected_shortfall: Decimal


def assess_payout(
    *,
    payout_due_on: date,
    cleared_cash: Money,
    restricted_cash: Money,
    protected_obligations: Money,
    payout_amount: Money,
    expected_receipts: tuple[ExpectedReceipt, ...] = (),
) -> LiquidityAssessment:
    values = (cleared_cash, restricted_cash, protected_obligations, payout_amount)
    if any(value.currency != cleared_cash.currency for value in values):
        raise ValueError("Currency mismatch in liquidity assessment")
    if any(r.money.currency != cleared_cash.currency for r in expected_receipts):
        raise ValueError("Currency mismatch in projected receipt")
    actual = cleared_cash.amount - restricted_cash.amount - protected_obligations.amount
    future = sum(
        (r.money.amount for r in expected_receipts if r.expected_available_on <= payout_due_on),
        Decimal(0),
    )
    projected = actual + future
    return LiquidityAssessment(
        currency=cleared_cash.currency,
        payout_due_on=payout_due_on,
        actual_available=actual,
        projected_available=projected,
        payout_amount=payout_amount.amount,
        actual_shortfall=max(Decimal(0), payout_amount.amount - actual),
        projected_shortfall=max(Decimal(0), payout_amount.amount - projected),
    )
