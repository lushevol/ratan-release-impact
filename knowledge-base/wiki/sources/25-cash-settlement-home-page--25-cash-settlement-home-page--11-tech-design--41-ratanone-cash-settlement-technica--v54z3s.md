---
type: source
title: Swift Generation Technical Design
authors: []
year: 2024
url: "https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2560471970"
venue: "Derivative Strategy Projects Confluence"
tags: [swift-generation, ratanone, fmrp, cash-settlement, technical-design]
related: [fmrp, ratanone, swift-service, swift-generation, what-service-owns-fmrp-ratanone-swift-generation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation Tech design.md"]
---

# Swift Generation Technical Design

## Summary

This source is a technical-design page concerning Swift generation in the RATANONE cash-settlement context. The supplied document is incomplete: it contains background and high-level-design links, section headings, and a reference to a database diagram, but it does not include implementation details.

The document establishes an association with an FMRP Swift Generation design, but it does not identify the owning service, supported SWIFT message formats, generation triggers, input contract, output contract, persistence model, or operational handling.

## Source links

- [FMRP Swift Generation - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/FMRP+Swift+Generation)
- [RATANONE Cash Settlement Technical Design - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2560471970)

## Available design structure

The source contains the following sections:

- Background
- High level design
- Design
- Database

The database section references an image attachment, but the image contents are not available in the supplied source:

```markdown
![image2024-6-27-9-19-31.png](attachments/image2024-6-27_9-19-31.png)
```

No SQL DDL, schema definition, API signature, configuration, or readable table is present. Database tables, fields, keys, indexes, and relationships must not be inferred from the unavailable image.

## Evidence boundaries

The source supports only the following conclusions:

- A design or project titled **FMRP Swift Generation** exists as a related background document.
- A RATANONE Cash Settlement Technical Design exists.
- Swift generation includes a database-design concern.
- The relationship between FMRP, RATANONE, and [[swift-service]] is unresolved.

The source does not establish that:

- FMRP owns Swift generation;
- RATANONE owns Swift generation;
- [[swift-service]] implements Swift generation;
- a particular SWIFT message type or protocol variant is supported;
- any specific database schema or persistence contract exists;
- message generation has particular retry, idempotency, acknowledgement, or reconciliation behavior.

## Knowledge gaps

Further documentation is needed to determine:

1. The owning service and system boundary for Swift generation.
2. Supported message formats and versions.
3. Generation triggers and required upstream data.
4. SSI, accounting, and settlement attributes used in message construction.
5. The authoritative persistence store.
6. Message-request, acknowledgement, retry, exception, audit, and reconciliation records.
7. Idempotency and operational recovery rules.
8. Whether the linked FMRP design remains current and how it maps to RATANONE.

This source should therefore be treated as a design reference with low evidentiary detail rather than as an authoritative architecture specification.
