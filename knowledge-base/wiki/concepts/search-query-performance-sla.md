---
type: concept
title: Search Query Performance SLA
created: 2026-08-24
updated: 2026-08-24
tags: [performance, sla, opensearch, cashflow, non-functional-requirements]
related: [opensearch-backed-cashflow-querying, opensearch, cashflow-blotter, graphql-query-performance-observability, what-are-the-authoritative-opensearch-performance-slos]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Open Search Plan.md"]
---
# Search Query Performance SLA

Search query performance SLA describes the workload-specific non-functional requirements stated for the planned OpenSearch rollout.

The principal requirement is two seconds for initial and subsequent filtered pages of 20,000 cashflows in the [[cashflow-blotter]]. The group blotter has the same page-size and latency target but is limited to pending records.

Other stated targets include one-second detail and query views, two-second dashboard and Static/Rules loading, one second for a single exception, three seconds for 1,000 exception or suppression records, and five seconds for 50,000 manual-netting records.

## Measurement Gap

The source does not specify latency percentiles, test data volume, concurrent-user load, whether rendering and network time are included, or whether 20,000 refers to scanned, returned, or indexed records. “CLS Netting 1 M per Month” has no defined unit. The requirements are therefore targets requiring a measurement contract, not demonstrated service levels.