---
type: concept
title: Live versus Full Cashflow Volume Reporting
created: 2026-08-22
updated: 2026-08-22
tags: [FMMIS, metrics, cashflow-volume, reporting, data-quality]
related: [fmmis, inter-entity-netting-coverage-metrics, inter-entity-netting-benefit, strategic-settlements-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features.md"]
---

# Live versus Full Cashflow Volume Reporting

Live versus full cashflow volume reporting distinguishes active cashflows from a historical or broader count that includes cancelled cashflows.

The source states that full volume includes cancelled cashflows and that FMMIS will report only live volumes going forward. This is a reporting-definition change, not necessarily a change in settlement activity.

## Analytical impact

Historical and future volume series may not be directly comparable. A decline after the reporting change could reflect the exclusion of cancelled cashflows rather than reduced processing demand.

Trend analysis should therefore:

- Record the reporting-definition change date.
- Identify whether historical values include cancelled cashflows.
- Restate historical values where possible, or present separate series.
- Avoid treating an unadjusted volume reduction as an operational improvement.
- Document the VD+2 reporting basis where applicable.

The source does not specify the effective date or the reconciliation process.