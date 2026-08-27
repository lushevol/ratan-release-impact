---
type: query
title: Is GraphQL Defer Supported End to End in RATAN?
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, defer, apollo-client, dgs, ratan, open-question]
related: [apollo-client, dgs, graphql-frontend-aggregation, cashflow-notification-and-auto-refresh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Proposal.md"]
---
# Is GraphQL Defer Supported End to End in RATAN?

The implementation table lists `@defer` as a supported Apollo Client feature, while the DGS server entry lists queries, mutations, and subscriptions but does not list `@defer`.

The source does not state whether deferred fields were deployed, whether the selected DGS version supports the required response protocol, or which transport the frontend uses. Client-library support alone does not establish end-to-end availability.

## Evidence Needed

- The deployed GraphQL server schema and DGS configuration.
- Apollo Client transport configuration.
- A production or test request using `@defer`.
- Incremental-response handling in the frontend.
- Compatibility and rollout details for `DGS@4.9.24`.
