---
type: entity
title: DGS
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, server-framework, backend, ratan]
related: [graphql, apollo-client, ratan, cash-settlement-query-service-graphql-read-model, is-graphql-defer-supported-end-to-end-in-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Proposal.md"]
---
# DGS

DGS is the server-side GraphQL framework identified in the RATAN GraphQL proposal. The recorded implementation version is `DGS@4.9.24`.

## Recorded Capabilities

The source lists support for:

- Queries.
- Mutations.
- Subscriptions.

The implementation details do not include resolver signatures, schema files, transport configuration, timeout values, authorization controls, query-complexity limits, or caching behavior. Although the client implementation lists `@defer`, the server capability list does not, so end-to-end deferred-response support remains an open question.

Project reference: [DGS GitHub repository](https://github.com/netflix/dgs-framework)

DGS is the server-side counterpart to [[entities/apollo-client]].