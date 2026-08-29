---
type: source
title: Netting Performance Test
authors: []
year: 2025
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [netting, performance-testing, un-net, withdrawal-retry, murex]
related: [netting-service, murex, netting-service-performance-testing, what-are-the-netting-service-performance-slos-and-test-conditions, does-netting-service-meet-peak-murex-volume-and-retry-resilience-requirements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design/Netting performance test.md"]
---
# Netting Performance Test

This internal note records point performance-test outcomes for Netting, Un-net, and a combined Netting and Withdrawal scenario. Each recorded execution is marked successful, but the source does not define the test environment, service version, dataset composition, concurrency, timing boundaries, repetition count, or performance acceptance threshold.

## Standalone Netting

| Netting number | Back end (Second) | Success |
| --- | ---: | --- |
| 2000 | 53 | true |
| 3400 | 83 | true |

The document records successful Netting completion for 2,000 items in 53 seconds and 3,400 items in 83 seconds.

## Standalone Un-net

| Unnet number | Back end (Second) | Success |
| --- | ---: | --- |
| 2000 | 47 | true |
| 3400 | 78 | true |

The document records successful Un-net completion for 2,000 items in 47 seconds and 3,400 items in 78 seconds.

Within these reported standalone cases, Un-net is 6 seconds faster than Netting at 2,000 items and 5 seconds faster at 3,400 items. These are scenario-specific observations rather than evidence of a general performance characteristic.

## Netting and Withdrawal Scenario

| Operation | Total | Back end (Second) | Success |
| --- | ---: | ---: | --- |
| Net number | 1996 | 53 | true |
| Unnet | 1996 | 78 | true |
| Withdrawal retry endurance | 1 | 64 | true |

All three operations are marked successful. The source does not specify their execution order, dependencies, retry conditions, failure injection, or success criteria.

The combined-scenario Un-net result is 78 seconds for 1,996 items, compared with 47 seconds for 2,000 items in the standalone case. The source does not explain the 31-second difference, so no causal conclusion can be drawn.

A single successful withdrawal retry execution does not establish endurance, long-term stability, or retry resilience.

## Historical Murex Volume Reference

The source provides the following historical Murex volume rows verbatim.

| **M_O_OP_ID** | **M_O_ACT_NAME** | **M_O_CPU_DATE** | **Netting amount** |
| --- | --- | --- | ---: |
| 16998991 | LDCN | Jan 13 2025 12:00AM | 1960 |
| 16999104 | LDCN | Jan 13 2025 12:00AM | 1960 |
| 16962953 | LDCN | Jan 6 2025 12:00AM | 1790 |
| 16962992 | LDCN | Jan 6 2025 12:00AM | 1790 |
| 17003876 | LDCN | Jan 14 2025 12:00AM | 1482 |
| 17003923 | LDCN | Jan 14 2025 12:00AM | 1482 |
| 16995746 | LNEI | Jan 13 2025 12:00AM | 1408 |
| 16998953 | LDCN | Jan 13 2025 12:00AM | 1298 |
| 16968081 | LDCN | Jan 7 2025 12:00AM | 1250 |

The displayed historical range is 1,250–1,960 items. The 1,996- and 2,000-item tests are slightly above the displayed maximum, while the 3,400-item test is substantially higher. This sample does not establish production peak workload or explain the semantics of `LDCN`, `LNEI`, or `Netting amount`.

## Interpretation Limits

The results support only the recorded single-case outcomes. They do not demonstrate:

- A Netting Service capacity guarantee or service-level objective.
- Stable latency, percentile performance, or throughput under repeated runs.
- Behavior under concurrent load, database contention, dependent-service latency, or partial failures.
- Retry resilience or endurance beyond the one documented withdrawal retry.
- Broad production representativeness of the supplied Murex sample.

See [[netting-service-performance-testing]] for the evidence boundary and what are the netting service performance slos and test conditions for unresolved test-condition and SLO questions.