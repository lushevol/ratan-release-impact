---
type: query
title: What Do Common, BAU, and CN Mean in the Ratan Service Landscape?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, service-landscape, ratan, architecture, open-question]
related: [cash-settlement-service-landscape, cash-settlement-platform, ratan, cashflow-lifecycle-service, ratan-cash-settlement-group-management-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design.md"]
---
# What Do Common, BAU, and CN Mean in the Ratan Service Landscape?

## Question

What formal scope and operational meaning do the `Common`, `BAU`, and `CN` labels have in the RatanOne and Cash Settlement service inventory?

## Why this matters

The source lists services in all three classifications but provides no definitions, responsibilities, owners, interfaces, or deployment status. The coexistence of `RATANONE-*` BAU services and `RATAN-*` CN services may indicate distinct product, regional, or migration boundaries, but this is not established.

## Required resolution

Confirm for every listed service:

- classification definition and governance meaning;
- business and technical owner;
- deployed, planned, deprecated, or migrated status;
- primary domain and data ownership;
- upstream and downstream dependencies; and
- correspondence, if any, to similarly named existing wiki entities.

This resolution is necessary before creating identity mappings between the source inventory and pages such as [[query-service]], [[netting-service]], [[rule-service]], and [[cashflow-lifecycle-service]].