---
type: entity
title: ratanone-foundation
created: 2026-08-22
updated: 2026-08-23
tags: ["software-service", "ratan-one", "inter-entity-netting", "cash-settlement", "sdk", "mapping", "scbml", "caching"]
related: ["inter-entity-netting", "ratan-cash-settlement-netting-service", "ratan-cash-settlement-group-management-service", "ratan-rule-service", "rule-service", "centralized-cashflow-field-mapping-governance", "query-service", "dynamic-cashflow-query-field-mapping"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter Entity Netting Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cashflow Query Service - GraghQL schema and DB column mapping for dynamic query.md"]
---
# ratanone-foundation

## Role in the Design

In the inter-entity netting design, `ratanone-foundation` is listed as a participating service requiring changes for the feature. That source does not specify which component owns the changes or whether the service performs cashflow matching.

In the cashflow query service design, `ratanone-foundation` is proposed as an SDK layer for distributing and applying versioned cashflow field mappings.

## Proposed SDK Responsibilities

The cashflow query service design proposes that `ratanone-foundation` may:

- Package a predefined mapping file and version sourced from [[rule-service]].
- Transform SCBML into logical-model JSON.
- Optionally retrieve mappings from [[rule-service]] by version and context, including `RATAN_DATA` and `CASHFLOW_DATA`.
- Optionally cache mappings for the active version and refresh hourly.
- Optionally consume mapping-version-upgrade events and refresh its cache.

That source does not define cache invalidation, event ordering, fallback during Rule service outages, or whether a consumer must use a pinned version rather than the latest version.

## Feature Branch

The inter-entity netting design associates this service with:

```text
feature/autonetting-interEntity
```

No release version is provided, so that source does not confirm that the branch was merged, released, or enabled in production.

## Related Services and Concepts

For inter-entity netting, the service appears in the same implementation scope as [[ratan-cash-settlement-netting-service]], [[ratan-cash-settlement-group-management-service]], and [[ratan-rule-service]]. The overall feature is described by [[inter-entity-netting]].