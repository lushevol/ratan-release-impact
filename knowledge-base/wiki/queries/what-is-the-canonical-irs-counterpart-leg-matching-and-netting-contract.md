---
type: query
title: What Is the Canonical IRS Counterpart-Leg Matching and Netting Contract?
tags: [irs, netting, matching, concurrency, idempotency]
related: [irs-counterpart-leg-matching, irs-cashflow-processing, netting-service, lifecycle-service, camunda-api-response]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md"]
---
# What Is the Canonical IRS Counterpart-Leg Matching and Netting Contract?

The IRS design identifies a candidate counterpart with matching `VD`, `CCY`, `Client`, and `TradeId`, plus `Waiting + PendingAnotherLeg` status. It does not define a complete netting contract.

## Questions to Resolve

- Are these four fields the complete and authoritative match key?
- Which system owns the authoritative values for the match fields and leg status?
- What happens when multiple matching candidates exist?
- Is searching, reserving, and netting both cashflows atomic?
- How are duplicate requests, retries, and concurrent arrival of both legs handled?
- Which `CamundaApiResponse` outcome is returned after successful two-leg netting?

The cited source describes this capability as In Progress and provides no test evidence.