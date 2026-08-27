---
type: concept
title: Backend Batch Partitioning
created: 2026-08-24
updated: 2026-08-24
tags: [bulk-processing, performance, load-balancing, thread-pools, database-connection-pools]
related: [bulk-exception-processing, query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# Backend Batch Partitioning

Backend batch partitioning divides one logical bulk operation into smaller execution batches that can be distributed across available service instances.

For the source's 1,000-cashflow `checker` scenario, the selected configuration creates 20 batches of 50 cashflows and uses all live instances. It records an application thread pool with 50 core threads, 50 maximum threads, and queue capacity 10,000, plus a database pool configured with `minimumIdle: 4` and `maximumPoolSize: 50`.

The reported cost was 70, compared with 132 for a single 1,000-item batch under 50 core threads and 210 for a single 1,000-item batch under 20 core threads. The cost unit, number of live instances, workload characteristics, and repeatability of the measurements are not specified.

This evidence supports the directional conclusion that smaller distributed execution batches outperformed a single large execution batch in the tested checker scenario. It does not establish a universal batch size or service-level objective.