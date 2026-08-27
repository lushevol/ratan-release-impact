---
type: concept
title: Message-Racing Prevention in Dual-Data-Centre Deployments
created: 2026-08-24
updated: 2026-08-24
tags: [messaging, concurrency, active-active, active-passive, fencing, disaster-recovery]
related: [mb, cash-settlement-dc-failover-strategy, cashflow-event-control, cashflow-batch-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Message-Racing Prevention in Dual-Data-Centre Deployments

Message-racing prevention is the control of concurrent processing by services operating in separate data centres. The risk arises when both sites can start message-processing components and compete for the same work.

The Indonesia architecture note identifies this risk under the two-profile, two-cluster option. It specifically states that MB startup should be manually restricted. This is an operational warning, not a complete concurrency-control design.

## Required Design Questions

A production-grade control should define:

- Which site owns processing at any moment.
- How ownership is acquired, renewed, and relinquished.
- How a failed or partitioned site is fenced.
- How queues, consumers, databases, and in-flight messages are coordinated.
- How duplicates, ordering, retries, and reconciliation are handled.
- How operators verify and audit the active processing site.

The source does not identify MB or provide automated mutual exclusion, leader election, queue exclusivity, database fencing, or idempotency details. These gaps are tracked in [[queries/what-is-mb-and-how-is-dual-dc-message-processing-fenced]].
