---
type: concept
title: Settlement Acknowledgement Flow
tags: [settlement, acknowledgement, ack, fmsgw, ratan]
related: [fmsgw, ratan, fmsgw-inbound-message-routing]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/001 BAHRAIN-SCB BAHRAI MAN(GBS).md"]
---
# Settlement Acknowledgement Flow

The settlement acknowledgement flow returns an ACK from [[fmsgw]] to the inbound settlement-message source, identified as [[ratan]] in the normal routing scenarios.

## Tested behavior

The UAT expects an ACK after:

- `MT103/202COV` processing.
- Standalone `MT202` processing.
- `MT192/292` processing.
- Approved high-value payment processing.
- Cancellation-related message processing.

For `MT103/202COV`, the source additionally states that `MT202COV` is released after the related `MT103` receives a successful ACK.

## Contract limitations

The source alternates between “ACK sent to RATAN” and “ACK sent to inbound system.” It does not provide ACK type, status, payload, recipient resolution, timing, retry rules, or idempotency behavior.