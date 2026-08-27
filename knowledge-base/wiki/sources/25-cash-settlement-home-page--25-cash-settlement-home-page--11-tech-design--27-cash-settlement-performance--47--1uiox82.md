---
type: source
title: Cashflow Blotter Query Performance Optimization
authors: []
year: 2025
url: ""
venue: "Internal technical design"
tags: [cash-settlement, cashflow-blotter, query-performance, value-date, PostgreSQL]
related: [cashflow-blotter, postgresql, value-date-query-performance-guardrail, cashflow-blotter-query-optimization-options, what-is-the-approved-cashflow-blotter-value-date-search-policy, cash-settlement-cashflow-read-model, domain-owned-postgresql-schemas]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Query Performance Optimization.md"]
---
# Cashflow Blotter Query Performance Optimization

## Summary

This internal technical design proposes restricting broad [[cashflow-blotter]] searches by adding a value-date (`VD`) predicate. The stated rationale is that value date materially affects response time and that limiting the queried date range should reduce the search space.

The proposal applies primarily to searches that do not contain identifier-like criteria. For those searches, the UI should automatically add `VD = Today` when the user has not supplied a value date. A user-supplied range greater than one month should trigger a warning and prevent execution until the range is reduced. Users who remove an automatically added VD criterion should also receive a warning.

The document describes this as a performance proposal, but automatic VD insertion changes the result set and therefore has search-semantics implications in addition to query-planning implications.

## Evidence and Scope

The evidence covers the period from 2025-04-01 to the document’s creation date. The source includes an attached performance image, but it does not provide machine-readable latency values, query plans, row counts, index details, or workload distributions.

![Performance evidence](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--47--1uiox82/image-2025-6-5_17-26-19.png)

The proposal covers:

- Quick Search
- Advanced Search
- Quick Filter
- Temporary filters
- Saved filters
- Mixed criteria entered through multiple search interfaces

## Proposal

When a user searches for non-identifier cashflow data from the Cashflow Blotter, the UI should check whether the criteria contain a VD predicate. If not, it should add `VD = Today` as an additional criterion, described in the source as being added through Quick Filter behavior.

Identifier-driven searches should retain current production behavior. Examples include searches using Cashflow ID, Trade ID, Original Trade ID, or Netting ID.

The source states that a VD range within one month provides the best performance and recommends restricting the range to less than one month. The precise boundary is not defined: the document alternately describes a limit of “less than 1 month” and blocking ranges “more than 1 month.”

## Operating Principles

1. Searches containing identifier-like fields such as Cashflow ID, Trade ID, Original Trade ID, or Netting ID should behave as they do in production.
2. Searches initiated from Quick Search, Advanced Search, or Quick Filter that do not contain identifier-like fields should default to `value date = today` when the user has not set a value date.
3. A user-supplied value-date range greater than one month should display an alert and prevent the search from executing.
4. A user who manually removes the value-date criterion should receive a warning.

## Cases

| Category | User Actions | Final Triggered Search Criteria | Mockup Screenshot |
| --- | --- | --- | --- |
| Search criteria contains id like fields, e.g. cashflow id, trade id, original trade id, netting id, etc. | - User search cashflow id in quick search - User search trade id in custom search | - Cashflow.Cashflow_Id = "M01749108487" - Trade.Trade_Id = "xxx" | No Impact, same like before. |
| Search criteria contains non-id like fields. | User search Taxonomy and Booking Entities in quick search. | Taxonomy = "ForeignExchange:Forward" and Booking Entity = "SCB SHANGH*SHA" and VD = TODAY | ![image-2025-6-5_16-45-47.png](attachments/image-2025-6-5_16-45-47.png) |
| User search Taxonomy and Booking Entities with temporary filter in custom search. | Taxonomy = "ForeignExchange:Forward" and Booking Entity = "SCB SHANGH*SHA" and VD = TODAY | ![image-2025-6-5_16-52-51.png](attachments/image-2025-6-5_16-52-51.png) |
| User search Taxonomy and Booking Entities with saved filter in custom search. | Taxonomy = "ForeignExchange:Forward" and Booking Entity = "SCB SHANGH*SHA" and VD = TODAY | ![image-2025-6-5_16-56-5.png](attachments/image-2025-6-5_16-56-5.png) ![image-2025-6-5_16-56-32.png](attachments/image-2025-6-5_16-56-32.png) |
| User search Taxonomy and Booking Entities in quick filter. | Taxonomy = "ForeignExchange:Forward" and Booking Entity = "SCB SHANGH*SHA" and VD = TODAY | ![image-2025-6-5_16-58-15.png](attachments/image-2025-6-5_16-58-15.png) |
| Mixed search criteria contains non-id like fields. | User search Taxonomy in quick search and search Entities in quick filter. | Taxonomy = "ForeignExchange:Forward" and Booking Entity = "SCB SHANGH*SHA" and VD = TODAY | ![image-2025-6-5_17-1-22.png](attachments/image-2025-6-5_17-1-22.png) |
| Cancel VD criteria manually | User can manually remove VD criteria after auto set up. | Taxonomy = "ForeignExchange:Forward" and Booking Entity = "SCB SHANGH*SHA" | ![image-2025-6-16_11-0-23.png](attachments/image-2025-6-16_11-0-23.png) |
| VD range more than 1 month | User search Taxonomy, Entities in quick search. Set VD range from "2025-06-01" to "2025-07-02". | NOT SEARCHED | ![image-2025-6-16_11-2-28.png](attachments/image-2025-6-16_11-2-28.png) |
| User in Advanced Search. Set VD range from "2025-06-01" to "2025-07-02". | NOT SEARCHED | ![image-2025-6-19_22-43-11.png](attachments/image-2025-6-19_22-43-11.png) |

## Proposal B: PostgreSQL Query Hints

The source proposes investigating the `pg_hint_plan` PostgreSQL extension as an alternative or complementary database-level optimization. The referenced project is:

[pg_hint_plan](https://github.com/ossc-db/pg_hint_plan)

![pg_hint_plan example](attachments/1.png)

The source does not establish that `pg_hint_plan` is approved or selected. It provides no compatibility assessment, benchmark, operational-risk analysis, or comparison with indexes, query rewrites, partitioning, statistics improvements, or read-model changes.

## Limitations and Unresolved Points

- The correct value-date boundary is unclear: strictly less than one month versus up to one month.
- “One month” is not defined as a calendar interval or a fixed number of days.
- The source does not state whether broad searches can be overridden for historical, reconciliation, audit, or operational use cases.
- The complete list of identifier-like fields is undefined.
- The behavior of mixed identifier and non-identifier searches is not specified.
- The source describes UI controls but does not establish backend enforcement.
- No latency, throughput, query-plan, result-count, timeout, or database-load acceptance criteria are provided.
- No rollout, monitoring, user-communication, or rollback plan is included.

## Related Wiki Pages

The proposal extends the broader [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--aw6os5]] performance work and concerns the [[entities/cashflow-blotter]] and [[entities/postgresql]]. It may also affect the [[concepts/cash-settlement-cashflow-read-model]] and [[concepts/domain-owned-postgresql-schemas]].