---
type: entity
title: Dashboard
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratan, ui, dashboard]
related: [ratan-ui-dropdown-data-source, cashflow-blotter, grouping-blotter, cashflow-dropdown-consistency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
---
# Dashboard

## Role

Dashboard is a peripheral Cash Settlement UI surface identified in the dropdown inventory. The source lists a Booking Entity Quick Search control.

## Data-Source Governance

No current or proper data source is recorded. The Booking Entity selector should be compared with the corresponding Cashflow Blotter and Grouping Blotter controls to determine whether code sets, labels, filtering semantics, and entitlements are required to match.

The source does not establish whether the Dashboard consumes a shared endpoint or maintains a separate lookup.