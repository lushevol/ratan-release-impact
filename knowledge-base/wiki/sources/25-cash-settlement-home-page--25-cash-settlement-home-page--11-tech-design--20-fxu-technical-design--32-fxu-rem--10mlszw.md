---
type: source
title: FXU Remaining Amount via OpenFin
authors: []
year: 2025
url: ""
venue: Internal technical design
tags: [cash-settlement, fxu, openfin, blade, ratan, cashflow-blotter]
related: [openfin, blade, ratan, trade-to-cashflow-navigation, cashflow-remaining-amount, cashflow-blotter]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Remaining Amount via OpenFin.md"]
---
# FXU Remaining Amount via OpenFin

This technical walkthrough documents a user journey from Blade to the Ratan cashflow blotter through OpenFin. It demonstrates that users can locate a trade in Blade and open its associated cashflows in Ratan, where a remaining amount is displayed.

## Prerequisites

- OpenFin must be installed or accessible for Blade / SM Markets.
- The source references the internal installation page: https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3287919844
- Ratan must be available through its OpenFin installation.
- The user must be able to sign in to Ratan.

## Documented workflow

1. Open [[blade]] from a manifest or desktop start icon.
2. Open the Trade Query workspace.
3. Search for a trade using a specific Trade ID.
4. Right-click the trade result and select `Show Cashflow in Ratan`.
5. [[ratan]] opens in a new window; sign in using the user account.
6. The [[cashflow-blotter]] opens automatically.
7. The cashflows associated with the selected trade are displayed with a remaining amount.

## Evidence and scope

The document provides screenshots for each step of the user interaction. It is strong evidence for the expected operational workflow and the existence of the `Show Cashflow in Ratan` action.

It does not define the remaining-amount calculation, source system, data contract, currency and rounding rules, or treatment of amendments, cancellations, and partial settlements. It also does not specify the technical mechanism that transfers the Trade ID from Blade to Ratan.

The workflow should not be taken as evidence that [[openfin]], [[blade]], or a particular cashflow query service calculates the displayed value.