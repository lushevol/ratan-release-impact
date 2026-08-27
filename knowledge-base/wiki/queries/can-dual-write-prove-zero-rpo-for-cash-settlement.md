---
type: query
title: Can Dual-Write Prove Zero RPO for Cash Settlement?
tags: [kafka, dual-write, rpo, disaster-recovery, reconciliation]
related: [application-level-dual-write, kafka-dual-cluster-disaster-recovery, cash-settlement-platform]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Message Middleware DR Solution.md"]
---
# Can Dual-Write Prove Zero RPO for Cash Settlement?

The source recommends application dual-write when a zero-minute RPO is required, but it does not define the protocol needed to prove that target.

## Questions to resolve

- Which failure model is in scope: broker loss, full data-centre loss, producer crash, network partition, timeout, or deployment failure?
- How are partial and ambiguous writes recorded, retried, and reconciled?
- Is a durable outbox, write ledger, or compensating replay mechanism available?
- What message identifier and idempotence contract prevents duplicates after retry and failover?
- What evidence from fault injection and DR drills is required to accept RPO = 0?

## Required outcome

Produce a documented write-state model, reconciliation procedure, monitoring design, and test results that distinguish a near-zero objective from a demonstrated zero-data-loss guarantee.