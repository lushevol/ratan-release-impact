---
type: concept
title: Nostro Stamping
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, stamping, cashflow, trade, accounting, ratan]
related: [ssi-plus, nostro-centralization, ratan, razor, rfi-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# Nostro Stamping

## Definition

Nostro stamping is the process of querying Nostro static data and attaching or applying the relevant Nostro information to a cashflow, trade, or accounting process.

## Requirement scope

The source specifically identifies two impacted `Ratan` use cases:

- Cashflow or trade stamping Nostro query.
- Accounting Nostro query.

A new connection with [[entities/ssi-plus|SSI+]] is expected. Query message formats and mappings remain to be confirmed.

The requirement does not state that [[entities/razor|Razor]] has the same query paths or implementation impact. Razor should therefore be assessed separately.

## Related mapping

`RFI stamping` is identified as overlapping scope because it requires portfolio-to-Nostro mapping. The source does not define the mapping keys, precedence, or lifecycle.

## Design gaps

- Query API and response schema.
- Runtime versus cached lookup.
- Missing or ambiguous Nostro behavior.
- Timeout and fallback behavior.
- Identifier and terminology normalization.
- Performance and availability targets.
