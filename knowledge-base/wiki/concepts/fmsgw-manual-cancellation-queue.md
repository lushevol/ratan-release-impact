---
type: concept
title: FMSGW Manual Cancellation Queue
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, manual-cancellation, validation-queue, mtn92, settlement]
related: [fmsgw, zambia-scb-zambia-lus-gbs, manual-entity-settlement-enablement, bulk-manual-fail-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/005 ZAMBIA SCB ZAMBIA LUS(GBS).md"]
---
# FMSGW Manual Cancellation Queue

The FMSGW Manual Cancellation Queue is an operational workflow for cancellation-related settlement transactions.

In the tested Zambia configuration:

- A cancelled trade with an originally released message becomes available for user processing or termination in the queue, with an inbound ACK and email notification stated as expected behavior.
- MTn92 messages enter the queue and can be processed onward to the Eligible currency validation check.
- Users can search for entries, inspect a detail screen containing Data and Action audit tabs, add a comment, and process a transaction so that it is removed from the queue.

The source does not establish the precise lifecycle states, authorization requirements, whether comments are mandatory, or whether cancellation queue creation precedes, follows, or runs in parallel with AMH delivery.