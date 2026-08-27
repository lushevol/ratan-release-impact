---
type: query
title: What Is the Canonical Precious-Metals Identification Rule for UBER Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, precious-metals, classification, cashflow]
related: [precious-metals-cashflow-identification, netting-service, swift-service, product-specific-delivery-location-extraction, ratan-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/UBER Precious Metals.md"]
---
# What Is the Canonical Precious-Metals Identification Rule for UBER Cashflows?

The source identifies `Custodian_SCI_FMID`, `Custodian_Name`, `Delivery_Location`, and `Settlement_Method` as inputs for precious-metals handling, but provides no formal predicate.

## Questions to resolve

- Which fields and values qualify a UBER cashflow as precious metals?
- Is the logic conjunctive, disjunctive, product-specific, or configuration-driven?
- Is `Custodian_Name` an authoritative inbound value or an FMID-derived enrichment result?
- What is the canonical delivery-location source when multiple trade paths are populated?
- How are missing, invalid, or conflicting values handled?
- Which service owns evaluation and persistence of the classification?

The answer affects [[netting-service]], [[swift-service]], Query Service, OpenSearch, cashflow stamping, and future rule configuration.