---
type: query
title: What Is the Authoritative Store for Entity Onboarding Configuration?
created: 2026-08-24
updated: 2026-08-24
tags: [source-of-truth, configuration, onboarding]
related: [centralized-static-configuration-management, ratan-static-entity-onboarding-config, config-server, ratan-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# What Is the Authoritative Store for Entity Onboarding Configuration?

For each configuration domain, is the authoritative store Config Server, `ratan_static__entity_onboarding_config`, a static-data table, or a downstream service database?

The source conflicts on this issue: Option 1 retains Config Server for selected settings, Options 2–3 migrate them to tables, and the draft table design marks several fields and tables for removal when Config Server is used.