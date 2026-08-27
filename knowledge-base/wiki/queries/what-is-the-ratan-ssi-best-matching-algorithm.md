---
type: query
title: What Is the RATAN SSI Best-Matching Algorithm?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, ssi, matching, cashflow, vostro]
related: [ssi-best-matching, ssi-plus, ratan-ssi-stamping, 5-ratan--17-ratan-interfaces--19-ratan-and-ssi-50509--zpvcrt]
sources: ["RATAN/RATAN -Interfaces/Ratan and SSI+ 50509.md"]
---
# What Is the RATAN SSI Best-Matching Algorithm?

The source states that RATAN uses booking-entity FMID, counterparty FM code, currency, and CFI code to identify a matching SSI record through SSI+. It does not define the algorithm that resolves matches.

## Questions

- Which listed inputs are required and which are optional?
- What is the precedence rule when multiple SSI records qualify?
- How are wildcard, null, inactive, or overlapping SSI records handled?
- What happens if SSI+ returns no match or an ambiguous result?
- Which SSI attributes are ultimately stamped onto the RATAN cashflow?

The linked Vostro SSI Best Matching documentation is a likely source for resolution.