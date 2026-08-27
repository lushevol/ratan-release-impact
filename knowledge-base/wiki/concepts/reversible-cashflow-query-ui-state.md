---
type: concept
title: Reversible Cashflow Query UI State
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, user-interface, query-state, toggle, navigation]
related: [cash-settlement-home-page, cash-settlement-query-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Quick Search & Custom Filter FE Query Validation.md"]
---

# Reversible Cashflow Query UI State

Reversible Cashflow Query UI State describes query controls that visibly indicate activation and can be cancelled by clicking the same control again.

## Query Amount

Query Amount is re-enabled. Clicking it navigates the user to detailed cashflows and highlights the button. Clicking it again disables that state.

The requirement does not specify whether the control applies a new query, changes only the view, or how it interacts with quick search and custom filters.

## Value Today

The top-right Value Today control is highlighted after the user clicks it. A second click cancels the query.

The source does not define the value-date calculation, the initial default state, or the behavior when another query or filter is active.

## Incomplete States

The source includes “By Default” and “Navigated” labels without accompanying acceptance criteria. Their expected UI states require clarification.