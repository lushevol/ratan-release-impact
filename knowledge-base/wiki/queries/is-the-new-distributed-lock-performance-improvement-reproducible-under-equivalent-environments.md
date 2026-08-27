---
type: query
title: Is the New Distributed-Lock Performance Improvement Reproducible Under Equivalent Environments?
created: 2026-08-24
updated: 2026-08-24
tags: [distributed-locking, benchmarking, netting, performance-testing]
related: [resource-lock-manager, batch-distributed-locking, netting-batch-processing-performance, cashflow-netting-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Distribution lock test cases  && Uber orchestration.md"]
---
# Is the New Distributed-Lock Performance Improvement Reproducible Under Equivalent Environments?

The recorded 7K comparison shows lower new-lock timing for acquisition and release, but compares four-server staging with one-server uat4. The 10K observations also span staging and FRMP1 without documented equivalence of inputs, topology, service versions, database state, cache state, or load.

A controlled benchmark should run old and new implementations with identical infrastructure, data, workload, concurrency, Redis configuration, database state, and warm-up procedure. It should use repeated trials and report percentile acquisition, release, preview, and end-to-end netting latency.

This evidence is relevant to [[netting-batch-processing-performance]], [[cashflow-netting-performance]], and [[which-netting-batch-strategy-meets-performance-and-correctness-requirements]].
---