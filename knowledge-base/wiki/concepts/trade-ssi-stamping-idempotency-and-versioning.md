---
type: concept
title: Trade SSI Stamping Idempotency and Versioning
created: 2026-08-24
updated: 2026-08-24
tags: [SSI-stamping, idempotency, versioning, optimistic-concurrency, UBER]
related: [trade-level-ssi-stamping, ratan-inbound-message, uber-inbound-message-idempotency-and-error-state]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---
# Trade SSI Stamping Idempotency and Versioning

The design proposes storing trade SSI results by `tradeId + majorVersion` and enforcing uniqueness on that pair to control concurrent stamping.

## Proposed concurrency flow

If no result exists for the key, stamping starts. Concurrent processes may race, but only one may persist successfully under the proposed unique constraint. A process that loses the persistence race should retry, observe the saved result, and avoid additional stamping.

## Unresolved identity questions

The source simultaneously questions whether `MajorVersion` should be used and considers `traceId` or `asOf + effectiveDate` as the UBER message identity. It also states that repeated upstream requests for the same trade may need separate records because currencies can differ, while another rule says an existing `tradeId + majorVersion` result should not be restamped.

The query API is described as accepting `tradeId`, whereas persistence is versioned. The design assumes downstream requests use the latest major version, but does not define latest-version ordering, historical lookup, or behavior for out-of-order delivery.

## Status

This is a proposed mechanism, not an authoritative idempotency contract. Before implementation, the team must define stable message identity, version semantics, deduplication scope, transaction boundaries, retry limits, result states, and stale-result handling.