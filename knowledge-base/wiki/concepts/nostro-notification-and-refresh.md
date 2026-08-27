---
type: concept
title: Nostro Notification and Refresh
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, notifications, event-processing, refresh, static-data]
related: [ssi-plus, nostro-centralization, nostro-stamping, nostro-static-data-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# Nostro Notification and Refresh

## Definition

Nostro notification and refresh is the proposed event-driven mechanism for keeping downstream TP-system data current after centralized static data changes in `SSI+`.

## Lifecycle events

The source explicitly names these events:

- `New`
- `Update`
- `Delete`

Each event is expected to trigger a Nostro refresh. The requirement leaves open whether additional event types must be supported.

## Unspecified contract behavior

The source does not define event payloads, transport, ordering, durability, replay, deduplication, idempotency, delivery acknowledgment, or failure recovery.

`Delete` requires particular care because a removed Nostro record may still be referenced by active or historical cashflows. This concern is connected to [[concepts/nostro-static-data-migration]].
