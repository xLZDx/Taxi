"""Pure domain types; no live Planfix, bank or payment connections."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import StrEnum


class Environment(StrEnum):
    SANDBOX = "sandbox"
    LIVE = "live"


class CashState(StrEnum):
    EARNED = "earned"
    CONFIRMED = "confirmed"
    RECEIVED = "received"
    CLEARED = "cleared"


@dataclass(frozen=True, slots=True)
class Money:
    amount: Decimal
    currency: str

    def __post_init__(self) -> None:
        if not isinstance(self.amount, Decimal) or not self.amount.is_finite():
            raise ValueError("Money requires a finite Decimal amount")
        if self.amount < 0:
            raise ValueError("Use explicit reversal events instead of negative money")
        if not self.currency or len(self.currency) != 3 or not self.currency.isalpha():
            raise ValueError("Currency must be a three-letter ISO code")
        object.__setattr__(self, "currency", self.currency.upper())


@dataclass(frozen=True, slots=True)
class FinancialEvent:
    tenant_id: str
    environment: Environment
    source_system: str
    source_event_id: str
    driver_id: str
    occurred_on: date
    state: CashState
    money: Money
    evidence_ref: str

    def __post_init__(self) -> None:
        for name in ("tenant_id", "source_system", "source_event_id", "driver_id", "evidence_ref"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} is required")
