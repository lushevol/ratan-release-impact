---
type: entity
title: ratanone-data-ambassador
created: 2026-08-23
tags: [ratan, integration-service, counterparty-data, graphql, api, service, cash-settlement, indonesia]
related: [ratan, sci, ratanone-trade-service, ratanone-rule-service, sci-regulatory-field-schema-deprecation, cpty-cache, what-is-the-authoritative-cpty-cache-ownership-and-data-residency-model, ratan-indonesia-onshoring-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Technical Check List.md"]
updated: 2026-08-23
---
# ratanone-data-ambassador

`ratanone-data-ambassador` exposes counterparty data to RATAN consumers, including the `/v1/counterparty` route implicated in the trade-validation path.

## EUE notice investigation

The EUE notice investigation marks the `/v1/counterparty` route as impacted because legal-entity Dodd-Frank facts flow toward [[ratanone-trade-service]] and [[ratanone-rule-service]].

The supplied Cashflow Blotter GraphQL queries are assessed as unaffected because their documented selections do not include `eueNotice`, `smallBankExem`, or `cftcClearingExemption`.

> The GraphQL conclusion is scoped to the supplied queries and does not establish that all consumers are unaffected.

## Indonesia Cash Settlement Platform checklist

The Indonesia Cash Settlement Platform technical checklist identifies `ratanone-data-ambassador` as the impacted service for a [[cpty-cache]] item.

### Documented role and limitations

The technical-checklist source establishes only that the service is impacted by [[cpty-cache]]. It does not specify whether the service reads, writes, owns, populates, replicates, or invalidates the cache.

No service interface, deployment placement, data-flow description, implementation owner, or operational requirement is provided by that source. Its role in [[ratan-indonesia-onshoring-2026]] therefore remains provisional.