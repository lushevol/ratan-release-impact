---
type: source
title: PT Batch Group Staging Performance
authors: []
year: 2026
url: ""
venue: "Internal performance-test report"
tags: [cash-settlement, performance-testing, kafka, uber-messages, staging]
related: [ratan, kafka, 51358-ratanone-static-data-service, cash-settlement-batch-job-performance, cash-settlement-asynchronous-batch-processing, cash-settlement-static-data-batch-optimization, kafka-consumer-rebalance-risk-in-cash-settlement, cash-settlement-validation-factory-reuse]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Batch Group Stg.md"]
---
# PT Batch Group Staging Performance

## Summary

This internal report evaluates a staging deployment that splits one input topic into seven topics, with each topic consuming Uber messages for Cash Settlement group-management processing. The tested path includes `ratan-cash-settlement-group-management-service` and its dependent `ratanone-static-data-service`.

The initial staging configuration was:

```text
Instance count: 4
Partitions: 12
Concurrency: 3
DB pool: min 2, max 32
```

The tests indicate that database-connection contention and repeated single-parameter static-data operations were important bottlenecks. Batch interfaces for Materialize and Currency cutoff, increased database connections, JVM and thread-pool tuning, and validation-factory reuse were identified as optimization directions.

## Test Results

| Conditions | Scenario | Time / duration | Average cashflow count | Result and resource observations |
|---|---|---:|---:|---|
| 1 trade and 40 cashflows | Each topic sends 148 trade series. Trade states include `TOBESENT`, `SENT`, `BOOKED`, `NONCONFIRMED`, and `TOBEVALIDATED`. The `cashflowId` is consistent within a trade series and different across series. | `07-25T15:46:38 ~ 16:06:28`; 1190 seconds; 7000 messages | 235 | No ERROR/Exception log. Group CPU 97.8%; lifecycle CPU 97.2%; orchestration CPU 91.4%; Kafka consume TPS 2; maximum DB connections 25 |
| 1 trade and 40 cashflows | Same production-like trade-series scenario. | `07-26 15:20:15 ~ 15:38:21`; 1086 seconds; 7000 messages | 257.8 | No ERROR/Exception log. Group CPU 94.6%; lifecycle CPU 95.4%; orchestration CPU 95.8%; maximum DB connections 25 |
| 1 trade and 40 cashflows | Seven topics, 1000 messages per topic. Every message has a different `cashflowId`, so no cashflows are filtered. This is the worst-case scenario. | `07-25T11:21:52 ~ 13:16:31`; 6879 seconds; 7000 messages | 40.7 | Retry error logs occurred and some messages were consumed one additional time. Group CPU 96.8%; lifecycle CPU 97.9%; orchestration CPU 96%; maximum DB connections 25; 13,455 consumptions including retries |
| After JVM and thread-pool tuning | Production-like trade-series scenario. | `07-27 23:47:07 ~ 07-28 00:02:53`; 946 seconds; 7000 messages | 295.9 | No ERROR/Exception log. Group CPU 95.4%; lifecycle CPU 97.3%; orchestration CPU 98.3%; Kafka consume TPS 2.41; maximum DB connections 27 |
| After JVM and thread-pool tuning | Seven topics, 1000 messages per topic. Every message has a different `cashflowId`, so no cashflows are filtered. | `07-27 22:20:00 ~ 23:40:31`; 4831 seconds; 7000 messages | 57.9 | Retry and duplicate consumption occurred. Group CPU 98.4%; lifecycle CPU 99.1%; orchestration CPU 98.9%; Kafka consume TPS 1.95; maximum DB connections 25; 13,549 consumptions including retries |
| DB-connection increase, thread-pool tuning, and batch interface | Seven topics, 1000 messages per topic. Every message has a different `cashflowId`, so no cashflows are filtered. | `08-02 21:07:52 ~ 21:20:56`; 784 seconds; 7000 messages | 357 | Group CPU 100%; lifecycle CPU 98.7%; orchestration CPU 99.7%; maximum DB connections 28 |

The source defines average cashflow count as:

```text
(total count / total second) * 40
```

The units of this metric are not explicitly defined.

## Optimization Comparison

| Condition | Prod Behavior | Add DB connection count to static | After optimization to batch |
|---|---:|---:|---:|
| Each Uber message has 40 different cashflows, sending 168 messages to 7 topics | 2 minutes 30 seconds; TPS 44.8 | 1 minute 35 seconds; TPS 70 | 16 seconds; TPS 420 |
| Each Uber message has 40 different cashflows, sending 168 messages to 2 topics | 2 minutes 32 seconds; TPS 44.2 | 2 minutes 27 seconds; TPS 45 | 21 seconds; TPS 320 |
| Each Uber message has 40 different cashflows, sending 168 messages to 1 topic | 6 minutes 30 seconds; TPS 17 | 2 minutes 36 seconds; TPS 43 | 35 seconds; TPS 192 |

The reported comparisons show substantial directional improvement after batching:

- Seven topics: 44.8 TPS to 420 TPS.
- Two topics: 44.2 TPS to 320 TPS.
- One topic: 17 TPS to 192 TPS.

Increasing static-data database connections alone improved the reported seven-topic case from 44.8 TPS to 70 TPS. However, the final batch comparison also includes other changes, including database-connection and thread-pool changes. The exact contribution of each intervention is therefore not isolated.

## Bottlenecks

### Database connection capacity

Only four dependent static-data service instances were configured. Under high concurrency, SQL requests waited for database connections.

The evidence reported:

- Production behavior: pending database connections and latency up to 2 seconds.
- After adding database connections to the static-data service: free database connections and latency reduced to 1.2 seconds.
- After batch optimization: latency reduced to a reported maximum of 156 ms.

This finding concerns the tested `ratanone-static-data-service` path and should not be generalized to every RATAN service.

### Repeated single-parameter operations

Materialize and Currency cutoff were implemented as single-parameter operations. The report states that this resulted in approximately twice as many cashflow calls per processing cycle and a large number of SQL queries.

The proposed remedy was to provide batch SQL-query interfaces for both operations.

### Repeated validation-factory creation

The report states that the validation factory bean was frequently created under high concurrency rather than reused. The resulting overhead was attributed to repeated object allocation, additional CPU consumption, and longer processing time.

The proposed remedy was to make `validatefactory` a singleton and initialize it only once.

## Resource and Reliability Observations

The report records the following observations:

1. The overview states a maximum of 25 database connections, while later tests report maxima of 27 and 28.
2. Maximum memory usage was 2 GB.
3. Longer message-consumption times increase the likelihood of triggering Kafka's rebalance mechanism.
4. The tested workloads frequently reached more than 95% CPU utilization, with group processing reaching 100% in the final reported test.
5. Retry and duplicate consumption occurred in worst-case workloads, including after JVM and thread-pool tuning.
6. Consumption counts that include retries are not equivalent to successfully completed business messages.

The evidence does not include Kafka `max.poll.interval.ms`, poll interval, batch-size settings, partition assignments, rebalance counts, consumer lag, or the complete retry and dead-letter policy.

## Evidence Sources

The source identifies Elastic and Grafana evidence for:

- `ratan-cash-settlement-group-management-service`
- `ratanone-static-data-service`
- `TdsxUberMessageListener`
- `Uber message handling completed, total`
- Database query wait
- `validatefactory` initialization time
- CPU, memory, database connections, latency, and request counts

The source includes internal Elastic and Grafana URLs for the test observations. These links are environment-specific and may require appropriate access.

## Interpretation and Limitations

The evidence is moderate for directional conclusions and weak-to-moderate for quantified causal attribution. It supports the conclusion that database waits occurred, batch processing reduced request volume and observed latency, and the tested system approached CPU saturation.

The test rounds changed multiple variables, including JVM settings, thread-pool configuration, database-connection count, batch interfaces, topic count, workload shape, and possibly deployment topology. Consequently, the reported improvements should be attributed to the combined change set unless controlled, isolated benchmarks are available.

The production-like and worst-case scenarios also differ materially in message composition and filtering behavior despite both being labelled “1 trade and 40 cashflows.” Topic count changes partition distribution and concurrency, so the results do not prove that topic splitting alone caused the observed improvement.

## Related Wiki Pages

- [[ratan]]
- [[kafka]]
- [[51358-ratanone-static-data-service]]
- [[cash-settlement-batch-job-performance]]
- [[cash-settlement-asynchronous-batch-processing]]
- [[paginated-cashflow-batch-processing]]
- [[cash-settlement-static-data-batch-optimization]]
- [[kafka-consumer-rebalance-risk-in-cash-settlement]]
- [[cash-settlement-validation-factory-reuse]]