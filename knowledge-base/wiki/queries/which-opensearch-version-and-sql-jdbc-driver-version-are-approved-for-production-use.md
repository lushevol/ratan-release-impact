---
type: query
title: Which OpenSearch Version and SQL JDBC Driver Version Are Approved for Production Use?
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, jdbc, compatibility, production-support]
related: [opensearch, opensearch-sql-jdbc-driver, opensearch-jdbc-client-connectivity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
---
# Which OpenSearch Version and SQL JDBC Driver Version Are Approved for Production Use?

## Question

Which deployed OpenSearch version, OpenSearch SQL support version, and JDBC-driver version are approved and supported for Cash Settlement production access?

## Known reference

The source references:

```text
opensearch-sql-jdbc-shadow-1.4.0.1.jar
```

It does not state the target cluster version, compatibility requirements, support status, vulnerability posture, or upgrade process.

## Evidence needed

- Production cluster and OpenSearch SQL plugin versions.
- Approved JDBC driver artifact and checksum/source location.
- Vendor or project compatibility evidence.
- Driver rollout, rollback, patching, and deprecation process.
- Tested DBeaver version and supported operating-system configurations.