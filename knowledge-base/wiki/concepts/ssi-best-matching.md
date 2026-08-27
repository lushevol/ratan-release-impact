---
type: concept
title: SSI Best Matching
created: 2026-08-25
updated: 2026-08-25
tags: [settlement, ssi, matching, cashflow, vostro]
related: [ssi-plus, ratan-ssi-stamping, what-is-the-ratan-ssi-best-matching-algorithm, what-is-the-authoritative-ratan-ssi-plus-50509-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and SSI+ 50509.md"]
---
# SSI Best Matching

SSI best matching is the identification of the SSI record applicable to an incoming RATAN cashflow.

For interface 50509, RATAN calls [[ssi-plus]] in real time and supplies cashflow information including:

- Booking entity FMID
- Counterparty FM code
- Currency
- CFI code

The matching SSI record provides data that RATAN attaches to the cashflow as part of [[ratan-ssi-stamping]].

## Undocumented Rules

The source establishes the matching inputs but does not specify:

- Whether all listed attributes are mandatory.
- Attribute precedence or tie-breaking where multiple SSI records match.
- No-match and ambiguous-match outcomes.
- The exact SSI fields returned or stamped.

These details remain open in [[what-is-the-ratan-ssi-best-matching-algorithm]].