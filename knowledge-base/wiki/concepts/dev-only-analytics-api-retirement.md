---
type: concept
title: Dev-Only Analytics API Retirement
created: 2026-08-24
updated: 2026-08-24
tags: [api-retirement, analytics, development-environment, frontend, audit-trail]
related: [audit-trail, single-ui-bff, shared-user-action-analytics-api, frontend-error-logging-and-user-action-analytics, cash-settlement-audit-api-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# Dev-Only Analytics API Retirement

Dev-only analytics API retirement is the planned removal of `/v1/ratan-analytic`, an [[audit-trail]] endpoint described as active only in development through frontend ternary logic.

Non-development environments use `/v1/fmo/print` instead. The endpoint writes to the `ratan-analytic-data` index and is marked as unnecessary to implement for Indonesia.

The source labels the item `todo`; it does not provide a decommissioning date, consumer inventory, frontend release plan, historical-data treatment, rollback process, or formal completion criteria.