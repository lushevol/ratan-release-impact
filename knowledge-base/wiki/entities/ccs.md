---
type: entity
title: CCS
created: 2026-08-22
updated: 2026-08-23
tags: [product, cross-currency-swaps, fmrp, cash-settlement, auto-netting, product-type, cross-currency-swap, ccs, trade-product]
related: [fmrp-prime-uk-uat-drop-2, fmrp, ratan, stella, murex, irs, ssi-stamping, cross-product-netting, cashflow-suppression, normalized-payment-schedule, schedule-to-cashflow-matching, expected-payment-count-for-auto-netting, what-is-the-schedule-currency-rule-for-ccs-amortization-payments, cashflow-event-control, cashflow-netting-and-auto-netting, btb3-5-7-trade-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md"]
---
# CCS

CCS is the cross-currency swap product type referenced by the product-agnostic payment-schedule requirement.

## Role in UAT

### Prime UK UAT

CCS is one of the products explicitly covered by the FMRP Prime UK UAT Drop 2 onboarding checklist.

### CN Drop 2 settlement UAT

The CN Drop 2 settlement UAT catalogue identifies CCS as a central product. Its CCS scenarios include:

- Single and package bookings
- Inter-entity and intra-entity trading
- Backdated events
- Upfront and termination fees
- Netting
- B2B non-China cashflow suppression
- Novation

The CN Drop 2 source uses CCS as a product-specific test subject. Its scenarios should not be generalized to IRS, NDF, or SCF processing without separate evidence.

## Required onboarding behavior

The FMRP Prime UK UAT Drop 2 onboarding checklist requires CCS coverage for:

- SSI auto-attachment
- CFI-code capture
- Settlement-method selection
- Nostro auto-stamping
- SWIFT generation
- Accounting generation

CCS is also included in:

- Markitwire allocation scenarios, where ALOC cashflows are not STP'd.
- Clearing-portfolio suppression for `CLIENT_CLRG_LCH_STL` and `CLIENT_CLR_HKEX_ST`.
- Cross-product netting within RATAN between STELLA IRS and CCS cashflows and other Murex cashflows.

The Prime UK onboarding checklist provides less product-specific lifecycle detail for CCS than for IRS. IRS-specific fixing and interest-netting behavior should not automatically be attributed to CCS.

## Payment schedules and auto-aggregation

The product-agnostic payment-schedule requirement states that CCS scope includes:

- Deliverable CCS coupons on both legs
- ND CCS coupons on both legs
- Non-MTM CCS principal exchanges
- CCS amortization schedules

Payment-schedule matching requires both the payment date and currency to equal those of the current cashflow.

### Amortization schedule currency

The supplied CCS amortization mappings contain schedule dates but no schedule-currency field. This prevents a fully specified application of the mandatory date-and-currency matching rule until the currency-derivation approach is defined. See what is the schedule currency rule for ccs amortization payments.