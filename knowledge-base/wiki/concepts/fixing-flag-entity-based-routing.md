---
type: concept
title: Fixing-Flag Entity-Based Routing
created: 2026-08-24
updated: 2026-08-24
tags: [routing, fixing-flag, fmid, booking-entity, indonesia, murex]
related: [batch-service, mxg-adaptor, indonesia-pending-fixing-flag-relay, murex-party-fmid-enrichment, ratan-eligible-entity-configuration, what-is-the-authoritative-indonesia-cashflow-classification-rule-for-fixing-flags]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Fixing Flag Process in Indonesia.md"]
---
# Fixing-Flag Entity-Based Routing

Fixing-Flag Entity-Based Routing is the proposed selection control under which GDC publishes a pending-fixing-flag message only when its related cashflow is identified as an Indonesia cashflow.

The proposed process has [[batch-service]] query [[mxg-adaptor]] for the cashflow's booking-entity FMID before publication.

The source does not define the authoritative FMID source, eligibility mapping, fallback treatment for missing or stale data, or whether attributes other than booking entity participate in the Indonesia classification. It is therefore related to [[murex-party-fmid-enrichment]] and [[ratan-eligible-entity-configuration]], but does not establish either concept's rules for this flow.