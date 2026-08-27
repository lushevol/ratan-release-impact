---
type: entity
title: LoanDepo
created: 2026-08-24
updated: 2026-08-23
tags: [LoanDepo, product, trade-validation, Stella, MO-validation, auto-validation]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--mg1utu, trade-validation-gated-cashflow-visibility, fmrp-payment-eligibility-and-suppression, stella, cdu, trade-validation-cashflow-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/RATAN Settlement Control on Trade Validation.md"]
---
# LoanDepo

## Role in trade validation

According to the trade-validation and cashflow-process requirement, `LoanDepo` is a product category identified in the trade-validation bypass rule. For Stella-sourced trades, a `LoanDepo` trade with:

```text
Instrument_Common.ISDA_Taxonomy == "InterestRate:LoanDeposit"
```

is excluded from the MO validation check described in that requirement.

## Proposed auto-validation enhancement

According to the RATAN Settlement Control on Trade Validation source, LoanDepo is one of the product scopes identified for a proposed Stella/CDU auto-validation enhancement.

The enhancement is described for September 2024 and marked TBC. Its intended benefit is reducing manual touch for Stella cashflows.

## Scope limitations

The trade-validation and cashflow-process source does not provide a product catalogue, ownership information, or effective-date history for the `InterestRate:LoanDeposit` predicate. Its bypass treatment should therefore be considered intended design evidence pending confirmation of the authoritative configuration.

The RATAN Settlement Control on Trade Validation source provides no additional product definition or validation-status rules.