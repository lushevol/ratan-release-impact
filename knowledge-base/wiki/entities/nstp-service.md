---
type: entity
title: nstp-service
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, stashing, backend-service, batch-loading]
related: [query-service, exception-service, dgs-data-loader-batching, n-plus-one-query-problem]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# nstp-service

`nstp-service` owns Stashing data associated with exceptions in the Cash Settlement nested data model.

The source identifies it as a backend that may be called by [[query-service]] when resolving child Stashing objects. It is expected to support list-key retrieval so that Data Loaders can batch Stashing lookups rather than making repeated per-object calls.

No API contract, key model, batch limit, result-correlation rule, or resilience behavior is specified.