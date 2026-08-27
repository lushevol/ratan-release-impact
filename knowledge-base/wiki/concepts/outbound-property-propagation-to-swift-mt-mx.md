---
type: concept
title: Outbound Property Propagation to SWIFT MT/MX
tags: [swift, mt, mx, message-header, orchestration, high-value-payment]
related: [swift, ratan, high-value-payment-control-technical-architecture, manual-entity-swift-mx-bifurcation, ssi-driven-swift-and-mx-field-population, what-is-the-complete-x-outbound-property-header-contract]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN/HVP Tech Design.md"]
---
# Outbound Property Propagation to SWIFT MT/MX

The design requires Orchestration service to add the following header when publishing cashflow messages:

```text
X-Outbound-Property-
```

Swift service is required to consume this header and add it to an MT/MX message header.

## Routing context

The source states that LOANIQ cashflows are sent to `message-bridge`, while Fmrp cashflows are sent to Swift service. It does not clarify whether both paths carry the same header or whether only the Fmrp-to-Swift route is subject to MT/MX enrichment.

## Unspecified contract

The documented header ends with a hyphen and has no supplied suffix, value schema, source field mapping, failure handling, or idempotency rule. It also does not identify equivalent target structures for MT and MX, which are distinct message formats.

This requirement is separate from [[ssi-driven-swift-and-mx-field-population]]: the source describes propagation of outbound control metadata, not SSI-derived field population.