---
type: entity
title: Config Server
created: 2026-08-24
updated: 2026-08-24
tags: [configuration, runtime-configuration, onboarding]
related: [centralized-static-configuration-management, self-service-entity-branch-onboarding, entity-onboarding-configuration-architecture-options]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# Config Server

Config Server is a proposed runtime configuration store in Option 1 of the self-service entity and branch onboarding design.

Under that option, `accouting-service`, [[swift-service]], `static-data-service`, and [[ratan-cash-settlement-orchestration]] would read selected settings from Config Server rather than `application.yml`. The alternative Options 2 and 3 instead propose migrating those values to database tables.

The design does not decide between Config Server and database-backed configuration, and it does not demonstrate hot-reload behavior, authorization, audit retention, or configuration versioning.