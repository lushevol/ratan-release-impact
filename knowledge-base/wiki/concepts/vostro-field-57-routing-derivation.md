---
type: concept
title: Vostro Field 57 Routing Derivation
created: 2026-08-23
updated: 2026-08-23
tags: [vostro, ssi, swift, field-57, routing, cross-border-debit]
related: [cross-border-debit-settlement, cross-border-debit-message-mapping, vostro-nostro-ssi-matching, ssi-swift-field-enrichment, what-does-vostro-si-field-57-control-in-cross-border-debit-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit/Cross Border Debit UAT.md"]
---
# Vostro Field 57 Routing Derivation

In cross-border debit receive-side UAT cases, the source states that “Tag 1 and Tag 2” are picked from field 57 of the Vostro settlement instruction.

## Evidence

The assertion is accompanied by tested routing contexts for USD, EUR, and GBP. The source explicitly associates the EUR case with `SCBLDEFX` and the GBP case with `SCBLGB2L`; USD examples include Hong Kong and Singapore header contexts.

This is evidence of an intended Vostro-field-57 dependency for receive-side routing or header selection. It is not a complete SWIFT field-enrichment specification.

## Unresolved Meaning

“Tag 1 and Tag 2” are not formally defined. The source does not identify whether they refer to FIN header blocks, sender and receiver BICs, internal routing fields, or another construct. It also does not define precedence if Vostro field 57 and Nostro 53B/BIC values differ.

See [[what-does-vostro-si-field-57-control-in-cross-border-debit-routing]].