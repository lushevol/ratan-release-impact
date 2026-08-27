---
type: concept
title: Value-Date Query Performance Guardrail
tags: [cash-settlement, cashflow-blotter, query-performance, value-date, search-guardrail]
related: [cashflow-blotter, postgresql, pg-hint-plan, cashflow-blotter-query-optimization-options, what-is-the-approved-cashflow-blotter-value-date-search-policy, timestamp-semantic-and-format-consistency]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Query Performance Optimization.md"]
---
# Value-Date Query Performance Guardrail

A value-date query performance guardrail limits broad Cashflow Blotter searches by requiring or automatically supplying a value-date (`VD`) criterion.

The proposal has two principal behaviors:

1. For searches without identifier-like criteria, automatically add `VD = Today` when the user has not supplied a value date.
2. Reject user-supplied VD ranges that exceed the permitted threshold, described in the source as one month.

The guardrail is intended to reduce database work, but the automatic predicate also changes which cashflows are returned. It is therefore both a performance control and a search-semantics policy.

## Applicability

The proposed rule applies to searches from:

- Quick Search
- Advanced Search
- Quick Filter
- Temporary filters
- Saved filters
- Mixed searches combining criteria from multiple interfaces

Searches containing identifier-like fields, such as Cashflow ID, Trade ID, Original Trade ID, or Netting ID, are intended to preserve existing production behavior.

## User Interaction

If the system automatically adds VD and the user removes it, the system should display a warning. If the selected range exceeds the permitted threshold, the system should display an alert and prevent execution.

The source does not define whether users may override the warning for historical, reconciliation, audit, or operational workflows.

## Enforcement Requirements

A robust implementation should define and consistently enforce:

- The complete set of identifier-like fields.
- The behavior of mixed identifier and non-identifier criteria.
- Whether “one month” means a calendar month or a fixed day count.
- Whether the boundary is strictly less than one month or less than or equal to one month.
- The timezone used to calculate `Today`.
- Equivalent validation in backend APIs, not only in the UI.
- Telemetry for latency, result counts, rejected searches, timeouts, and user overrides.

## Evidence Status

The source reports that limited VD improves response time, but it provides no quantitative benchmark, query plan, index analysis, or acceptance threshold. The one-month limit should therefore be treated as a hypothesis requiring validation rather than as an established performance fact.

This concept should be resolved through [[what-is-the-approved-cashflow-blotter-value-date-search-policy]] and evaluated alongside [[cashflow-blotter-query-optimization-options]].