---
type: concept
title: Payment-Date Proximity Matching
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, matching, payment-date, heuristic]
related: [ratan, rebook-exception, amendment-driven-cashflow-correlation, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Ingenuine Rebook Exception in Ratan.md"]
---
# Payment-Date Proximity Matching

Payment-date proximity matching is the Ratan heuristic used to select cashflows that may be related to a trade amendment when direct original-to-replacement cashflow lineage is unavailable.

A prospective new cashflow is considered for a [[rebook-exception]] when another cashflow:

- Has the same Trade ID; Murex cashflows use Original Trade ID.
- Has the same currency.
- Is already released or settled.
- Has a payment date within the configured window.

## Window change

The documented earlier window was 15 days. Production logic deployed on 2026-05-30 reduced the window to 5 days.

Narrowing the window is intended to reduce false alerts by limiting unrelated cashflows that qualify through date proximity. It may also exclude genuine amendment rebooks whose payment dates differ by more than five days. The source provides exception volume data but no validated precision, recall, or missed-rebook analysis; see [[what-is-the-validated-precision-and-recall-of-the-five-day-ratan-rebook-rule]].

## Limitation

Payment-date proximity is not causal evidence of an amendment. Adding direction may improve specificity, but authoritative correlation requires an explicit lineage relationship, potentially supplied through Uber trade events.