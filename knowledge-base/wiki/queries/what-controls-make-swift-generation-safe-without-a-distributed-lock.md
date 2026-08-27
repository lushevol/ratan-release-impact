---
type: query
title: What Controls Make Swift Generation Safe Without a Distributed Lock?
created: 2026-08-24
updated: 2026-08-24
tags: [swift, distributed-lock, idempotency, concurrency, eventual-consistency]
related: [eventual-consistency-for-cashflow-exceptions-and-swift-status, retry-and-failure-persistence-semantics, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--13iana4]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement 2.0 Technical Design.md"]
---
# What Controls Make Swift Generation Safe Without a Distributed Lock?

The source proposes removing the Swift Service distributed lock and allowing eventually consistent write-back to lifecycle-service. It does not define a replacement concurrency-control model.

## Questions to resolve

- What idempotency key prevents duplicate SWIFT generation and duplicate external submission?
- How are concurrent generation attempts serialized or safely deduplicated?
- What is the ordering and conflict-resolution rule for Swift status write-backs?
- Which system is authoritative when Swift and lifecycle-service report different states?
- What retry, timeout, terminal-failure, reconciliation, and operational-recovery controls apply?
- What evidence shows that lock removal reduces contention without introducing duplicate or lost work?