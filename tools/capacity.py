#!/usr/bin/env python3
"""Capacity calculator: instances needed for a target load, with headroom and redundancy."""
import argparse
import math


def instances_needed(peak_rps: float, per_instance_rps: float, headroom: float = 0.3, redundancy: int = 1) -> int:
    """Instances so that, after losing `redundancy` instances, utilisation stays under (1 - headroom).

    needed_for_load = peak / (per_instance * (1 - headroom))
    total           = ceil(needed_for_load) + redundancy
    """
    if peak_rps < 0 or per_instance_rps <= 0:
        raise ValueError("peak_rps must be >= 0 and per_instance_rps > 0")
    if not 0 <= headroom < 1:
        raise ValueError("headroom must be in [0, 1)")
    if redundancy < 0:
        raise ValueError("redundancy must be >= 0")
    usable = per_instance_rps * (1 - headroom)
    return math.ceil(peak_rps / usable) + redundancy


def forecast(peak_rps: float, monthly_growth: float, months: int):
    """Yield (month, projected peak rps) with compound growth."""
    for m in range(months + 1):
        yield m, peak_rps * (1 + monthly_growth) ** m


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--peak-rps", type=float, required=True)
    ap.add_argument("--per-instance-rps", type=float, required=True)
    ap.add_argument("--headroom", type=float, default=0.3)
    ap.add_argument("--redundancy", type=int, default=1)
    ap.add_argument("--growth", type=float, default=0.0, help="monthly growth, e.g. 0.08 = 8%%")
    ap.add_argument("--months", type=int, default=0)
    a = ap.parse_args()

    n = instances_needed(a.peak_rps, a.per_instance_rps, a.headroom, a.redundancy)
    print(f"Instances needed now: {n}")
    if a.months:
        print("month  peak_rps  instances")
        for m, rps in forecast(a.peak_rps, a.growth, a.months):
            print(f"{m:>5}  {rps:>8.0f}  {instances_needed(rps, a.per_instance_rps, a.headroom, a.redundancy):>9}")


if __name__ == "__main__":
    main()
