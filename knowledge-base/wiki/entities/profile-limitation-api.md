---
type: entity
title: Profile Limitation API
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, api, profile-limitation, validation]
related: [batch-profile-limitation-validation, what-is-the-canonical-batch-limitation-check-identifier-field, what-service-and-data-source-own-profile-limitations]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Batch Limitation Check API Doc.md"]
---
# Profile Limitation API

The Profile Limitation API is a proposed API surface for validating cashflow amounts against profile and currency limitations.

## Documented operation

```http
POST /v1/profileLimitation/checkLimitationsBatch
```

The operation accepts multiple identifier, currency, and amount items in one request and returns a separate validation result for each item.

## Known behavior

A processable batch may contain both passed and failed item checks. The supplied example returns top-level `success: true` while one result has `success: false` because limitation data cannot be obtained for a profile and currency.

A request with null parameters is documented to return:

```json
{
  "results": null,
  "success": false,
  "reason": "Request items cannot be empty"
}
```

## Boundaries and unknowns

The source does not establish that this API is deployed, name its implementation service, identify its owner, or identify the profile or limitation-data source. It also does not define authorization, audit, HTTP-status, retry, or idempotency behavior.

The request contract is internally inconsistent over whether the identifier field is `referenceId` or `cashflowId`. See [[what-is-the-canonical-batch-limitation-check-identifier-field]].

This API supports [[batch-profile-limitation-validation]] and refers to cashflows, but the source does not prove that [[cashflow-blotter]] or [[ratan-cashflow-lifecycle-service]] invokes it.