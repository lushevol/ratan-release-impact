---
type: query
title: What Is the Authoritative SSI CFI Granularity Matching Rule?
tags: [query, ssi, cfi-code, wildcard-matching, specification-gap]
related: [cfi-code-ssi-granularity-matching, ssi-stamping, ssi-stamping-notification, scbml-ssi-field-mapping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/SSI Notification Flow.md"]
---
# What Is the Authoritative SSI CFI Granularity Matching Rule?

## Question

What exact predicate determines whether `Settlement_Instruction.CFI_Code` is at a higher or equal granular level than `Instrument_Common.CFI_Code`?

## Evidence from the requirement

| SSI CFI | Cashflow CFI | Expected result |
| --- | --- | --- |
| `*R****` | `SRXXXX` | Select the cashflow |
| `*F****` | `JFXXXX` | Select the cashflow |
| `******` | `SRXXXX` | Select the cashflow |
| `SRF***` | `SRXXXX` | Do not select the cashflow |

The requirement also describes the comparison as using the “same values,” which conflicts with the wildcard examples. The authoritative interpretation must distinguish exact matching from CFI pattern or granularity matching.

## Information needed

Resolve:

- Wildcard position semantics.
- Character-level versus hierarchy-based comparison.
- Specificity ordering.
- Validation of CFI length and permitted characters.
- Null, malformed, and unsupported CFI behavior.
- Whether the matching rule is implemented in SSI+, Ratan, or a shared reference service.

The current source provides examples but not a complete implementation contract.