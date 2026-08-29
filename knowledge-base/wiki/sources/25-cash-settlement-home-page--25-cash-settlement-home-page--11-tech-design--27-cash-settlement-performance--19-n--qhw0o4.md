---
type: source
title: Netting Cost Comparation
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, performance, benchmarking, dev, batching]
related: [netting-batch-processing-performance, which-netting-batch-strategy-meets-performance-and-correctness-requirements, what-caused-netting-performance-variance-between-2025-07-14-and-2025-07-15, netting-service, cash-settlement-performance-and-stress-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Netting Test Result/Netting Cost Comparation.md"]
authors: []
year: 2025
url: ""
venue: "Dev"
---
# Netting Cost Comparation

This source records Dev elapsed-time comparisons for `net` and `unet` processing at 596 and 1,999 cashflows. It compares the old `for each` implementation, key-holder variants using `{message_id, version}`, a manual batch-SQL variant, and `select after insert`.

The document does not define `net`, `unet`, `key holder`, the workload composition, database technology, or test controls. The measurements are therefore limited evidence from the recorded Dev runs and do not establish production performance, capacity, or an SLA.

## Recorded results

Env: Dev

| cashflows count | for each(old) | key holder (batch_size=1000, column={message_id, version}) | key holder (batch_size=200,column={message_id, version}) | key holder((manual batch SQL)) (batch_size=200,column={message_id, version}) | select after insert |
| --- | --- | --- | --- | --- | --- |
| **net** | **unet** | **net** | **unet** | **net** | **unet** | **net** | **unet** | **net** | **unet** |
| 596 (2025.07.14) | 30.78s | 28.06s | 33.13s | 27.93s | 24.03s | 21.09s |  |  | 32.13s | 23.17s |
| 1999 (2025.07.14) | 54.33s | 42.84s | 54.41s DB: 10244ms | 45.98s DB: 8947ms | 58.85s DB: 10825ms | 54.92s DB: 9068ms |  |  | 1.3min DB: 9125ms | 44.28s DB: 9946ms |
|  |  |  |  |  |  |  |  |  |  |  |
| 1999 (2025.07.15) | 40.7s | 36.19s | 40.08s DB: 5947ms | 38.28s DB: 5714ms | 33.75s DB: 5190ms (DB one batch: 568ms) | 31.62s DB: 5424ms (DB one batch: 569ms) | 36.42s DB: 6717ms (DB one batch: 595ms) | 35.06s DB: 7109ms (DB one batch: 674ms) | 38.75s DB: 5002ms (DB one batch: 496ms, DB one batch query: 5ms) | 38.78s DB: 5097ms (DB one batch: 451ms, DB one batch query: 3ms) |

## Recorded observations

At 1,999 cashflows on 2025.07.15, the key-holder variant with batch size 200 had the lowest recorded total duration among complete alternatives: 33.75s for `net` and 31.62s for `unet`.

`select after insert` reported the lowest aggregate DB times in that run, but not the lowest end-to-end durations. Aggregate DB time alone is therefore not sufficient to select an implementation.

The old implementation and the batch-size-1,000 key-holder implementation changed materially across the two 1,999-cashflow test dates. Cross-date comparisons require caution because the source provides no information about environment stability, concurrent load, data state, warm-up, or repeated trials.

The manual batch-SQL result was fastest at 596 cashflows, but at 1,999 cashflows on 2025.07.15 it was slower than the non-manual batch-size-200 key-holder variant.

See [[netting-batch-processing-performance]] for interpretation boundaries and which netting batch strategy meets performance and correctness requirements for validation requirements.