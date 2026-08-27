---
type: entity
title: FM Swift Gateway
tags: [swift, gateway, nack, cash-settlement]
related: [fmsgw, emdi, ebbs, razor, swift-status-reconciliation]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes.md"]
---
# FM Swift Gateway

## Role

FM Swift Gateway is a downstream SWIFT-generation component named in the 2024 cash-settlement delivery plan.

## Delivery scope

The plan records a 2024 H1 NACK-status function as `Closed`. EMDI is also described as establishing a Solace connection with EBBS/FM Swift Gateway.

The source separately names Razor/FMSGW for Swift Generation and NACK handling. It does not establish whether FM Swift Gateway and FMSGW are the same service, related services, or different deployment components.

## Open ownership question

The relationship between FM Swift Gateway, FMSGW, and [[entities/razor]] requires confirmation before these names are merged.