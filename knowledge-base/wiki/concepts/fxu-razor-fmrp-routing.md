---
type: concept
title: FXU RAZOR/FMRP Routing
tags: [FXU, RAZOR, FMRP, routing, integration, single-entity]
related: [fxu, razor, fmrp, ratan]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Dependencies for expansion to other Markets.md"]
---
# FXU RAZOR/FMRP Routing

FXU must support both RATAN and RAZOR for a single entity, resolving a current integration limitation identified in the source.

## Required behavior

FXU must:

1. Identify whether a trade belongs to RAZOR or FMRP.
2. Trigger the request to the correct system.

The source does not specify whether ownership is determined by entity, trade book, product, market, legal entity, or another attribute.

## Unresolved routing behavior

The design must define the routing key, the relationship between RAZOR and FMRP ownership, handling of missing or conflicting ownership data, and behavior when ownership changes after trade creation. No implementation status is established by the source.