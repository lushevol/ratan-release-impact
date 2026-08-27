---
type: query
title: When Is the Cash Settlement Search Bar Disabled?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, search-bar, user-interface, query-mode]
related: [cash-settlement-home-page, cash-settlement-query-validation, reversible-cashflow-query-ui-state]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Quick Search & Custom Filter FE Query Validation.md"]
---

# When Is the Cash Settlement Search Bar Disabled?

Is the search bar permanently disabled on the Cash Settlement Home Page, or only disabled while quick search, Query Amount, Value Today, or custom-filter mode is active?

## Evidence

The source says to disable the search bar and separately requires clearing its value when a query search or filter starts. If the bar is permanently disabled, the clearing behavior has little functional effect. This suggests that disablement may be conditional, but the triggering states are not defined.

## Decision Needed

Specify:

- Which controls or modes disable the search bar.
- Whether activation of Query Amount or Value Today also disables it.
- Whether a user can return to ordinary search after cancelling a query.
- Whether clearing occurs before or after query validation.
- The disabled-state message and accessibility behavior.