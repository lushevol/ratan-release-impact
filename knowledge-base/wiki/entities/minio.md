---
type: entity
title: MinIO
created: 2026-08-24
updated: 2026-08-24
tags: [object-storage, s3-compatible, cash-settlement, indonesia]
related: [postgresql, database-object-storage-separation, minio-cross-site-disaster-recovery, presigned-url-access-control, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# MinIO

[[MinIO]] is the proposed S3-compatible object-storage platform for large raw trade-message XML/JSON payloads in the Indonesia Cash Settlement Platform. The proposal places object metadata and references in [[postgresql]], rather than retaining payloads in relational large fields.

The source recommends Distributed Mode with at least four nodes, erasure coding, object versioning, cross-site replication, TLS, server-side encryption, IAM separation, and monitoring. These are proposed design elements, not evidence of an approved or deployed configuration.

The proposed Shanghai/Beijing primary/DR topology must be assessed against [[indonesia-ratan-data-residency-isolation]]. MinIO failover also needs coordination with application, database, messaging, and traffic-routing failover procedures.

See [[minio-cross-site-disaster-recovery]], [[object-storage-data-consistency-reconciliation]], and [[presigned-url-access-control]].