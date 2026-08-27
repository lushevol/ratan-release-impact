---
type: source
title: CN Settlement — Payment MXML Sample Files
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cn-settlement, murex-211, mxml, payment-integration, manualcraft, swift]
related: [cn-settlement-murex-211-integration, murex-211, murex-ratan-bidirectional-cashflow-integration, murex-ratan-cashflow-message-contract, manualcraft-mxml-enrichment, cn-settlement-payment-message-catalogue, what-does-manualcraft-change-in-murex-211-payment-mxml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Payment MXML sample files.md"]
---
# CN Settlement — Payment MXML Sample Files

## Purpose

This document identifies the intended production payment MxML/MXML samples for the CN Settlement integration with [[entities/murex-211]]. It is structured around a comparison between the raw Murex payment message and the message after enrichment by ManualCraft.

## Sample inventory

The source provides the following table without populated samples or enrichment results:

| Swift type | Raw MXML | After enrichment (ManualCraft) |
| --- | --- | --- |
| mt202_CMS | | |
| mt210 | | |
| mt103 | | |
| mt202 | | |
| mt202_210_cms | | |
| mt192 | | |
| mt103_cms | | |
| mt103_cover | | |
| mt202_cover_new | | |
| mt192_cover | | |

## Evidence boundaries

The source establishes the expected sample categories and identifies ManualCraft as an enrichment stage. It does not provide XML payloads, file names, field values, transformation rules, validation results, timestamps, environment details, or downstream-consumption evidence.

The listed identifiers should therefore be treated as sample-catalogue labels rather than confirmed standard SWIFT message types. In particular, composite or suffixed identifiers such as `mt202_210_cms` and `mt202_cover_new` require clarification before they are used as authoritative message-contract terminology.

The source also uses both “MxML” and “MXML”. The canonical naming convention remains unresolved.

## Related integration context

The inventory is relevant to the [[concepts/murex-ratan-cashflow-message-contract]] and the broader [[concepts/murex-ratan-bidirectional-cashflow-integration]]. CMS-labelled variants may relate to [[concepts/cms-dependent-swift-message-generation]], while `mt210` may relate to [[concepts/notice-to-receive-mt210-control]].

This document should not be used by itself to validate or override field-level rules documented in existing SWIFT, cashflow-message, or validation pages.

## Required follow-up evidence

To make the comparison operationally useful, the sample set should include:

- Raw MXML payloads from Murex 2.11.
- Corresponding ManualCraft-enriched payloads.
- Sample provenance, environment, timestamp, and version information.
- Field-level descriptions of additions, removals, and transformations.
- Message-type-specific validation and error samples.
- Clarification of whether each identifier is an external SWIFT type or an internal processing label.

See [[queries/what-does-manualcraft-change-in-murex-211-payment-mxml]] for the unresolved transformation question.