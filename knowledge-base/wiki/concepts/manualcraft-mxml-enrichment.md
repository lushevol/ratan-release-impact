---
type: concept
title: ManualCraft MXML Enrichment
created: 2026-08-24
updated: 2026-08-24
tags: [manualcraft, mxml, enrichment, payment-messages, murex-211]
related: [manualcraft, murex-211, murex-ratan-cashflow-message-contract, cn-settlement-payment-message-catalogue, cash-settlement-inbound-outbound-message-validation, what-does-manualcraft-change-in-murex-211-payment-mxml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Payment MXML sample files.md"]
---
# ManualCraft MXML Enrichment

ManualCraft MXML enrichment is the intended transformation boundary between raw payment MXML from [[entities/murex-211]] and an enriched payment MXML representation used in the CN Settlement integration.

## Current evidence

The source contains a comparison template with two states:

- Raw MXML.
- MXML after enrichment by ManualCraft.

The template is organized by payment labels such as `mt202_CMS`, `mt210`, `mt103`, `mt202`, `mt202_210_cms`, `mt192`, `mt103_cms`, `mt103_cover`, `mt202_cover_new`, and `mt192_cover`.

The source contains no payloads or populated comparison cells. It therefore does not establish which XML nodes ManualCraft changes, whether enrichment is mandatory, or whether processing differs across message variants.

## Contract that requires documentation

A complete enrichment contract should identify:

1. The input MXML schema and producer.
2. The output MXML schema and consumer.
3. Fields or structures added, removed, or transformed.
4. Message-type-specific rules.
5. Validation, rejection, retry, and error behavior.
6. Version and environment dependencies.
7. Traceability between each raw sample and its enriched output.

Until those details are evidenced, this concept describes an intended integration boundary rather than a confirmed implementation.

The boundary should be reconciled with the [[concepts/murex-ratan-cashflow-message-contract]] and the validation expectations in [[concepts/cash-settlement-inbound-outbound-message-validation]].