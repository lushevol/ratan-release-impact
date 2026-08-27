---
type: query
title: What Is the Effective-Date Rule for Lien Cashflow NSTP?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, lien, nstp, cashflows, event-time, settlement]
related: [lien-driven-cashflow-nstp, trade-to-cashflow-lien-correlation, cashflow-lifecycle-state-machine, business-versioned-cashflow-persistence, murex, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration.md"]
---
# What Is the Effective-Date Rule for Lien Cashflow NSTP?

## Question

When a Lien is added or removed during a trade lifecycle, which existing and future cashflows must RATAN update, suppress, or allow to settle STP?

## Evidence

The requirement gives three outcomes:

- A Lien added at booking applies to all underlying cashflows.
- A Lien added during the lifecycle applies to cashflows after the Lien update.
- A Lien removed before maturity means cashflows after removal do not receive a `Lien` exception and may be STP if no other exception exists.

The source does not define whether “after” means after event receipt, event effective time, cashflow creation, cashflow amendment, value date, or migration time.

## Decisions Required

The implementation specification should clarify:

1. Whether Lien placement retroactively updates already-created future cashflows.
2. Whether Lien removal independently removes only the `Lien` exception.
3. How other exceptions interact with the post-removal STP outcome.
4. How amended, withdrawn, and recreated cashflows inherit Lien treatment.
5. How event order is resolved when Lien changes and cashflow updates are asynchronous.

This resolution is required for the [[concepts/cashflow-lifecycle-state-machine]], migration testing, and reconciliation controls.
