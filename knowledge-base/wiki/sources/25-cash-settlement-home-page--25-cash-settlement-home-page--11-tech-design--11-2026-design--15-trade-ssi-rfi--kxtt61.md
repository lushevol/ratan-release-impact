---
type: source
title: Trade SSI - RFI
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page technical design"
tags: [cash-settlement, rfi, trade-ssi, cashflow-ssi, technical-design]
related: [rfi, trade-standing-settlement-instructions, cashflow-standing-settlement-instructions, what-is-the-authoritative-trade-and-cashflow-ssi-resolution-model-for-rfi, how-does-portfolio-based-nostro-stamping-relate-to-trade-ssi-in-rfi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Trade SSI - RFI.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Trade SSI - RFI

This technical-design document identifies [[rfi]], Trade SSI, and Cashflow SSI as its intended scope. Its readable text does not define the abbreviation RFI, specify SSI ownership, or describe the implementation.

## Background reference

The document links to the following Confluence page as background:

[RFI Nostro stamping based on Portfolio - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/RFI+Nostro+stamping+based+on+Portfolio)

The linked title establishes background relevance for portfolio-based Nostro stamping, but the source itself does not establish that this is an implemented Trade SSI rule.

## Document structure

The source contains empty sections for:

- Cashflow SSI
- Trade SSI
- Overall technical design
- Detail

The only retained detail content consists of two embedded attachments:

- `attachments/image-2026-7-14_17-7-52.png`
- `attachments/image-2026-7-15_9-44-4.png`

The diagrams have not been transcribed in the available source text. Consequently, this source cannot establish an architecture, data flow, API contract, data model, system boundary, or SSI-resolution rule.

## Evidence limits

The document supports only the following inventory-level conclusions:

- Trade SSI and [[cashflow-standing-settlement-instructions|Cashflow SSI]] are intended as distinct areas of design.
- RFI is central to the intended design scope but remains undefined.
- Portfolio-based Nostro stamping is a background topic, not a confirmed technical behavior.
- The substantive design appears to be stored in diagrams requiring OCR or manual transcription.

No SQL DDL, API signatures, configuration, schemas, or tabular specifications are present in the extract.

## Follow-up

The unresolved model is tracked in [[what-is-the-authoritative-trade-and-cashflow-ssi-resolution-model-for-rfi]]. The specific relationship between portfolio-based Nostro stamping and Trade SSI is tracked in [[how-does-portfolio-based-nostro-stamping-relate-to-trade-ssi-in-rfi]].