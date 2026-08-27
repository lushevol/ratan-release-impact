---
type: query
title: What Is the Ratan Auto Un-Netting Contract for Cancellation and Termination Events?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, netting, cancellation, termination, trade-market-event]
related: [automatic-un-netting-on-trade-market-events, ratan, cashflow-withdrawal-and-new, reversal-and-correction-cashflow-processing, what-is-the-authoritative-murex-cancellation-removal-cashflow-sequencing-and-correlation-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Auto Un-Net - Trade market event.md"]
---
# What Is the Ratan Auto Un-Netting Contract for Cancellation and Termination Events?

## Question

What processing, status transitions, resultant disposition, and user-review controls apply when Cancellation or Termination events affect a previously netted Ratan component?

## Evidence

The source lists Amendment, Cancellation, and Termination as trade-market events that may arrive after FMRP strategy netting. However, it provides a detailed outcome only for an Amendment from Stella.

That Amendment releases all components in the affected group and marks the original Ratan resultant `Dead`. No equivalent example or rule is supplied for Cancellation or Termination.

## Clarifications needed

- Whether Cancellation and Termination always trigger group-level un-netting.
- Whether they result in component withdrawal, replacement cashflow creation, or a status-only change.
- Whether the existing resultant must become `Dead` in every case.
- Whether the same `NSTP` versus `Queued` ambiguity applies.
- Required accounting, payment, and settlement restrictions where the resultant has progressed downstream.
- Whether source-system-specific rules differ for Stella, Murex 2.11, and MXCash.

Related: [[cashflow-withdrawal-and-new]], [[reversal-and-correction-cashflow-processing]], and [[what-is-the-authoritative-murex-cancellation-removal-cashflow-sequencing-and-correlation-model]].