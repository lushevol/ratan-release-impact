---
type: query
title: What Is the Authoritative RATAN Dashboard Status Catalogue and Overlap Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, dashboard, status-catalogue, counting, open-question]
related: [ratan-cashflow-dashboard, dashboard-cashflow-status-counting, grouped-cashflow-monitoring, aspire-accounting-status-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/RATAN Cashflow Dashboard.md"]
---
# What Is the Authoritative RATAN Dashboard Status Catalogue and Overlap Rule?

The dashboard predicates use `WAITING`, `FAILED`, `Error`, `PENDING`, and `ERROR`, as well as specified Accounting Status and Swift Status values. The source does not identify an authoritative field catalogue, case-matching rule, or counter-overlap policy.

## Questions

- What are the authoritative valid values for Cashflow State, Accounting Status, Swift Status, and Group State?
- Is `Error` an exact valid Cashflow State, and is matching case-sensitive?
- Are Accounting Error and Swift Error status lists exhaustive?
- Can a cashflow contribute to multiple banners?
- Are dashboard counts independent, mutually exclusive, or deduplicated?
- What drill-down behaviour applies when populations overlap?

Do not infer that the Accounting Status values belong to the Aspire lifecycle in [[aspire-accounting-status-lifecycle]] without evidence identifying Aspire as the source.