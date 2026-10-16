"""Deterministic, entirely synthetic Planfix lab data. Never use as accounting truth."""

import csv
import json
import random
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path


def _amount(value: Decimal) -> str:
    return f"{value:.2f}"


def build_synthetic_fleet(
    *, vehicles: int = 500, seed: int = 42
) -> tuple[dict[str, list[dict[str, str]]], dict[str, object]]:
    """Prepare CSV import rows with no personal or real fleet information."""
    if not isinstance(vehicles, int) or not 1 <= vehicles <= 1000:
        raise ValueError("Vehicle count must be an integer from 1 to 1000")

    rng = random.Random(seed)
    drivers: list[dict[str, str]] = []
    fleet: list[dict[str, str]] = []
    settlements: list[dict[str, str]] = []
    exceptions: list[dict[str, str]] = []
    total_confirmed = Decimal("0")
    total_received = Decimal("0")
    total_cleared = Decimal("0")
    unknown_count = 0
    base_date = date(2026, 10, 1)

    for n in range(1, vehicles + 1):
        driver_id = f"SYN-DRV-{n:04d}"
        vehicle_id = f"SYN-VEH-{n:04d}"
        earned = Decimal(rng.randrange(120, 281)) * Decimal("100")
        is_pending = n % 5 == 0
        report_date = base_date + timedelta(days=(14 if is_pending else 3 + n % 6))
        confirmed = None if is_pending else earned
        if confirmed is None:
            received = Decimal("0")
            cleared = Decimal("0")
            reason = "STATEMENT_PENDING"
            unknown_count += 1
        elif n % 4 == 0:
            received = confirmed
            cleared = confirmed
            reason = ""
        elif n % 4 == 1:
            received = confirmed * Decimal("0.60")
            cleared = received
            reason = "COLLECTION_PENDING"
        elif n % 4 == 2:
            received = confirmed
            cleared = received * Decimal("0.80")
            reason = "CLEARING_PENDING"
        else:
            received = Decimal("0")
            cleared = Decimal("0")
            reason = "COLLECTION_PENDING"

        drivers.append({
            "Name": f"SYNTHETIC Driver {n:04d}",
            "ExternalDriverID": driver_id,
            "ExternalVehicleID": vehicle_id,
        })
        fleet.append({
            "Name": f"SYNTHETIC Vehicle {n:04d}",
            "ExternalVehicleID": vehicle_id,
            "ExternalDriverID": driver_id,
            "State": "SYNTHETIC_SERVICE" if n % 17 == 0 else "SYNTHETIC_ACTIVE",
        })
        settlements.append({
            "TenantID": "synthetic-taxi-lab",
            "Environment": "sandbox",
            "Period": "2026-09",
            "AsOf": "2026-10-09",
            "ExternalDriverID": driver_id,
            "ExternalVehicleID": vehicle_id,
            "EarnedMDL": _amount(earned),
            "ReportExpectedOn": report_date.isoformat(),
            "ConfirmedMDL": "" if confirmed is None else _amount(confirmed),
            "ReceivedMDL": _amount(received),
            "ClearedMDL": _amount(cleared),
            "EvidenceRef": f"SYNTHETIC-{n:04d}",
            "SourceStatus": "UNKNOWN" if is_pending else "CONFIRMED",
        })
        if reason:
            exceptions.append({
                "Name": f"SYNTHETIC settlement exception {n:04d}",
                "ExternalDriverID": driver_id,
                "ExternalVehicleID": vehicle_id,
                "Reason": reason,
                "ConfirmedMDL": "" if confirmed is None else _amount(confirmed),
                "ReceivedMDL": _amount(received),
                "ClearedMDL": _amount(cleared),
                "InternalDueDate": "09-10-2026",
                "SourceStatus": "UNKNOWN" if is_pending else "CONFIRMED",
            })
        if confirmed is not None:
            total_confirmed += confirmed
        total_received += received
        total_cleared += cleared

    payout_due = total_cleared + Decimal("1000000.00")  # Synthetic shortfall injection.
    manifest: dict[str, object] = {
        "synthetic_only": True,
        "tenant": "synthetic-taxi-lab",
        "scenario": "Month-end driver reporting and investor payout stress test",
        "assumptions": [
            "One fictional driver per vehicle; this is NOT a statement about the customer fleet.",
            "All monetary amounts and documents are invented in MDL.",
            "Snapshot date is 2026-10-09; investor contractual obligation is artificial.",
            "Investor payment is set to synthetic cleared cash + MDL 1,000,000.",
            "UNKNOWN reports are not treated as confirmed zero or as collectible cash.",
            "No bank or Planfix connectivity; cleared funds are simulated, not evidenced.",
        ],
        "seed": seed,
        "vehicles": vehicles,
        "drivers": len(drivers),
        "driver_report_unknown": unknown_count,
        "exception_tasks": len(exceptions),
        "confirmed_mdl": _amount(total_confirmed),
        "received_mdl": _amount(total_received),
        "simulated_cleared_mdl": _amount(total_cleared),
        "hypothetical_investor_due_on": "2026-10-10",
        "hypothetical_investor_due_mdl": _amount(payout_due),
        "simulated_cleared_cash_gap_mdl": _amount(max(Decimal(0), payout_due - total_cleared)),
    }
    return {
        "drivers.csv": drivers,
        "vehicles.csv": fleet,
        "settlements.csv": settlements,
        "exceptions.csv": exceptions,
    }, manifest


def write_synthetic_fleet(
    output: Path, *, vehicles: int = 500, seed: int = 42
) -> dict[str, object]:
    """Write CSV + manifest; fail rather than replace existing generated files."""
    rows_by_file, manifest = build_synthetic_fleet(vehicles=vehicles, seed=seed)
    filenames = tuple(rows_by_file) + ("manifest.json",)
    if any((output / name).exists() for name in filenames):
        raise FileExistsError(f"Existing sandbox data in {output}; choose a clean folder")
    output.mkdir(parents=True, exist_ok=True)
    for filename, rows in rows_by_file.items():
        if not rows:
            raise ValueError(f"No rows to write for {filename}")
        with (output / filename).open("x", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    with (output / "manifest.json").open("x", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return manifest
