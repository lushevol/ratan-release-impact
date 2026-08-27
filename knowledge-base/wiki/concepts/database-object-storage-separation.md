---
type: concept
title: Database-Object Storage Separation
created: 2026-08-24
updated: 2026-08-24
tags: [architecture, object-storage, database, large-payloads]
related: [minio, postgresql, object-reference-storage-pattern, large-field-dual-write-migration, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# Database-Object Storage Separation

Database-object storage separation stores large payloads in object storage while retaining business metadata and object references in a relational database.

For the proposed Indonesia design, raw trade-message XML/JSON would be stored in [[minio]] and `trade_message` would retain metadata in [[postgresql]]. Expected benefits include reducing relational-table bloat and decoupling payload capacity from operational database growth.

The pattern creates a cross-system consistency boundary. Object availability, reference durability, deletion, reconciliation, lifecycle rules, and access control must be explicitly designed; a database transaction cannot atomically commit both MinIO and PostgreSQL in the proposed model.