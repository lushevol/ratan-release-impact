---
type: concept
title: Strategy Rounding Ownership
created: 2026-08-22
updated: 2026-08-22
tags: [rounding, settlement, stella, fixing, trade, cashflow, ownership]
related: [stella, ratan, strategy-golden-source, global-rates-settlement-strategy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md"]
---
# Strategy Rounding Ownership

Strategy rounding ownership concerns the placement of rounding rules across trade, cashflow, fixing, confirmation, fixing notices, and settlement.

The requirement requests generic universal rounding logic in Stella so that trade, cashflow, and fixing-related outputs share the same behavior. Peter Arnold's comment states that rounding required for settlements should instead be performed by Settlements.

This is an unresolved ownership tension. A final design must determine whether one shared rounding authority is required or whether settlement-specific rounding may legitimately differ from booking and fixing calculations.