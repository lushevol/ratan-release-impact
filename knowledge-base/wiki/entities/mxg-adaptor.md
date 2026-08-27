---
type: entity
title: mxg-adaptor
created: 2026-08-24
updated: 2026-08-24
tags: [service, murex, adaptor, fmid, indonesia]
related: [batch-service, fixing-flag-entity-based-routing, murex-party-fmid-enrichment, what-is-the-authoritative-indonesia-cashflow-classification-rule-for-fixing-flags]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Fixing Flag Process in Indonesia.md"]
---
# mxg-adaptor

`mxg-adaptor` is proposed as the provider of an API that returns a cashflow's booking-entity FMID for Indonesia pending-fixing-flag routing.

The GDC [[batch-service]] depends on this lookup before deciding whether to publish a fixing-flag message for Indonesia. The draft does not define the API endpoint, response schema, authentication, error handling, latency, or authoritative FMID mapping. This use case is related to, but does not establish, [[murex-party-fmid-enrichment]] as the authoritative source.