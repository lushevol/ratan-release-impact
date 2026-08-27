---
type: concept
title: Trade Remaining-Amount Visibility
tags: [remaining-amount, Blade, FXU, utilization, trade-ticket]
related: [fxu, blade, ratan, fxu-settlement-method-amendment]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Dependencies for expansion to other Markets.md"]
---
# Trade Remaining-Amount Visibility

The source requires the remaining amount to be displayed in Blade for operational and FO stakeholders.

## Required views

The remaining amount must be:

- Visible in the same Blade trade ticket.
- Available in a single Blade view for FO stakeholders.
- Displayed in Blade generally.

The three statements may reinforce one requirement or may represent different audiences and views. The source does not define the distinction.

## Unspecified display contract

The source does not define the remaining-amount formula, currency, precision, data source, refresh timing, treatment of partial utilization, treatment of FX-swap legs, or audit and permission behavior. These details are required before the display can serve as an authoritative operational value.