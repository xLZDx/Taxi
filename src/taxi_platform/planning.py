"""Internal scheduling contingency; not a financial reserve."""

from datetime import datetime, timedelta
from decimal import Decimal, ROUND_CEILING


def with_contingency(duration: timedelta, factor: Decimal = Decimal("0.20")) -> timedelta:
    if duration < timedelta(0) or factor < 0:
        raise ValueError("Duration and factor must not be negative")
    seconds = Decimal(str(duration.total_seconds()))
    buffered = (seconds * (Decimal(1) + factor)).to_integral_value(rounding=ROUND_CEILING)
    return timedelta(seconds=int(buffered))


def internal_start_before_external_deadline(
    external_deadline: datetime,
    planned_duration: timedelta,
    factor: Decimal = Decimal("0.20"),
) -> datetime:
    if external_deadline.tzinfo is None:
        raise ValueError("Deadline must have an explicit timezone")
    return external_deadline - with_contingency(planned_duration, factor)
