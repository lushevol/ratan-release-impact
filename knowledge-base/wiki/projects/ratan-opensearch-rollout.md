---
type: project
title: RATAN OpenSearch Rollout
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, opensearch, rollout, migration, cashflow]
related: [opensearch, opensearch-agent, opensearch-backed-cashflow-querying, db-to-opensearch-data-migration, database-opensearch-reconciliation, search-query-performance-sla]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Open Search Plan.md"]
status: planned
owner: ""
start_date: 2025-12-31
target_date: 2026-02-07
---
# RATAN OpenSearch Rollout

## Objective

Introduce [[opensearch]]-backed query capability for RATAN cash-settlement workloads to improve UI responsiveness and reduce relational-database pressure.

## Planned Delivery Sequence

1. Deliver the [[opensearch-agent]] for technical data loading.
2. Deliver a new query service and a new cashflow blotter for pilot users through a new tile.
3. Complete reconciliation, cross-data-center HA work, UAT, data migration, and Kibana access.
4. Run DB and OpenSearch in parallel for one month.
5. Reconcile data and remove DB dependency if cutover criteria are met.

## Recorded Owners

- Zeyu Zhou: Kibana readiness; OpenSearch Agent installation.
- zhang jiangnan: OpenSearch Agent installation and delivery; schema update.
- Xinmiao Huang: schema update.
- Chen Yang: DB-to-OpenSearch migration strategy.
- Recon strategy: no owner recorded.

## Risks and Dependencies

- CCR is stated not to synchronize data between two data centers.
- FMO Comment timestamps use nanosecond format in Discover/Elastic.
- Real-time reconciliation is missing.
- Proper UAT has not yet been completed.
- Infrastructure ownership and maintenance strategy are listed as NFRs but not defined.

The source does not confirm completion of any dates or milestones. The separate 2025-12-31 and 2026-01-31 OpenSearch Agent milestones need clarification before project status can be assessed.