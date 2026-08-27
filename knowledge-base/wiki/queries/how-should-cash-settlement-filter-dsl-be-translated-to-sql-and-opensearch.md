---
type: query
title: How Should Cash Settlement Filter DSL Be Translated to SQL and OpenSearch?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-dsl, sql, opensearch, graphql]
related: [cash-settlement-advanced-query-dsl, nested-boolean-filtering, cashflow-ultra-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# How Should Cash Settlement Filter DSL Be Translated to SQL and OpenSearch?

The design intends to align its GraphQL filter tree with OpenSearch and illustrates SQL equivalents, but it does not define a canonical translation.

The complex example translates `NOTIN` as SQL `in (...)` and ends with `and ()`, indicating that the documented mapping is incomplete or erroneous.

Define and test:

- predicate and grouping translation rules;
- parentheses and precedence;
- field-name mapping;
- `NOTIN`, `IN`, and wildcard semantics;
- empty-group and empty-list handling;
- OpenSearch query equivalents;
- error reporting when a filter cannot be translated.

This work is necessary to substantiate the stated OpenSearch migration objective.