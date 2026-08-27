---
type: query
title: What Is the Authoritative Korea Murex-to-RATAN SWIFT Message and Field Mapping?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea-migration, murex, ratan, swift, message-mapping, open-question]
related: [murex-korea, ratan, korea-cash-settlement-migration, ratan-swift-message-generation, swift-message-reconciliation, swift-ordering-party-field-selection, which-version-of-the-fmrp-swift-field-rules-is-authoritative]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Swift Comparison between Korea Murex and RATAN.md"]
---

# What Is the Authoritative Korea Murex-to-RATAN SWIFT Message and Field Mapping?

## Question

Where is the approved, message-by-message comparison between Korea Murex and RATAN for the Korea Migration scope?

The source lists the following categories as used in KR Murex:

```text
MT 103
MT 202
MT 202COV
MT 210
MT 192
MT 292
```

However, it does not state which messages RATAN generates, consumes, suppresses, or reconciles. It also does not provide the field mappings, routing rules, exception paths, or test evidence needed to validate the interface.

## Required comparison scope

The authoritative artifact should identify, for each listed message:

- The triggering business event and processing direction.
- Whether Korea Murex or RATAN generates, receives, suppresses, or reconciles the message.
- Sender, receiver, correspondent, and intermediary derivation.
- Field-by-field mapping, including the applicable options for `50a`, `52a`, `53`, `56`, `58a`, and `59`.
- SWIFT formatting and validation rules.
- Manual-processing and exception paths.
- Sample Murex and RATAN messages.
- Test results, production reconciliation evidence, and known differences.
- The accountable owner and the applicable SWIFT/FMRP template version.

## Unresolved terminology

The source refers to `MT 202(Flip)` without defining the flow or explaining how it differs from standard `MT 202` and `MT 202COV`. It also uses `MTx92` without specifying whether this is only a shorthand for `MT 192` and `MT 292` or represents an additional processing category.

The field list is also not tied unambiguously to individual message templates. Generic descriptions cannot establish the implementation contract because field availability and option selection are message-specific.

## Version dependency

The source links to the `H12024` section of the FMRP SWIFT Generation documentation. It is not established whether this reference is approved and current for the 2026 Korea Migration implementation. Applicability should be confirmed through [[queries/which-version-of-the-fmrp-swift-field-rules-is-authoritative]] before the mapping is approved.

## Current assessment

This remains an open question. The source is insufficient to demonstrate equivalence or differences between Korea Murex and RATAN, and it should not be used as evidence that RATAN supports the six listed MT categories.

The missing artifact is also relevant to [[concepts/swift-message-reconciliation]], [[concepts/ratan-swift-message-generation]], and [[projects/korea-cash-settlement-migration]].