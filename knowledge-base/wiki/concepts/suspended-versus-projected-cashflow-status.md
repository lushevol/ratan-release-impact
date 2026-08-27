---
type: concept
title: "SUSPENDED Versus PROJECTED Cashflow Status"
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, suspended, projected, status, settlement, group-blotter]
related: [stella-ratan-cashflow-filtering, cash-settlement-home-page, ratan-cashflow-dashboard, dashboard-cashflow-status-counting, maker-checker-cashflow-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SUSPENDED vs PROJECTED cashflow status in Ratan.md"]
---
# SUSPENDED Versus PROJECTED Cashflow Status

## Definitions

`SUSPENDED` identifies a cashflow that is not currently eligible for normal settlement processing. The source assigns straightforward exclusion rules to Stella, including migration, placeholder, ETD, PreAllocation, and selected portfolio-reassignment cashflows.

`PROJECTED` identifies a cashflow that remains represented as an expected future settlement or is retained for downstream processing. In particular, FXO-generated FXD may need to remain `PROJECTED` in Ratan so it can be netted with `LNBR` and `CCS` components.

The source also uses “suppressed,” “filtered,” and “aborted” as processing outcomes, but does not establish whether they are separate statuses or stages in one lifecycle.

## Operational behavior

Suspended cashflows are dropped from the Cash Settlement Home Page group blotter. A suspended cashflow may nevertheless be manually STPed into the cashflow blotter through maker-checker control.

The exact effect of manual STP is unresolved: it is not clear whether STP changes the status, bypasses suppression, or creates a new processing attempt.

## Important distinction

The current Stella rule suspends eligible FX `additionalPayment` cashflows. A future rule is described as publishing all FX cashflows as `PROJECTED`. The source does not specify the migration date, precedence, or authoritative owner of the future behavior.

This status ambiguity affects [[concepts/dashboard-cashflow-status-counting]], [[concepts/ratan-cashflow-dashboard]], and settlement routing to [[entities/razor]].