---
type: entity
title: DBeaver
created: 2026-08-24
updated: 2026-08-24
tags: [dbeaver, sql-client, jdbc, opensearch, operational-support]
related: [opensearch, opensearch-sql-jdbc-driver, opensearch-jdbc-client-connectivity, opensearch-business-data-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
---
# DBeaver

DBeaver is a desktop database client proposed as an alternative to [[opensearch-dashboards]] for exploring [[opensearch]] business data through SQL-like queries.

The source spells the product name as “DBever”; this page uses the established product name DBeaver. The described setup adds `opensearch-sql-jdbc-shadow-1.4.0.1.jar` to the driver libraries and configures TLS-related properties before testing connectivity.

The source does not specify the JDBC URL, authentication protocol, approved client configuration, access permissions, or audit controls. Direct desktop-client access should be governed by [[what-data-entitlement-and-audit-controls-govern-dbeaver-and-opensearch-dashboards-access]].