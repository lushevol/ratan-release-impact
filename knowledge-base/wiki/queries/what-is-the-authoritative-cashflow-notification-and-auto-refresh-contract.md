---
type: query
title: What Is the Authoritative Cashflow Notification and Auto-Refresh Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow, notifications, auto-refresh, open-question]
related: [cashflow-notification-and-auto-refresh, cashflow-version-tuple-comparison, entitlement-aware-ui-notifications, cashflow-blotter, query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/cashflow notification.md"]
---

# What Is the Authoritative Cashflow Notification and Auto-Refresh Contract?

## Question

What notification, freshness, authorization, and user-interaction contract should govern Cashflow Blotter auto-refresh and updates to an open cashflow?

## Known Requirements

The source supports the following intended behavior:

- New cashflows should appear in the blotter without manual refresh.
- New list records should be visually highlighted rather than require a blocking pop-up.
- Notifications should contain full cashflow data and avoid a follow-up UI query.
- Entitlements must apply to notifications.
- Level 1 updates must be evaluated against current search and sorting conditions.
- Level 2 updates must be compared with the currently open cashflow before taking action.
- A stale open cashflow must be refreshed before normal actions continue.
- Latest status and exceptions must determine allowable actions after refresh.

## Decisions Needed

1. Is the Level 2 interaction a Yes/No prompt, where “No” closes the cashflow, or an OK-only mandatory refresh alert?
2. What happens to unsaved user changes?
3. Is freshness based on tuple inequality, monotonic ordering, or another rule for `cashflowVersion`, `cashflowBusinessVersion`, and `cashflowMinorVersion`?
4. How are duplicate, delayed, out-of-order, and missed events handled?
5. Where are entitlement checks enforced?
6. Which status enumeration is authoritative, and how are `cashFlowStatus` and nested `cashflow_State` reconciled?
7. Are delete, cancel, or withdrawal events required?
8. What transport, retry, replay, acknowledgement, and observability guarantees apply?
9. Does “full data” include settlement-account fields for every entitled recipient?
10. What throughput and payload-size limits apply during high-volume auto-refresh?

## Evidence Boundary

The source is a design proposal. It does not establish an implemented transport, production behavior, performance baseline, or approved security architecture.