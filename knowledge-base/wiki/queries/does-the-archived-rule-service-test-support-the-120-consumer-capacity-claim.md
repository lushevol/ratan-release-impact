---
type: query
title: Does the Archived Rule-Service Test Support the 120-Consumer Capacity Claim?
created: 2026-08-24
updated: 2026-08-24
tags: [capacity-planning, performance-testing, ratan-one, rule-service, archived]
related: [rule-service-performance-testing, ratan-one-rule-service, what-caused-rule-service-throughput-to-plateau-below-31-percent-cpu]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]
---
# Does the Archived Rule-Service Test Support the 120-Consumer Capacity Claim?

## Current assessment

No. The archived report records a `PASS` conclusion for six instances and 120 consumer applications, but the documented results cover only one trade-validation scenario with up to 30 concurrent users. There is no stated workload model connecting a consumer application to request rate, concurrency, payload mix, rule complexity, or instance distribution.

## Evidence gap

The report also lacks:

- Results for the stated 60-concurrent-user target.
- A 12-hour 1x-load soak result.
- Cluster-wide testing across six instances.
- An end-to-end work mix for declared upstream and downstream interfaces.
- Production-equivalence evidence beyond broadly similar server specifications.
- Raw JMeter reports needed to verify the malformed first results row and calculate mean latency.

## Required resolution evidence

Obtain the original JMeter `.jtl` files, HTML reports, and exact `.jmx` version from `ratanone-performancetest-api`. Define a consumer traffic model and conduct representative cluster tests covering peak and endurance conditions. Acceptance criteria should separately assess mean latency, high-percentile latency, errors, throughput, resource use, and dependency behaviour.

See [[rule-service-performance-testing]] and [[ratan-one-rule-service]].