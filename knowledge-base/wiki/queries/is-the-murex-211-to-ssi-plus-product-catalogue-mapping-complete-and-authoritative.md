---
type: query
title: Is the Murex 2.11 to SSI+ Product Catalogue Mapping Complete and Authoritative?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-2-11, ssi-plus, product-catalogue, mapping, vostro-ssi]
related: [murex-2-11, ssi-plus, ratan-10123, vostro-ssi-redundancy-and-product-scoping, cfi-code-mapping-for-murex-vostro-ssi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI.md"]
---
# Is the Murex 2.11 to SSI+ Product Catalogue Mapping Complete and Authoritative?

Can the asserted Murex 2.11-to-SSI+ mapping be recovered as a textual, versioned, one-to-one mapping for China and Global `CURR` and `IRD` catalogues?

## Why this is open

RATAN-10123 concludes that the catalogues are the same, citing five screenshots and an attached **Murex 2.11 CN Vostro SSI** dataset. Those artefacts are absent from the supplied source content.

The source does not identify catalogue versions, extraction dates, mapping rules, unmatched values, or approval ownership. It also does not demonstrate that catalogue correspondence makes product-scoped SSI records interchangeable.

## Evidence needed

- The five referenced catalogue screenshots or their source extracts.
- The **Murex 2.11 CN Vostro SSI** attachment.
- A versioned table mapping Murex family/group/type values to SSI+ `Security` values.
- Completeness, uniqueness, and exception results for China and Global catalogues.
- Ownership and change-control evidence for the mapping.

## Decision impact

An authoritative mapping is needed to distinguish a catalogue-alignment finding from an SSI routing or de-duplication decision.