---
type: query
title: Is GraphQL Candidate Query Performance Within SLA?
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, performance, candidate-ssi, latency, open-question]
related: [graphql-api-segment-performance-criteria, graphql-frontend-aggregation, cashflow-data-provider-query-performance, cashflow-query-connection-pool-capacity, ssi-stamping-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Proposal.md"]
---
# Is GraphQL Candidate Query Performance Within SLA?

The GraphQL proposal reports an average full-request latency of 393ms but a maximum candidate-query latency of 9.6 seconds. The source describes this maximum as potentially disastrous and suggests a 2-second timeout without confirming that the timeout was implemented.

The source also records the Vostro candidate REST operation at 990ms for a 3.9kB response. It is unclear whether the 9.6-second maximum measures a GraphQL aggregate request, an individual resolver, or an underlying candidate service.

## Evidence Needed

- Resolver-level latency traces for Vostro and Nostro candidate fields.
- Request volume, concurrency, and percentile measurements.
- Payload size and compression details.
- Timeout, retry, and fallback configuration.
- The user-visible behavior when candidate data is unavailable.
- Confirmation of the authoritative performance target.

This query should be resolved before treating the GraphQL aggregation as consistently meeting the proposal’s performance criteria.