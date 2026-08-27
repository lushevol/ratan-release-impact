---
type: concept
title: Configuration Dependencies
created: 2026-08-24
updated: 2026-08-24
tags: [configuration, dependencies, validation, publication, ratan]
related: [static-configuration-management, centralized-static-configuration-management, pending-configuration-change-isolation, unified-json-configuration, what-is-the-dependency-model-for-ratan-ui-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft)/Static Code In UI.md"]
---
# Configuration Dependencies

Configuration dependencies exist when one configuration item requires another item, schema, or deployed capability to be valid. The source explicitly identifies this requirement but does not provide a dependency graph.

In `mfe-cashflow-blotter`, inferred examples include quick filters depending on valid backend fields and operator mappings; booking-entity records supplying quick-filter values; column definitions requiring query fields; and status presentation requiring valid workflow statuses.

A configuration service should model dependencies explicitly where they are authoritative, validate a complete compatible set before publication, assign versions, and support rollback. These relationships are inferred from the inventory in [[static-code-in-ui]], not approved system contracts.