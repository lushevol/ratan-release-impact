---
type: concept
title: Murex 2.11 Source-Specific CFI Stamping
tags: [cfi-code, cashflow, ratan, stella, tds3, source-specific-processing]
related: [murex-211, ratan, stella, tds3, cfi-code-mapping-for-murex-vostro-ssi, ssi-stamping-behavior-differences, how-does-ratan-map-mx211-cfi-prefixes-to-vostro-ssis]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex 2.11 Vostro SSI.md"]
---
# Murex 2.11 Source-Specific CFI Stamping

The functional requirement assigns CFI-code stamping according to the source of the cashflow.

## Responsibility split

| Cashflow population | CFI-code stamping system |
|---|---|
| BLADE trades | [[stella]] |
| CFETS trades | [[stella]] |
| S2BX trades | [[stella]] |
| Murex 2.11 cashflows | [[ratan]] |

For Murex 2.11, RATAN retains the first two characters of the CFI code previously stamped on the trade in [[tds3]]. The source does not specify the exact transformation, validation, precedence, or fallback behavior.

## Design tension

The same requirement states that RATAN fetches SSIs using the CFI code on cashflows while describing a two-character TDS3-derived value for Murex 2.11 stamping. It is therefore unresolved whether:

- the full CFI code is used for SSI lookup;
- the first two characters are used as a classification prefix;
- the two representations are used at separate stages; or
- a broad value such as `XFXXXX` acts as a lookup alias.

This distinction is tracked in [[how-does-ratan-map-mx211-cfi-prefixes-to-vostro-ssis]].