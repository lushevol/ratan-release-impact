---
type: concept
title: Trade Standing Settlement Instructions
tags: [trade-ssi, settlement-instructions, cash-settlement, rfi]
related: [rfi, cashflow-standing-settlement-instructions, what-is-the-authoritative-trade-and-cashflow-ssi-resolution-model-for-rfi, how-does-portfolio-based-nostro-stamping-relate-to-trade-ssi-in-rfi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Trade SSI - RFI.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Trade Standing Settlement Instructions

Trade Standing Settlement Instructions (Trade SSI) are named as a dedicated design area in *Trade SSI - RFI*. The source does not provide a definition, data model, lifecycle point, or technical behavior for this term.

## Documented boundary

The source structurally distinguishes Trade SSI from [[cashflow-standing-settlement-instructions|Cashflow SSI]]. It does not state whether cashflow-level instructions are inherited from, derived from, validated against, or allowed to override trade-level instructions.

## Undocumented requirements

The following remain unconfirmed:

- the authoritative source and owner of Trade SSI;
- the point at which Trade SSI is resolved or stamped;
- persistence, versioning, audit, and correction semantics;
- validation rules and missing-data handling;
- whether portfolio or Nostro information participates in selection;
- downstream consumers and interfaces.

These gaps are tracked in [[what-is-the-authoritative-trade-and-cashflow-ssi-resolution-model-for-rfi]].