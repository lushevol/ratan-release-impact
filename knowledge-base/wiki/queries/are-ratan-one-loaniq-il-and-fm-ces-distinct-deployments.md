---
type: query
title: Are RATAN ONE, LOANIQ.IL, and FM CES Distinct Deployments?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, tenant-identity, deployment-scope, open-question]
related: [ratan-fmo-portal-tenant-integration, x-ratanone, loaniq, ces, ssdr-51507]
sources: ["RATAN/RATAN -Interfaces/Ratan(FMO Portal) and STAMP FSS LOANIQ SSI+ SSDR CES.md"]
---

# Are RATAN ONE, LOANIQ.IL, and FM CES Distinct Deployments?

## Question

Are `RATAN ONE`, `LOANIQ.IL`, and `FM CES` distinct tenant applications or deployments, or are they named variants of the existing `X_RATANONE`, `LOANIQ`, and `CES` entities?

## Current evidence

The source lists the three names as FMO Portal tenants and assigns them the statuses `Online`, `Online`, and `Pending`, respectively. The existing wiki contains related entities, but the source does not establish identity equivalence or deployment scope.

## Why this remains open

Merging these names into existing entity pages could incorrectly combine tenant-specific status claims with platform-level information. The identity and scope should be confirmed before consolidation.