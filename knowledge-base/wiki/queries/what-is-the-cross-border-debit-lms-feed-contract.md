---
type: query
title: What Is the Cross-Border Debit LMS Feed Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, LMS, cash-settlement, integration, cross-border-debit]
related: [cross-border-debit, mt202-crossdebit, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit.md"]
---
# What Is the Cross-Border Debit LMS Feed Contract?

## Question

What interface and operational contract governs delivery of the cross-border debit cashflow feed to [[lms]]?

## Evidence

The requirement states that both receive and pay cross-border debit cashflows must produce a cashflow feed for LMS. It does not define the feed schema, transport, event trigger, timing, acknowledgement behavior, retry policy, or failure handling.

## Required Resolution

Confirm:

- The LMS interface, topic, API, or file format.
- Required identifiers, statuses, amounts, currencies, settlement dates, and message references.
- Whether the feed is emitted after SWIFT generation, accounting generation, or both.
- Delivery guarantees, deduplication, acknowledgement, and retry behavior.
- Handling when SWIFT generation succeeds but LMS delivery fails.
- Whether receive-flow `MT202 CROSSDEBIT` and pay-flow standard `MT103`/`MT202` feeds share the same contract.

The missing integration details should be resolved with the LMS owner and the detailed SWIFT-generation documentation in [[fmrp]].