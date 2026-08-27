---
type: entity
title: ratan-suppression-service
created: 2026-08-24
updated: 2026-08-24
tags: [service, bau-rules, suppression, legacy, cash-settlement]
related: [ratanone-rule-service, rule-service-consolidation, does-ratan-suppression-service-mean-ratanone-suppression-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# ratan-suppression-service

`ratan-suppression-service` is named in the archived design as the BAU-rule service intended to migrate into [[ratanone-rule-service]]. The migration scope includes Suppression Rules and Netting Rules.

The document also calls the compared service `ratanone-suppression-service` in its database section. It is not safe to assume these labels identify the same deployed service, a simple rename, or a typographical inconsistency. See [[does-ratan-suppression-service-mean-ratanone-suppression-service]].

The BAU schema source table is written as `ratanone.ratan_suppresion_rule`; the spelling must be retained when referring to the physical identifier.