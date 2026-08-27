---
type: concept
title: Manual Un-Netting
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, un-netting, cashflow-lifecycle]
related: [ccil-manual-netting, automatic-un-netting-on-trade-market-events, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/02 CCIL Netting.md"]
---
# Manual Un-Netting

Manual un-netting is a user-initiated reversal of a CCIL netting result.

A user selects the resultant cashflow, invokes **Un-Net Cashflow**, and confirms **Un-Net all Cashflow**. The source expects the original resultant to transition to `DEAD` and all component cashflows to return to `WAITING` with sub-state `Pending Netting`.

The restored components may subsequently be submitted through CCIL manual netting to produce a new resultant. In the acceptance case, `N1` becomes `DEAD` and re-netting its components generates `N2`.

Manual un-netting is distinct from [[automatic-un-netting-on-trade-market-events]], which is triggered by withdrawal of a component before the resultant is released or settled.