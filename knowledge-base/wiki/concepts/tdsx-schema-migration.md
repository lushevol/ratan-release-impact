---
type: concept
title: TDSX Schema Migration
created: 2026-08-24
updated: 2026-08-24
tags: [tdsx, schema-migration, data-compatibility, ratanone]
related: [ratanone-data-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratanone-Foundation release note.md"]
---
# TDSX Schema Migration

The RatanOne foundation release migrates the TDSX proto schema from `V7.1-RELEASE` to `V7.8-RELEASE`.

## Reported changes

The migration includes:

- Conversion of some fields from single values to arrays
- Corrections to internal field value types
- Addition of a new internal field for FXU

## Compatibility risks

Scalar-to-array changes can affect application code, serializers, persistence mappings, XPath extraction, enrichment logic, and downstream consumers. The release note does not identify the affected fields or provide a consumer migration plan.

Before adoption, teams should obtain the complete schema diff, identify all scalar assumptions, validate generated mappings, and test backward and forward compatibility where required.

This concept applies to TDSX and should not be merged with [[tds3]] without additional evidence.
