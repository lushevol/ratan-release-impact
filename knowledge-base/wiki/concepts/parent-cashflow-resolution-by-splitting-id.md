---
type: concept
title: Parent Cashflow Resolution by Splitting ID
tags: [netting, cashflow, splitting-id, high-value-payment, service-api]
related: [high-value-payment-control-technical-architecture, high-value-payment-queue, what-is-the-authoritative-high-value-payment-decision-rule, how-does-hvp-control-handle-netted-and-split-cashflows]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN/HVP Tech Design.md"]
---
# Parent Cashflow Resolution by Splitting ID

Netting service is required to provide an internal API that queries a parent cashflow using `splittingId`.

The requirement establishes a split-to-parent lookup dependency for the HVP technical design. It does not define identifier cardinality, treatment of missing parents, response fields, or error handling.

## HVP relevance

Parent resolution may be relevant where HVP controls need a payment-level view beyond an individual split cashflow. However, the source does not state whether HVP classification or approval is performed against:

- the child cashflow;
- the resolved parent cashflow; or
- an aggregate of split or netted cashflows.

That evaluation scope remains open in [[how-does-hvp-control-handle-netted-and-split-cashflows]].