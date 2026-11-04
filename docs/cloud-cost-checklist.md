# Cloud cost checklist

## Visibility
- [ ] Tag every resource with owner, environment and cost centre
- [ ] Budgets and anomaly alerts per subscription/team
- [ ] Weekly cost review; show cost per request or per customer, not just total

## Compute
- [ ] Right-size using real CPU/memory data (often 30-50% over-provisioned)
- [ ] Autoscale; scale to a small floor out of hours in non-prod
- [ ] Stop or delete idle dev/test VMs and clusters on a schedule
- [ ] Spot/preemptible instances for fault-tolerant batch work
- [ ] Reserved instances or savings plans for the steady baseline only
- [ ] Prefer newer instance generations (better price/performance)

## Kubernetes
- [ ] Set requests close to real usage; avoid giant limits that block bin-packing
- [ ] Cluster autoscaler scale-down enabled; remove unused node pools
- [ ] Namespace quotas and cost allocation (labels)

## Storage
- [ ] Delete unattached disks and old snapshots
- [ ] Lifecycle rules: move cold data to cheaper tiers, expire temporary data
- [ ] Right-size provisioned IOPS/throughput

## Network
- [ ] Keep chatty services in the same zone/region where safe
- [ ] Use CDN/caching to cut egress
- [ ] Review NAT gateway and cross-zone traffic costs

## Observability
- [ ] Drop noisy logs at the source; sample traces
- [ ] Set retention by value (e.g. 30 days hot, archive the rest)
- [ ] Limit high-cardinality metric labels

## Governance
- [ ] Cost is a design input in reviews, with an estimate before launch
- [ ] Decommission checklist when services retire
