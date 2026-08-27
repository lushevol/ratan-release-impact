---
type: query
title: How Does Settlement Advanced Search Map to OpenSearch or the Authoritative Query Backend?
tags: [advanced-search, query-backend, opensearch, query-translation, open-question]
related: [settlement-advanced-search, nested-boolean-advanced-search, opensearch, opensearch-backed-cashflow-querying, what-is-the-opensearch-index-schema-for-cashflow-querying]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design/Ratan Advanced Search Guide.md"]
---

# How Does Settlement Advanced Search Map to OpenSearch or the Authoritative Query Backend?

## Question

Which service executes Settlement Advanced Search queries, and how are nested groups, level-specific `AND`/`OR` combinators, duplicate fields, operators, and values translated into the authoritative query language?

## Evidence and boundary

The source describes UI and query-builder behavior only. It does not name [[opensearch]], another search engine, a query service, an index, field mappings, or a translation contract. Therefore, it must not be treated as evidence that Settlement Advanced Search uses [[opensearch-backed-cashflow-querying]].

## Information needed

The implementation documentation should identify:

- The authoritative query-execution service.
- The mapping from UI fields to backend fields.
- Operator-to-query translation.
- Grouping and Boolean nesting semantics.
- Maximum-depth enforcement.
- Duplicate-field handling.
- Authorization and data-entitlement enforcement.
- Query validation, failure behavior, and performance limits.

This question is related to [[what-is-the-canonical-advanced-search-filter-schema-and-query-semantics]], which covers the filter representation independently of the backend.