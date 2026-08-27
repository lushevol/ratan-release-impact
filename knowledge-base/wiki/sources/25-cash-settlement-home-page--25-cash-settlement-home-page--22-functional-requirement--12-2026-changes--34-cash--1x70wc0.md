---
type: source
title: Swift Comparison between Korea Murex and RATAN
authors: []
year: 2026
url: ""
venue: Cash Settlement Home Page functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea-migration, murex, ratan, swift, functional-requirement]
related: [murex-korea, ratan, korea-cash-settlement-migration, ratan-swift-message-generation, swift-message-reconciliation, swift-ordering-party-field-selection, which-version-of-the-fmrp-swift-field-rules-is-authoritative, what-is-the-authoritative-korea-murex-to-ratan-swift-message-and-field-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Swift Comparison between Korea Murex and RATAN.md"]
---

# Swift Comparison between Korea Murex and RATAN

## Source assessment

This document is located in the Korea Migration functional-requirement material for 2026. Despite its title, it does not provide an actual comparison of Korea Murex and RATAN outputs. It contains a reported Korea Murex message inventory, selected SWIFT field descriptions, and a reference to the FMRP SWIFT-generation documentation.

The document does not establish RATAN message support, field mappings, output equivalence, routing behavior, suppression rules, exception handling, test evidence, reconciliation results, ownership, or approval status.

## Reported MT categories used in KR Murex

The source lists the following message categories verbatim:

```text
MT 103

MT 202

MT 202COV

MT 210

MT 192

MT 292
```

This inventory should be treated as source-reported scope only. The document does not state whether the messages are generated, consumed, suppressed, or reconciled in production, and it does not provide a date, version, volume, direction, or business-event mapping.

## Message headings in the source

The source contains the following message headings:

```text
## MT103

## MT202 and MT202cov and MT202(Flip)

## MT210

## MTx92
```

The meaning of `MT 202(Flip)` is not defined. Likewise, `MTx92` appears to be a shorthand grouping for `MT 192` and `MT 292`, but the source provides no further specification.

## Field descriptions

The following field descriptions are preserved from the source:

| Field | Description |
|---|---|
| `50a` | Ordering Customer |
| `53` | Sender's Correspondent |
| `56` | Intermediary Institution |
| `59` | Beneficiary Customer |
| `52a` | Ordering Institution |
| `58a` | Beneficiary Institution |

The source does not map each field unambiguously to a specific message template or define the applicable option letter, derivation rule, validation rule, or system ownership. In particular, the proximity of `52a` to the MT103 field list and its separate placement under `MT 202` creates a classification ambiguity.

These descriptions should not be treated as a complete implementation contract. Message-specific field availability and options must be confirmed against the applicable SWIFT and FMRP templates.

## Reference link

The source cites the following FMRP reference:

[ FMRP Swift Generation - Derivative Strategy Projects - Confluence ](https://confluence.global.standardchartered.com/display/DSP/FMRP+Swift+Generation#FMRPSwiftGeneration-SwiftMessageTemplate-H12024)

The link points to an `H12024` template anchor. The source does not confirm that this reference remains authoritative for the 2026 Korea Migration scope. This dependency relates to [[queries/which-version-of-the-fmrp-swift-field-rules-is-authoritative]].

## Evidence limitations

No comparison matrix, sample messages, field-by-field transformation, receiver derivation, exception rule, test result, reconciliation result, or remediation decision is included. Consequently, this source cannot support a conclusion that Korea Murex and RATAN produce aligned SWIFT messages or that RATAN supports all six listed MT categories.

The missing comparison artifact is tracked in [[queries/what-is-the-authoritative-korea-murex-to-ratan-swift-message-and-field-mapping]]. The source is relevant to [[concepts/swift-message-reconciliation]] and [[concepts/ratan-swift-message-generation]], but it should be treated as an incomplete input rather than as reconciliation evidence.