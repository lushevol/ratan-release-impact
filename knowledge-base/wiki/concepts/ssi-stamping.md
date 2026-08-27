---
type: concept
title: SSI Stamping
created: 2026-08-22
updated: 2026-08-23
tags: [ssi, stamping, settlement, SSI-stamping, settlement-instructions, cash-settlement, Nostro, trade-enrichment, confirmations]
related: [standard-settlement-instructions, ssi-selection-hierarchy, ratan, cash-settlement-2025-roadmap, ssi-stamping-service, fmrp, ccy-pair-based-nostro-selection, primary-nostro-fallback, vostro-nostro-ssi-matching, scbml-trade-enrichment-api, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md"]
---
# SSI Stamping

SSI stamping is the application of selected Standard Settlement Instruction data to a trade, cashflow, or related settlement record.

The Egypt technical design describes SSI stamping as resolving settlement instructions from trade attributes and embedding the results into an enriched SCBML trade or confirmation message. The compatibility design describes it as selecting or enriching settlement instructions for a cashflow.

> **Design status:** The compatibility design records a proposed design rather than confirmed production behavior. The Egypt technical design describes intended behavior for a UAT integration and does not establish production behavior or a complete operational contract.

## Cashflow Selection Design

According to the compatibility design, SSI stamping's central responsibility is selecting the expected Nostro account for eligible local-currency cashflows.

The proposed selection key is `CCY Pair`, subject to:

- Entity eligibility
- Product eligibility
- Payment-currency eligibility

The proposed behavior differs depending on whether the result is:

- A single Vostro
- A missing Vostro
- Multiple Vostro outcomes

## SCBML Trade and Confirmation Enrichment

According to the Egypt technical design, processing follows this model:

1. Receive a Base64-encoded SCBML message.
2. Extract trade attributes such as legal-entity FMID, counterparty FMID, currencies, product information, and payer/receiver relationships.
3. Query Vostro settlement instructions where applicable.
4. Query Nostro settlement instructions using the legal entity, currency, and Vostro-derived values.
5. Enrich the SCBML message with resolved settlement details or fallback text.
6. Return the enriched message and side- or leg-level result details.

### Side and Leg Behavior

According to the Egypt technical design:

- SCB Pay / sell processing evaluates both Vostro and Nostro outcomes.
- SCB Receive / buy processing evaluates Nostro outcomes only.
- Single-leg products expose `singleLegResult`.
- Multi-leg products expose `nearLegResult` and `farLegResult`.

### Fallback Behavior

According to the Egypt technical design, a missing or multiple settlement-instruction match can produce fallback confirmation text rather than preventing all enrichment:

- `Please advise` for an unresolved counterparty account.
- `To Be Advise` for an unresolved SCB account.
- A default Nostro based on `Currency + MAIN` in the applicable scenario.

These strings are retained as source-system text and require validation before any normalization.

## Relationship to SSI Selection

[[ssi-selection-hierarchy]] determines which instruction should be selected. SSI stamping applies the resulting instruction to the relevant record.

The roadmap source does not document the exact boundary between instruction selection and stamping. The compatibility design provides a proposed cashflow selection approach, while the Egypt technical design provides intended UAT SCBML-enrichment behavior; neither establishes confirmed production behavior.

## Roadmap References

The 2025 plan includes:

- Strategic One Stop SSI stamping as an undated annual initiative.
- Work item `7523847`, which seeks to synchronize UK Prime trade SSI stamping best-match behavior with cashflow behavior.

This implies a need for consistent instruction selection and propagation between trade and cashflow processing.

## Unknowns

The roadmap does not provide:

- The stamping data model
- Required SSI fields
- Matching logic
- Override behavior
- Re-stamping rules
- Audit requirements
- Exception handling
- Delivery status for Strategic One Stop SSI stamping