---
type: query
title: What Is the Authoritative RATAN EMS2 Entitlement API Contract?
tags: [ratan, ems2, api-contract, entitlement, access-control]
related: [ratan, ems2, x-ratanone, ratan-ems2-user-entitlement-integration, ratan-interface-inventory]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/Ratan and EMS2-34010 FMAA.md"]
---
# What Is the Authoritative RATAN EMS2 Entitlement API Contract?

## Question

What are the authoritative EMS2 interface and authorization rules used by RATAN to retrieve and apply `X_RATANONE` subjects?

## Known evidence

The source provides sample account and entitlement REST URLs and states that the subject list controls blotter visibility and right-click permissions.

## Information required

- HTTP methods, headers, authentication, and response schemas.
- Login/session retrieval and caching behavior.
- Timeout, retry, fallback, and invalidation policies.
- Mapping from subjects to blotters and context-menu actions.
- Independent server-side authorization requirements.
- Audit and operational ownership responsibilities.