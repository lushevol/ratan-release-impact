---
type: concept
title: Unified JSON Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, configuration, json, schema-design]
related: [static-configuration-management, schema-evolution-for-cash-settlement, shared-static-configuration-maker-checker-engine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# Unified JSON Configuration

Unified JSON configuration stores multiple configuration domains in one table using a type discriminator and a JSON data payload.

The source presents this as an alternative to typed domain tables. Its advantages are fewer generic APIs and potentially lower frontend effort. Its stated trade-offs include weaker support for database uniqueness constraints, customized validation, direct SQL import/export, and adding new configuration values without additional generic handling.

The source also describes a metadata-driven variant that stores field definitions and values separately. That variant can support generated UI and basic validation but may not support specialized controls or domain-specific validation well.

The design does not establish that either unified approach should be adopted.