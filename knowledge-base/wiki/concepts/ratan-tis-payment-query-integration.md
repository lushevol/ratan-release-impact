---
type: concept
title: RATAN-to-TIS Payment Query Integration
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, tis, api, cash-settlement, korea-migration, read-only]
related: [ratan, tis, oltp, scfb-seoul, korea-cash-settlement-migration, korea-settlement-account-routing, korea-tis-payment-type-classification, what-is-the-authoritative-ratan-tis-api-error-contract, how-are-post-query-cancellations-and-reversals-reconciled-in-tis-and-oltp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# RATAN-to-TIS Payment Query Integration

The RATAN-to-TIS Payment Query Integration is a date-parameterized interface for Korean cashflows. [[tis]] queries [[ratan]] for eligible cashflows and passes payment information to [[oltp]], replacing daily manual OLTP(UI) re-keying.

## Integration model

```text
RATAN → TIS → OLTP(UI)
```

RATAN is the data provider. TIS is a read-only consumer: it sends no post-query acknowledgement or status update, and a query does not change the RATAN cashflow state.

The interface is restricted to [[scfb-seoul]] (`FMID 10036645`).

## Query routes

- Pay-side route: `/api/ratan/v1/tis/query/payment/{paymentDate}`
  - `NOX` settlement means.
  - `UISUS` or `UIBOK` settlement-account marker.
  - `Pay` direction.
- Receipt route: `/api/ratan/v1/tis/query/receipt/{paymentDate}`
  - `NOX` settlement means.
  - `UIDD` settlement-account marker.
  - `Receive` direction.

Both routes require the selected settlement date and require FMAA authentication headers: `FMAA-token`, `FMAA-userId`, and `FMAA-appId`.

## Eligibility control

The documented population is limited to cashflows in `Released` or `Settled` state, excludes `Cashflow_Event_Reason = 'Reversal'`, and applies the requested payment date.

Withdrawal and cancellation reversals are deliberately excluded. Since TIS does not refresh duplicate records identified by trade ID/cashflow ID, a cashflow retrieved before a later reversal has no compensating signal through this API. See [[how-are-post-query-cancellations-and-reversals-reconciled-in-tis-and-oltp]].

## Contract limitations

The available URLs use a pre-production host. The document calls the endpoint header table “POST header” but does not conclusively state the HTTP method or request body. It also provides HTTP error codes alongside `msg = "failed"` behavior without defining the no-data response shape. See [[what-is-the-authoritative-ratan-tis-api-error-contract]].