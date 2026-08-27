---
type: query
title: Which Service Owns Fields, Validation Rules, and Profile Limitation?
created: 2026-08-24
updated: 2026-08-24
tags: [service-ownership, static-data, validation-rules, profile-limitation]
related: [rule-service-domain-boundaries, ratanone-rule-service, ratan-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# Which Service Owns Fields, Validation Rules, and Profile Limitation?

The archived design states that Fields and frontend Validation Rules should leave Rule Service for static data service ownership, while Profile Limitation stays within the Rule domain service.

## Questions to resolve

- Which concrete service owns Fields and Fields Xpath?
- Which service owns frontend Validation Rules and their versioned configuration?
- What APIs, persistence, entitlement controls, and client migrations are required?
- Is Profile Limitation implemented and governed by `ratanone-rule-service` or another Rule domain component?
- What is the target transition and deprecation plan for legacy endpoints?

No target architecture or accountable owner is identified in the source.