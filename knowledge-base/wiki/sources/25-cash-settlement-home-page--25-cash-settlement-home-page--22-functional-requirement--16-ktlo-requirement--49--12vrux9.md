---
type: source
title: Update Counterparty BIC Display in i Icon
authors: []
year: 2025
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement-home-page, cashflow-details, counterparty, swift-bic, sci, ui-requirement, ktlo]
related: [cash-settlement-home-page, sci, cashflow-detail-field-projection, counterparty-bic-display-mapping, what-is-the-authoritative-counterparty-bic-display-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/8870075-Update counterparty BIC display in  i  icon.md"]
---
# Update Counterparty BIC Display in i Icon

This functional requirement changes the proposed source-field mapping for the `SWIFT BIC` value shown in the counterparty section of Cashflow Details on the [[cash-settlement-home-page]].

## Scope

The affected user interaction is:

1. Double-click a cashflow.
2. Open `Cashflow Details-Counterparty` through the “i” icon.
3. View the counterparty `SWIFT BIC` field.

The source characterizes the change as potentially front-end-only, subject to confirmation with a UI developer.

## Current behavior

The current implementation calls [[sci]] to obtain a BIC type value and displays that value under `SWIFT BIC`.

> Call SCI to get the BIC type value then set the value to `SWIFT BIC`

## Proposed behavior

The proposed implementation calls SCI and uses `addrLine` as the displayed `SWIFT BIC` value when the relevant item has `mediumUsage = 'MAIN'`.

> Call SCI to get the below item, then set the value of `addrLine` to `SWIFT BIC` when `mediumUsage` = `'MAIN'` if the `SWIFT BIC` != `SCBLGB2LXXX`

This is a specialized field-projection rule within [[cashflow-detail-field-projection]].

## Unresolved rule semantics

The source does not establish whether `SCBLGB2LXXX` is compared with:

- the current BIC type value;
- the selected `addrLine` value; or
- the final value displayed as `SWIFT BIC`.

It also does not specify the fallback behavior when no `MAIN` item exists, `addrLine` is blank, or more than one item has `mediumUsage = 'MAIN'`. These gaps are tracked in [[what-is-the-authoritative-counterparty-bic-display-mapping]].

## Attached evidence

![Counterparty BIC display context](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-ktlo-requirement--49--12vrux9/image-2025-7-4_15-45-53.png)

![Cashflow Details-Counterparty context](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-ktlo-requirement--49--12vrux9/image-2025-7-4_15-44-57.png)

![SCI item example](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-ktlo-requirement--49--12vrux9/image-2025-7-2_15-5-6.png)