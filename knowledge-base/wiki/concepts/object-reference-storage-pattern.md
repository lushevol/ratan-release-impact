---
type: concept
title: Object Reference Storage Pattern
created: 2026-08-24
updated: 2026-08-24
tags: [data-model, object-storage, checksum, metadata]
related: [postgresql, minio, database-object-storage-separation, object-storage-data-consistency-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# Object Reference Storage Pattern

The object reference storage pattern represents a payload in relational data through object-store location and integrity metadata rather than inline content.

The proposed fields are `raw_msg_bucket`, `raw_msg_key`, `raw_msg_size`, and `raw_msg_checksum`. The checksum is intended to be SHA-256 and the size is measured in bytes.

The source alternates between the target fields and an undefined `object_key` field. Before implementation, the team must establish one canonical schema, its nullability and uniqueness constraints, indexes for lookups and reconciliation, versioning semantics, and a deterministic object-key convention.