---
type: concept
title: Manual Cashflow Rounding
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, payment, manual-rounding, settlement]
related: [usd-equivalent-cashflow-adjustment-limit, cashflow-amendment-maker-checker-control, settlement-accounting, tlm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding.md"]
---
# Manual Cashflow Rounding

Manual Cashflow Rounding is a proposed capability allowing a user to increase or decrease a payment cashflow amount by a small amount, described in the requirement as “few cents.”

The adjustment is intended to be controlled by a [[concepts/cashflow-amendment-maker-checker-control]] workflow and constrained by the [[concepts/usd-equivalent-cashflow-adjustment-limit]]. The source associates the action with the `WAITING` cashflow state, but does not confirm whether `WAITING` is the only eligible state.

## Downstream behavior

The final requirement direction is that SWIFT and [[entities/settlement-accounting]] use the same updated amount. This is related to, but distinct from, the general [[concepts/outbound-property-propagation-to-swift-mt-mx]] contract.

## Scope boundaries

The source does not define eligible cashflow types, currencies, decimal precision, minimum or maximum native-currency delta, repeated adjustments, zero or negative resulting amounts, or the complete audit record.

An adjustment may create a trade/cashflow reconciliation difference. This risk requires alignment with the [[stakeholders/recon-team]] and clarification of whether [[entities/tlm]] is the appropriate checking system.

## User interface

The proposed popup is limited to the amount and currency/USD amount. The source does not clarify whether these values represent the adjustment, revised total, or USD-equivalent delta.
