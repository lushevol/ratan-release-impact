---
type: concept
title: Synchronous Kafka-to-Camunda Orchestration
tags: [kafka, camunda, synchronous-processing, orchestration, offset-commit]
related: [kafka, camunda, orchestration, cash-settlement-orchestration-inbound, downstream-http-limited-workflow-throughput, cash-settlement-asynchronous-batch-processing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Orchestration Stg.md"]
---
# Synchronous Kafka-to-Camunda Orchestration

In the measured Cash Settlement `InboundRoute`, Kafka consumption, workflow creation, inline Camunda BPMN progression, and offset commit form one synchronous execution chain:

```text
Kafka consume
-> RawMessage / DuplicationCheck
-> PublishEventProcessor
-> WorkflowProcessor#startConfirmationFlow
-> Camunda startProcessInstanceByKey(...)
-> inline BPMN progression
-> CommitKafkaOffsetProcessor
```

A Kafka consumer thread remains occupied until `startProcessInstanceByKey(...)` returns. Because the offset commit follows workflow progression, latency from Camunda service tasks and their downstream dependencies becomes consumer-thread occupancy time.

## Throughput Consequence

Increasing topic partitions alone cannot provide proportional throughput when the available consumer threads spend much of their time executing synchronous work. Effective parallelism is bounded by consumer capacity, service capacity, CPU availability, and downstream-call latency.

The staging study found that changing from 36 partitions and 9 consumers to 72 partitions and 18 consumers reduced a 56,000-cashflow run from 6,255 to 5,027 seconds, rather than approaching a twofold throughput increase. This is evidence about this route and staging environment, not a general claim about Kafka or a demonstrated Camunda engine defect.

## Design Considerations

Potential improvements include eliminating duplicate remote checks, reducing synchronous service-task count, reusing intermediate results, and evaluating an asynchronous handoff only where ordering, idempotency, consistency, and offset semantics remain safe. This route should not be conflated with [[concepts/cash-settlement-asynchronous-batch-processing]], which concerns batch processing rather than inbound orchestration.

See [[concepts/downstream-http-limited-workflow-throughput]], [[entities/camunda]], and [[entities/orchestration]].