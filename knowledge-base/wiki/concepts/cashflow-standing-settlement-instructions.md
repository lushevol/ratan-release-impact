---
type: concept
title: Cashflow Standing Settlement Instructions
tags: [cashflow-ssi, settlement-instructions, cash-settlement, rfi]
related: [rfi, trade-standing-settlement-instructions, what-is-the-authoritative-trade-and-cashflow-ssi-resolution-model-for-rfi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Trade SSI - RFI.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Cashflow Standing Settlement Instructions

Cashflow Standing Settlement Instructions (Cashflow SSI) are named as a separate section in *Trade SSI - RFI*. The readable source contains no explanatory content for the section.

## Relationship to Trade SSI

The separate headings show that the design intends to distinguish Cashflow SSI from [[trade-standing-settlement-instructions|Trade SSI]]. They do not establish a precedence, propagation, override, or reconciliation relationship.

## Required clarification

Authoritative design evidence is needed to determine:

- whether Cashflow SSI is independently selected or derived from Trade SSI;
- the owner and source of the value;
- when it is assigned and whether it can change;
- fallback behavior for missing, ambiguous, inactive, or invalid instructions;
- auditability of selected instructions and any overrides.

See [[what-is-the-authoritative-trade-and-cashflow-ssi-resolution-model-for-rfi]].