---
type: concept
title: Centralized Cashflow Field-Mapping Governance
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, governance, field-mapping, versioning, rule-service]
related: [rule-service, ratanone-foundation, dynamic-cashflow-query-field-mapping, query-service, what-is-the-authoritative-versioned-logical-field-to-xpath-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cashflow Query Service - GraghQL schema and DB column mapping for dynamic query.md"]
---
# Centralized Cashflow Field-Mapping Governance

Centralized field-mapping governance assigns ownership of logical cashflow fields and their mappings to a single service rather than allowing UI and query consumers to maintain independent definitions.

The source proposes [[rule-service]] as that authority, with mappings selected by version and context. [[ratanone-foundation]] would distribute and transform mappings for consumers such as [[query-service]].

## Intended benefit

The design aims to prevent mismatches between UI-displayed/filterable fields and Query Service-supported fields by using a common mapping source.

## Required policy decisions

A usable governance model needs explicit decisions on:

- mapping ownership and approval;
- version lifecycle and compatibility;
- meaning and allowed values of context;
- consumer selection of latest versus pinned versions;
- mapping publication, cache freshness, and outage fallback;
- reconciliation between UI fields, GraphQL exposure, physical storage, and field-level authorization.

The source presents optional cache refresh and event publication, not settled architecture.