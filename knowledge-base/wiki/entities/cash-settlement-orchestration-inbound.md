---
type: entity
title: Cash_Settlement_Orchestration_Inbound
tags: [kafka, topic, cash-settlement, orchestration]
related: [kafka, orchestration, camunda, synchronous-kafka-to-camunda-orchestration, downstream-http-limited-workflow-throughput]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Orchestration Stg.md"]
---
# Cash_Settlement_Orchestration_Inbound

`Cash_Settlement_Orchestration_Inbound` is the Kafka topic used to feed Cash Settlement orchestration processing in the staging performance study.

The study tested 36 and 72 partitions with total consumer-thread counts of 9 and 18. For the 56,000-cashflow worst-case workload, the 36-partition/9-thread configuration completed in 6,255 seconds, while the 72-partition/18-thread configuration completed in 5,027 seconds.

This evidence shows that additional partitions and consumers improved elapsed time in this specific environment, but did not deliver linear scaling. The synchronous workflow path described in [[concepts/synchronous-kafka-to-camunda-orchestration]] and high dependent-service CPU utilization constrained effective parallelism.

See [[entities/kafka]] and [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--20-p--ws3t1t]].