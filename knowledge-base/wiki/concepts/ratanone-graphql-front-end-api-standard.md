---
type: concept
title: RATANONE GraphQL Front-End API Standard
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, ratanone, frontend, api-standard, schema-design]
related: [ratan, rule-service, data-modelling, centralized-cashflow-field-mapping-governance, dynamic-cashflow-query-field-mapping, cash-settlement-query-service-graphql-read-model, cashflow-notification-and-auto-refresh, what-is-the-authoritative-ratanone-graphql-transport-and-bypass-policy, what-are-the-canonical-ratanone-graphql-schemas-and-subscription-semantics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN.md"]
---
# RATANONE GraphQL Front-End API Standard

The source defines an intended standard that RATANONE frontend queries to backend APIs should go through GraphQL. This is normative design intent, not evidence that all frontend reads currently use GraphQL.

## Design Direction

Each use case should have a clearly defined GraphQL schema before implementation. The intended benefit is aggregation of backend data into UI-facing responses, reducing UI-to-backend API calls.

The source allows an exception when an aggregation component causes a performance issue: it may be made a single API call. It does not define whether this remains a single GraphQL operation or permits a frontend client to bypass GraphQL through REST or another backend interface.

## Field Governance

GraphQL fields and attributes must originate from a standard logical model or business term in [[data-modelling]], or from a RATAN extension. Fields defined in [[rule-service]] and Data Modelling indexed terms are preferred. RATAN-specific fields must be explicitly defined and marked `RATAN_DATA`.

This broad API-field governance direction complements [[centralized-cashflow-field-mapping-governance]] and [[dynamic-cashflow-query-field-mapping]], but does not define a field registry, approval workflow, versioning model, or enforcement mechanism.

## Intended UI Coverage

The stated coverage includes trade, cashflow, counterparty, and exception reads. Queries and subscriptions are recommended in Ratan; subscriptions are proposed for trade, cashflow, and exception notifications. Quick Search, Custom Filter, and Custom View are named UX capabilities.

The source does not define the actual schemas, filtering syntax, selected-field allowlists, pagination, authorization, or subscription contracts required to implement these capabilities.

## Related Implementations

This standard supplies product-level rationale for GraphQL frontend consumption. It does not make the existing [[cash-settlement-query-service-graphql-read-model]] a canonical implementation for every RATANONE use case, and it does not replace the existing semantics documented for [[cashflow-notification-and-auto-refresh]].