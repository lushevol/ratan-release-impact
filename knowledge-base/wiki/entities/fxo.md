---
type: entity
title: FXO
created: 2026-08-22
updated: 2026-08-22
tags: ["FXO", "business-domain", "trade-migration", "settlement", "product", "foreign-exchange", "onboarding", "cash-settlement"]
related: ["fxo-mini-trade-migration-ratan-cash-settlement", "fmrp", "murex-2-11", "stella", "ratan-settlement", "ratan", "murex", "cashflow-status-handling", "ssi-stamping", "netting-key-selection"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# FXO

## Source-specific definitions

The source documents characterize FXO in related but distinct ways:

- **Ratan cash-settlement migration runbook:** FXO is the business or application domain for the mini trade migration. The runbook does not provide a broader definition of FXO or quantify business outcomes.
- **F2B milestone onboarding checklist:** FXO is the product or product-family identifier named by the checklist. This source does not expand the acronym, so its precise local product scope should be confirmed rather than inferred.

## Mini trade migration

The Ratan cash-settlement runbook identifies the FXO project using `Runbook_MiniMigration_FXO.xlsx` and configuration names beginning with `FXO-Mini_TM`.

In that runbook, the FXO project coordinates selected trade and cashflow processing across [[murex-2-11]], [[stella]], and [[ratan-settlement]].

## Onboarding scope

According to the F2B milestone onboarding checklist, FXO processing spans [[murex]], [[fmrp]], and [[ratan]], with dependencies on [[razor]], [[stella]], [[aspire]], and [[ebbs]]. The checklist covers:

- SSI, Nostro, and Vostro handling.
- Cashflow presentation and status control.
- Exercise and expiry events.
- Booking-model impacts.
- Manual, automatic, and cross-product netting.
- SWIFT MT and ISO 20022 MX generation.
- Settlement accounting.
- Migration and duplicate-payment prevention.
- Branch, currency, routing, and suppression configuration.

The checklist explicitly expects FXO to receive [[ssi-stamping]]. It also expects FX spot, forward, and swap cashflows to be `SUSPENDED` and to bypass MO validation. These requirements apply to the stated FX flow scope and should not be generalized to other products.

## Limitations and unresolved items

The onboarding checklist does not establish that FXO onboarding is complete or approved. It also includes controls for Loan, Loan Deposit, IRS, CCS, NDS, and precious-metal currencies; consequently, some checklist entries may be generic onboarding controls rather than FXO-specific behavior.

The handling of three-agent trades remains unresolved. The checklist describes SSI processing as supporting one or two agents, but not three. See [[how-are-three-agent-trades-handled]].