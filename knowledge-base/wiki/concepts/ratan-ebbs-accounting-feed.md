---
type: concept
title: RATAN-to-eBBS Accounting Feed
tags: [ratan, ebbs, accounting, payment-accounting, solace, real-time, json]
related: [ratan, ebbs, solace, settlement-accounting, post-trade-orchestration, ratan-interface-architecture, operational-level-agreement, what-is-the-canonical-ratan-to-ebbs-interface-contract, what-does-real-time-mean-for-the-ratan-to-ebbs-feed]
sources: ["RATAN/RATAN -Interfaces/Ratan and EBBS 14147.md"]
created: 2026-08-24
updated: 2026-08-24
---
# RATAN-to-eBBS Accounting Feed

The RATAN-to-eBBS Accounting Feed is the intended interface through which [[ratan]] generates payment-accounting entries and sends them to [[ebbs]].

## Design assertion

The source states that the feed will be real time, use [[solace]] as the intermediary transport, and represent accounting-entry messages as JSON.

```text
Ratan → Central Solace → eBBS
```

This is an architecture and capability statement, not evidence that the integration is live or that any performance target is being met.

## Relationship to settlement accounting

The feed is an outward delivery path for payment-accounting entries and is therefore related to [[settlement-accounting]]. It may also support [[post-trade-orchestration]], but the source does not describe downstream accounting processing, settlement lifecycle effects, or reconciliation responsibilities.

## Operational dependency

The source says the existing BPMS OLA requires no change. This is an asserted dependency on [[operational-level-agreement]], not a documented OLA contract for the interface.

## Contract limitations

The source does not specify payload fields, schema versioning, triggering events, message identity, transport destination, delivery semantics, idempotency, retries, failures, monitoring, reconciliation, or support ownership. These gaps prevent the overview from serving as a complete technical contract.

The blank publication Status field also leaves approval and production readiness unresolved. See [[what-is-the-canonical-ratan-to-ebbs-interface-contract]] and [[is-the-ratan-to-ebbs-interface-published-and-production-ready]].