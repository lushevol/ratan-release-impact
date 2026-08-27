---
type: query
title: Which Cash Settlement Dropdowns Must Be Consistent Across Blotter, Grouping, Dashboard, and Vostro Views?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ui, dropdowns, consistency, open-question]
related: [ratan-ui-dropdown-data-source, cashflow-dropdown-consistency, cashflow-blotter, grouping-blotter, dashboard, canonical-dropdown-data-source]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
---
# Which Cash Settlement Dropdowns Must Be Consistent Across Blotter, Grouping, Dashboard, and Vostro Views?

## Question

Which business fields must expose identical or intentionally compatible option sets, labels, codes, filtering semantics, and entitlement behavior across Cashflow Blotter, Grouping Blotter, Dashboard, and Cashflow Details — Vostro Exception?

## Evidence

Booking Entity is listed in Cashflow Blotter Quick Search, Quick Filter, and Custom Search contexts, as well as Grouping Blotter Quick Search and Dashboard Quick Search contexts. Other fields appear repeatedly in the table, but omitted Topic cells make some associations ambiguous.

## Required Resolution

The owning teams should confirm:

- Whether repeated fields use one canonical vocabulary
- Whether screen-specific filtering is allowed
- Whether inactive or historical values remain searchable
- Whether user entitlements change available values by screen
- Whether codes and labels are shared across APIs
- Whether state and exception values align with the relevant domain state machines

The original editable inventory or screenshots should be reviewed before treating carried-forward Topic values as definitive.