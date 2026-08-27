---
type: entity
title: OpenSearch SQL JDBC Driver
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, jdbc, sql, driver, connectivity]
related: [opensearch, dbeaver, opensearch-jdbc-client-connectivity, sql-over-opensearch]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
---
# OpenSearch SQL JDBC Driver

The OpenSearch SQL JDBC Driver enables JDBC clients such as [[dbeaver]] to connect to an [[opensearch]] cluster that supports OpenSearch SQL.

The source references:

```text
opensearch-sql-jdbc-shadow-1.4.0.1.jar
```

It directs users to the official JDBC documentation and the `opensearch-project/sql-jdbc` GitHub repository. The documented artifact version is a configuration reference, not evidence that it is currently approved or compatible with the deployed OpenSearch cluster.

The source does not record the cluster version, SQL plugin version, driver lifecycle, support status, or upgrade process. See [[which-opensearch-version-and-sql-jdbc-driver-version-are-approved-for-production-use]].