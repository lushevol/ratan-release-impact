---
type: query
title: What Is the Next Validation State After MTn92 Manual Cancellation Processing?
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, mtn92, manual-cancellation, validation, open-question]
related: [manual-cancellation-queue, fmsgw-manual-payment-validation-queues, fmsgw, scb-nigeria-lag-gbs, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--51mg19]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/009 NIGERIA SCB NIGERIA LAG(GBS).md"]
---

# What Is the Next Validation State After MTn92 Manual Cancellation Processing?

The UAT evidence confirms that an `MTn92` message can be processed from the [[manual-cancellation-queue]], with a comment recorded and the item removed from the queue. The destination is described only as the “next Eligible currency validation check.”

## Questions to Resolve

- What is the canonical name and state identifier of the next validation stage?
- What eligible-currency rule is evaluated and what outcomes can it produce?
- Does processing generate an outbound message, an ACK, or a notification?
- What audit record is required for comments and process actions?