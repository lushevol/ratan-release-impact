---
type: concept
title: Dashboard Quick Search Filtering
created: 2026-08-23
updated: 2026-08-23
tags: [dashboard, quick-search, filtering, front-end, static-data]
related: [ratan-cashflow-dashboard, ratan, cashflow-blotter, what-is-the-authoritative-ratan-dashboard-country-to-booking-entity-mapping, who-governs-ratan-dashboard-front-end-hard-coded-filter-lists]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/RATAN Cashflow Dashboard.md"]
---
# Dashboard Quick Search Filtering

Quick Search is intended to refresh the RATAN Cashflow Dashboard using search criteria.

## Specified Dimensions

| Filter | Requirement detail |
|---|---|
| Country | A mapped country list is intended. The only shown Country is China, but no dropdown value or mapped query condition is supplied. |
| Booking Entity | A Front End hard-coded list of in-scope booking-entity `FMCODE` values. |
| Client Type | A Front End hard-coded list of in-scope client types. |
| Status | A Front End hard-coded list of in-scope cashflow statuses. |
| Sub Status | `Pending Operator` and `Pending Verification`. |

## Requirement Gaps

The source does not define default selections, empty-selection behaviour, filter combination logic, reset behaviour, permissions, query contracts, or whether all dashboard counters and Cashflow Pending Settlement use the same filters.

The incomplete Country mapping is tracked in [[what-is-the-authoritative-ratan-dashboard-country-to-booking-entity-mapping]]. Governance of Front End hard-coded Booking Entity, Client Type, and Status lists is tracked in [[who-governs-ratan-dashboard-front-end-hard-coded-filter-lists]].

The source does not define an integration with the [[cashflow-blotter]].