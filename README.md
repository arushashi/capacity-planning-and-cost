# capacity-planning-and-cost

Simple, honest tools and checklists for **capacity planning** and **cloud cost control**.

| Path | Purpose |
|---|---|
| `tools/capacity.py` | Calculates required replicas from traffic, per-instance capacity, headroom and N+1 redundancy; forecasts growth |
| `tests/` | Unit tests for the calculator |
| `docs/capacity-planning.md` | Method: measure, model, load-test, add headroom, review |
| `docs/cloud-cost-checklist.md` | Practical savings checklist (compute, storage, network, observability) |

## Example

```bash
# 1200 requests/s peak, one instance handles 150 rps, 30% headroom, survive one failure
python tools/capacity.py --peak-rps 1200 --per-instance-rps 150 --headroom 0.3 --redundancy 1

# forecast 8% monthly growth for 12 months
python tools/capacity.py --peak-rps 1200 --per-instance-rps 150 --growth 0.08 --months 12
```

Output (first example): `Instances needed now: 13`. Usable capacity per instance is 150 x 0.7 = 105 rps, so 1200 / 105 = 11.4, rounded up to 12, plus 1 spare for a failure. See the formula in `docs/capacity-planning.md`.

## License

MIT
