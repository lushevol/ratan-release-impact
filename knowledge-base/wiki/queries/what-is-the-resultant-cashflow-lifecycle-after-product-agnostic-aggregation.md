---
type: query
title: What Is the Resultant Cashflow Lifecycle After Product-Agnostic Aggregation?
created: 2026-08-22
updated: 2026-08-22
tags: [auto-aggregation, auto-netting, cashflow-lifecycle, settlement]
related: [product-agnostic-cashflow-aggregation, expected-payment-count-for-auto-netting, cashflow-auto-netting, ratan-cashflow-lifecycle-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md"]
---
# What Is the Resultant Cashflow Lifecycle After Product-Agnostic Aggregation?

The source states that an “Aggregation Resultant Cashflow can be Netted” after the expected-payment completeness condition is met. It does not define the resultant cashflow's construction or lifecycle.

## Questions

- Is a new resultant cashflow created, or are constituent cashflows transitioned directly?
- How are payment amount, direction, identifiers, and audit links derived?
- Which lifecycle state and sub-state are assigned before and after netting?
- How are constituent cashflows represented after aggregation?
- Which downstream settlement and messaging interfaces consume the result?

## Impact

These details are required to connect schedule-derived completeness gating with the operational lifecycle described in [[ratan-cashflow-lifecycle-state-machine]].