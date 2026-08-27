---
type: concept
title: Pending Fixing Flag Processing
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, pending-fixing, fixing-flag, lifecycle-processing]
related: [lien, lien-stamping-and-re-stamping, pending-fixing-and-waiting-another-leg, fixing-flag-notification-processing, fixing-notification-event-ordering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LIEN Processing & Pending Fixing Flag Technical Design.md"]
---
# Pending Fixing Flag Processing

## Definition

`PendingFixingFlag` identifies a cashflow that is waiting for fixing-related processing. In this design, it intersects with LIEN processing because a cashflow may need to be re-stamped when it leaves a waiting state.

## Known lifecycle states

The source explicitly identifies:

- `WAITING + Pending Netting`
- `WAITING + Pending AnotherLeg`
- `WAITING + Pending Fixing`
- `WAITING + Pending Exception`

The first two states have the action `Net/RevertToQueued` and the possible next statuses `NETTED/QUEUED`. The pending-exception state uses `RevertToQueued` and has possible next statuses `QUEUED/Ready`.

The action and next status for `WAITING + Pending Fixing` are both unresolved.

## Relationship to existing fixing processing

This concept should be read together with [[concepts/fixing-flag-notification-processing]] and [[concepts/fixing-notification-event-ordering]]. It extends those areas with a specific question about lifecycle rollback, LIEN re-stamping, and status selection. It does not establish a replacement for the existing fixing-notification contract.

## Required resolution

An authoritative state-machine decision is needed for:

- The event that clears or satisfies `PendingFixingFlag`.
- The action taken when a waiting cashflow becomes processable.
- Whether LIEN is stamped before or after the status transition.
- Whether the next status is `QUEUED`, `READY`, `NETTED`, or another state.
- Retry and duplicate-event behavior.

See [[what-should-happen-for-waiting-pending-fixing-cashflows]].