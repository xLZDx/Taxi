"""In-memory demo journal and per-driver settlement reconciliation.

Not a persistent ledger. Do not use for real settlements or payments.
"""

from dataclasses import dataclass
from decimal import Decimal

from taxi_platform.domain import Environment, FinancialEvent


class ConflictingSourceEvent(ValueError):
    """The same source event ID has conflicting immutable content."""


class TenantAccessError(PermissionError):
    """Caller context does not match the event tenant."""


class InMemoryJournal:
    def __init__(self) -> None:
        self._events: dict[tuple[str, Environment, str, str], FinancialEvent] = {}

    def ingest(
        self, *, tenant_context: str, environment: Environment, event: FinancialEvent
    ) -> bool:
        if tenant_context != event.tenant_id or environment != event.environment:
            raise TenantAccessError("Tenant or environment mismatch")
        key = (event.tenant_id, event.environment, event.source_system, event.source_event_id)
        existing = self._events.get(key)
        if existing is None:
            self._events[key] = event
            return True
        if existing != event:
            raise ConflictingSourceEvent("Conflicting duplicate source event; review required")
        return False

    def list_for_tenant(
        self, *, tenant_context: str, environment: Environment
    ) -> tuple[FinancialEvent, ...]:
        return tuple(
            event
            for (tenant, scope, _, _), event in self._events.items()
            if tenant == tenant_context and scope == environment
        )


@dataclass(frozen=True, slots=True)
class DriverSettlement:
    driver_id: str
    confirmed: Decimal | None
    received: Decimal

    def __post_init__(self) -> None:
        if self.confirmed is not None and self.confirmed < 0:
            raise ValueError("Confirmed amount cannot be negative")
        if self.received < 0:
            raise ValueError("Received amount cannot be negative")
        if self.confirmed is not None and self.received > self.confirmed:
            raise ValueError("Overpayment requires a separate exception")

    @property
    def outstanding(self) -> Decimal | None:
        if self.confirmed is None:
            return None
        return self.confirmed - self.received
