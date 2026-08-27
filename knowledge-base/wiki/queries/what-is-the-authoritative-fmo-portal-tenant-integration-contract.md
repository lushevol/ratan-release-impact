---
type: query
title: What Is the Authoritative FMO Portal Tenant Integration Contract?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, fmo-portal, interface-contract, open-question]
related: [ratan-fmo-portal-tenant-integration, fmo-portal, ratan-sdk, ratan-nginx, ems2, ratan-interface-architecture]
sources: ["RATAN/RATAN -Interfaces/Ratan(FMO Portal) and STAMP FSS LOANIQ SSI+ SSDR CES.md"]
---

# What Is the Authoritative FMO Portal Tenant Integration Contract?

## Question

What are the authoritative APIs, SDK methods, authentication rules, routing configuration, operational expectations, and support responsibilities for RATAN tenant integration with FMO Portal?

## Current evidence

The source documents only these high-level flows:

```text
Tenant -- (RATAN SDK)--> EMS2
Tenant Front End page --> RATAN Nginx --> Tenant Back End server
```

It provides no endpoint paths, payload schemas, security model, error handling, service-level objectives, monitoring requirements, or interface-team contact.

## Why this remains open

The article is an architectural overview and status snapshot, not a complete interface specification. An authoritative contract is needed before implementation or operational claims are treated as verified.