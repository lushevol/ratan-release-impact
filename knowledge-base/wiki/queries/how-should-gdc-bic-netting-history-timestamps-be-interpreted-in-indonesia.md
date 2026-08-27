---
type: query
title: How Should GDC Bic Netting History Timestamps Be Interpreted in Indonesia?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, gdc, indonesia, bic-netting, timestamps, interoperability]
related: [ratan-gdc, ratan-indonesia, ratan-indonesia-time-zone-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UTC Time zone impact - Indonesia/Time Fields Summary.md"]
---
# How Should GDC Bic Netting History Timestamps Be Interpreted in Indonesia?

Bic netting static/history `updated at` and `created at` are classified Local Time in the source, carry `Z`-suffixed values, and include the note that “gdc not use utc/local time function.”

## Unresolved behavior

The source does not define whether the GDC values represent UTC, server-local time, database-local time, or a UI-specific representation. Therefore, neither their storage semantics nor a safe Indonesia conversion rule can be inferred.

## Required clarification

Obtain the GDC field contract and implementation behavior for:

- `updated at` and `created at` serialization;
- persistence zone and database type;
- UI display conversion;
- API consumer expectations;
- migration and reconciliation behavior between GDC and Indonesia.

The answer must be incorporated into the [[ratan-indonesia-time-zone-contract]] without assuming that the `Z` suffix is merely decorative.