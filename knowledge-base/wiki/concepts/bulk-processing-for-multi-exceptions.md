---
type: concept
title: Bulk Processing for Multi-Exceptions
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, multi-exceptions, bulk-processing, workflow]
related: [bulk-cashflow-selection-homogeneity, bulk-exception-preview-eligibility, cashflow-bulk-submit-and-approve, cashflow-blotter, cashflow-filtering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions/Bulk UI Technical Design.md"]
---
# Bulk Processing for Multi-Exceptions

Bulk processing for multi-exceptions is the workflow for applying a supported action to multiple selected cashflows from the Cash Settlement Home Page.

## Entry Conditions

The bulk right menu is shown only when:

- At least two cashflows are selected.
- All selected cashflows satisfy the state, sub-state, sub-state-type, and user-profile criteria for a specific bulk action.

A single selected cashflow therefore does not qualify for the bulk right menu.

## Supported Actions

- An `Initial` user can use **Bulk Submit** for cashflows in `WAITING`, with sub-state `Pending Operator` and sub-state type `Pending Exception`.
- A `Verify` user can use **Bulk Approve** for cashflows in `WAITING`, with sub-state `Pending Verification` and sub-state type `Pending Exception`.

## Validation Stages

Bulk processing uses two distinct gates:

1. **Action and selection gate:** Determines whether the bulk right menu and a specific action are available.
2. **Preview gate:** Validates homogeneous business attributes and evaluates checker, exception, risk-permission, and authorization-limit conditions.

Passing the first gate does not guarantee that the selection can enter or complete bulk preview.

## Scope and Unresolved Rules

The design does not specify whether mixed-status selections hide the menu, disable an action, or produce an error. It also does not state whether a single ineligible cashflow rejects the whole batch or is reported separately. These rules require confirmation through [[queries/what-is-the-authoritative-bulk-multi-exception-eligibility-matrix]] and [[queries/does-one-ineligible-cashflow-block-the-entire-bulk-operation]].