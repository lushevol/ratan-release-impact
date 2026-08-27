---
type: query
title: What Is the Authoritative Post-Split Withdrawal, Amendment, and Netting Model?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, split, withdrawal, amendment, netting, lifecycle]
related: [cashflow-events-control-draft2, cashflow-status-lifecycle, cashflow-netting-and-un-netting, reversal-and-correction-cashflow-processing, ratan, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft2.md"]
---
# What Is the Authoritative Post-Split Withdrawal, Amendment, and Netting Model?

The deprecated draft shows a gross cashflow becoming `SPLIT` and creating split cashflows, but explicitly leaves the subsequent outcome unresolved for withdrawal, amendment, and netting.

## Questions to resolve

- Does a withdrawal of a split gross cashflow cancel, reverse, or supersede each child cashflow?
- How are amendment-driven reversal and correction events allocated across split children?
- Can split children be netted independently, and what resultant correlation is required?
- What happens when one or more split children are released or settled?
- Which records remain visible in the cashflow blotter, and what audit history is retained?

A current functional specification or implementation evidence is required because the source does not answer these questions.