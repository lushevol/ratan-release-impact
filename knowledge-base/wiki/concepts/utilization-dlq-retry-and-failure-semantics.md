---
type: concept
title: Utilization DLQ Retry and Failure Semantics
created: 2026-08-24
updated: 2026-08-24
tags: [utilization, dlq, retry, failure-handling, nack]
related: [utilization-service, fxu-utilization-response-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md"]
---
# Utilization DLQ Retry and Failure Semantics

The draft separates utilization technical failures into two response paths.

## Malformed request

A request that is not well-formed JSON is not described as retryable. It receives a `NACK` response with:

- Empty `Utilization_Id`
- `Error_Reason: "Raw message error."`
- The original input under `Request_Info.Raw_Request`

## Ratan internal error

A syntactically valid request that encounters a Ratan internal error is sent through a DLQ retry path. The utilization service retries at most five times and then returns a `NACK` with:

- The request's utilization ID
- `Error_Reason: "Ratan internal error."`
- The parsed utilization request under `Request_Info.Utilization`

The draft does not specify retry delays, backoff, idempotency behavior, message ownership, observability, or terminal disposition after the fifth attempt. These omissions are material because retries can cause duplicate processing unless the request and downstream effects are idempotent.