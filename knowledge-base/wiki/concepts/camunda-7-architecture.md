---
type: concept
title: Camunda 7 Architecture
created: 2026-08-24
updated: 2026-08-24
tags: [camunda, camunda-7, architecture, relational-database, workflow-engine]
related: [camunda, camunda-7, activiti-5, camunda-persistence-schema, destructive-workflow-data-purge]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda migration from 7.X to 8.X.md"]
---

# Camunda 7 Architecture

The source provides a high-level description of Camunda 7 architecture:

- Camunda 7 is based on the [[activiti-5]] workflow engine.
- Camunda 7 stores workflow data in a relational database.
- Workflow data handling uses Java objects, workflow variables, and listeners.

These statements establish a legacy-platform baseline but do not describe the Cash Settlement implementation in detail. In particular, the source does not identify the database product, Camunda schema version, transaction behavior, history settings, retention policy, listener implementations, or variable serialization formats.

The relational-persistence statement is consistent with [[concepts/camunda-persistence-schema]]. It provides background for database administration and purge discussions, but does not establish the safety or approval of destructive operations described in [[concepts/destructive-workflow-data-purge]].

For migration planning, the architecture baseline implies that process definitions, runtime variables, Java extensions, listener behavior, and persisted workflow records require separate impact assessment.
