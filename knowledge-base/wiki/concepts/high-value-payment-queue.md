---
type: concept
title: High Value Payment Queue
tags: [fmsgw, high-value-payment, def-rule, approval, exception-queue]
related: [fmsgw, fmsgw-inbound-message-routing, settlement-acknowledgement-flow]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/001 BAHRAIN-SCB BAHRAI MAN(GBS).md"]
---
# High Value Payment Queue

The High Value Payment Queue is an approval gate for settlement messages that match a DEF rule and are classified as high-value payments.

## UAT behavior

For `MT103` and `MT202`, the expected workflow is:

1. Receive the message from [[ratan]].
2. Place it in the High Value Payment Queue.
3. Obtain user approval.
4. Send the approved message to [[amh]] through [[fmsgw]].
5. Return an ACK to RATAN.
6. Send a notification.

The scenario is marked **Pass**.

## Unknowns

The source does not identify the DEF rule, value threshold, approver role, rejection behavior, timeout behavior, or notification contract.