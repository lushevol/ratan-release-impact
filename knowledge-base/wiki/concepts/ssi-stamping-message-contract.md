---
type: concept
title: SSI Stamping Message Contract
tags: [ssi, api-contract, scbml, fpml, cashflow-versioning, json]
related: [ssi-stamping-service, adhoc-ssi-maker-checker-workflow, cashflow-version-tuple-comparison, what-is-the-authoritative-adhoc-ssi-api-contract]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/SSI Stamping Service Design/SSI Stamping Design.md"]
---
# SSI Stamping Message Contract

The Adhoc SSI interface carries a full SCBML cashflow XML message, embedding FpML confirmation data, alongside a metadata envelope and a `trackingId`.

## Cashflow identity and version context

Requests include:

- `cashflowId`
- `businessVersion`
- `cashflowVersion`
- `minorVersion`

This is a four-part cashflow version context consistent with [[cashflow-version-tuple-comparison]]. Its use suggests callers must correlate and protect updates against the specific represented cashflow version, but stale-version and concurrent-submission behavior is unspecified.

## Nested SSI encoding

The Maker request uses `metadata.requestBody` as a stringified JSON document containing `fitVostro` and `fitNostro`. Consumers must deserialize the outer request and then deserialize this string field. The Checker rejection request instead shows `requestBody` as an empty JSON object, despite the interface table describing it as `null`.

## Response inconsistency

The Maker response identifies versions as `businessVersion` and `minorVersion`. The concrete Checker-rejection response instead uses `cashflowBusinessVersion` and `cashflowMinorVersion`, and adds `stampingId`. Clients need an authoritative versioned schema or normalization layer before relying on either shape.

Because the complete message may contain sensitive settlement, party, and account data, logging, masking, retention, and access-control rules should be defined before using payload fixtures outside controlled environments.