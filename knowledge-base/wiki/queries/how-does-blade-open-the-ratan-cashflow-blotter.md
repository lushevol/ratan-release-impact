---
type: query
title: How Does Blade Open the Ratan Cashflow Blotter?
tags: [blade, ratan, openfin, integration, deep-linking]
related: [blade, ratan, openfin, trade-to-cashflow-navigation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Remaining Amount via OpenFin.md"]
---
# How Does Blade Open the Ratan Cashflow Blotter?

Blade exposes the `Show Cashflow in Ratan` user action, after which Ratan opens and displays the selected trade's cashflows. The technical integration contract is not documented.

## Questions to resolve

- Is the transfer implemented through an OpenFin message, deep link, URL, manifest parameter, or shared state?
- What identifier or payload is passed from Blade to Ratan?
- How is the target cashflow-blotter filter constructed from the Trade ID?
- What happens if Ratan is unavailable, the user session is stale, or the trade cannot be found?
- Which entitlement checks occur before and after navigation?

## Current evidence

[[fxu-remaining-amount-via-openfin]] establishes the user-visible sequence but not its transport, payload, or failure semantics.