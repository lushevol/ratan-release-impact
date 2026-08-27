---
type: concept
title: Product-Specific Delivery-Location Extraction
created: 2026-08-24
updated: 2026-08-24
tags: [uber, delivery-location, schema-evolution, opensearch, query-service]
related: [opensearch, cash-settlement-schema-alignment, schema-evolution-for-cash-settlement, precious-metals-cashflow-identification]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/UBER Precious Metals.md"]
---
# Product-Specific Delivery-Location Extraction

Product-specific delivery-location extraction is the requirement to obtain delivery location and associated precious-metals attributes from UBER trade structures for OpenSearch indexing and Query Service exposure.

## Required source paths

```text
- Trade.Structured_Instrument.Forward_Future_Instrument.Far_Leg.Delivery_Location
- Trade.Structured_Instrument.Forward_Future_Instrument.Near_Leg.Delivery_Location
- Trade.Loan_Deposit_Instrument.Delivery_Location
- Trade.Forward_Future_Instrument.Delivery_Location
- Trade.Swap_Instrument.Commodity_Leg.First_Leg.Delivery_Location
- Trade.Swap_Instrument.Commodity_Leg.Second_Leg.Delivery_Location
- Trade.Option_Instrument.Commodity_Leg.Delivery_Location
- Trade.Intent_To_Allocate
- Trade.Entity.Custodian_Name
- Trade.Entity.Custodian_SCI_FMID
- Trade.Delivery_Location
```

## Required design decisions

The supplied list contains both delivery-location paths and non-delivery attributes. A canonical contract must define:

- which path applies to each product structure;
- precedence for trades containing multiple populated locations or legs;
- normalization and null behavior;
- the semantic role and target representation of `Intent_To_Allocate` and custodian fields; and
- index and API backward-compatibility behavior.

The source does not provide OpenSearch mappings, reindexing plans, or Query Service API schemas. This is therefore a propagation-scope requirement, not a finalized schema contract.