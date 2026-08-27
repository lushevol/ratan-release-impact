---
type: query
title: How Does RATAN Map MX2.11 CFI Prefixes to Vostro SSIs?
tags: [open-question, ratan, murex-211, cfi-code, vostro-ssi, ssi-plus]
related: [murex-211-vostro-ssi, murex-211-vostro-ssi-reuse, murex-211-source-specific-cfi-stamping, cfi-code-mapping-for-murex-vostro-ssi, what-is-the-authoritative-cfi-code-mapping-for-murex-211-vostro-ssi-securities, ratan, ssi-plus, tds3]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex 2.11 Vostro SSI.md"]
---
# How Does RATAN Map MX2.11 CFI Prefixes to Vostro SSIs?

## Question

Does RATAN match Murex 2.11 cashflows to Vostro SSIs using the full CFI code, the first two characters retained from TDS3, or a separate broad SSI+ mapping value?

## Evidence

The source states that:

- RATAN fetches SSIs using the CFI code stamped on the cashflow.
- Existing SSI+ Security IDs must be updated with CFI codes.
- SSI granularity may be broader than product granularity; `XFXXXX` is cited across FX Spot, Forward, and Swap.
- RATAN stamps CFI codes for Murex 2.11 cashflows.
- RATAN retains the first two characters of the CFI code stamped on the Murex 2.11 trade in TDS3.

## Information required to resolve the query

1. The canonical field used by RATAN for lookup.
2. Whether `XFXXXX` is a CFI code, prefix, alias, Security ID value, or display value.
3. The mapping and fallback behavior when the cashflow has no CFI code.
4. The precedence between a TDS3-derived value and a value supplied by another upstream system.
5. Whether FX Spot, Forward, and Swap intentionally share one SSI mapping.
6. Validation behavior when multiple SSIs match the same broad value.

Until these points are confirmed, the source supports the existence of a CFI-based lookup requirement but not a complete implementation contract.