"""No production access, no real individuals or money in fixture generation."""

import csv
import json
from decimal import Decimal

import pytest

from taxi_platform.sandbox_data import build_synthetic_fleet, write_synthetic_fleet


def test_five_hundred_synthetic_fleet_rows_are_unique_and_relationships_match() -> None:
    rows, manifest = build_synthetic_fleet(vehicles=500, seed=42)
    assert len(rows["drivers.csv"]) == 500
    assert len(rows["vehicles.csv"]) == 500
    assert len(rows["settlements.csv"]) == 500
    assert manifest["synthetic_only"] is True
    driver_ids = {row["ExternalDriverID"] for row in rows["drivers.csv"]}
    vehicle_ids = {row["ExternalVehicleID"] for row in rows["vehicles.csv"]}
    assert len(driver_ids) == 500
    assert len(vehicle_ids) == 500
    assert all(row["ExternalDriverID"] in driver_ids for row in rows["vehicles.csv"])
    assert all(row["ExternalVehicleID"] in vehicle_ids for row in rows["drivers.csv"])
    assert all("SYNTHETIC" in row["Name"] for row in rows["drivers.csv"])
    assert all("SYNTHETIC" in row["Name"] for row in rows["vehicles.csv"])


def test_missing_driver_report_is_unknown_not_confirmed_zero() -> None:
    rows, manifest = build_synthetic_fleet(vehicles=500, seed=42)
    unknown = [row for row in rows["settlements.csv"] if row["SourceStatus"] == "UNKNOWN"]
    assert manifest["driver_report_unknown"] == 100
    assert len(unknown) == 100
    assert all(row["ConfirmedMDL"] == "" for row in unknown)
    assert any(row["Reason"] == "STATEMENT_PENDING" for row in rows["exceptions.csv"])


def test_confirmed_received_cleared_totals_keep_financial_distinctions() -> None:
    rows, manifest = build_synthetic_fleet(vehicles=500, seed=42)
    for row in rows["settlements.csv"]:
        if row["ConfirmedMDL"]:
            assert (
                Decimal(row["ClearedMDL"])
                <= Decimal(row["ReceivedMDL"])
                <= Decimal(row["ConfirmedMDL"])
            )
    assert Decimal(manifest["simulated_cleared_cash_gap_mdl"]) == Decimal("1000000.00")
    assert Decimal(manifest["simulated_cleared_mdl"]) < Decimal(manifest["received_mdl"])
    assert Decimal(manifest["received_mdl"]) < Decimal(manifest["confirmed_mdl"])
    assert all(row["InternalDueDate"] == "09-10-2026" for row in rows["exceptions.csv"])


def test_generator_is_deterministic_by_seed_and_rejects_bad_sizes() -> None:
    assert build_synthetic_fleet(vehicles=10, seed=9) == build_synthetic_fleet(
        vehicles=10, seed=9
    )
    with pytest.raises(ValueError):
        build_synthetic_fleet(vehicles=0)
    with pytest.raises(ValueError):
        build_synthetic_fleet(vehicles=1001)


def test_csvs_and_manifest_are_written_without_overwriting(tmp_path) -> None:
    output = tmp_path / "sandbox"
    manifest = write_synthetic_fleet(output, vehicles=15, seed=17)
    with (output / "drivers.csv").open(encoding="utf-8", newline="") as handle:
        drivers = list(csv.DictReader(handle))
    with (output / "manifest.json").open(encoding="utf-8") as handle:
        stored_manifest = json.load(handle)
    assert len(drivers) == 15
    assert stored_manifest == manifest
    assert (output / "exceptions.csv").is_file()
    with pytest.raises(FileExistsError):
        write_synthetic_fleet(output, vehicles=15, seed=17)
