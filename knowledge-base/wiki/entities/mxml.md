---
type: entity
title: MXML
created: 2026-08-23
updated: 2026-08-23
tags: [murex, message-format, xml, cashflow-migration]
related: [murex-korea, scbml, korea-direct-comp-driven-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/COMP status to drive STP process.md"]
---
# MXML

MXML is the Murex message format named as the source of trade information for the Korea direct `COMP` integration to RATAN.

The documented mappings read `tradeStatus/validationLevel` for `COMP`, `mainEvent/action` for `validation`, the trade-view entity and internal trade identifier, and the trade category fields used to derive an SCBML product taxonomy value.

The source provides image-based examples for one standalone trade and two package-child trades, but no extractable complete MXML payload. The exact schema, namespaces, and package-specific behavior remain unverified.