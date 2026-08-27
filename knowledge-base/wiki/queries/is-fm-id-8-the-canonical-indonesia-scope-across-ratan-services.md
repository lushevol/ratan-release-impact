---
type: query
title: Is FM ID 8 the Canonical Indonesia Scope Across RATAN Services?
tags: [RATAN, Indonesia, FM-ID, data-migration, scope]
related: [ratan-indonesia-entity-scoped-data-migration, ratan-indonesia-onshoring-2026, ratan-indonesia-isolated-deployment]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Data Migration - Indonesia.md"]
---
# Is FM ID 8 the Canonical Indonesia Scope Across RATAN Services?

## Question

Does value `'8'` identify the same Indonesia entity across `party1_fm_id`, `entity__booking_entity_sci_fmid`, `booking_entity_fmid`, `booking_entity_id`, and `entity_fmid`?

## Evidence

The migration inventory applies `'8'` to all of these fields, but does not provide a canonical mapping, data dictionary, or cross-service validation. The fields may represent different identifier domains despite using the same value.

## Resolution needed

Confirm the authoritative Indonesia identifier and document a service-by-service mapping. Validate the mapping against representative records in every listed schema before migration population is finalized.