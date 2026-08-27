---
type: query
title: What Is the Authoritative FMRP entityFMID and entityLEID Mapping?
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, message-contract, entity-identifiers, mxpayml, open-question]
related: [fmrp, murex-211, fmrp-outbound-cashflow-enrichment, ratan-murex-211-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
---
# What Is the Authoritative FMRP entityFMID and entityLEID Mapping?

The `fmrpEnrich` transformation populates:

- `entityFMID` from `M_ATLAS_LEID`.
- `entityLEID` from `M_SCI_ID`.

The formula names and output labels may be intentional, but the source contains no recipient schema, interface contract, sample accepted payload, or mapping rationale.

Confirm the FMRP message contract and static-data definitions before treating this mapping as authoritative or changing it. The investigation should also verify the expected semantics of `counterpartyFMID`.