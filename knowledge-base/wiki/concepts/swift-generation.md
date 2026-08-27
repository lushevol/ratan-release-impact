---
type: concept
title: Swift Generation
created: 2026-08-24
updated: 2026-08-24
tags: [swift-generation, cash-settlement, ratanone, fmrp]
related: [fmrp, ratanone, swift-service, what-service-owns-fmrp-ratanone-swift-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation Tech design.md"]
---

# Swift Generation

## Definition

Swift generation is the capability of producing SWIFT-formatted settlement messages or files from upstream trade, cashflow, settlement, SSI, or accounting data. In this source, the term identifies the subject of a RATANONE cash-settlement technical design, but the actual message-generation behavior is not documented.

## Source context

The related background link is titled **FMRP Swift Generation**. The source also links to the RATANONE Cash Settlement Technical Design. These references show a relationship between the two design areas but do not define whether Swift generation is:

- a capability within FMRP;
- a RATANONE service capability;
- an implementation of [[swift-service]]; or
- a downstream integration component.

## Undocumented contract

The supplied design does not specify:

- supported SWIFT message formats or versions;
- input events and source data;
- message mapping and validation rules;
- output destinations;
- persistence tables or authoritative storage;
- acknowledgement and delivery behavior;
- retry, idempotency, exception, or reconciliation handling.

The referenced database diagram is unavailable, so no schema claims can be made.

## Related architecture

Swift generation may depend on information managed by existing cash-settlement components such as [[ratan-cashflow-standardization-service]], [[ratan-cashflow-lifecycle-service]], [[ratan-cash-settlement-orchestration]], [[accounting-service]], or [[ssi-stamping-and-best-match]]. The source does not establish any of these dependencies and they require confirmation from the linked design material.

See [[what-service-owns-fmrp-ratanone-swift-generation]] for the unresolved ownership and interface question.
