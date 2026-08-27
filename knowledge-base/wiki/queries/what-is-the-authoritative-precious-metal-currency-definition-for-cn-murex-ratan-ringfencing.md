---
type: query
title: What Is the Authoritative Precious-Metal Currency Definition for CN Murex-RATAN Ringfencing?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, precious-metals, currency-static-data, ringfencing]
related: [murex-ratan-cashflow-ringfencing, precious-metal-currency-classification, precious-metal-cashflow-vostro-requirement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# What Is the Authoritative Precious-Metal Currency Definition for CN Murex-RATAN Ringfencing?

The ringfencing rule keeps all cashflows of a trade in Murex 2.11 when an in-scope China entity has at least one cashflow containing a precious-metal currency. The source does not identify the authoritative static-data catalogue, field, ownership model, or change-control process that determines precious-metal classification.

It also does not specify whether an amendment that adds or removes a precious-metal cashflow reroutes the whole trade.

## Evidence needed

- Authoritative precious-metal currency list and static-data source.
- Effective-date and ownership controls for the classification.
- Amendment routing rules for changes to precious-metal cashflows.
- Test evidence for mixed-currency trades and multi-flow amendments.