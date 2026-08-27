---
type: query
title: What Is the Authoritative Manual Cancellation Queue Lifecycle?
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, cancellation, validation-queue, swift, operations]
related: [fmsgw, fmsgw-manual-validation-queues, amh, what-is-the-authoritative-ratan-fmsgw-ack-and-release-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/004 KENYA SCB KENYA B NBO(GBS).md"]
---
# What Is the Authoritative Manual Cancellation Queue Lifecycle?

The UAT states that a cancellation `MT202` or `MT103` can be sent to AMH and acknowledged to RATAN while the cancelled trade is also available in the Manual Cancellation Queue. It further confirms that a user can process or terminate a queued transaction.

The lifecycle requires clarification:

- Does the queue hold the cancellation instruction, the underlying trade, or a post-release operational record?
- Does release to AMH occur before, during, or after manual processing?
- What state transitions and side effects result from **Process** and **Terminate**?
- Which users may act, and what maker-checker or audit controls apply?
- What is the next eligible-currency validation check for `MTn92`, and what happens if it fails?
- How are notifications, acknowledgements, and downstream reversals handled?

The documented UAT verifies the available user actions for the Kenya / SCB Kenya B / NBO (GBS) configuration, not the complete lifecycle contract.