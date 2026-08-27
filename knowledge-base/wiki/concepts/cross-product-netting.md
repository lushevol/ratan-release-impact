---
type: concept
title: Cross-Product Netting
created: 2026-08-22
updated: 2026-08-22
tags: [netting, cash-settlement, ratan, products, irs, ccs, stella, murex]
related: [ratan, auto-netting, netting-over-netting, netting-key-selection, resultant-cashflow, component-cashflow, fmrp-prime-uk-uat-drop-2, irs, ccs, stella, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md"]
---
# Cross-Product Netting

Cross-product netting combines eligible settlement obligations or cashflows from different products within a shared netting and settlement process.

## RATAN Scope

The FXO onboarding checklist explicitly lists cross-product netting within [[ratan]]. However, it does not identify:

- Eligible product combinations.
- Matching criteria or netting keys.
- Applicable legal agreements.
- Supported currencies.
- Settlement dates.
- Exception behavior.

The FXO checklist records cross-product netting as an onboarding area but provides no evidence that it has been configured or tested.

## Prime UK Requirement

The Prime UK checklist requires [[ratan]] to net [[irs]] and [[ccs]] cashflows originating from [[stella]] with other [[murex]] cashflows. This is a specific cross-product and cross-source-system requirement; it does not establish that every product or cashflow is eligible.

## Distinctions from Related Netting

Cross-product netting should be distinguished from:

- **[[netting-over-netting]]:** Cross-product netting groups obligations from different products, whereas netting-over-netting applies another netting layer to obligations that may already be [[resultant-cashflow|resultant cashflows]].
- **IRS interest [[auto-netting]]:** The Prime UK requirement to net STELLA-originated IRS and CCS cashflows with other Murex cashflows is distinct from IRS interest auto-netting.

## Required Design Details

A complete cross-product netting design should specify:

- Eligible product pairs or groups.
- Counterparty, entity, currency, account, and value-date compatibility.
- [[netting-key-selection|Netting keys]] and hierarchy.
- Links between [[component-cashflow]] records and the [[resultant-cashflow]].
- Treatment of cancellations, amendments, failures, and partial settlement.
- Accounting and payment-message behavior.
- Legal and operational authorization.

## Testing Expectations

Testing should prove:

- Product and cashflow eligibility.
- Source-system interoperability, including the required interaction between STELLA-originated cashflows and other Murex cashflows.
- Grouping criteria.
- Creation and traceability of resultant cashflows.
- Settlement status behavior.
- Exclusion or suppression behavior.