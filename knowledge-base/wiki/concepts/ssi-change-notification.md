---
type: concept
title: SSI Change Notification
created: 2026-08-25
updated: 2026-08-25
tags: [ssi, event-driven-integration, solace, settlement, cashflow]
related: [ssi-plus, solace, ratan-ssi-stamping, how-does-ratan-handle-ssi-change-notifications, what-happens-to-processed-cashflows-after-ssi-changes]
sources: ["RATAN/RATAN -Interfaces/Ratan and SSI+ 50509.md"]
---
# SSI Change Notification

SSI change notification is the real-time publication of SSI record changes from [[ssi-plus]] to RATAN through [[solace]].

The documented events are:

- SSI record update
- SSI record addition
- SSI record deletion

This event-driven path complements RATAN's synchronous SSI+ API lookup. It is intended to keep RATAN informed when centrally maintained SSI information changes.

## Cashflow Impact

The source states that SSI changes may affect previously processed cashflows and could require re-evaluation or adjustment to preserve data consistency and accuracy. This is a potential impact, not confirmation that RATAN automatically reprocesses cashflows.

## Undocumented Delivery Behaviour

The source does not specify the Solace topic or destination, event schema, delivery and acknowledgement semantics, ordering, deduplication, retry, replay, or RATAN's handling of missed notifications. These gaps are tracked in [[how-does-ratan-handle-ssi-change-notifications]].