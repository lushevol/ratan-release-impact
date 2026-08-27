---
type: concept
title: GraphQL Partial Failure and Path Retry
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, error-handling, retry, frontend, cashflow]
related: [graphql-frontend-aggregation, cashflow-query-response-null-semantics, cash-settlement-exception-handling, cash-settlement-dependent-service-failure, ratan-query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Proposal.md"]
---
# GraphQL Partial Failure and Path Retry

GraphQL partial failure and path retry is the proposed behavior for a request in which one or more field resolvers fail while other fields succeed.

## Proposed Behavior

The source proposes that:

1. The response retains the expected key or field path.
2. A failed field is returned with an “empty value.”
3. The user interface can continue to process the expected response structure.
4. A retry resends only the failed paths instead of refetching the complete request.

This approach limits the cost of recovery and avoids repeating successful backend work.

## Contract Gap

“Empty value” is not sufficiently precise for an interoperable GraphQL contract. The implementation should define whether the value is:

- `null`;
- an empty list;
- an empty object;
- an omitted field;
- a custom error representation; or
- a value accompanied by a standard GraphQL `errors` entry and field `path`.

The contract should also define retry limits, backoff, timeout ownership, error classification, and the user-visible behavior when a retry remains unsuccessful. These questions connect directly to [[concepts/cashflow-query-response-null-semantics]].