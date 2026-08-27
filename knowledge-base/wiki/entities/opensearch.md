---
type: entity
title: OpenSearch
created: 2026-08-24
updated: 2026-08-24
tags: ["search", "indexing", "analytics", "ratan", "infrastructure", "opensearch", "search-platform", "cash-settlement", "ratanone", "nosql"]
related: ["opensearch-agent", "opensearch-backed-cashflow-querying", "db-to-opensearch-data-migration", "database-opensearch-reconciliation", "ratan-opensearch-rollout", "ratanone", "ratanone-opensearch-agent", "opensearch-business-live", "three-way-data-reconciliation", "idempotent-historical-data-migration", "cashflow", "opensearch-dashboards", "opensearch-sql-jdbc-driver", "flow-zero", "opensearch-business-data-visibility", "sql-over-opensearch", "ratan", "ratan-opensearch-integration", "how-should-cash-settlement-filter-dsl-be-translated-to-sql-and-opensearch"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Open Search Plan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md", "RATAN/RATAN -Core Function copy/Function_RATAN-OpenSearch.md"]
---
# OpenSearch

## Role and scope

OpenSearch is a proposed query and indexing layer for RATAN cash-settlement workloads. The Open Search Plan states that it is intended to improve UI query performance and reduce pressure on the relational database.

For the RatanOne Cash Settlement business-live transition, the OpenSearch Business Live Plan describes OpenSearch as the target search and persistence platform. That source states that OpenSearch is already technically live for cashflow and cashflow-history persistence.

The Open Search Data Visiability source presents OpenSearch as a strategic business-data storage platform for Cash Settlement and [[flow-zero]], supporting search, data exploration, and statistics. That source describes it as a main NoSQL database.

The Open Search Plan documents scope for:

- [[cashflow-blotter]]
- Cashflow details
- Dashboard
- Group blotter
- Third-party API exposure

The OpenSearch Business Live Plan identifies current coverage for:

- Cashflow data
- Cashflow history

That source identifies potential additional coverage for:

- Trade
- NSTP Exception
- Other domains currently exposed through the GraphQL query surface

Neither the Open Search Plan nor the OpenSearch Business Live Plan establishes that every listed workload or domain has been implemented and indexed in OpenSearch. In particular, the OpenSearch Business Live Plan does not establish that all exception, SSI, affirmation, or netting data will be indexed; it states that each domain requires an explicit source-of-truth decision.

## Query, persistence, and authority

According to the OpenSearch Business Live Plan, the proposed business-live state makes OpenSearch the default source for internal cashflow-blotter, cashflow-detail, and cashflow-dashboard queries.

The Open Search Plan does not establish that OpenSearch is the authoritative operational data source for all listed workloads. Its available evidence characterizes OpenSearch as a transition target rather than a proven replacement.

Although the Open Search Data Visiability source calls OpenSearch a main NoSQL database, that source does not specify whether it is a system of record, replicated read model, search index, or analytics store. It also does not identify:

- Authoritative upstream stores
- Index ownership
- Ingestion mechanisms
- Reconciliation requirements

See [[is-opensearch-the-authoritative-store-or-a-read-model-for-cash-settlement]] and [[what-are-the-canonical-cash-settlement-opensearch-indices-mappings-and-data-retention-rules]].

## Transition behavior

The Open Search Plan proposes a cutover with one month of relational-database and OpenSearch parallel operation, reconciliation between the two stores, and later removal of database dependency.

The OpenSearch Business Live Plan describes the initial internal rollout as follows:

- OpenSearch is the default query source.
- PG persistence continues.
- Queries can fall back to PG if production issues occur.
- Historical data is migrated before business go-live.
- Reconciliation compares lifecycle-service history, PG, and OpenSearch.

The Business Live Plan therefore describes a transitional dual-write and dual-read architecture. The duration of PG retention and its exit criteria are unresolved.

## Operational access

The Open Search Data Visiability source describes operational access through [[opensearch-dashboards]] and SQL-capable desktop clients, including [[dbeaver]], using the [[opensearch-sql-jdbc-driver]].

## RATAN relationship

The source file `RATAN/RATAN -Core Function copy/Function_RATAN-OpenSearch.md` names OpenSearch as a topic associated with [[ratan]]. Its body was unavailable, so that source does not establish an implemented RATAN integration or describe a confirmed OpenSearch deployment.

Based on that unavailable-body source, the role of OpenSearch in [[ratan]] is unknown. In particular, it does not confirm:

- Which services connect to OpenSearch
- What data is indexed
- Whether OpenSearch supports cash-settlement querying
- Who owns the cluster, indexes, mappings, and operational support
- Whether OpenSearch is authoritative or a derived search projection

The potentially related question of query semantics is tracked in [[how-should-cash-settlement-filter-dsl-be-translated-to-sql-and-opensearch]].

## Readiness gaps and operational dependencies

The Open Search Plan identifies the following readiness gaps:

- Cross-data-center synchronization
- FMO Comment nanosecond timestamp compatibility
- Missing real-time reconciliation
- Incomplete UAT

The OpenSearch Business Live Plan identifies dependencies on:

- [[ratanone-opensearch-agent]] for integration and persistence processing
- Kafka retry and DLT handling
- Enhanced real-time reconciliation
- OpenSearch Dashboards for operational visibility
- A canonical relationship among `RatanCashSettlementData.proto`, `ResultNew`, and the OpenSearch schema