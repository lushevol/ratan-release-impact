---
type: source
title: Settlement Advanced Search Design
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7529554"
venue: "Cash Settlement Home Page Technical Design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, advanced-search, graphql, query-dsl, pagination]
related: [ratanone, graphql, cashflow-blotter, dashboard, cash-settlement-advanced-query-dsl, nested-boolean-filtering, cashflow-ultra-query, cashflow-ultra-query-count, flat-filter-builder-vs-nested-query-dsl, what-is-the-canonical-cash-settlement-query-dsl, how-should-cash-settlement-filter-dsl-be-translated-to-sql-and-opensearch, what-are-the-cash-settlement-query-value-and-operator-types, what-is-the-cash-settlement-query-pagination-and-sorting-contract, graphql-vs-restful-cashflow-querying]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# Settlement Advanced Search Design

This design proposes an advanced-search capability for cash settlement that replaces a flat, implicit-`AND` filter builder with nested Boolean groups. The stated business driver is the “Commodity or PM for UK payment” requirement, referenced as Azure DevOps work item `7529554`.

The design prioritizes preserving existing query scenarios, enabling `AND`/`OR`/group composition, and aligning the query model with OpenSearch for a future migration. It is implemented front to back through GraphQL; the UI stack is Redux-Toolkit and `graphql-codegen`.

## Proposed filter model

The central recursive GraphQL input is:

```graphql
input LogicFilter {
  and: [LogicFilter!]
  or: [LogicFilter!]
  filters: [FilterArg!]
}
```

`and` and `or` contain child logical filters. `filters` contains atomic `FilterArg` predicates. The source specifies a maximum nesting depth of three and a normalization rule: each `LogicFilter` object should contain exactly one of `and`, `or`, or `filters`.

The documented constraints additionally state that root-level `filters` have at most one item, nested `filters` have one or more items, and redundant one-child `and` or `or` groups should be flattened. The exact meaning of “first level” and the treatment of single-child groups need clarification; see [[what-is-the-canonical-cash-settlement-query-dsl]].

## Result-query contract

```graphql
type Query {
  cashflowUltraQuery(payload: RatanUltraQuery): UltraQueryResult!
}

input RatanUltraQuery {
  filters: LogicFilter!
  pagingOption: PagingOption!
  pageIndex: Int!
  itemsPerPage: Int!
  orderArgs: [QueryOrder!]!
  # placeholder
  cursor: String
}

input QueryOrder {
  orderField: String!
  orderType: QueryOrderType!
}

enum QueryOrderType {
  ASC
  DESC
}

enum PagingOption {
  CURSOR
  PAGE_INDEX
  NO_PAGINATION
}

type ResultCursorType {
  previous: String
  next: String
}

type UltraQueryResult {
  # totalHits
  totalResult: Int!
  # pageNo
  pageIndex: Int
  pageSize: Int!
  lastPage: Boolean!
  pagingCursors: ResultCursorType
  results: [ResultNew!]!
}
```

`PAGE_INDEX` pagination is the implemented scope. `CURSOR` and `NO_PAGINATION` are schema placeholders, not implemented features. Sorting is also a placeholder: the design says results default to created-time ordering and may later accept `orderArgs`, but it does not define direction, sortable fields, stability, null ordering, or validation.

## Count-query contract

```graphql
type Query {
  cashflowUltraQueryCount(payload: RatanUltraQueryCount): UltraQueryCountResult!
}

input RatanUltraQueryCount {
  filters: LogicFilter!
}

type UltraQueryCountResult {
  count: Int!
}
```

The source reports that the GraphQL count API performs better overall than the older normal-query API in Dashboard screenshots. No machine-readable latency measurements, workload details, dataset size, concurrency, cache state, or memory measurements are supplied. High-volume cashflow performance testing remains a stated TODO.

## Example request

```json
{
  "payload": {
    "filters": {
      "and": [
        {
          "filters": [
            {
              "field": "Cashflow.Payment_Date",
              "operator": "IN",
              "values": [
                "2025-01-24",
                "2025-03-17"
              ]
            },
            {
              "field": "Cashflow.Cashflow_State",
              "operator": "IN",
              "values": [
                "WAITING",
                "RELEASED",
                "SETTLED",
                "READY"
              ]
            }
          ]
        },
        {
          "or": [
            {
              "filters": [
                {
                  "field": "Cashflow.Is_Commodity",
                  "operator": "EQ",
                  "values": "true"
                },
                {
                  "field": "Instrument_Common.ISDA_Taxonomy",
                  "operator": "EQ",
                  "values": "Commodity:Metals:Precious:SpotFwd:Physical"
                }
              ]
            }
          ]
        }
      ]
    },
    "itemsPerPage": 1000,
    "orderArgs": [],
    "pageIndex": 0,
    "pagingOption": "PAGE_INDEX"
  }
}
```

## Design limitations and documentation issues

The intended OpenSearch compatibility is a migration objective, not a demonstrated mapping. `FilterArg` is referenced but not defined, leaving value types, coercion, null behavior, and operator-specific cardinality unspecified.

The source has internal inconsistencies. Its count-request example places both `and` and `or` in one `LogicFilter`, contrary to the one-role-per-node rule. A complex SQL example translates `NOTIN` as `in (...)` and terminates with `and ()`. These examples should not be considered an authoritative execution mapping without resolution through [[how-should-cash-settlement-filter-dsl-be-translated-to-sql-and-opensearch]].