---
type: query
title: "What Is the Canonical RATAN/RatanOne Service Identity?"
tags: [ratan, ratanone, service-identity, naming, scope]
related: [ratan, ratanone, ratanone-settlement-orchestration-service, ratan-service-governance]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -App Docs/RATAN -App Docs.md"]
---
# What Is the Canonical RATAN/RatanOne Service Identity?

## Question

Are **RATAN**, **RATAN ONE**, and **RatanOne** names for the same service, or do they identify different application scopes, products, or historical versions?

## Evidence

The documentation register uses `RATAN` in its title and service records, `RATAN ONE` in the OLA title, and `Ratan One` in the Korea processing-guide title. Existing wiki pages separately reference [[ratanone]] and [[ratanone-settlement-orchestration-service]].

The recovery, restore, and capacity records use the identifier `51358`, but the register does not explicitly map that identifier to an existing canonical entity.

## Required verification

Review the linked `ASRM`, SLA, OLA, and OnePoint plans for:

- Canonical service name and service boundaries
- Service identifier mapping
- Ownership and support scope
- Whether the Korea, Settlement, and Trade guides cover one service or multiple components
- Historical naming or product-version distinctions