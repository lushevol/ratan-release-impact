---
type: concept
title: Auto DVP Cashflow Cardinality
created: 2026-08-23
updated: 2026-08-23
tags: [dvp, cashflow, split-processing, safety-control]
related: [auto-dvp, receive-to-pay-cashflow-linkage, dvp-nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# Auto DVP Cashflow Cardinality

Auto DVP applies a constrained cardinality rule when a receive cashflow finds multiple pay cashflows.

A one-to-one receive-to-pay relationship is eligible when all other conditions pass. If an original pay cashflow was split into child cashflows, RATAN may close the DVP exception on each eligible `Waiting` child. A child already settled is not changed.

If one receive cashflow maps to multiple independent, non-split pay cashflows, RATAN must take no automatic action. Operations must decide whether any pay obligation can be released. This restriction prevents an observed receipt from automatically releasing unrelated obligations.