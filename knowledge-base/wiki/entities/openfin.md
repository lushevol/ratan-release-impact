---
type: entity
title: OpenFin
tags: [desktop-runtime, application-integration, cash-settlement]
related: [blade, ratan, trade-to-cashflow-navigation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Remaining Amount via OpenFin.md"]
---
# OpenFin

OpenFin is the desktop/runtime integration entry point used in the documented Blade-to-Ratan workflow.

Users install or access OpenFin for Blade / SM Markets, then launch [[blade]] from a manifest or desktop icon. The workflow subsequently opens [[ratan]] in a separate window after the user selects `Show Cashflow in Ratan` for a trade.

## Scope of evidence

The source establishes OpenFin as a delivery and launch mechanism for the user journey. It does not establish that OpenFin transports the Trade ID, provides authorization handoff, retrieves cashflows, or calculates [[cashflow-remaining-amount]].