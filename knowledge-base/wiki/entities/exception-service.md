---
type: entity
title: exception-service
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, exceptions, backend-service, batch-loading]
related: [query-service, nstp-service, dgs-data-loader-batching, bulk-exception-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# exception-service

`exception-service` owns exception data in the Cash Settlement nested data model.

The source identifies it as a dependency of [[query-service]] when cashflows include exceptions. To avoid one backend call per cashflow, it must provide a list-based retrieval API that accepts the exception keys collected during a request. This capability is a prerequisite for [[dgs-data-loader-batching]].

The source does not define the batch request and response schema, key type, ordering guarantees, missing-key behavior, partial failures, retries, or maximum batch size.