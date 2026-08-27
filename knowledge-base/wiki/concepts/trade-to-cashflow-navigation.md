---
type: concept
title: Trade-to-Cashflow Navigation
tags: [cash-settlement, trade-query, cross-application-navigation, cashflow-blotter]
related: [blade, ratan, openfin, cashflow-blotter, cashflow-remaining-amount]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Remaining Amount via OpenFin.md"]
---
# Trade-to-Cashflow Navigation

Trade-to-cashflow navigation is a user journey that starts from a selected trade and opens the cashflows associated with that trade in a cashflow view.

In the documented workflow, a user searches for a Trade ID in [[blade]] Trade Query, then selects `Show Cashflow in Ratan`. [[ratan]] opens in a new window, authenticates the user, and automatically opens the [[cashflow-blotter]] for the trade's cashflows.

## Known behavior

- The navigation starts from a Blade trade-search result.
- The visible user action is `Show Cashflow in Ratan`.
- Ratan authentication occurs after the new window opens.
- The cashflow blotter is expected to open automatically.

## Undocumented behavior

The source does not specify how the trade context is passed between applications, whether the navigation is implemented as a deep link or messaging flow, or how missing trades and authorization failures are handled. Those concerns are tracked in [[how-does-blade-open-the-ratan-cashflow-blotter]].