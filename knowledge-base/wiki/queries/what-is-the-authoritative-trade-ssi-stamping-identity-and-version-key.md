---
type: query
title: What Is the Authoritative Trade SSI Stamping Identity and Version Key?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, SSI-stamping, identity, versioning, idempotency]
related: [trade-ssi-stamping-idempotency-and-versioning, trade-level-ssi-stamping, uber, ratan-inbound-message]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---
# What Is the Authoritative Trade SSI Stamping Identity and Version Key?

## Question

Should trade SSI stamping results be identified by `tradeId + majorVersion`, by an inbound message identity such as `traceId`, by `asOf + effectiveDate`, or by another canonical key?

## Evidence and conflict

The design proposes a unique `tradeId + majorVersion` key and says that major-version changes may make currency data incompatible. It also contains an unresolved question about whether `MajorVersion` should be used, considers alternative message identifiers, and describes a query API that accepts only `tradeId`.

The same source says existing results should not be restamped, but also says repeated upstream requests may require separate records because currencies can differ.

## Required resolution

Define version ordering, latest-version selection, deduplication, historical lookup, out-of-order delivery behavior, effective-date semantics, and retry behavior. The result should align with the broader [[queries/what-is-the-ratan-inbound-message-idempotency-status-and-version-contract]] contract.