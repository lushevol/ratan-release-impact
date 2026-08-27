---
type: entity
title: Data Modelling
created: 2026-08-24
updated: 2026-08-24
tags: [data-governance, logical-model, business-terms, graphql, ratanone]
related: [rule-service, ratanone-graphql-front-end-api-standard, centralized-cashflow-field-mapping-governance, dynamic-cashflow-query-field-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN.md"]
---
# Data Modelling

Data Modelling (DM) is identified as the source of standard logical-model and business-term definitions for fields exposed through RATANONE GraphQL queries.

## Role in GraphQL Field Selection

The source states that GraphQL fields and attributes should be defined natively in DM or as RATAN extensions. Data Modelling indexed terms are the preferred choice, alongside fields defined in [[rule-service]]. A RATAN-specific field that is not available as a standard term must be defined and marked `RATAN_DATA`.

The source does not provide a DM API, indexed-term catalogue, ownership model, approval process, or validation mechanism. It therefore does not establish how applications enforce the stated provenance policy.