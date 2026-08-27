---
type: query
title: What Are the Authoritative Alphabetical Sorting Rules for Cashflow Blotter Filters and Views?
tags: [cashflow-blotter, sorting, custom-search, views, open-question]
related: [cashflow-blotter, alphabetical-custom-search-view-ordering, cashflow-blotter-filter-rationalization]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244022-Cashflow filter enhancement.md"]
---
# What Are the Authoritative Alphabetical Sorting Rules for Cashflow Blotter Filters and Views?

The source requires alphabetical ordering for Cashflow Blotter filters and views but does not define the sorting semantics or complete scope.

## Questions to resolve

1. Which locale and collation algorithm apply?
2. Is sorting case-sensitive?
3. How are numeric prefixes, punctuation, symbols, and blank names ordered?
4. Are standard filters, system views, shared views, and user-created views sorted separately or in one list?
5. Are duplicate display names permitted, and what tie-breaker is used?
6. Must ordering remain stable after views are created, renamed, edited, or shared?
7. Is the same sorting rule applied to filters and views?

A resolved specification is needed to make the alphabetical-ordering requirement deterministic and testable.