---
type: query
title: What Is the Canonical Trade-Message Object Reference Schema?
created: 2026-08-24
updated: 2026-08-24
tags: [schema, trade-message, minio, postgresql]
related: [postgresql, minio, object-reference-storage-pattern, large-field-dual-write-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# What Is the Canonical Trade-Message Object Reference Schema?

The proposed target DDL defines `raw_msg_bucket` and `raw_msg_key`, but migration and cleanup sections refer to `object_key`. The source also includes the bucket within its key naming convention.

Define the authoritative fields, nullability, uniqueness constraints, indexes, object-version representation, deterministic key format, checksum algorithm, byte-size semantics, and migration status model.