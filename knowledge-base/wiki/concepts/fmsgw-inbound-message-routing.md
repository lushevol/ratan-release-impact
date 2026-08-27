---
type: concept
title: FMSGW Inbound Message Routing
tags: [fmsgw, message-routing, settlement, amh, ratan, uat]
related: [fmsgw, ratan, amh, settlement-acknowledgement-flow]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/001 BAHRAIN-SCB BAHRAI MAN(GBS).md"]
---
# FMSGW Inbound Message Routing

FMSGW inbound message routing is the flow in which settlement messages received from [[ratan]] are processed by [[fmsgw]] and forwarded to [[amh]] when the relevant validations and approvals permit release.

## UAT evidence

The Bahrain SCB manual-entity UAT records passing scenarios for:

- `MT103/202COV`
- standalone `MT202`
- `MT192/292`
- approved high-value `MT103` and `MT202`
- cancellation-related `MT103` and `MT202`

The source describes an ACK being returned to RATAN after processing. Approval queues and validation exceptions interrupt direct routing rather than replacing the downstream route.

## Evidence boundary

The source does not specify message schemas, transport channels, correlation keys, retry behavior, or the exact point at which the ACK is emitted.