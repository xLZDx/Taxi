from datetime import date
from decimal import Decimal

import pytest

from taxi_platform.domain import CashState, Environment, FinancialEvent, Money
from taxi_platform.reconciliation import (
    ConflictingSourceEvent,
    DriverSettlement,
    InMemoryJournal,
    TenantAccessError,
)


def event(*, tenant: str = "a", amount: str = "10") -> FinancialEvent:
    return FinancialEvent(
        tenant_id=tenant,
        environment=Environment.SANDBOX,
        source_system="synthetic-dispatch",
        source_event_id="evt-1",
        driver_id="driver-synthetic",
        occurred_on=date(2026, 10, 16),
        state=CashState.CONFIRMED,
        money=Money(Decimal(amount), "MDL"),
        evidence_ref="synthetic-evidence",
    )


def test_duplicate_identical_event_is_idempotent() -> None:
    j = InMemoryJournal()
    assert j.ingest(tenant_context="a", environment=Environment.SANDBOX, event=event())
    assert not j.ingest(tenant_context="a", environment=Environment.SANDBOX, event=event())
    assert len(j.list_for_tenant(tenant_context="a", environment=Environment.SANDBOX)) == 1


def test_conflicting_duplicate_fails_closed() -> None:
    j = InMemoryJournal()
    j.ingest(tenant_context="a", environment=Environment.SANDBOX, event=event())
    with pytest.raises(ConflictingSourceEvent):
        j.ingest(tenant_context="a", environment=Environment.SANDBOX, event=event(amount="11"))


def test_cross_tenant_or_live_ingest_is_denied() -> None:
    j = InMemoryJournal()
    with pytest.raises(TenantAccessError):
        j.ingest(tenant_context="b", environment=Environment.SANDBOX, event=event())
    with pytest.raises(TenantAccessError):
        j.ingest(tenant_context="a", environment=Environment.LIVE, event=event())
    assert j.list_for_tenant(tenant_context="b", environment=Environment.SANDBOX) == ()


def test_tenant_queries_only_return_authorized_rows() -> None:
    j = InMemoryJournal()
    for tenant in ("a", "b"):
        j.ingest(tenant_context=tenant, environment=Environment.SANDBOX, event=event(tenant=tenant))
    assert [x.tenant_id for x in j.list_for_tenant(
        tenant_context="a", environment=Environment.SANDBOX
    )] == ["a"]
    assert j.list_for_tenant(tenant_context="a", environment=Environment.LIVE) == ()


def test_unknown_statement_is_not_assumed_zero() -> None:
    unknown = DriverSettlement(driver_id="driver-synthetic", confirmed=None, received=Decimal(0))
    assert unknown.outstanding is None
    assert DriverSettlement(
        driver_id="driver-synthetic", confirmed=Decimal(100), received=Decimal(60)
    ).outstanding == Decimal(40)


def test_overpayment_requires_exception() -> None:
    with pytest.raises(ValueError):
        DriverSettlement(driver_id="driver-synthetic", confirmed=Decimal(10), received=Decimal(20))
