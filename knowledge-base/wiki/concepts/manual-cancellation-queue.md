---
type: concept
title: Manual Cancellation Queue
tags: [fmsgw, cancellation, validation-queue, manual-processing, uat]
related: [fmsgw, fmsgw-inbound-message-routing, settlement-acknowledgement-flow]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/001 BAHRAIN-SCB BAHRAI MAN(GBS).md"]
---
# Manual Cancellation Queue

The Manual Cancellation Queue holds cancellation-related settlement items that require user intervention.

## UAT workflows

For a cancelled trade whose original message was released, the source expects the settlement message to be sent to [[amh]], an ACK to be returned, and the transaction to appear in this queue. The user receives an email notification and can process or terminate the transaction. The tested reference is `M00127113321`.

For an `MTn92` message, the user can:

- Open the queue and search for one or more entries.
- Open a detail view with **Data** and **Action audit** tabs.
- Add a comment.
- Select **Process**.
- Release the payment transaction to the next eligible-currency validation check.
- Remove the transaction from the queue.

The `MTn92` scenario is marked **Pass** with reference `DV55M00127113321`.

## Ambiguity

The source uses the same queue for cancelled trades and `MTn92` messages but does not explain whether these are one workflow with multiple entry reasons or distinct queue subtypes. It also does not define the effects of Process versus Terminate on downstream settlement.