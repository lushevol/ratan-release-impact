---
type: entity
title: TDS3 API
created: 2026-08-22
updated: 2026-08-22
tags: [api, trade-data, cash-settlement, trade-identifiers]
related: [ratan, ratan-cash-settlement-netting-service, murex, trade-level-clearing-id-propagation, active-cashflow-trade-identifier-refresh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Swap Agent Day2.md"]
---
# TDS3 API

## Role

The TDS3 API is the trade-data service queried by Ratan after a cashflow is received. In the Settlement Day 2 Swap Agent requirement, it supplies values for `Clearing_Organization_Trade_Id` and `Trade_External_Id`.

## Retrieval and refresh behavior

The requirement specifies that:

- Ratan calls TDS3 after receiving the cashflow.
- A trade event indicating that a source trade value changed triggers a refresh.
- Refresh applies to active cashflows in `PROJECTED`, `QUEUED`, `WAITING`, and `READY`.
- The latest value is displayed when a user manually queries the cashflow.
- The refresh is not notification-driven from the user-interface perspective.

The source does not define the API contract, error handling, caching behavior, persistence location, or response precedence when TDS3 differs from the source trade payload.

## Related requirement

See [[active-cashflow-trade-identifier-refresh]] and [[cash-settlement-home-page-settlement-day-2-swap-agent-requirement]].