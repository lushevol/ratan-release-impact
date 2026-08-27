---
type: concept
title: Auto DVP Pilot Scope
created: 2026-08-23
updated: 2026-08-23
tags: [dvp, rollout, booking-entity, country-scope, configuration]
related: [auto-dvp, ebbs-rta-notification, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# Auto DVP Pilot Scope

The intended Auto DVP pilot covers India, Indonesia, Hong Kong, China branches, the United Kingdom, Malaysia, and South Africa, subject to final agreement based on volume.

The source frames this as a booking-entity list but also states that country code in a CorporateFinancial RTA identifies the account country. The authoritative scope dimension is therefore unresolved: RATAN may need to filter by booking entity, RTA account country, or both.

Scope and product checks should be backend-configurable so additional countries and products can be introduced without redesign.