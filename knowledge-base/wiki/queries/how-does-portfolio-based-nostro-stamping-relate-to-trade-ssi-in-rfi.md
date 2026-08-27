---
type: query
title: How Does Portfolio-Based Nostro Stamping Relate to Trade SSI in RFI?
tags: [rfi, trade-ssi, nostro, portfolio, settlement-instructions, open-question]
related: [rfi, trade-standing-settlement-instructions, cashflow-standing-settlement-instructions, what-is-the-authoritative-trade-and-cashflow-ssi-resolution-model-for-rfi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Trade SSI - RFI.md"]
created: 2026-08-24
updated: 2026-08-24
---
# How Does Portfolio-Based Nostro Stamping Relate to Trade SSI in RFI?

## Question

Does portfolio-based Nostro stamping participate in Trade SSI resolution in [[rfi]], and if so, what rule, lifecycle point, and audit record govern it?

## Evidence boundary

The source links to a Confluence page titled “RFI Nostro stamping based on Portfolio.” This title establishes background relevance only. It does not prove that a Nostro is an SSI attribute, that portfolio is a Trade SSI input, or that a specific stamping process is implemented.

## Clarifications required

- Is portfolio directly used to select a Nostro?
- Is the selected Nostro an input to SSI resolution, an output of it, or a separate enrichment?
- At which lifecycle stage does stamping occur?
- Which system owns the rule and the resulting value?
- What happens when portfolio data or a matching Nostro is unavailable?
- Are user actions, input values, rule versions, timestamps, and corrections retained for audit?

Resolve alongside [[what-is-the-authoritative-trade-and-cashflow-ssi-resolution-model-for-rfi]] after reviewing the referenced Confluence content and transcribing the embedded diagrams.