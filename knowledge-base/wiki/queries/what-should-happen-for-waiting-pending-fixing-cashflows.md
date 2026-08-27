---
type: query
title: What Should Happen for WAITING Pending Fixing Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, pending-fixing, lien, lifecycle-processing]
related: [pending-fixing-flag-processing, lien-stamping-and-re-stamping, fixing-flag-notification-processing, fixing-notification-event-ordering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LIEN Processing & Pending Fixing Flag Technical Design.md"]
---
# What Should Happen for WAITING Pending Fixing Cashflows?

## Question

When a cashflow is in `WAITING + Pending Fixing`, what event clears the condition, what action is performed, and what is the next status?

## Evidence

The lifecycle breakpoint matrix explicitly leaves both the LIEN stamping or re-stamping action and the next status as `??`. This is the central unresolved behavior in the design.

## Required resolution

The decision should define:

- Whether fixing completion triggers `RevertToQueued`, `Net`, or another action.
- Whether the cashflow moves to `QUEUED`, `READY`, `NETTED`, or another status.
- When the latest LIEN amount is retrieved.
- Whether SCBML is re-stamped before status advancement.
- How duplicate fixing notifications and failed LIEN queries are handled.

The result must be reconciled with [[concepts/fixing-flag-notification-processing]] and [[concepts/pending-fixing-and-waiting-another-leg]].