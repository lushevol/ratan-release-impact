---
type: concept
title: Cash Settlement Schema Alignment
created: 2026-08-24
updated: 2026-08-24
tags: [schema, graphql, protobuf, opensearch, cash-settlement]
related: [opensearch, opensearch-business-live, ratanone, cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md"]
---
# Cash Settlement Schema Alignment

## Definition

Cash Settlement schema alignment is the process of defining consistent relationships among the protobuf data contract, the GraphQL query contract, and the OpenSearch index schema.

The source names these surfaces as:

```text
RatanCashSettlementData.proto
ResultNew GraphQL schema
OpenSearch schema definition
```

## Persistence and query models

The design explicitly distinguishes the persistence model from the query model. An OpenSearch document should not automatically be treated as the public GraphQL representation.

Each field and query domain should be classified according to:

- Authoritative owner.
- Persistence location.
- Indexing and denormalization rules.
- Query-time domain-service enrichment.
- Null and missing-value semantics.
- Versioning and compatibility requirements.
- Authorization and data-entitlement behavior.

## Scope

The current query surface includes cashflow, cashflow history, exceptions, SSI stashing, SSI candidates, affirmation details, and netting components. The source does not yet determine which of these are indexed in OpenSearch and which remain served by domain services.
