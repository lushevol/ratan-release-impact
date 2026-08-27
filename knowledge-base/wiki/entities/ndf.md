---
type: entity
title: NDF
created: 2026-08-24
updated: 2026-08-24
tags: [ndf, non-deliverable-forward, trade-product, cash-settlement]
related: [cashflow-event-control, trade-event-undo-semantics, cashflow-suppression-rules, ratan-cashflow-acknowledgement-and-release-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/CN Drop 2 UAT - Settlements Scenarios - 2024.md"]
---
# NDF

NDF is a central product in the CN Drop 2 settlement UAT catalogue. Coverage includes single and BTB3/5/7 booking, backdated booking, termination fees, portfolio reassignment, novation, withdrawal, reversal, suppression, and NSTP alert behavior.

One detailed issue sequence models an NDF cashflow lifecycle in which released cashflow `C1` is amended, withdrawn, replaced by `C2`, and then withdrawn again. The source specifies `SWIFT_SUPPRESSED` handling for accounting generation and manual drafting of `MT192` messages in [[entities/amh]]. It also calls for an NSTP alert when a withdrawal occurs without a newly released cashflow.

These rules are specific to the tested NDF sequence and should not be treated as universal cancellation behavior.