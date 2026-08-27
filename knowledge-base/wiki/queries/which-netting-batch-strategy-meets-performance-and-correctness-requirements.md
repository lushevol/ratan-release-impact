---
type: query
title: Which Netting Batch Strategy Meets Performance and Correctness Requirements?
created: 2026-08-24
updated: 2026-08-24
tags: [netting, batching, performance, correctness, validation]
related: [netting-batch-processing-performance, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--19-n--qhw0o4, netting-service, cash-settlement-performance-and-stress-testing, what-caused-netting-performance-variance-between-2025-07-14-and-2025-07-15]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Netting Test Result/Netting Cost Comparation.md"]
---
# Which Netting Batch Strategy Meets Performance and Correctness Requirements?

The 2025.07.15 Dev result at 1,999 cashflows identifies the key-holder variant with batch size 200 and `{message_id, version}` as the fastest complete recorded option for both `net` and `unet`. This is insufficient to make it the preferred strategy without confirming functional equivalence and repeatable behavior.

## Evidence to obtain

- Repeat controlled benchmarks at 596, 1,999, expected peak, and production-scale cashflow volumes.
- Define `net`, `unet`, and `key holder`, including the function of `{message_id, version}`.
- Confirm equivalent output records, ordering, transaction atomicity, error handling, retry behavior, and idempotency for every variant.
- Measure lock contention, deadlocks, timeout behavior, and concurrent-processing effects.
- Record database and infrastructure configuration, data distribution, warm-up treatment, and concurrent load.
- Validate end-to-end results in a production-like environment, rather than selecting solely by aggregate DB time.

## Current evidence

[[netting-batch-processing-performance]] summarizes the available Dev comparison. The batch-size-200 key-holder option is a candidate for validation, not an approved implementation choice.