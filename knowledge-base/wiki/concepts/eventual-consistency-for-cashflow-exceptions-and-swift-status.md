---
type: concept
title: Eventual Consistency for Cashflow Exceptions and Swift Status
created: 2026-08-24
updated: 2026-08-24
tags: [eventual-consistency, cashflow, exceptions, swift, nstp, ssi]
related: [cashflow-lifecycle-state-machine-restructuring, retry-and-failure-persistence-semantics, kafka-persistent-retry-and-dlt-recovery, what-controls-make-swift-generation-safe-without-a-distributed-lock]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement 2.0 Technical Design.md"]
---
# Eventual Consistency for Cashflow Exceptions and Swift Status

The source proposes accepting delayed consistency in two scoped areas:

- NSTP and SSI exceptions need not all be synchronously closed; workflow may close applicable exceptions after a new cashflow arrives or a cashflow is reinstated.
- Swift Service status write-back to lifecycle-service may be eventually consistent after removal of the SWIFT-generation distributed lock.

The source uses both “final consistency” and “eventual consistency” without a formal definition. It does not identify the authoritative state owner, delivery guarantees, retry policy, correlation keys, idempotency rules, reconciliation interval, stale-state detection, alerting, or manual recovery process.

This proposal is especially sensitive because the same source reports a state/message divergence in which lifecycle becomes `released2Razor` despite failed workflow consumption. It should not be interpreted as an approved general reliability policy.