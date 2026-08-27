---
type: entity
title: Apollo Client
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, frontend, client-library, ratan]
related: [graphql, dgs, ratan, cash-settlement-query-service-graphql-read-model, is-graphql-defer-supported-end-to-end-in-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Proposal.md"]
---
# Apollo Client

Apollo Client is the frontend GraphQL client identified in the RATAN GraphQL proposal. The implementation version recorded by the source is `Apollo-Client@3.7.13`.

## Recorded Capabilities

The source lists support for:

- Queries.
- Mutations.
- Subscriptions.
- `@defer`.

The proposal does not provide the client configuration, cache policy, transport configuration, authorization integration, retry behavior, or subscription reconnection policy. It also does not establish whether `@defer` was used in production or only supported by the client library.

Project reference: [Apollo Client GitHub repository](https://github.com/apollographql/apollo-client)

Apollo Client is the client-side counterpart to [[entities/dgs]] in the proposed [[concepts/graphql-frontend-aggregation]] architecture.