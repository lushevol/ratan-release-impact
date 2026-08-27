---
type: source
title: OpenSearch Data Visibility
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, cash-settlement, business-data, dashboards, jdbc, operational-guidance]
related: [opensearch, opensearch-dashboards, dbeaver, opensearch-sql-jdbc-driver, flow-zero, opensearch-business-data-visibility, sql-over-opensearch, opensearch-jdbc-client-connectivity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# OpenSearch Data Visibility

This operational setup note presents two approaches for making Cash Settlement business data visible for investigation and statistics:

1. [[opensearch-dashboards]] as the native browser-based interface.
2. [[dbeaver]] connected through the [[opensearch-sql-jdbc-driver]].

The document states that Cash Settlement and [[flow-zero]] were designed to use [[opensearch]] as a main NoSQL business-data store. It does not establish whether OpenSearch is authoritative for any data domain, a materialized read model, or an analytics/search projection.

## Solution A: OpenSearch Dashboards

The source points to the OpenSearch Dashboards documentation:

<https://docs.opensearch.org/latest/dashboards/>

It characterizes OpenSearch Dashboards as having no capability difference from Kibana. This should be treated as informal guidance rather than a version-qualified capability comparison.

## Solution B: DBeaver through JDBC

The source instructs users to download the OpenSearch SQL JDBC driver:

- JDBC documentation: <https://docs.opensearch.org/latest/sql-and-ppl/sql/jdbc/>
- Driver repository: <https://github.com/opensearch-project/sql-jdbc>
- Referenced driver artifact: `opensearch-sql-jdbc-shadow-1.4.0.1.jar`

The JAR is described as available in the `shadowJar` directory after extracting the downloaded archive.

Connection information is said to be available from the `51358-ratanone-service-properties` repository. Its possible relationship to [[itam-app-instance-51358]] requires confirmation.

### Preserved driver properties

```properties
trustSelfSigned = true

trustStoreLocation = C:\Users\1633330\certs\ssl\java\ratan_truststore_fmrp2.jks

trustStorePassword = getFromConfiguration
```

The supplied truststore is `ratan_truststore_fmrp2.jks`, described as being obtained from the server for the FMRP reference setup.

## SQL usage

The source says users can explore OpenSearch data with SQL-like queries and refers to:

<https://docs.opensearch.org/latest/sql-and-ppl/sql/index/>

It advises that simple and complex query forms are broadly similar to relational SQL, while functions differ. It provides no example query, index mapping, JDBC URL, authentication method, compatibility matrix, or query-performance limits.

## Governance gaps

The setup note does not define:

- accessible indices, mappings, or business-data classifications;
- whether exploratory access is approved production reporting;
- authentication, data-entitlement, country-filtering, masking, audit, or export controls;
- approved secret and truststore distribution or rotation procedures;
- supported OpenSearch and JDBC-driver versions;
- retention, reconciliation, backup, and recovery responsibilities.

Setting `trustSelfSigned = true` may be appropriate for a controlled internal environment, but requires explicit security governance and endpoint-validation controls before broad operational use.