---
type: query
title: Are DGS Data Loaders Deployed for Exception and Stashing Retrieval?
created: 2026-08-24
updated: 2026-08-24
tags: [dgs-framework, graphql, data-loader, exception-service, nstp-service]
related: [dgs-data-loader-batching, n-plus-one-query-problem, query-service, exception-service, nstp-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# Are DGS Data Loaders Deployed for Exception and Stashing Retrieval?

The source recommends DGS Framework Data Loaders to batch exception and Stashing retrieval, but the performance results describe thread-pool changes and backend batch partitioning rather than Data Loader implementation or measurements.

Confirm whether Data Loaders are deployed in [[query-service]] for both [[exception-service]] and [[nstp-service]], and document:

- Batch keys and backend list-loading endpoints.
- Result ordering and key-to-record correlation.
- Request-scoped caching behavior.
- Missing-key and partial-failure handling.
- Batch limits, timeouts, retries, and observability.
- Measurements demonstrating the reduction in backend request count.

Related source: [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--11yr784]].