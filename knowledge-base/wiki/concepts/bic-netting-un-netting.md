---
type: concept
title: BIC-Netting Un-Netting
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, un-netting, withdrawal, amendment]
related: [beneficiary-bic-netting, netting-resultant-cashflow, cashflow-withdrawal-and-new, ratan, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting.md"]
---
# BIC-Netting Un-Netting

BIC-netting un-netting separates a resultant cashflow back into its component cashflows or reverses the netting arrangement.

## Dispute-driven un-netting

In the BAU process, settlement operations manually un-net the resultant payment when a client disputes its affirmation. The resultant may be in the maker or checker queue. If required by the client, operations can return to the BIC netting queue and perform netting again.

## Automatic pre-release un-netting

The meeting minutes require Ratan to automatically un-net the resultant cashflow when:

- A withdrawal occurs, or
- An amendment occurs,
- And the resultant cashflow has not been released.

The source does not define the exact state restoration, component-cashflow versioning, or audit events produced by this operation.

## Post-release behavior

The source notes that a trade amendment may occur after the resultant payment has settled and that Murex BAU has different cases. It does not define whether Ratan should reverse the resultant, create a replacement resultant, reopen components, or route the case to manual exception handling.

## Required controls

Un-netting should preserve the relationship between the resultant and its components through `Cashflow.Netting_Id` or an equivalent correlation mechanism. It should also prevent the same components from being concurrently selected for another BIC or bilateral netting operation.