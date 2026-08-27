---
type: concept
title: Automatic Un-Netting Error Handling
created: 2026-08-24
updated: 2026-08-24
tags: [netting, un-netting, error-handling, API-contract]
related: [ratan-cash-settlement-netting-service, ratan-cash-settlement-orchestration, product-agnostic-cashflow-aggregation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
---
# Automatic Un-Netting Error Handling

Automatic un-netting error handling covers endpoint availability, request-payload validation, locking, retries, and operational recovery for system-triggered removal of cashflows from netted groups.

The testing notes expose two separate failure modes for `N00000062630`, `C06810140005`, and `C06810141005`:

1. The orchestration call to `/v2/netting/camunda/autoUnNet` returned “No static resource”.
2. A subsequent execution reached `UnNettingService` and failed with `Payload must not be null`.

These failures should be tracked independently. Endpoint routing or deployment corrections do not demonstrate that the request payload contract is valid, and a payload fix does not establish that replay or retry behavior is safe.