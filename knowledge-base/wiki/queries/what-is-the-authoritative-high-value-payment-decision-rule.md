---
type: query
title: What Is the Authoritative High Value Payment Decision Rule?
tags: [open-question, high-value-payment, approval, usd-equivalent, lifecycle, netting]
related: [high-value-payment-control-technical-architecture, high-value-payment-queue, high-value-payment-approval-queue, parent-cashflow-resolution-by-splitting-id]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN/HVP Tech Design.md"]
---
# What Is the Authoritative High Value Payment Decision Rule?

The design requires USD-equivalent support, lifecycle lookup, user metadata retrieval, and parent-cashflow lookup, but it does not define an HVP classification or release decision.

## Information needed

Determine the approved:

- high-value threshold and currency treatment;
- FX-rate provider, valuation time, rounding, and precision;
- role of STP/NSTP information and `lastUser`;
- approval, queueing, rejection, and release conditions;
- parent, child, or aggregate cashflow basis for evaluation;
- processing order among lifecycle lookup, parent resolution, valuation, and routing.

Until this is resolved, the design must not be interpreted as an authoritative rule for [[high-value-payment-queue]] or [[high-value-payment-approval-queue]].