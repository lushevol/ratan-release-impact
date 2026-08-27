---
type: concept
title: Object Storage Data Consistency Reconciliation
created: 2026-08-24
updated: 2026-08-24
tags: [reconciliation, integrity, object-storage, operations]
related: [minio, postgresql, object-reference-storage-pattern, object-storage-compensating-transactions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# Object Storage Data Consistency Reconciliation

Object-storage data consistency reconciliation validates that every persisted database reference resolves to an existing object and, where required, that the object checksum matches recorded integrity metadata.

The proposal schedules weekly checks in batches of 1,000 using `statObject()`, with optional checksum comparison, and alerts on any consistency failure. It also proposes daily orphan cleanup.

A valid reconciliation compares the precise set of canonical references—bucket, key, and version identifier if versioning is used. Broad database-versus-bucket object counts are insufficient because buckets can contain versions, retry artefacts, pending objects, and unrelated data.