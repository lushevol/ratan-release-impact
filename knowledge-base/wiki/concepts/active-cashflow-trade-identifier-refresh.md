---
type: concept
title: Active Cashflow Trade-Identifier Refresh
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, trade-identifiers, ratan, tds3, data-refresh]
related: [tds3-api, ratan, ratan-cash-settlement-netting-service, trade-level-clearing-id-propagation, cash-settlement-home-page-settlement-day-2-swap-agent-requirement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Swap Agent Day2.md"]
---
# Active Cashflow Trade-Identifier Refresh

Active cashflow trade-identifier refresh is the requirement to retrieve and display current parent-trade identifiers for cashflows that remain operationally active in Ratan.

## Fields

The Ratan Cashflow Blotter view builder must expose:

- `Clearing_Organization_Trade_Id`
- `Trade_External_Id`

These fields may be added to a user's custom view but are not included in the customized cashflow filter.

## Active states

The requirement names these cashflow states as eligible for refresh:

```text
PROJECTED
QUEUED
WAITING
READY
```

A trade event may indicate that the source trade value changed. The value is then refreshed through the [[tds3-api]]. When the user manually queries the cashflow, the latest value is displayed. The source explicitly distinguishes this behavior from notification-driven display updates.

## Boundary conditions

The requirement does not define:

- Whether the values are persisted on the cashflow or resolved dynamically.
- Behavior when TDS3 returns no identifier.
- Precedence when TDS3 and the source trade payload disagree.
- Refresh behavior after a cashflow leaves the listed active states.
- Whether the generic `Clearing ID` dependency refers to one field or both fields.

This concept extends [[trade-level-clearing-id-propagation]] with the active-state and manual-query semantics specified for Settlement Day 2.