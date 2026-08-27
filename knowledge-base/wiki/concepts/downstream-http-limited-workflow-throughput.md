---
type: concept
title: Downstream HTTP-Limited Workflow Throughput
tags: [http, latency, throughput, camunda, orchestration, performance]
related: [synchronous-kafka-to-camunda-orchestration, orchestration, camunda, group-service, cashflow-lifecycle-service, cash-settlement-performance-and-stress-testing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Orchestration Stg.md"]
---
# Downstream HTTP-Limited Workflow Throughput

Downstream HTTP latency is the largest measured contributor to Cash Settlement workflow-start time in the staging orchestration study. Across STG-A, STG-B, and STG-C, `http_sum` was 1,210.9–1,489.9 ms and represented 50.7%–56.1% of the measured runtime.

Because [[concepts/synchronous-kafka-to-camunda-orchestration]] keeps consumer threads occupied through inline BPMN execution, remote-call latency directly limits Kafka consumption throughput.

## Priority Hotspots

The recurring calls identified by the study are:

- `msgEventCheck`
- `cashflow/stamp`
- `status/move`
- `checkPaymentDateForIRS`
- `netForIRS`
- `preCheck`

`status/move` was invoked 136 times in STG-C, twice the frequency of the other listed calls. Its cumulative cost may therefore be substantial despite a lower per-call average.

## Optimization Priority

The study supports prioritizing high-contribution remote calls and reducing avoidable synchronous steps over micro-optimizing Kafka commit, raw-message processing, or pre-workflow processing. Raw-message processing was 19.1–29.7 ms, pre-workflow processing was 52.1–73.6 ms, and Kafka commit was 13.0–16.9 ms.

The evidence does not yet quantify endpoint contribution across the entire workflow, establish service-side causes, or show whether changes preserve workflow semantics. See [[queries/which-downstream-http-calls-have-the-largest-end-to-end-orchestration-latency-contribution]].