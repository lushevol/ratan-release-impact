---
type: query
title: What Is the Approved Cashflow Blotter Value-Date Search Policy?
tags: [cash-settlement, cashflow-blotter, open-question, value-date, query-performance]
related: [cashflow-blotter, value-date-query-performance-guardrail, cashflow-blotter-query-optimization-options, pg-hint-plan, cash-settlement-cashflow-read-model]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Query Performance Optimization.md"]
---
# What Is the Approved Cashflow Blotter Value-Date Search Policy?

The Cashflow Blotter performance proposal recommends automatically adding `VD = Today` to searches without identifier-like criteria and blocking value-date ranges greater than one month. The approved policy remains unresolved because the source does not define the exact boundary, exceptions, enforcement layer, or evidence threshold.

## Questions to Resolve

- Is the permitted range strictly less than one month, or is a range of exactly one month allowed?
- Does “one month” mean a calendar month or a fixed 30-day period?
- Which fields qualify as identifier-like?
- How should searches combining identifier and non-identifier fields be handled?
- Can users override the guardrail for historical, reconciliation, audit, or operational workflows?
- Must the rule be enforced by backend APIs as well as the UI?
- Which business timezone determines `VD = Today`?
- What behavior applies to existing saved filters that return more than one month of data?
- What benchmark supports the chosen threshold?
- What are the rollout, monitoring, communication, and rollback requirements?

## Evidence Needed

Approval should be based on measurements that include latency percentiles, query plans, result counts, database resource use, timeout and error rates, and the impact on legitimate broad searches. The effect of adding VD should be evaluated separately from planner-level alternatives such as `pg_hint_plan`.

Until these points are resolved, [[value-date-query-performance-guardrail]] should be treated as a proposed policy rather than an implemented or approved contract.