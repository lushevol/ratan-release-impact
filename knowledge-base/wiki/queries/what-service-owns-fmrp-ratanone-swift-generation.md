---
type: query
title: What Service Owns FMRP and RATANONE Swift Generation?
created: 2026-08-24
updated: 2026-08-24
tags: [swift-generation, fmrp, ratanone, service-ownership, architecture]
related: [swift-generation, fmrp, ratanone, swift-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation Tech design.md"]
---

# What Service Owns FMRP and RATANONE Swift Generation?

## Question

Is Swift generation owned by FMRP, a RATANONE component, [[swift-service]], or another downstream integration service?

## Current evidence

The source links a background design titled **FMRP Swift Generation** and a RATANONE Cash Settlement Technical Design. It contains no service ownership statement, API contract, message-flow description, or database schema. The referenced database diagram is also unavailable.

Consequently, the wiki should not attribute Swift-generation responsibilities to FMRP, RATANONE, or [[swift-service]] until the linked design documents and attachment are reviewed.

## Evidence required

Resolve this question by identifying:

- the service that receives the generation request;
- the source event or workflow that triggers generation;
- the input and output interfaces;
- the supported SWIFT message formats;
- the authoritative persistence store;
- acknowledgement, retry, idempotency, and exception ownership;
- the relationship between FMRP and RATANONE implementations.

## Related pages

- [[swift-generation]]
- [[fmrp]]
- [[ratanone]]
- [[swift-service]]
