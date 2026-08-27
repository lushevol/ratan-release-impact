---
type: concept
title: Application-Level Dual-Write
tags: [kafka, dual-write, disaster-recovery, idempotence, rpo]
related: [kafka-dual-cluster-disaster-recovery, cash-settlement-platform, kafka, can-dual-write-prove-zero-rpo-for-cash-settlement, message-racing-prevention-in-dual-dc-deployments]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Message Middleware DR Solution.md"]
---
# Application-Level Dual-Write

Application-level dual-write has each producer publish a message to both active and passive Kafka clusters while consumers normally consume only from the active cluster. It is proposed for the Cash Settlement Platform because the passive cluster may already hold messages when the active site fails.

The source recommends this approach when RPO = 0 minutes is required and producer changes are permitted. It describes its RPO as near-zero to zero and its RTO as low relative to restore-based approaches.

## Required controls

Dual-write creates a distributed consistency problem because a message can succeed on one cluster and fail, time out, or have an ambiguous acknowledgement on the other. A viable design requires:

- Stable message identifiers and idempotent consumers.
- Explicit handling of first-write and second-write failure.
- Durable retry or outbox/ledger behavior.
- Audit trails and divergence detection.
- Reconciliation before, during, and after failover.
- Duplicate-processing controls.
- Monitoring for per-cluster publish status and lagging repair.
- DR tests covering producer crashes, network partitions, broker loss, and data-centre loss.

Dual-write alone does not prove zero data loss. The exact write protocol and recovery evidence remain open in [[can-dual-write-prove-zero-rpo-for-cash-settlement]].