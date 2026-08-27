---
type: concept
title: Cashflow Notification and Auto-Refresh
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow, event-driven-ui, auto-refresh, notifications]
related: [cashflow-blotter, cashflow-version-tuple-comparison, entitlement-aware-ui-notifications, query-service, cash-settlement-cashflow-read-model, cashflow-blotter-query-performance, cash-settlement-release-cutoff-controls]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/cashflow notification.md"]
---

# Cashflow Notification and Auto-Refresh

Cashflow notification and auto-refresh is the proposed event-driven mechanism for keeping the Cashflow Blotter current and preventing users from acting on stale cashflow detail data.

## Notification Levels

### Level 1: Blotter List Notification

A newly created or updated cashflow is published to the UI. The UI applies its current search and sorting conditions before changing the visible list. New records should be highlighted at the top of the list with a color or column rather than forcing a pop-up.

This behavior is intended to improve visibility of value-today cashflows and cashflows approaching operational cutoffs.

### Level 2: Open Detail Notification

When a cashflow currently open in a detail dialog changes, the UI must compare the incoming version with the displayed cashflow. If the incoming version is different, the user must be informed and the detail view must be refreshed before normal actions continue.

After refresh, allowable actions must be recalculated from the latest cashflow status and exceptions. The detail view must not silently overwrite information while the user is interacting with it.

## Full-Data Notifications

The proposed notification contains the full cashflow rather than requiring the UI to issue a follow-up query. This can reduce round trips and support immediate UI updates, but it also increases payload size, schema-coupling, and sensitive-data exposure. Settlement-account fields require particular attention.

## Filtering and Authorization

The proposal separates presentation filtering from notification publication: the backend does not apply the user’s current blotter filter, and the UI decides whether to display the received record.

This does not eliminate the need for server-side or transport-level entitlement enforcement. Client-side filtering is not an authorization boundary.

## Delivery Gaps

The source defines `CASHFLOW_CREATE` and `CASHFLOW_UPDATE` only. A production contract would also need to define duplicate delivery, ordering, replay, missed-event recovery, deletion or cancellation, message identity, retries, and observability.

## Specification Tensions

The source contains two different Level 2 interaction descriptions:

- A Yes/No reload prompt, where “No” closes the cashflow.
- An OK-only alert that blocks every action except refresh.

These alternatives must be reconciled before implementation. See [[queries/what-is-the-authoritative-cashflow-notification-and-auto-refresh-contract]].