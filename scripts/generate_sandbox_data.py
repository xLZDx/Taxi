"""Offline CSV fixture generator for an entirely synthetic Planfix lab."""

import argparse
from pathlib import Path

from taxi_platform.sandbox_data import write_synthetic_fleet


def main() -> int:
    parser = argparse.ArgumentParser(description="Write synthetic Planfix lab CSV data")
    parser.add_argument("--vehicles", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=Path, default=Path("artifacts/sandbox"))
    args = parser.parse_args()
    manifest = write_synthetic_fleet(
        args.output, vehicles=args.vehicles, seed=args.seed
    )
    print(
        f"SYNTHETIC ONLY: {manifest['vehicles']} vehicles, "
        f"{manifest['drivers']} drivers, "
        f"{manifest['exception_tasks']} Planfix task candidates."
    )
    print(f"CSV output: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
