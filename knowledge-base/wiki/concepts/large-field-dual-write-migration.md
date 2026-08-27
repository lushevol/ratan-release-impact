---
type: concept
title: Large-Field Dual-Write Migration
created: 2026-08-24
updated: 2026-08-24
tags: [migration, dual-write, minio, postgresql, zero-downtime]
related: [minio, postgresql, ratan-indonesia-entity-scoped-data-migration, object-reference-storage-pattern]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# Large-Field Dual-Write Migration

Large-field dual-write migration moves inline relational payloads to object storage without an immediate read outage. The proposed sequence is: dual-write new payloads to database and MinIO, backfill old records, read from MinIO when a reference exists, verify migration, retain legacy data for at least two weeks, then drop the legacy column.

The source proposes batches of 500 every five seconds and checksum sampling of 1,000 records. Its illustrated `parallelStream()` has uncontrolled concurrency, and its use of Java `String.length()` does not represent encoded byte size. A bounded worker pool, UTF-8 byte accounting, deterministic keys, claim/lock semantics, resumable retry tracking, and exact reference reconciliation are needed.

This is related to [[ratan-indonesia-entity-scoped-data-migration]] but addresses payload externalisation rather than entity-scoped relational migration.