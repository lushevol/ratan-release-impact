---
type: concept
title: Netting Batch Processing Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, batching, performance, benchmarking, dev]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--19-n--qhw0o4, netting-service, cash-settlement-performance-and-stress-testing, which-netting-batch-strategy-meets-performance-and-correctness-requirements, what-caused-netting-performance-variance-between-2025-07-14-and-2025-07-15]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Netting Test Result/Netting Cost Comparation.md"]
---
# Netting Batch Processing Performance

Netting batch processing performance compares end-to-end elapsed time and database timing across alternative processing patterns. The recorded Dev benchmark evaluates old per-item processing, key-holder batching with `{message_id, version}`, manual batch SQL, and `select after insert`.

## Observed Dev result

For the 1,999-cashflow run dated 2025.07.15, the key-holder variant using batch size 200 produced the fastest complete recorded end-to-end results:

- `net`: 33.75s
- `unet`: 31.62s

In the same run, this was faster than the old `for each` implementation, the batch-size-1,000 key-holder variant, manual batch SQL with batch size 200, and `select after insert`.

This supports prioritizing the batch-size-200 key-holder variant for further evaluation. It does not by itself approve the implementation or establish production readiness.

## Evaluation dimensions

Performance interpretation must distinguish:

- **End-to-end elapsed time**, which is the primary recorded measure of processing duration.
- **Aggregate DB time**, which may not predict end-to-end duration.
- **Per-batch DB time** and **per-batch query time**, where recorded, which help isolate database contribution.
- **Cashflow volume**, because a result at 596 cashflows did not rank variants in the same way as the later 1,999-cashflow run.
- **Run date and environment conditions**, because the same 1,999-cashflow scenarios varied materially between 2025.07.14 and 2025.07.15.

The benchmark does not define the implementation semantics of `key holder` or the role of `{message_id, version}` beyond identifying them as the columns used in the tested variants.

## Limits

The source provides no repeated-trial statistics, workload definition, concurrent-load information, hardware specification, database state, warm-up protocol, transaction boundaries, correctness checks, locking behavior, or retry behavior. It should be treated as targeted Dev evidence rather than a capacity forecast.

This performance evidence may be relevant to [[netting-service]], but the source does not explicitly identify a service release, endpoint, or deployment. It complements the broader evidence in cash settlement performance and stress testing without changing netting business rules such as [[ccil-netting]].