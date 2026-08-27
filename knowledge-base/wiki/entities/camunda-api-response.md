---
type: entity
title: CamundaApiResponse
tags: [camunda, workflow, api-response, cash-settlement]
related: [irs-cashflow-processing, irs-counterpart-leg-matching, netting-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md"]
---
# CamundaApiResponse

`CamundaApiResponse` is a workflow response type named by the IRS netting design.

## Known IRS-Flow Outcomes

For the IRS-specific netting flow, the source specifies:

- `SUCCESS` when no counterpart leg exists and the current cashflow is successfully changed through `WaitingLeg` to `WAITING + PendingAnotherLeg`.
- `FILTERED` for any exception, with an error message in `description`.

The source does not define the complete response contract or the expected outcome after a matching counterpart is found and both cashflows are netted. It also does not distinguish business filtering, validation failure, and transient technical failure.

See [[irs-counterpart-leg-matching]] and [[what-camunda-api-response-should-irs-netting-return-for-each-outcome]].