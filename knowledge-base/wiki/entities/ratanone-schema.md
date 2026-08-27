---
type: entity
title: ratanone Schema
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, schema, ratanone, camunda, cash-settlement]
related: [camunda, postgresql, camunda-persistence-schema, destructive-workflow-data-purge]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda ER diagram and purge script.md"]
---
# ratanone Schema

`ratanone` is the PostgreSQL schema namespace targeted by the documented Camunda purge script.

The script names Camunda-style history, runtime, and byte-array tables under this schema. This establishes that the script operates on `ratanone` objects, but it does not identify the schema owner, environment, service ownership, data-retention policy, or authorization model.

## Operational significance

Because all documented statements use `TRUNCATE ... CASCADE`, the actual impact can include dependent tables beyond those named explicitly. The target schema's DDL or PostgreSQL catalog output is required to determine the cascade scope.

See [[what-foreign-key-dependencies-are-affected-by-ratanone-camunda-truncate-cascade]].