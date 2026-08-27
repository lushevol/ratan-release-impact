---
type: source
title: PT Orchestration Stg
authors: []
year: 2026
url: ""
venue: Internal technical design documentation
tags: [cash-settlement, performance-testing, staging, orchestration, kafka, camunda]
related: [orchestration, kafka, camunda, group-service, cashflow-lifecycle-service, cash-settlement-performance-and-stress-testing, synchronous-kafka-to-camunda-orchestration, downstream-http-limited-workflow-throughput, cash-settlement-orchestration-inbound, what-is-the-optimal-orchestration-capacity-and-kafka-concurrency-for-uber-volume, which-downstream-http-calls-have-the-largest-end-to-end-orchestration-latency-contribution]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Orchestration Stg.md"]
---
# PT Orchestration Stg

This staging performance study assesses Cash Settlement orchestration after Uber settlement integration. It tests Kafka partitions and consumer-thread counts for a 56,000-cashflow workload, then analyzes three staging runtime datasets.

## Environment

```text
service: orchestration

staging:  Instance count：4

JVM： -Xms1024m -Xmx2048m
DB connections: miniIdle: 4, maxPoolSize: 20
```

## 56,000-Cashflow Test Summary

| | Scene A: partition:36, total consumer thread: 9 | Scene B: partition:36, total consumer thread: 18 | Scene C: partition:72, total consumer thread: 9 | Scene D: partition:72, total consumer thread: 18 | conclusion |
| --- | --- | --- | --- | --- | --- |
| total cost time | 104 m 15 s = 6255s | 98 m 47 s = 5927s | 88 m 7s = 5287s | 83 m 47s = 5027s | Scene D is 21 minutes shorter than Scene A. |
| db connections （active connections） | group : 30 lifecycle : 6 orchestration : 9 | group : 24 lifecycle : 6 orchestration : 11 | group : 21 lifecycle : 5 orchestration : 9 | group : 24 lifecycle : 7 orchestration : 18 | The number of db connections in scenario D also doubled. |
| CPU（max） | group : 90.4 lifecycle : 92.3 orchestration : 88.2 | group : 95.1 lifecycle : 96.4 orchestration : 94.4 | group : 98.3 lifecycle: 97.6 orchestration : 98.0 | group : 98.2 lifecycle : 99.1 orchestration : 99.7 | Maximum CPU usage close to 100% |

The combined change from Scene A to Scene D reduced elapsed time by 1,228 seconds (about 19.6%). This is an improvement, but not proportional to doubling both partitions and consumer threads. CPU was near saturation across [[entities/orchestration]], [[entities/group-service]], and [[entities/cashflow-lifecycle-service]] in the fastest scenario.

The statement that database connections “also doubled” is only supported for Orchestration active connections (9 to 18); Group declined from 30 to 24 and Lifecycle rose from 6 to 7.

## Detailed 36-Partition Results

**topic: `Cash_Settlement_Orchestration_Inbound`， partition：36**

| Conditions | Scenario | group cost time | orchestration cost time | result |
| --- | --- | --- | --- | --- |
| 1 trade and 40 cashflows | Send messages to 7 topics, each with 200 messages. Each message has a completely different cashflowId, meaning the group will not filter any cashflows, which is the worst-case scenario. consumersCount： 9 | start time: 2026-08-14 20:07:49 end time: 2026-08-14 20:12:19 total cost: 4m30s = 270s Total count of messages : 1400 total count of cashflow: 5.6W | start time: 2026-08-14 20:07:57 end time: 2026-08-14 21:52:12 total cost: 104m15s = 6255s | no error logs group max cpu: 90.4 lifecycle max cpu: 92.3 orchestration max cpu: 88.2 group db active connections used: 30 lifecycle db active connections used: 6 orchestration db active connections used: 9 |
| 1 trade and 40 cashflows | Send messages to 7 topics, each with 200 messages. Each message has a completely different cashflowId, meaning the group will not filter any cashflows, which is the worst-case scenario. consumersCount： 18 | start time: 2026-08-13 23:16:58 end time: 2026-08-13 23:21:09 total cost: 4m7s = 247s Total count of messages : 1400 total count of cashflow: 5.6W | start time: 2026-08-13 23:17:09 end time: 2026-08-14 00:55:56 total cost: 98m47s = 5927s | no error logs group max cpu: 95.1 lifecycle max cpu: 96.4 orchestration max cpu: 94.4 group db active connections used: 24 lifecycle db active connections used: 6 orchestration db active connections used: 11 |

## Detailed 72-Partition Results

**topic: `Cash_Settlement_Orchestration_Inbound`， partition：72**

| Conditions | Scenario | group cost time | orchestration cost time | result |
| --- | --- | --- | --- | --- |
| 1 trade and 40 cashflows | Send messages to 7 topics, each with 200 messages. Each message has a completely different cashflowId, meaning the group will not filter any cashflows, which is the worst-case scenario. consumersCount： 9 | start time: 2026-08-15 15:32:14 end time: 2026-08-15 15:36:33 total cost: 4 m 19 s = 259 s Total count of messages : 1400 total count of cashflow: 5.6W | start time: 2026-08-15 15:32:19 end time: 2026-08-15 17:00:26 total cost: 88 m 7s = 5287s | no error logs group max cpu: 98.3 lifecycle max cpu: 97.6 orchestration max cpu: 98.0 group db active connections used: 21 lifecycle db active connections used: 5 orchestration db active connections used: 9 |
| 1 trade and 40 cashflows | Send messages to 7 topics, each with 200 messages. Each message has a completely different cashflowId, meaning the group will not filter any cashflows, which is the worst-case scenario. consumersCount： 18 | start time: 2026-08-15 17:32:09 end time: 2026-08-15 17:37:19 total cost: 5 m 10 s = 310 s Total count of messages : 1400 total count of cashflow: 5.6W | start time: 2026-08-15 17:32:19 end time: 2026-08-15 18:56:06 total cost: 83 m 47s = 5027s | no error logs group max cpu: 98.2 lifecycle max cpu: 99.1 orchestration max cpu: 99.7 group db active connections used: 24 lifecycle db active connections used: 7 orchestration db active connections used: 18 |

## Processing Path

```text
Kafka consume
-> RawMessage / DuplicationCheck
-> PublishEventProcessor
-> WorkflowProcessor#startConfirmationFlow
-> Camunda startProcessInstanceByKey(...)
-> inline BPMN progression
-> CommitKafkaOffsetProcessor
```

The source identifies this as a synchronous chain: a consumer thread remains occupied while Camunda progresses the process and makes downstream calls, and the offset is committed only after `startProcessInstanceByKey(...)` returns. See [[concepts/synchronous-kafka-to-camunda-orchestration]].

## STG Runtime Dataset Comparison

| Metric | STG-A | STG-B | STG-C | Class Or Method |
| --- | --- | --- | --- | --- |
| Complete samples | 21 | 40 | 33 | |
| `raw-message` avg | 19.1ms | 29.7ms | 19.6ms | RawMessageProcessor |
| `pre-workflow` avg | 53.5ms | 73.6ms | 52.1ms | WorkflowProcessor#doProcess |
| `start-process-instance-by-key` avg | 2655.5ms | 2863.4ms | 2260.6ms | WorkflowProcessor.startProcessInstance |
| `end-to-end-consume-to-commit` avg | 2751.1m | 2998.6ms | `2357.6ms | CommitKafkaOffsetProcessor#doProcess |
| `kafka-commit` avg | 13.0ms | 16.9ms | 15.9ms | CommitKafkaOffsetProcessor#doProcess |
| `service_sum` avg | 1971.7ms | 2050.9ms | 1650.2ms | BaseJavaDelegate#execute |
| `http_sum` avg | 1489.9ms | 1451.5ms | 1210.9ms | call downstream-http |

| Component | STG-A | STG-B | STG-C |
| --- | --- | --- | --- |
| Downstream HTTP share | 56.1% | `50.7% | 53.6% |
| Task-local processing share | 18.1% | 20.9% | 19.4% |
| Camunda / process-progression share | 25.8% | `28.4% | 27.0% |

The documented baseline spans approximately 2.3–3.0 seconds. The STG-A `2751.1m` value and unmatched backticks are retained verbatim from the source and should be validated before being used as an authoritative measurement.

## Stable HTTP Hotspots

| Endpoint | Count | Avg (ms) | Max (ms) |
| --- | --- | --- | --- |
| /v1/ratan/camunda/lifecycle/msgEventCheck | 68 | 242.2 | 306 |
| /v2/ratan/camunda/cashflow/stamp | 68 | 205.6 | 321 |
| /v1/netting/camunda/checkPaymentDateForIRS | 68 | 172.6 | 300 |
| /v2/ratan/camunda/lifecycle/status/move | 136 | 129.1 | 226 |
| /v2/ratan/camunda/cashflow/preCheck | 68 | 128.7 | 195 |
| /v1/netting/camunda/netForIRS | 68 | 124.3 | 225 |

| Hotspot | STG-B Avg (ms) | STG-C Avg (ms) | Change |
| --- | --- | --- | --- |
| msgEventCheck | 351.9 | 242.2 | Significant improvement |
| cashflow/stamp | 201.7 | 205.6 | Roughly flat |
| status/move | 127.8 | 129.1 | Roughly flat |
| checkPaymentDateForIRS | 155.5 | 172.6 | Slightly higher |
| preCheck | 148.2 | 128.7 | Significant improvement |
| netForIRS | 142.4 | 124.3 | Significant improvement |

Downstream HTTP accounts for 50.7%–56.1% of observed process-start runtime. `status/move` has a lower average latency than some calls but occurs twice as often, so its cumulative contribution requires explicit call-count-weighted analysis. See [[concepts/downstream-http-limited-workflow-throughput]] and [[queries/which-downstream-http-calls-have-the-largest-end-to-end-orchestration-latency-contribution]].

## Limitations

“No error logs” does not establish processing completeness, absence of retries or duplicates, or business-level correctness. The test matrix has no repeated runs, tail percentiles, service-side CPU profiles, or independent server-capacity scaling experiment. Consequently, it does not determine the optimal coordinated configuration for Uber volume.