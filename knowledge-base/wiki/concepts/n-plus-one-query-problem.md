---
type: concept
title: N+1 Query Problem
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, performance, backend-queries, cash-settlement]
related: [query-service, exception-service, nstp-service, dgs-data-loader-batching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# N+1 Query Problem

The N+1 query problem occurs when retrieving a parent collection requires one initial request and then one additional request for each returned parent object.

In the Cash Settlement example, loading 50 cashflows requires one request to retrieve the cashflow list and, under a naïve implementation, 50 separate calls to [[exception-service]] to retrieve each cashflow's exceptions. Nested Stashing retrieval from [[nstp-service]] can add further repeated calls.

The supported concern is growth in backend request count and latency as nested data is resolved. The source does not provide evidence that the workload grows exponentially. The proposed mitigation is [[dgs-data-loader-batching]] using backend APIs that accept lists of keys.