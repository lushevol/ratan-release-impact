---
type: query
title: What CamundaApiResponse Should IRS Netting Return for Each Outcome?
tags: [camunda, irs, netting, error-handling, workflow]
related: [camunda-api-response, irs-counterpart-leg-matching, netting-service, cash-settlement-exception-handling]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md"]
---
# What CamundaApiResponse Should IRS Netting Return for Each Outcome?

The IRS design specifies `SUCCESS` when no matching leg exists and the current cashflow is successfully placed in `WAITING + PendingAnotherLeg`. It specifies `FILTERED`, with an error message in `description`, for any exception.

## Questions to Resolve

- What response is returned when a matching leg is found and both cashflows are netted?
- Should business-rule exclusion, invalid input, missing data, and transient technical failure all return `FILTERED`?
- Which failures should be retried rather than filtered?
- What required fields, error codes, and message format comprise `CamundaApiResponse`?
- Does `FILTERED` have the same workflow consequences as the classifications in [[cash-settlement-exception-handling]]?

The source provides no response schema or outcome matrix.