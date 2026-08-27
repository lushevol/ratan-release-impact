---
type: concept
title: Cash Settlement Dropdown Consistency
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ui, dropdowns, consistency, reference-data]
related: [ratan-ui-dropdown-data-source, ui-dropdown-data-source-governance, cashflow-blotter, grouping-blotter, dashboard, cashflow-group-and-message-state-machines]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
---
# Cash Settlement Dropdown Consistency

Cash Settlement dropdown consistency is the requirement that the same business field have intentional and traceable option semantics across different UI surfaces.

## Relevant Surfaces

The source lists overlapping or potentially overlapping controls across:

- Cashflow Blotter
- Grouping Blotter
- Dashboard
- Cashflow Details — Vostro Exception
- Nostro Static

Booking Entity is explicitly represented in Cashflow Blotter, Grouping Blotter, and Dashboard contexts. Product Taxonomy, Currency (CCY), and state-related fields also appear repeatedly or appear to continue across adjacent table rows, although some associations are ambiguous.

## Consistency Dimensions

Consistency should be evaluated for:

- Codes and identifiers
- Display labels
- Available values
- Filtering and search semantics
- User entitlements
- Sorting and default ordering
- Effective-date behavior
- Empty, inactive, and unknown values

A shared business field does not necessarily require the same endpoint, but differences should be explicit and justified.

## Current Evidence

The source identifies the controls but leaves both data-source columns blank. It does not prove that the screens currently share a lookup source or that they currently expose identical option sets. Alignment with [[concepts/cashflow-group-and-message-state-machines]] is also not established for state-related selectors.