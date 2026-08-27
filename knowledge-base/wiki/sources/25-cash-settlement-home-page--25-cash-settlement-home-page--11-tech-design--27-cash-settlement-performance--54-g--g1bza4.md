---
type: source
title: Multi-Topic Uber Message Consumption Performance Test
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, performance-testing, kafka, uber-messages, database-connection-pool]
related: [kafka, fmrp2, staging, uber-message-topics, multi-topic-kafka-consumer-parallelism, database-connection-pool-saturation, what-partition-and-db-pool-configuration-sustains-uber-message-load, cash-settlement-performance-and-stress-testing, synchronous-kafka-to-camunda-orchestration, cashflow-lifecycle-service, orchestration, grouping-management-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"]
authors: []
year: 2026
url: ""
venue: "Cash Settlement Performance"
---
# Multi-Topic Uber Message Consumption Performance Test

## Purpose

This test evaluates distributing Uber messages across seven Kafka topics rather than consuming from one topic. It compares fmrp2 and staging configurations across partition counts, payload sizes, and database connection-pool limits.

The source has no written conclusion. Its observations should therefore be treated as preliminary test evidence rather than an approved production configuration.

## Test Topology

The seven-topic topology uses [[uber-message-topics]] on [[kafka]]:

```text
tdsx_uber_message_json_inbound_fx_other
tdsx_uber_message_json_inbound_fx_spot
tdsx_uber_message_json_inbound_equity
tdsx_uber_message_json_inbound_cash
tdsx_uber_message_json_inbound_commodity
tdsx_uber_message_json_inbound_interestrate
tdsx_uber_message_json_inbound_loan
```

The observed pipeline includes Group or [[grouping-management-service]], [[cashflow-lifecycle-service]], [[orchestration]], and the database. Topic-level parallelism did not remove downstream capacity constraints.

## Environment Configuration

| Environment | Instance count | Configured partitions | Active partitions / concurrencies | Consumer concurrency | DB pool |
|---|---:|---:|---:|---:|---|
| [[fmrp2]] | 3 | 12 | 9 | 3 | min 2, max 8 |
| [[staging]] | 4 | 12 | 12 | 3 | min 2, max 24 or max 56 |

The fmrp2 and staging results are not a controlled environment comparison because active partition concurrency and database-pool limits differ.

## fmrp2 Results

| Scenario | Time | Send TPS | Result | Remark |
|---|---|---:|---|---|
| 1 trade and 40 cashflows; distribute 100 messages to 7 topics in 50 seconds | 07-13 10:16 | 2 | max consume TPS: 0.467; Group max CPU: 81.7% | No exception |
| 1 trade and 40 cashflows; distribute 100 messages to 7 topics in 25 seconds | 07-13 10:30 | 3 | max consume TPS: 2.14; Group max CPU: 83.2% | No exception |
| 1 trade and 40 cashflows; distribute 100 messages to 7 topics in 25 seconds | 07-13 09:38 | 4 | max consume TPS: 0.418; Group max CPU: 82.8% | DB timeout; DB connection limit reached |
| 1 trade and 40 cashflows; distribute 100 messages to 7 topics in 20 seconds | 07-06 09:10 | 5 | max consume TPS: 2.52; Group max CPU: 68.0% | DB timeout; DB connection limit reached |
| 1 trade and 12 cashflows; distribute 1,000 messages to 7 topics in 250 seconds | 07-06 10:34 | 4 | max consume TPS: 3.35; Group max CPU: 69.8% | No exception |
| 1 trade and 12 cashflows; distribute 1,000 messages to 7 topics in 200 seconds | 07-06 10:52 | 5 | max consume TPS: 3.28; Group max CPU: 72.5% | No exception |
| 1 trade and 12 cashflows; distribute 1,000 messages to 7 topics in 166 seconds | 07-07 09:06 | 6 | max consume TPS: 2.98; Group max CPU: 90.8% | DB timeout; DB connection limit reached |
| 1 trade and 6 cashflows; distribute 1,000 messages to 7 topics in 100 seconds | 07-06 09:35 | 10 | max consume TPS: 3.33; Group max CPU: 72.9% | No exception |
| 1 trade and 6 cashflows; distribute 1,000 messages to 7 topics in 83 seconds | 07-06 09:43 | 12 | max consume TPS: 3.08; Group max CPU: 74.8% | No exception |
| 1 trade and 6 cashflows; distribute 1,000 messages to 7 topics in 72 seconds | 07-14 13:11 | 14 | max consume TPS: 3.23; Group max CPU: 81.1% | DB timeout; DB connection limit reached |
| 1 trade and 6 cashflows; distribute 1,000 messages to 7 topics in 63 seconds | 07-13 13:19 | 16 |  | DB timeout; DB connection limit reached |

For successful fmrp2 tests, reported maximum consumer TPS was approximately 3 TPS for the 6- and 12-cashflow payloads. Higher ingress rates were associated with database timeout and connection-limit errors rather than demonstrably higher sustained consumer throughput.

## Staging Results

| Partition configuration | Payload | DB pool | Scenario | Time to lag = 0 | Average cashflow count `(total count / total second) * 40` | Result / observations |
|---|---|---|---|---|---:|---|
| 6 partitions | 1 trade and 6 cashflows | min 2, max 24 | Each topic contains about 1,000 messages; 7 topics | 07-20 19:57:05 to 20:08:00; 655s; total count: 7,000 | 64 | No exception. Group max CPU: 87.4%; lifecycle: 86.4%; orchestration: 88.7%; Kafka consume TPS: 3.37. |
| 6 partitions | 1 trade and 12 cashflows | min 2, max 24 | Each topic contains about 1,000 messages; 7 topics | 07-20 20:32:21 to 20:46:36; 855s; total count: 7,000 | 98.2 | No exception. Group max CPU: 86.9%; lifecycle: 89.4%; orchestration: 86.8%; Kafka consume TPS: 1.62. |
| 6 partitions | 1 trade and 40 cashflows | min 2, max 24 | Each topic contains about 1,000 messages; 7 topics | 07-20 21:06:10 to 21:51:00; 2,690s; total count: 9,379, including retries | 139.4 | No exception. Group max CPU: 87.6%; lifecycle: 87.5%; orchestration: 87.8%; Kafka consume TPS: 1.78. |
| 12 partitions | 1 trade and 6 cashflows | min 2, max 24 | Each topic contains about 1,000 messages; 7 topics | 07-20 22:03:19 to 22:10:30; 431s; total count: 7,000 | 97.4 | No exception. Group max CPU: 84.4%; lifecycle: 84.1%; orchestration: 85.3%; Kafka consume TPS: 1.56. |
| 12 partitions | 1 trade and 6 cashflows | min 2, max 56 | Each topic contains about 1,000 messages; 7 topics | 07-21 20:03:39 to 20:10:30; 411s; total count: 7,000 | 102 | Group max CPU: 92.0%; lifecycle: 91.5%; orchestration: 87.3%; Kafka consume TPS: 1.62. |
| 12 partitions | 1 trade and 12 cashflows | min 2, max 24 | Each topic contains about 1,000 messages; 7 topics | 07-20 22:13:50 to 22:28:10; 860s; total count: 7,000 | 97.6 | No exception. Group max CPU: 87.2%; lifecycle: 87.1%; orchestration: 87.6%; Kafka consume TPS: 3.03. |
| 12 partitions | 1 trade and 12 cashflows | min 2, max 56 | Each topic contains about 1,000 messages; 7 topics | 07-21 20:16:15 to 20:29:05; 770s; total count: 7,327, including retries | 114 | Group max CPU: 84.0%; lifecycle: 88.5%; orchestration: 84.3%; Kafka consume TPS: 1.79. |
| 12 partitions | 1 trade and 40 cashflows | min 2, max 56 | Each topic contains about 1,000 messages; 7 topics | 07-21 20:41:52 to 21:19:37; 2,265s; total count: 7,000 | 123 | Reference: `153 SCBML: 137`. Uber message handling completed; total time cost: `16.186403032`. |

For the comparable 6-cashflow, pool-max-24 runs, increasing active partitions from 6 to 12 reduced completion time from 655 seconds to 431 seconds. This is a 34% reduction in elapsed time.

## Recorded Seven-Topic Dispatch

The 100-message, 20-second fmrp2 run reported the following source dispatch:

```text
2026-07-06 09:10:11,202 [INFO] Total send seconds: 20.050
2026-07-06 09:10:11,202 [INFO] Total send TPS: 4.99
2026-07-06 09:10:11,202 [INFO] Done. generated=100 sent=100
2026-07-06 09:10:11,202 [INFO] Topic dispatch summary:
2026-07-06 09:10:11,202 [INFO]   tdsx_uber_message_json_inbound_fx_other -> 18
2026-07-06 09:10:11,202 [INFO]   tdsx_uber_message_json_inbound_fx_spot -> 13
2026-07-06 09:10:11,202 [INFO]   tdsx_uber_message_json_inbound_equity -> 11
2026-07-06 09:10:11,202 [INFO]   tdsx_uber_message_json_inbound_cash -> 13
2026-07-06 09:10:11,202 [INFO]   tdsx_uber_message_json_inbound_commodity -> 13
2026-07-06 09:10:11,202 [INFO]   tdsx_uber_message_json_inbound_interestrate -> 19
2026-07-06 09:10:11,202 [INFO]   tdsx_uber_message_json_inbound_loan -> 13
```

The source explicitly reports that a database exception caused messages to enter the topic retry queue, with “Database connection timed out, connection limit reached.”

## Interpretation Limits

- The source labels the reported calculation as `(total count / total second) * 40`, but values such as `64` for 7,000 messages in 655 seconds align with multiplication by 6, not 40. The metric definition or heading requires correction.
- Reported Kafka consume TPS does not align with elapsed-time-derived message rates. For example, 7,000 messages in 431 seconds is about 16.2 messages per second, whereas the reported Kafka consume TPS is 1.56. The source does not define the latter metric.
- Runs that include retries cannot be directly compared with runs processing exactly 7,000 records.
- The available data does not establish that a pool maximum of 56 is optimal.
- CPU maxima of approximately 84% to 92% show material utilization but do not independently prove a CPU bottleneck or identify one service as the sole constraint.
- No database connection utilization, wait-time, database-side connection-limit, query-duration, or transaction-duration measurements are provided.

## Related Investigation

[[multi-topic-kafka-consumer-parallelism]] describes why topic splitting raises available Kafka parallelism but cannot bypass downstream limits. [[database-connection-pool-saturation]] captures the observed fmrp2 failure mechanism.

The unresolved production sizing decision is tracked in [[what-partition-and-db-pool-configuration-sustains-uber-message-load]].