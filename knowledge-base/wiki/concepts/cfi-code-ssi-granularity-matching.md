---
type: concept
title: CFI Code SSI Granularity Matching
tags: [ssi, cfi-code, wildcard-matching, cashflow, settlement-instruction]
related: [ssi-stamping, ssi-stamping-notification, global-and-branch-specific-ssi-scope, what-is-the-authoritative-ssi-cfi-granularity-matching-rule]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/SSI Notification Flow.md"]
---
# CFI Code SSI Granularity Matching

## Definition

CFI Code SSI granularity matching determines whether an SSI notification can identify a cashflow for re-stamping. The SSI CFI Code is compared with the cashflow CFI Code from `Instrument_Common.CFI_Code`.

The requirement states that the SSI CFI Code must be at a higher or equal granular level than the cashflow CFI Code. This is not equivalent to literal equality because the SSI value may contain wildcard characters.

## Source examples

| SSI CFI | Cashflow CFI | Good to pick up cashflow? |
| --- | --- | --- |
| `*R****` | `SRXXXX` | Yes |
| `*F****` | `JFXXXX` | Yes |
| `******` | `SRXXXX` | Yes |
| `SRF***` | `SRXXXX` | No |

These examples are evidence for the required behavior, but they do not provide a complete comparison algorithm.

## Data mapping

| Data source | Logical model field |
| --- | --- |
| Cashflow | `Instrument_Common.CFI_Code` |
| SSI data | `Settlement_Instruction.CFI_Code` |

## Open semantics

The requirement does not define:

- Which positions are wildcardable.
- Whether comparison is positional, hierarchical, or based on a CFI reference catalogue.
- Whether a wildcard represents any character or an omitted level of specificity.
- Why `SRF***` is rejected for `SRXXXX`.
- How malformed, null, or differently sized CFI values are handled.

Until confirmed, implementations should preserve the source examples without generalizing them into a formal predicate. The unresolved specification is tracked in [[queries/what-is-the-authoritative-ssi-cfi-granularity-matching-rule]].