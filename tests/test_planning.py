from datetime import UTC, datetime, timedelta
from decimal import Decimal

import pytest

from taxi_platform.planning import (
    internal_start_before_external_deadline,
    with_contingency,
)


def test_default_time_contingency_is_twenty_percent() -> None:
    assert with_contingency(timedelta(days=5)) == timedelta(days=6)
    assert with_contingency(timedelta(seconds=1)) == timedelta(seconds=2)


def test_reverse_schedule_preserves_fixed_external_deadline() -> None:
    deadline = datetime(2026, 11, 10, 10, 0, tzinfo=UTC)
    assert internal_start_before_external_deadline(
        deadline, timedelta(days=5)
    ) == datetime(2026, 11, 4, 10, 0, tzinfo=UTC)


def test_cannot_use_naive_deadline_or_negative_time() -> None:
    with pytest.raises(ValueError):
        internal_start_before_external_deadline(
            datetime(2026, 11, 10, 10, 0), timedelta(days=1)
        )
    with pytest.raises(ValueError):
        with_contingency(timedelta(days=-1))
    with pytest.raises(ValueError):
        with_contingency(timedelta(days=1), Decimal("-0.2"))
