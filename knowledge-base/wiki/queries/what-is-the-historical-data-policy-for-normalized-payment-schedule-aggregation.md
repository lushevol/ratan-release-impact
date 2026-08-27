---
type: query
title: What Is the Historical-Data Policy for Normalized Payment Schedule Aggregation?
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, historical-data, aggregation, migration, reconciliation]
related: [normalized-payment-schedule, product-agnostic-cashflow-aggregation, 2026-brp-q3-ratansett-product-agnostic-aggregation, ratan]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft", "auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"]
---
# What Is the Historical-Data Policy for Normalized Payment Schedule Aggregation?

The document explicitly references “Historical Data-User Cases,” but the behavior is contained only in unavailable screenshots and `analysis.xlsx`. No historical-data policy can be derived from the supplied text.

## Questions to resolve

- Which pre-cutover cashflows and trades are eligible for the new aggregation mechanism?
- Is historical data migrated, backfilled, replayed, excluded, or processed through legacy rules?
- How are pre-existing aggregation results reconciled with newly generated results?
- What idempotency controls apply to reprocessing?
- What audit trail identifies the aggregation path and source schedule?
- How are exceptions, partially migrated records, and rollback handled?

The historical-data worksheet and associated acceptance criteria are needed before a migration approach can be specified.