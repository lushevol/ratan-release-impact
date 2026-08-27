---
type: query
title: What Is the Dependency Model for Ratan UI Configuration?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, configuration, dependencies, validation, rollback]
related: [static-code-in-ui, configuration-dependencies, centralized-static-configuration-management, pending-configuration-change-isolation, ratan-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft)/Static Code In UI.md"]
---
# What Is the Dependency Model for Ratan UI Configuration?

The source states that one configuration depends on another but does not define dependent items, ordering, validation, publication, or rollback.

A decision is needed on how the service declares dependencies between field definitions, quick filters, operator mappings, query mandatory fields, status metadata, booking-entity lists, and frontend behavior identifiers. The model should also specify compatibility checks against deployed frontend and backend versions and the recovery procedure for invalid publication.