---
type: concept
title: Back Valued Message Queue
tags: [fmsgw, validation, exception-queue, back-value-date, notifications]
related: [fmsgw, fmsgw-inbound-message-routing, settlement-acknowledgement-flow]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/001 BAHRAIN-SCB BAHRAI MAN(GBS).md"]
---
# Back Valued Message Queue

The Back Valued Messages Queue is an exception queue for inbound settlement messages whose value date is earlier than the permitted processing date.

## UAT behavior

The tested back-value-dated transaction, `DV55M00127114754`, is expected to:

1. Appear in the queue.
2. Retain validation-failure details.
3. Generate an ACK to the inbound system.
4. Trigger a notification.

The test case is marked **Pass**.

## Unknowns

The source does not identify the exact validation rule, permitted date window, ACK status, notification recipient, notification channel, or user action required to release or terminate the item.