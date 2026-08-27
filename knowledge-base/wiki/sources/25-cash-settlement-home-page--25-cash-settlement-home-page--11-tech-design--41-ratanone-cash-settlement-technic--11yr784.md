---
type: source
title: Multi-Exception Handling - Bulk Submit Approve Reject Tech Design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, bulk-processing, graphql, performance, exception-handling]
related: [exception-service, nstp-service, query-service, n-plus-one-query-problem, dgs-data-loader-batching, bulk-exception-processing, backend-batch-partitioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Multi-Exception Handling - Bulk Submit Approve Reject Tech Design

This technical design addresses two related Cash Settlement concerns:

1. Avoiding repeated backend retrieval when GraphQL resolves nested cashflow, exception, and Stashing data.
2. Improving the performance of large checker bulk-resolution operations by partitioning backend work across live instances.

The document identifies `query-service` as the owner of cashflows, `exception-service` as the owner of exceptions, and `nstp-service` as the owner of Stashing data.

## Nested retrieval and N+1 risk

A naïve request for 50 cashflows with related exceptions would issue one query for the cashflow list plus 50 calls to `exception-service`, for 51 requests before loading nested Stashing data. The source recommends list-based loading through DGS Framework Data Loaders, contingent on `exception-service` and `nstp-service` providing APIs that accept lists of keys.

The source characterizes future nested retrieval as potentially growing “exponentially.” The directly supported concern is repeated per-object backend calls and resulting latency; no complexity measurement is supplied.

See [[n-plus-one-query-problem]] and [[dgs-data-loader-batching]].

## Referenced bulk task endpoints

```text
POST http://localhost:8080/v2/camunda/task/NSTPSSI/maker
POST http://localhost:8080/v2/camunda/task/NSTPSSI/checker
```

The source labels the first endpoint as Submit. Its Reject section renders the checker URL incorrectly as:

```text
http://localhost:8080/v2/camunda/task/NSTPSSI/c)hecker
```

No request or response bodies are provided. The authoritative endpoint and the Submit, Approve, and Reject API contract remain open questions.

## Performance evidence

The reported measurements apply to the `checker` API. The unit and methodology of the `Cost` column are not defined.

| | Case | Count | API | Thread Pool | DB pool | Solution / Change | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 100 cashflows in a single batch and verify the checker under 20 core threads | 100 | checker | app thread pool: core thread size: 20 max thread size: 50 queue capacity: 10000 | | | 22.84 |
| 2 | 1000 cashflows in a single batch and verify the checker under 20 core threads | 1000 | checker | app thread pool: core thread size: 20 max thread size: 50 queue capacity: 10000 | | | 210 （10X） |
| 3 | 1000 cashflows in a single batch and verify the checker under 50 core threads | 1000 | checker | app thread pool: core thread size: 50 max thread size: 50 queue capacity: 10000 | | | 132 |
| 4 | 50 per batch by backend service and utilize all the live instances capability | 1000 | checker | app thread pool: core thread size: 50 max thread size: 50 queue capacity: 10000 | db thread pool: minimumIdle: 4maximumPoolSize: 50 | backend divided into 20 batches, with 50 cashflows in each batch | 70 |

## Recorded design direction

For a logical bulk size of 1,000 cashflows, the preferred configuration partitions the workload into 20 backend batches of 50 cashflows, uses all live instances, configures 50 application core threads, and specifies a database pool of `minimumIdle: 4` and `maximumPoolSize: 50`.

The reported cost improved from 210 for a single 1,000-item batch under 20 core threads to 70 for the 50-item partitioning configuration. The source does not establish whether this configuration is a production implementation, an experiment, or a proposal. It also does not demonstrate that DGS Data Loaders caused the measured result.

See [[backend-batch-partitioning]] and [[bulk-exception-processing]].