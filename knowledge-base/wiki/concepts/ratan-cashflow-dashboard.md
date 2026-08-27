---
type: concept
title: RATAN Cashflow Dashboard
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, dashboard, cashflow-monitoring, exception-monitoring]
related: [ratan, ratan-14764, dashboard-cashflow-status-counting, dashboard-quick-search-filtering, cashflow-blotter, group-blotter, grouped-cashflow-monitoring, timer-based-dashboard-exception-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/RATAN Cashflow Dashboard.md"]
---
# RATAN Cashflow Dashboard

The RATAN Cashflow Dashboard is a monitoring surface for categorized cashflow and exception status in [[ratan]]. It is associated with the Dashboard MVP work item [[ratan-14764]].

## Defined MVP Capabilities

- Quick Search refresh using Country, Booking Entity, Client Type, Status, and Sub Status.
- Count banners for selected cashflow, accounting, Swift, and group-state conditions.
- A Cashflow Pending Settlement section, although the source provides no functional definition for that section.

The exact counter predicates are documented in [[dashboard-cashflow-status-counting]]. The filter dimensions and their gaps are documented in [[dashboard-quick-search-filtering]].

## Relationship to Other Monitoring Views

The dashboard provides summary aggregation distinct from detailed operational views such as the [[cashflow-blotter]] and [[group-blotter]]. The source does not specify navigation, drill-down, shared filtering, or data synchronization between these views.

Dashboard group counters cover `PENDING` and `ERROR` states, complementing [[grouped-cashflow-monitoring]] and [[group-pending-monitoring]]. This requirement does not establish a complete group-state lifecycle.

## Limitations of the Requirement

The source leaves unspecified:

- personas, entitlements, and refresh expectations;
- whether banner populations overlap or are deduplicated;
- status-value authority and case-matching rules;
- time-zone and calendar semantics for date-based counters;
- Queued and Hold counter definitions;
- the detailed behaviour of Cashflow Pending Settlement.

Timer-based dashboard visibility described in [[timer-based-dashboard-exception-visibility]] is separate from this dashboard's status- and payment-date-based counters.