---
type: source
title: "RATAN Foundation 2.0 - OpenSearch: Development Plan - 202407"
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, opensearch, cashflow, performance, rollout]
related: [opensearch, opensearch-agent, opensearch-backed-cashflow-querying, db-to-opensearch-data-migration, database-opensearch-reconciliation, search-query-performance-sla, ratan-opensearch-rollout]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Open Search Plan.md"]
authors: []
year: 2024
url: "https://confluence.global.standardchartered.com/display/DSP/RATAN+Foundation+2.0+-+OpenSearch+%3A+Development+Plan+-+202407#RATANFoundation2.0OpenSearch:DevelopmentPlan202407-No-FunctionRequirementDefinition"
venue: "Confluence, Derivative Strategy Projects"
---
# RATAN Foundation 2.0 - OpenSearch: Development Plan - 202407

This development plan proposes [[opensearch-backed-cashflow-querying]] to improve RATAN UI-query performance and reduce load on the relational database. It identifies the cashflow blotter as the primary workload, while also naming cashflow details, dashboard, group blotter, and third-party APIs as impacted surfaces.

The document records intended requirements and a rollout plan. It does not provide benchmark results, completed UAT evidence, approved architecture decisions, index mappings, or reconciliation rules.

## Use Case Definition

1. Main goal 1. Better performance on UI query 2. Less pressure on relational database
2. Impacted blotters: 1. cashflow blotter 2. cashflow details page 3. dashboard 4. Group blotter 5. API expose to third party

| **Item** | **Details** | **NFR** |
| --- | --- | --- |
| Cashflow blotter | Payment date query SLA | 2s for initial loading & each subsequent page loading of 20k cashflows including usage of filters Default page size: 20,000 Update the load next button to 20,000 Remove the limitation to fetch more than 30 days and replace it with limitation based on volume |
| Pre Validation Blotter (Group Blotter) | | 2s for initial loading & each subsequent page loading of 20k cashflows Default page size: 20,000 Pending only Update the load next button to 20,000 |
| Dashboard | | 2s to load |
| Trade Details | | Depending on TDS/TDSX performance |
| Cashflow Details | | 1 seconds |
| Cashflow History | | 1 seconds |
| Swift Query | | 1 seconds |
| Accounting Query | | 1 seconds |
| Static/Rules | | 2 seconds |
| | | |
| Exception handling | Single exception processing | 1 s |
| | Bulk exception processing | 3 s for 1000 records |
| Netting | Manual Netting | 5 seconds for 50,000 records |
| | CLS Netting | 1 M per Month |
| Swift/Cashflow Suppression | Bulk | 3 s for 1000 records |
| | Single | 1 seconds |

The performance requirements are workload-specific. In particular, the cashflow-blotter requirement applies to initial and subsequent filtered pages of 20,000 cashflows; it is not evidence of a universal two-second service SLA. Trade Details is explicitly dependent on TDS/TDSX performance.

## Delivery Plan and Risks

The rollout proposes an [[opensearch-agent]] for technical data loading, a new query-service and cashflow-blotter implementation for pilot users through a new tile, then UAT, migration, reconciliation, and a one-month DB/OpenSearch parallel run before removing DB dependency.

Known unresolved issues are:

1. HA issue. CCR does not work for data sync up between 2 data centers.
2. Data issue: FMO Comment timestamp data format on nano. Discover - Elastic
3. Real time recon missing
4. No proper UAT yet

| | Activity | Time | Purpose |
| --- | --- | --- | --- |
| 1 | Open Search Agent Delivery to production | 2026-01-31 | Technical live for data loading |
| 2 | Query service delivery (new code, no overlap) UI delivery (New cashflow blotter) (new code, no overlap) | 2026-02-07 | Technical live for pilot users only, a new tile |
| 3 | | | |
| 4 | Real time recon | | |
| 5 | CCR issue | | |
| 6 | UAT | | |
| 7 | Data migration | | |
| 8 | Production data dev access (Kibana) | | |

## FMRP2 Activities

On FMRP2:

1. Kibana readiness @Zeyu Zhou
2. New open search agent installation @zhang jiangnan @Zeyu Zhou

| | | Complete date | Owner |
| --- | --- | --- | --- |
| Development | OpenSearch schema update based on UBER Open search agent Query service | 2026-01-28 | @zhang jiangnan @Xinmiao Huang |
| **Open search Agent delivery** | Technical go live to receive | 2025-12-31 | @zhang jiangnan @Zeyu Zhou |
| Development | Data migration strategy from DB to Open Search | 2026-02-06 | @Chen Yang |
| Development | Recon strategy | 2026-02-06 | |
| UAT | UAT on cashflow blotter based on the Open search | | |
| | | | |
| | | | |
| Go Live | DB + Open search in parallel run for 1 month | | |
| Go live | Recon between DB and Open Search | | |
| Go Live | Remove DB dependency post say 1 month | | |
| | | | |

## Non Functional Requirement

1. Supporting Model, infra ownership 1. Maintenance strategy
2. Data Migration

## Interpretation Boundaries

The document has two distinct OpenSearch Agent dates: 2025-12-31 for technical go-live to receive and 2026-01-31 for production delivery. Their relationship is not explained.

“New code, no overlap” is also ambiguous because the plan separately requires a DB and OpenSearch parallel run. The source does not establish which system is authoritative during that run, the rollback criteria, or the reconciliation contract. These gaps are tracked in [[what-is-the-authoritative-db-to-opensearch-reconciliation-contract]] and [[what-is-the-opensearch-cross-data-center-ha-strategy]].