---
type: entity
title: IRS
created: 2026-08-22
updated: 2026-08-23
tags: [product, interest-rate-swaps, fmrp, cash-settlement, auto-netting, product-type, interest-rate-swap, irs, trade-product]
related: [fmrp-prime-uk-uat-drop-2, fmrp, ratan, stella, murex, ccs, ssi-stamping, auto-netting, cross-product-netting, cashflow-suppression, normalized-payment-schedule, schedule-to-cashflow-matching, expected-payment-count-for-auto-netting, cashflow-event-control, ndirs-cny-leg-mapping, cashflow-netting-and-auto-un-netting, murex-211]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/CN Drop 2 UAT - Settlements Scenarios - 2024.md"]
---
# IRS

IRS is the interest-rate swap product type referenced by the product-agnostic payment-schedule requirement. It is also a central test product in the CN Drop 2 settlement UAT catalogue.

## UAT scope and scenarios

The CN Drop 2 settlement UAT scenarios cover:

- Single and BTB3/5/7 bookings.
- Inter-entity and intra-entity trades.
- Backdated bookings.
- Customized coupons and spreads.
- Fees.
- Termination.
- Portfolio reassignment.
- Netting.
- Re-fixing.

These scenarios are linked to [[cashflow-event-control]] and [[ndirs-cny-leg-mapping]].

## Role in Prime UK UAT

The FMRP Prime UK UAT Drop 2 onboarding checklist identifies IRS as one of the products in scope.

The onboarding checklist requires IRS coverage for:

- SSI auto-attachment.
- Correct CFI-code capture.
- Settlement-method selection.
- Nostro auto-stamping.
- SWIFT generation.
- Accounting generation.

IRS-specific settlement scenarios in the checklist include:

- Interest auto-netting after the corresponding floating leg is received.
- Re-netting after refixing breaks the previous netting.
- ND IRS handling, for which the checklist states that behavior is the same as for normal IRS.
- Clearing-portfolio suppression for `CLIENT_CLRG_LCH_STL` and `CLIENT_CLR_HKEX_ST`.
- Markitwire allocation handling, in which ALOC cashflows are not STP'd.
- Cross-product netting with CCS and other Murex cashflows through RATAN.

The checklist also records a potential SSI hierarchy issue in which `UK MXGBLANK` is selected instead of the Global IRS SSI. This is an expected test scenario, not evidence that the issue was resolved.

## Product-agnostic payment-schedule requirement

According to the product-agnostic payment-schedule requirement, deliverable and ND IRS coupons use periodic adjusted interest payment dates and settlement or notional currencies extracted from both the first and second IR legs.

A current cashflow contributes to Expected Payment Count when its payment date and currency exactly match a schedule entry on either leg.

The requirement does not define a product-level deduplication rule for payments that match multiple schedule entries. See [[schedule-to-cashflow-matching]].

## Trade-specific pending issue

A specific pending issue concerns NDIRS CNY fixed-floating IRS trade `4348263238`, which was mapped into RATAN as USD Coupon/float for both legs. This finding belongs to that trade and mapping scenario only; it is not evidence of a general IRS processing failure.