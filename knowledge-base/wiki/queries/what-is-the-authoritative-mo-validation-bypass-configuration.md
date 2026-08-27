---
type: query
title: What Is the Authoritative MO Validation Bypass Configuration?
created: 2026-08-24
updated: 2026-08-24
tags: [query, MO-validation, bypass, entity-eligibility, FMID, Stella, RATAN]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--mg1utu, trade-validation-gated-cashflow-visibility, entities/scf, loandepo, fmrp-payment-eligibility-and-suppression, what-is-the-authoritative-fmrp-entity-eligibility-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process.md"]
---
# What Is the Authoritative MO Validation Bypass Configuration?

## Question

Which controlled reference-data source defines the entities, FMIDs, products, taxonomies, owner, effective date, and change process for trades that bypass the MO validation gate?

## Candidate rule

The requirement identifies Stella-sourced trades in the following categories:

- Egypt, Nepal, and Saudi FMIDs `401036553`, `400991880`, and `400007847`.
- `SCF` with `Instrument_Common.CFI_Code == "MMMXXX"`.
- `LoanDepo` with `Instrument_Common.ISDA_Taxonomy == "InterestRate:LoanDeposit"`.
- Listed CN FMIDs when the taxonomy is `ForeignExchange:Forward`, `ForeignExchange:Spot`, `ForeignExchange:NDF`, or `ForeignExchange:Swap`.

The source repeats this predicate but does not identify its authoritative configuration store or effective date. The FMID list also varies in presentation across the source context and should be reconciled before implementation.

## Required resolution

Confirm whether the predicate is complete and current, define precedence when multiple predicates apply, and establish how additions or removals are versioned and propagated to RATAN.