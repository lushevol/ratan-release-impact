---
type: source
title: Solace Queue Split PT for Uber
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, performance-test, staging, solace, uber, queue-splitting]
related: [solace, solace-queue-splitting-for-asset-class-workloads, queue-throughput-metric-definition, cash-settlement-performance-and-stress-testing, kafka, grouping-management-service, orchestration, what-is-the-optimal-orchestration-capacity-and-kafka-concurrency-for-uber-volume]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/solace queue split PT for Uber.md"]
authors: [Anil]
year: 2026
url: ""
venue: "Internal technical design documentation"
---
# Solace Queue Split PT for Uber

## Scope

This source records a staging performance test of an Uber inbound workload split across product-specific Solace queues.

- Environment: `staging`
- VPN: `FMEDMI2_GDCW_PT`
- Test run: 2026-05-13
- Monitoring references: log monitors, Kafka topic `tdsx_uber_message_json_inbound`, Group, and Orchestration

## Reported Performance Data

The following table is preserved verbatim from the source.

| queue name | start time | end time | total messages | total time(sec) | average rate(msg/sec) | TPS(msg/sec) |
| --- | --- | --- | --- | --- | --- | --- |
| total | 2026-05-13 17:59 PM | 2026-05-13 22:30 PM | 696547 | 16260 | 42.8 | |
| fx-other-msg | 2026-05-13 17:59:00 | 2026-05-13 18:42:48 | 31842 | 2628 | 12.1 | 23 |
| fx-spot-msg | 2026-05-13 17:59:00 | 2026-05-13 18:06:14 | 1624 | 434 | 3.7 | 17 |
| equity-msg | 2026-05-13 17:59:00 | 2026-05-13 18:03:51 | 306 | 291 | 1 | 13 |
| cash-msg | 2026-05-13 17:59:00 | 2026-05-13 18:23:45 | 13822 | 1485 | 9.3 | 19 |
| com-msg | 2026-05-13 17:59:00 | 2026-05-13 21:33:13 | 213766 | 12853 | 16.6 | 23 |
| interestrate-msg | 2026-05-13 17:59:00 | 2026-05-13 22:29:06 | 432012 | 16206 | 26.7 | 39 |
| loan-msg | 2026-05-13 17:59:00 | 2026-05-13 18:05:17 | 3173 | 377 | 8.4 | 53 |
| credit-msg | 2026-05-13 17:59:00 | 2026-05-13 17:59:04 | 2 | 4 | 0.5 | 1 |

## Observed Baseline

The combined workload processed 696,547 messages in 16,260 seconds, giving the reported elapsed-time average of 42.8 msg/s.

`interestrate-msg` was the dominant queue, processing 432,012 messages (about 62.0% of the total) and running for 16,206 seconds. `com-msg` processed 213,766 messages (about 30.7%) over 12,853 seconds. Together, these queues accounted for about 92.7% of the reported workload.

The reported run therefore provides a staging baseline for the queue-split Uber workload. It does not establish an SLA pass, production readiness, or the capacity of any individual downstream component.

## Interpretation Limits

The source does not define `TPS(msg/sec)`. Its values differ materially from each queue's run-wide average rate, so TPS must not be treated as equivalent to elapsed-time throughput without a documented calculation method. See [[queue-throughput-metric-definition]].

The included Kafka, Group, and Orchestration screenshots confirm that cross-layer monitoring was considered, but no readable metrics or interpretation are transcribed. The source therefore does not identify whether Solace, Kafka, Group, Orchestration, a database, or downstream HTTP dependencies constrained completion time.

Queue-level rates also have unequal volumes and durations. In particular, the 53 TPS reported for `loan-msg` concerns only 3,173 messages and is not evidence that the complete pipeline can sustain that rate under the dominant interest-rate workload. The two-message `credit-msg` result is not meaningful capacity evidence.

## Related Work

This result is staging evidence for [[cash-settlement-performance-and-stress-testing]]. It is relevant to [[solace-queue-splitting-for-asset-class-workloads]] and to the capacity investigation in [[what-is-the-optimal-orchestration-capacity-and-kafka-concurrency-for-uber-volume]].

The test monitored [[kafka]], [[grouping-management-service]], and [[orchestration]], but it does not demonstrate that any of those components was a bottleneck.