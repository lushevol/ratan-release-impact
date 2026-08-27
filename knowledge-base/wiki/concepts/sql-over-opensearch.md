---
type: concept
title: SQL over OpenSearch
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, sql, query-language, data-exploration]
related: [opensearch, opensearch-sql-jdbc-driver, dbeaver, opensearch-business-data-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
---
# SQL over OpenSearch

SQL over OpenSearch provides SQL-like querying against OpenSearch data through OpenSearch SQL support and clients such as [[dbeaver]].

The source states that simple and complex queries are broadly similar to relational database SQL, while functions differ. This is high-level orientation only: it does not establish full relational-SQL compatibility or define supported syntax, index-to-table semantics, aggregation behavior, pagination, result limits, joins, or workload suitability.

Operational users should validate queries against the OpenSearch SQL documentation and approved environment-specific runbooks rather than assume that relational SQL semantics transfer unchanged.