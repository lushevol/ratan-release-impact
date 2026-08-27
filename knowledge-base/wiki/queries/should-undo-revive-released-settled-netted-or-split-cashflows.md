---
type: query
title: Should Undo Revive Released, Settled, Netted, or Split Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-undo, withdrawal, lifecycle-state, settlement, uat]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-trade-cashflow-events--1p4c878, cashflow-lifecycle-state-model, released-settled-amendment-control, cashflow-netting-and-auto-un-netting, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/Drop 2 UAT Open Issues and test cases.md"]
---
# Should Undo Revive Released, Settled, Netted, or Split Cashflows?

When an undo is performed after a settled withdrawal FT, which cashflow lifecycle states may be revived?

## Evidence

The Drop 2 UAT action register states that a cashflow will not be revived if it is in `released`, `settled`, `netted`, or `split` status. However, the same entry explicitly says, “Expectation to be discussed?”

This is an unresolved expected-behaviour question, not an authoritative lifecycle policy. The document also records that the Ratan regression test package required additional undo cases.

## Information Needed

- Approved business rules for undo after settled withdrawal.
- State-specific expected outcomes for `released`, `settled`, `netted`, and `split`.
- Required treatment of netting resultants and split cashflows.
- Regression cases and results for the Ratan undo package.

## Related Pages

- [[cashflow-lifecycle-state-model]]
- [[released-settled-amendment-control]]
- [[cashflow-netting-and-auto-un-netting]]
- [[ratan]]
- [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-trade-cashflow-events--1p4c878]]