---
type: query
title: What Happens When Netting Calculates to Zero?
created: 2026-08-23
updated: 2026-08-23
tags: [netting, calculation, zero-balance, cashflow, precision]
related: [cashflow-netting, netting-resultant-cashflow, what-is-the-authoritative-bilateral-netting-amount-calculation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Service - GUI & API intergration.md"]
---
# What Happens When Netting Calculates to Zero?

The specified calculation treats SCB `Pay` amounts as positive and `Receive` amounts as negative. It defines `Pay` for a positive signed total and `Receive` for a negative signed total, but does not define processing for a zero total.

## Required resolution

Clarify whether RATAN must:

- Reject a zero-balance component selection.
- Create no resultant and release components through another process.
- Create a zero-amount resultant with a defined direction and lifecycle.
- Apply rounding before or after zero testing.
- Use currency-specific decimal precision and tolerance rules.

The resolution must also define exceptions, audit records, and component state transitions for the chosen outcome.