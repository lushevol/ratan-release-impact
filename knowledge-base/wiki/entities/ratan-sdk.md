---
type: entity
title: RATAN SDK
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, sdk, entitlement, tenant-integration]
related: [ratan-fmo-portal-tenant-integration, ems2, ratan-data-entitlement]
sources: ["RATAN/RATAN -Interfaces/Ratan(FMO Portal) and STAMP FSS LOANIQ SSI+ SSDR CES.md"]
---

# RATAN SDK

## Role

RATAN SDK is the tenant-side mechanism identified for obtaining an entitlement list. The documented flow is:

```text
Tenant -- (RATAN SDK)--> EMS2
```

## Evidence boundary

The source does not provide SDK versions, package names, method signatures, authentication requirements, response schemas, or error handling. No additional capabilities should be inferred from this article.