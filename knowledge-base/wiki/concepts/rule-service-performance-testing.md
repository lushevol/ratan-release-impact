---
type: concept
title: Rule Service Performance Testing
created: 2026-08-24
updated: 2026-08-24
tags: [performance-testing, api-load-testing, rule-engine, capacity-planning, non-functional-requirements]
related: [ratan-one-rule-service, does-the-archived-rule-service-test-support-the-120-consumer-capacity-claim, what-caused-rule-service-throughput-to-plateau-below-31-percent-cpu, dynamic-drl-compilation, rule-engine-session-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]
---
# Rule Service Performance Testing

Rule-service performance testing measures the behaviour of a rule-evaluation API under a defined workload. It must distinguish performance of the complete service path from performance attributable to a rule engine alone.

The archived [[rule-service-performance-testing]] record illustrates why a test plan needs explicit workload, acceptance, and environment evidence.

## Essential evidence

A usable performance conclusion should document:

- API operations, business flows, rule types, payload-size distribution, and product mix.
- Rule-engine version, rule count, compilation or refresh approach, and [[rule-engine-session-lifecycle]].
- Concurrency, arrival rate, duration, warm-up, pacing, retries, and load-generator capacity.
- Mean, median, percentile latency, throughput, error definitions, and functional validation.
- Per-instance and cluster-wide load distribution, including load-balancer behaviour.
- CPU, memory, I/O, garbage collection, thread pools, connection pools, datastore metrics, and downstream latency.
- Production-parity evidence for deployment topology, data, configuration, dependencies, and network paths.

## NFR traceability

Each stated NFR requires direct evidence:

- A maximum-concurrency target needs execution at that concurrency or an explicit validated capacity model.
- An average-latency target requires reported mean latency; percentile metrics alone cannot prove or disprove it.
- A soak requirement needs sustained execution for the required duration.
- Fleet capacity requires cluster-level testing or a documented, validated scaling model rather than multiplication of one run's result.

## Interpretation cautions

Low CPU does not prove available capacity. A throughput plateau with low CPU can indicate external dependency latency, locking, rule-session contention, thread or connection-pool limits, I/O waits, garbage collection, serialization costs, or load-generator constraints.

Likewise, nominally similar host specifications do not establish production equivalence. Topology, configuration, data volume, dependency performance, and traffic characteristics can materially affect results.

Performance claims involving dynamic rule loading or [[dynamic-drl-compilation]] are not transferable without the tested implementation details.