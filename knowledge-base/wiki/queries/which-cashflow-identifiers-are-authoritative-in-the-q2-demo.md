---
type: query
title: Which Cashflow Identifiers Are Authoritative in the Q2 Demo?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, test-data, traceability, cash-settlement]
related: [fmrp-china-cash-settlement, fmo-post-trade-portal, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Which Cashflow Identifiers Are Authoritative in the Q2 Demo?

## Question

Which cashflow identifiers should be used as the canonical test-data references for the Q2 2023 cash-settlement demonstrations?

## Evidence

Several scenarios list identifiers in the `8192550531xx` range, while their expected-result sections refer to different identifiers in the `8192550522xx` range. The IRS scenarios additionally use identifiers beginning with `N00000000`. Examples include the Hold scenario, manual failure scenarios, and Settle as Gross scenarios.

The differences may represent regenerated test data, copied test cases, or documentation errors. The source does not identify the environment, execution date, or test-data version needed to distinguish these possibilities.

## Required resolution

Obtain the canonical test dataset or execution evidence and map each scenario identifier to its expected result. Until then, raw identifiers should not be used as an auditable traceability baseline.
