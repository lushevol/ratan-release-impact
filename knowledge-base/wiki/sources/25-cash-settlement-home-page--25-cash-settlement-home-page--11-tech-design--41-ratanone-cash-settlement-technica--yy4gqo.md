---
type: source
title: "Korea Swift - Enisis"
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, swift, enisis, integration, technical-design]
related: [enisis, ratanone, swift-service, enisis-legacy-connection-retention, incremental-enisis-flow-extension, what-is-the-existing-enisis-connection-contract, what-new-enisis-logic-is-required-in-the-existing-flow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Swift - Enisis.md"]
---
# Korea Swift - Enisis

## Summary

This document provides two high-level implementation directives for the Enisis integration in the Korea Swift and settlement-accounting context:

1. Follow the existing flow and add new logic for Enisis.
2. Retain the old way for Enisis connection.

Together, these directives indicate that Enisis-specific functionality should be added incrementally while preserving the established Enisis connection approach.

## Implementation Directives

> Follow the existing flow and add new logic for Enisis

> Retain the old way for Enisis connection

The document does not define which existing flow is intended, what new logic is required, or what constitutes the old connection method.

## Scope and Limitations

This is a design constraint rather than a complete technical specification. It contains no documented:

- Swift message types or field mappings;
- Enisis protocol, endpoint, authentication, certificate, or network details;
- API signatures, schemas, or payload examples;
- processing sequence or ownership model;
- retry, timeout, acknowledgement, reconciliation, or monitoring behavior;
- deployment, migration, rollback, or cutover procedure; or
- test cases and measurable acceptance criteria.

The source does not establish that [[swift-service]], [[accounting-service]], Aspire, or EBBS owns or implements the Enisis integration. Those relationships require confirmation.

## Open Questions

- Which concrete existing flow is the implementation baseline?
- What exact connection mechanism must remain unchanged?
- What new Enisis business or technical logic is required?
- Which service owns the change and the legacy connection?
- What regression, connectivity, reconciliation, and rollback criteria are required?

See [[what-is-the-existing-enisis-connection-contract]] and [[what-new-enisis-logic-is-required-in-the-existing-flow]].