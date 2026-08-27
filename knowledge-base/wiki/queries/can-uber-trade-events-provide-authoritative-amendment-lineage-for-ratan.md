---
type: query
title: Can Uber Trade Events Provide Authoritative Amendment Lineage for Ratan?
created: 2026-08-23
updated: 2026-08-23
tags: [uber, ratan, trade-event, lineage, trade-amendment]
related: [ratan, amendment-driven-cashflow-correlation, rebook-exception, payment-date-proximity-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Ingenuine Rebook Exception in Ratan.md"]
---
# Can Uber Trade Events Provide Authoritative Amendment Lineage for Ratan?

The source proposes adding trade-event information after Uber is enabled. This could replace or supplement proximity-based rebook detection with explicit amendment lineage.

## Questions to resolve

- Which Uber event identifies an amendment and links the original trade or cashflow to its replacement?
- Which identifiers are stable across Murex, Uber, and Ratan?
- When is the event available relative to withdrawal, new-cashflow creation, and release processing?
- Can events be replayed safely and reconciled against Ratan exception decisions?
- Who owns the data contract, operational support, and exception handling?
- Does the event coverage include both Murex and [[stella]] populations?

A viable design must show that the event establishes an original-to-replacement relationship rather than merely providing another approximate matching attribute.