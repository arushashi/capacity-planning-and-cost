# Capacity planning method

1. **Measure demand.** Peak requests per second, daily/weekly patterns, seasonal events, and growth rate. Use peaks, not averages.
2. **Measure supply.** Load-test one instance to find the throughput where latency SLO still holds (not the point where it falls over).
3. **Model it.**
   `instances = ceil(peak / (per_instance_capacity * (1 - headroom))) + redundancy`
   - *Headroom* (20-40%) absorbs spikes and gives autoscaling time to react.
   - *Redundancy* (N+1 or N+2, or a whole zone) keeps SLOs when instances or zones fail.
4. **Find the bottleneck.** The limit may be CPU, memory, connections, disk IOPS, a database or a downstream API. Scale the real constraint.
5. **Forecast.** Compound growth: `peak * (1 + g)^months`. Plan procurement or quota requests with lead time in mind.
6. **Automate where possible.** HPA / autoscale on CPU or a request-based metric; keep a floor for fast surges.
7. **Review.** Re-run after major releases and each quarter; compare forecast with reality.

## Signals that you are near the limit
- p95/p99 latency climbing while average looks fine
- CPU throttling, run queue growth, memory swapping
- Connection pool exhaustion, queue depth growing
- Autoscaler pinned at max

## Common mistakes
- Planning on averages
- Ignoring the failure case (capacity after losing a zone)
- Forgetting dependencies (database connections, API rate limits, quotas)
- Never load-testing
