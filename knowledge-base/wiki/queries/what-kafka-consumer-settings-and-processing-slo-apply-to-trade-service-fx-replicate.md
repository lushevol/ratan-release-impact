---
type: query
title: What Kafka Consumer Settings and Processing SLO Apply to Trade Service FX Replicate?
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, trade-service, fx-replication, consumer-lag, slo, configuration]
related: [ratanone-trade-service, kafka-consumer-poll-timeout, environment-specific-kafka-consumer-configuration, tds3, rule-service, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka consumer issue for large lag during drop3 migration testing.md"]
---
# What Kafka Consumer Settings and Processing SLO Apply to Trade Service FX Replicate?

## Question

What Kafka configuration values, workload assumptions, and measurable performance objectives govern the `ratanone-trade-service-fx-replicate` consumer?

## Known Evidence

A 19 March 2024 warning confirms that the Trade service consumer exceeded `max.poll.interval.ms`. The source reports deployment of `max.poll.interval.ms` and `session.timeout.ms` changes to EKS, plus SCBML-to-JSON parsing optimization through [[rule-service]].

A later Drop3 rerun was reported to have no Trade service lag or delay, but the source supplies neither settings values nor performance measurements.

## Information Needed

- Exact deployed values for `max.poll.interval.ms`, `session.timeout.ms`, and `max.poll.records`.
- Kafka topic names, partition counts, consumer concurrency, assignment behavior, and message-size distribution.
- Before-and-after consumer lag, processing-time, throughput, and rebalance metrics.
- Peak and sustained test-load profile used for the reported successful rerun.
- A processing SLO and consumer-lag threshold that define acceptable operation.
- Controlled evidence separating the impact of configuration changes from the [[rule-service]] SCBML parsing optimization.
- EKS and UAT comparisons for CPU, memory, throttling, networking, pod scaling, Kafka-client configuration, and workload.
- The rule and accountable owner for applying these settings to other application services.

## Why It Matters

Without these details, the reported closure demonstrates an encouraging operational observation but cannot establish a reusable Kafka configuration baseline or a verified root cause for the EKS incident.