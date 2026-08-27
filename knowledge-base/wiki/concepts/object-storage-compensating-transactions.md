---
type: concept
title: Object Storage Compensating Transactions
created: 2026-08-24
updated: 2026-08-24
tags: [consistency, compensation, orphan-cleanup, messaging]
related: [minio, postgresql, kafka, object-storage-data-consistency-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# Object Storage Compensating Transactions

An object-storage compensating transaction repairs an object uploaded successfully when the corresponding database reference fails to persist.

The proposed flow uploads to [[minio]], then writes the reference to [[postgresql]]. On database failure, an asynchronous delete is requested and an orphan cleaner identifies remaining unreferenced objects.

This is eventual consistency, not an atomic transaction. A durable command topic, idempotent cleanup consumer, retry policy, terminal DLQ, authorization to delete, and scheduled reconciliation are required. A DLQ should not be the primary compensation work queue. The source does not define the required pending-object lifecycle or durable outbox design.