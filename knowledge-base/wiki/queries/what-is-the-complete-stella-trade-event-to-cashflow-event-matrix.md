---
type: query
title: What Is the Complete Stella Trade Event-to-Cashflow Event Matrix?
created: 2026-08-24
updated: 2026-08-24
tags: [stella, cashflow-events, trade-events, cdu, business-rules]
related: [stella, cdu, trade-confirmation-driven-cashflow-stp, trade-cashflow-correlation-by-trade-version]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md"]
---
# What Is the Complete Stella Trade Event-to-Cashflow Event Matrix?

The supplied Stella business-case matrix is described as covering common cases but contains incomplete and potentially inconsistent rows.

Resolve the authoritative mapping and confirmation behavior for:

- `Fixing`.
- `PortfolioReassignment`.
- `Trade | Revive`, including its `V3`, `C2`, and `C1` relationship.
- Cancellation and withdrawal “special STP” handling.
- `Trade | Expiry` filtering.
- Exceptional Murex scenarios referenced but not supplied.
- The meaning of `Y` and `NA` in the CDU confirmation and STP columns.