---
type: query
title: What Is the Final Dedicated Nostro Data Model and Uniqueness Constraint?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, static-data, schema, uniqueness]
related: [dedicated-nostro-static-data-model, ratanone-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md"]
---
# What Is the Final Dedicated Nostro Data Model and Uniqueness Constraint?

The source references `nostroType`, `nostroKey`, `dedicated_info`, JSONB, and child tables without a definitive schema. It also specifies a five-factor duplicate key that excludes portfolio. Confirm the physical model, indexes, lookup query, and uniqueness rule that support portfolio-specific RFI records while preventing multiple matches.