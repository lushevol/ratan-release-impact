---
type: query
title: What Is the Authoritative Mixed-Stack Netting Rule?
created: 2026-08-24
updated: 2026-08-24
tags: [netting, cash-settlement, RATAN, LMS, stack-flow, open-question]
related: [netting-resultant-stack-derivation, source-stack-flow-name-propagation, cashflow-netting-and-auto-un-netting, ratan, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Source Stack Flow Name in LMS Feed.md"]
---

# What Is the Authoritative Mixed-Stack Netting Rule?

## Question

How should RATAN derive the stack-flow value and LMS source value when the components of a netting resultant have different stack-flow values?

## Evidence

The source says that same-valued components should produce a resultant with the common parent value. The Murex-related rule states that differing components should fall back to `FMRPSTELLA`. A mixed-stack integration test reports successful LMS receipt with an expected value beginning with `FMRPSTELLA`, but the expected-result text is incomplete.

## Required Resolution

Define:

- The field used for component comparison.
- The precedence order for `FMRPSTELLA`, `FMRPSTELLA-LOANIQ`, `FMRPMUREX`, `BCSSTELLA`, legacy `FMRP`, and legacy `LOANIQ`.
- The result for null or missing stack values.
- Whether mixed-stack resultants always use `FMRPSTELLA`.
- The exact LMS source value and formatting.
- Behavior for withdrawal events after release.

The rule should be implemented in the netting service before the LMS source-field change, as described in the two-release deployment plan.