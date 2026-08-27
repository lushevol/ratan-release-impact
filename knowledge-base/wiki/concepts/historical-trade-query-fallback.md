---
type: concept
title: Historical Trade Query Fallback
tags: [ssi-stamping, trade-data, fallback, historical-query]
related: [graphql-trade-snapshot-retrieval, ratan-ssi-stamping, what-triggers-historical-trade-query-fallback-for-ssi-stamping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade Strategic SSI Stamping Tech Design.md"]
---
# Historical Trade Query Fallback

The SSI-stamping design distinguishes a historical-query fallback from the normal GraphQL retrieval path.

The normal path requests a field-limited GraphQL projection. By contrast, the historical fallback queries all trade fields.

## Unspecified behavior

The source does not define:

- the condition that triggers fallback;
- whether fallback is automatic or manually initiated;
- the historical data source or interface;
- trade major- and minor-version selection semantics;
- schema equivalence with the GraphQL response;
- payload, latency, retry, or failure behavior.

These unresolved operational details are tracked in [[what-triggers-historical-trade-query-fallback-for-ssi-stamping]].