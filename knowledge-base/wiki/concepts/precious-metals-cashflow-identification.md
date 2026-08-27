---
type: concept
title: Precious-Metals Cashflow Identification
created: 2026-08-24
updated: 2026-08-24
tags: [precious-metals, uber, cashflow, classification]
related: [ratanone, netting-service, swift-service, product-specific-delivery-location-extraction, what-is-the-canonical-precious-metals-identification-rule-for-uber-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/UBER Precious Metals.md"]
---
# Precious-Metals Cashflow Identification

Precious-metals cashflow identification is the intended classification of UBER-message cashflows using these attributes:

- `Custodian_SCI_FMID`
- `Custodian_Name`
- `Delivery_Location`
- `Settlement_Method`

The classification is intended to activate special handling for resultant generation, custodian-name stamping, Swift Field 26C generation, CIS querying, and future rule setup.

## Unresolved rule contract

The source does not define:

- whether every field is mandatory;
- the qualifying values or combinations of values;
- whether `Custodian_Name` is authoritative or derived from `Custodian_SCI_FMID`;
- null and invalid-value handling;
- how classification is persisted, recalculated, or audited; or
- whether the rule applies before or after cashflow stamping.

Accordingly, this concept records a requirement rather than an executable business rule. The canonical predicate is tracked in [[what-is-the-canonical-precious-metals-identification-rule-for-uber-cashflows]].