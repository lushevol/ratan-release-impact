---
type: query
title: How Does HVP Control Handle Netted and Split Cashflows?
tags: [open-question, high-value-payment, netting, splitting-id, cashflow]
related: [parent-cashflow-resolution-by-splitting-id, high-value-payment-control-technical-architecture, what-is-the-authoritative-high-value-payment-decision-rule]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN/HVP Tech Design.md"]
---
# How Does HVP Control Handle Netted and Split Cashflows?

Netting service must resolve a parent cashflow from `splittingId`, but the design does not state how that relationship affects HVP assessment.

## Information needed

Clarify whether HVP control evaluates:

- each split child independently;
- the parent cashflow returned by Netting service;
- an aggregate of all related splits;
- a netted resultant cashflow; or
- different bases for classification, approval, and SWIFT propagation.

The contract should also define missing-parent handling, relationship cardinality, and consistency requirements between Netting and HVP processing.