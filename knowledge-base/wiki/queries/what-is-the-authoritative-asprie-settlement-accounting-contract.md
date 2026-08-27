---
type: query
title: What Is the Authoritative Asprie Settlement-Accounting Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [asprie, settlement-accounting, cash-settlement, swift-generation, integration-contract]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technica--tx0zkt, accounting-service, accounting-update, swift-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Accounting for Asprie.md"]
---
# What Is the Authoritative Asprie Settlement-Accounting Contract?

The available source contains no document body. As a result, Asprie's role and its settlement-accounting contract remain unverified.

## Questions to resolve

- What is Asprie: a distinct system, service, product flow, external platform, or legacy identifier?
- Which system produces and owns the authoritative accounting state?
- Does Asprie integrate directly with Cash Settlement, through [[accounting-service]], through [[accounting-update]], or through another intermediary?
- What cashflow, settlement, or SWIFT lifecycle state triggers accounting processing?
- Which identifiers correlate cashflows, accounting entries, SWIFT messages, settlements, corrections, and reconciliation results?
- What idempotency key, retry policy, duplicate-prevention behavior, and failure-recovery process apply?
- How are amendments, cancellations, reversals, and un-netting events reflected in accounting?
- Are SWIFT generation and accounting processing transactionally coupled or eventually consistent?

## Evidence needed

Obtain the body of `Accounting for Asprie.md` and any referenced interface specifications, event schemas, database definitions, sequence diagrams, reconciliation procedures, and operational runbooks. Do not infer a relationship with [[accounting-service]], [[accounting-update]], or [[swift-service]] until explicit evidence is available.