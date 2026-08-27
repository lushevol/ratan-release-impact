---
type: concept
title: DGS Data Loader Batching
created: 2026-08-24
updated: 2026-08-24
tags: [dgs-framework, graphql, data-loader, batching, performance]
related: [n-plus-one-query-problem, query-service, exception-service, nstp-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# DGS Data Loader Batching

DGS Framework Data Loaders collect keys requested during GraphQL resolution and invoke a batch loader with the accumulated list. This allows a data fetcher to replace repeated single-key backend requests with a list-based request.

For Cash Settlement, [[query-service]] can collect exception identifiers across returned cashflows and load them through one list-oriented call to [[exception-service]]. The same pattern can be applied to Stashing retrieval from [[nstp-service]].

## Preconditions

- Each owning backend must expose a list-key retrieval capability.
- The batch loader must correlate returned records with requested keys.
- Callers need defined behavior for absent keys and partial failures.
- Batch size, timeouts, retry policy, and cache scope require an authoritative contract.

The source recommends this approach but does not demonstrate its deployment or associate it causally with the reported bulk checker measurements.