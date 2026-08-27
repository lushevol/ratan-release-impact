---
type: concept
title: Netting Resultant Stack Derivation
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, RATAN, LMS, stack-flow, cashflow]
related: [cashflow-netting-and-auto-un-netting, source-stack-flow-name-propagation, ratan, lms, fmrp, what-is-the-authoritative-mixed-stack-netting-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Source Stack Flow Name in LMS Feed.md"]
---

# Netting Resultant Stack Derivation

## Purpose

A netting resultant must retain a deterministic stack-flow identity so that downstream settlement and LMS publication remain consistent. The source requires stack-value derivation in the netting service before the LMS source-field change is released.

## Documented Rules

The source indicates the following intended behavior:

- If component cashflows have the same stack, derive that common stack value for the resultant.
- If component cashflows have different stacks, use a fallback behavior; the Murex-related proposal states `FMRPSTELLA` as the fallback.
- The derived value is then propagated to the LMS source field under Proposal 1.

The source does not define whether “same” means identical `Source_Stack_Flow_Name` values, identical LMS source values, identical settlement processes, or another attribute.

## Evidence

The source reports successful netting-resultant LMS receipt for:

- `FMRPSTELLA-LOANIQ`.
- `FMRPMUREX`.
- A mixed-stack case resulting in `FMRPSTELLA`.

The mixed-stack test row has an incomplete expected-result value, so it demonstrates operational behavior but does not establish a complete canonical contract.

## Deployment Control

The recommended sequence is:

1. Release stack-value derivation in the netting service.
2. Release the LMS data-source mapping in a subsequent release.

This protects cashflows netted before the change but released afterward from inconsistent source identity.

## Unresolved Contract

The source leaves the `Netting derive logic` section empty. An authoritative rule is still required for:

- Component comparison.
- Same-stack derivation.
- Mixed-stack fallback.
- Null or missing stack values.
- Legacy values `FMRP` and `LOANIQ`.
- Formatting and delimiter validation.

Track resolution in [[what-is-the-authoritative-mixed-stack-netting-rule]].