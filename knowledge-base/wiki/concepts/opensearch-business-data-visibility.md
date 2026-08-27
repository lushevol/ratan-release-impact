---
type: concept
title: OpenSearch Business-Data Visibility
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, business-data, visibility, operations, analytics]
related: [opensearch, opensearch-dashboards, dbeaver, sql-over-opensearch, opensearch-jdbc-client-connectivity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
---
# OpenSearch Business-Data Visibility

OpenSearch business-data visibility is the ability for operational users to inspect, query, and derive statistics from business data held in [[opensearch]].

The documented access paths are:

- [[opensearch-dashboards]] for native search and visualization.
- [[dbeaver]] with the [[opensearch-sql-jdbc-driver]] for SQL-like exploration.

These paths establish an operational investigation capability, not a governed reporting or authoritative-data contract. The source does not define visible data sets, report certification, roles, data classification, entitlement filtering, audit trails, or export restrictions.

Business-data visibility must remain distinct from cache-oriented designs such as [[database-first-static-data-caching]], which concern static-reference-data access rather than queryable business-data storage.