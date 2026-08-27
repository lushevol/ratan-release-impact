---
type: query
title: What Is the Authoritative Settlement Method Precedence for Netting Resultants?
created: 2026-08-23
updated: 2026-08-23
tags: [netting, settlement-method, DVP, CCIL, precedence]
related: [netting-resultant-settlement-method-selection, netting-resultant-cashflow, ccil]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Service - GUI & API intergration.md"]
---
# What Is the Authoritative Settlement Method Precedence for Netting Resultants?

The resultant mapping calls for `Gross` as the hard-coded settlement method, while also requiring `DVP` when any component is `DVP` and `CCIL` for IRS Netting.

## Required resolution

Specify:

- Whether `Gross` is a default or an unconditional value.
- Whether any `DVP` component overrides `Gross`.
- Whether IRS Netting overrides `DVP`.
- The rule where DVP and CCIL conditions both apply.
- Whether the selected method is validated against all components before resultant creation.

See [[netting-resultant-settlement-method-selection]].