---
type: source
title: RATAN Cashflow Dashboard Functional Requirement
authors: []
year: 2024
url: "https://jira.global.standardchartered.com/browse/RATAN-14764"
venue: "Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow-dashboard, functional-requirement, monitoring]
related: [ratan, ratan-14764, ratan-cashflow-dashboard, dashboard-cashflow-status-counting, dashboard-quick-search-filtering, grouped-cashflow-monitoring, group-pending-monitoring, cashflow-blotter, group-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/RATAN Cashflow Dashboard.md"]
---
# RATAN Cashflow Dashboard Functional Requirement

## Purpose

The RATAN Cashflow Dashboard is intended to let users check categorized cashflow and exception status. The linked Dashboard MVP requirement is [[ratan-14764]].

The document specifies dashboard search dimensions and several counting-banner predicates. It does not define dashboard drill-down behaviour, aggregation semantics, data ownership, entitlement rules, or refresh latency.

## Dashboard UI

![Dashboard UI](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--24-ratan-cashflow-dashbo--10odcxq/image2024-7-10_16-54-10.png)

## Quick Search

Quick Search supports dashboard refresh using search criteria.

![Quick Search](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--24-ratan-cashflow-dashbo--10odcxq/image2024-7-11_10-50-33.png)

The source content, including its incomplete Country mapping structure, is preserved below.

| Filter | Source-defined content |
|---|---|
| Country | mapped country list |
| Value in dropdown | |
| Mapped query condition | |
| China | |
| Booking Entity | hard coded list from FE. list of in scope booking entity FMCODE |
| Client Type | hard coded list from FE. List of in scope client type |
| Status | hard coded list from FE. list of in scope cashflow status |
| Sub Status | Pending Operator; Pending Verification |

The Country mapping does not provide a dropdown value or mapped query condition for China. Booking Entity, Client Type, and Status lists are specified as hard-coded Front End lists; no owner, source of truth, or change-control process is identified. See [[dashboard-quick-search-filtering]].

## Counting Banner

![Counting Banner](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--24-ratan-cashflow-dashbo--10odcxq/image2024-7-11_10-51-3.png)

| Banner | Exact selection criterion |
|---|---|
| Waiting VD Today | `Cashflow State = "WAITING" and Payment Date = Current Date` |
| Failed VD Today | `Cashflow State = "FAILED" and Payment Date = Current Date` |
| Error | `Cashflow State = "Error" and Payment Date >=Current Date and Payment Date<=Current Date + 7D` |
| Accounting Error | `Accounting Status in ('SENT', 'DISABLED','HOLDING','REJECTED','MISSING_INFO')` |
| Swift Error | `Swift Status in ('AMH Error', 'FMSGW Error', 'FMSRE Error', 'MX Generation Error', 'Ratan Internal Error', 'SCPAY Error')` |
| Queued | No criterion specified. |
| Hold | No criterion specified. |
| Group Pending | `Group State ='PENDING'` |
| Group Error | `Group State ='ERROR'` |

These predicates distinguish Cashflow State, Accounting Status, Swift Status, and Group State. The source does not say whether counters are mutually exclusive, whether a cashflow may appear in multiple counters, or whether status matching is case-sensitive. It also does not define the time zone or calendar convention for `Current Date` and `Current Date + 7D`.

The group predicates add dashboard-level summaries related to [[grouped-cashflow-monitoring]] and [[group-pending-monitoring]]; they do not define the complete group-state model.

## Cashflow Pending Settlement

![Cashflow Pending Settlement](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--24-ratan-cashflow-dashbo--10odcxq/image2024-7-11_11-10-39.png)

The supplied requirement contains only this heading and screenshot. It provides no fields, criteria, behaviour, or acceptance criteria for the section.

## Open Requirement Gaps

- The Country-to-query mapping is incomplete.
- Queued and Hold have no counting definitions.
- Cashflow Pending Settlement has no textual specification.
- The valid status catalogues and multi-banner overlap rules are not identified.
- Date and seven-day-window semantics are not defined.
- Front End hard-coded filter lists have no documented governance.

See [[ratan-cashflow-dashboard]], [[dashboard-cashflow-status-counting]], and [[dashboard-quick-search-filtering]].