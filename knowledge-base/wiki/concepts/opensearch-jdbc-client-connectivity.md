---
type: concept
title: OpenSearch JDBC Client Connectivity
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, jdbc, tls, truststore, dbeaver]
related: [opensearch, dbeaver, opensearch-sql-jdbc-driver, sql-over-opensearch]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
---
# OpenSearch JDBC Client Connectivity

OpenSearch JDBC client connectivity is the configuration pattern in which a desktop SQL client connects to an OpenSearch SQL-enabled cluster using the [[opensearch-sql-jdbc-driver]].

The documented DBeaver pattern is:

1. Obtain connection details from `51358-ratanone-service-properties`.
2. Add `opensearch-sql-jdbc-shadow-1.4.0.1.jar` under Driver Settings → Libraries.
3. Configure the required TLS driver properties.
4. Test the connection before querying data.

```properties
trustSelfSigned = true

trustStoreLocation = C:\Users\1633330\certs\ssl\java\ratan_truststore_fmrp2.jks

trustStorePassword = getFromConfiguration
```

The source does not define an approved truststore-distribution process, secret handling, certificate rotation, hostname verification, user authentication, or least-privilege authorization model. `trustSelfSigned = true` requires explicit security approval and operational controls, particularly for production access.