---
type: concept
title: IRS Counterpart-Leg Matching
tags: [irs, netting, cashflow, matching, waiting-state]
related: [irs-cashflow-processing, netting-service, lifecycle-service, camunda-api-response, pending-fixing-and-waiting-another-leg]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md"]
---
# IRS Counterpart-Leg Matching

IRS counterpart-leg matching is the intended netting-service operation for locating a second IRS cashflow leg already held in a waiting state.

## Stated Match Criteria

The source requires the candidate leg to have the same:

- `VD`
- `CCY`
- `Client`
- `TradeId`

The candidate must have status `Waiting + PendingAnotherLeg`. The netting service is intended to obtain trade-related cashflows through the lifecycle trade-query API.

## Intended Outcomes

When a matching leg exists, the service is intended to net both cashflows. When no matching leg exists, it calls `WaitingLeg` to change the current cashflow from `QUEUED` to `WAITING + PendingAnotherLeg`, then returns `CamundaApiResponse` with `SUCCESS`.

For any exception, the source says to return `FILTERED` with an error message in `description`.

## Open Contract Gaps

The source does not specify whether the four matching fields are the complete match key, how candidates are selected if more than one exists, or whether the two-leg netting operation is atomic and idempotent. Concurrent arrival of both legs is not addressed. The successful-netting response outcome is also unstated.

`PendingAnotherLeg` is similar to terminology on [[pending-fixing-and-waiting-another-leg]], but this source does not establish that the two usages share a canonical state machine.

See [[what-is-the-canonical-irs-counterpart-leg-matching-and-netting-contract]].