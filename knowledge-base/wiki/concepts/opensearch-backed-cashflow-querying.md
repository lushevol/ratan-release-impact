---
type: concept
title: OpenSearch-Backed Cashflow Querying
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, cashflow, querying, ui-performance, api]
related: [opensearch, opensearch-agent, search-query-performance-sla, db-to-opensearch-data-migration, cashflow-blotter, graphql-cashflow-blotter-aggregate-queries]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Open Search Plan.md"]
---
# OpenSearch-Backed Cashflow Querying

OpenSearch-backed cashflow querying is the proposed use of [[opensearch]] as a search and query layer for RATAN cash-settlement UI and API workloads, with the stated goals of faster UI responses and reduced relational-database pressure.

The initial pilot is described as a new query-service implementation and a new cashflow-blotter UI available through a separate tile. The phrase “new code, no overlap” is not defined; it should not be interpreted as eliminating the planned DB/OpenSearch parallel operation.

## Scope Boundaries

The plan names several surfaces, but does not provide a mapping from each surface to an OpenSearch implementation:

- [[cashflow-blotter]] and Pre Validation Blotter / Group Blotter
- Dashboard and Cashflow Details
- Cashflow History, Swift Query, Accounting Query, and Static/Rules
- Third-party APIs
- Exception handling, netting, and Swift/Cashflow Suppression

The source defines performance targets for these workloads, not achieved performance or a universal architectural commitment.