---
type: query
title: What Is the Authoritative Cashflow Materialization Threshold?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, materialization, value-date, open-question]
related: [cashflow-materialization, cashflow-status-lifecycle, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md"]
---
# What Is the Authoritative Cashflow Materialization Threshold?

The Sprint 14 specification expects VD-7 cashflows to begin as `Projected` and to become `Queued` when materialization runs on VD-5. It also expects VD-5 and VD-4 imports to begin as `Queued`.

Open points:

- Does VD denote calendar days, business days, or a settlement-specific offset?
- Is VD-5 the universal threshold?
- What schedule and idempotency behaviour apply to the materialization job?
- Which attributes make a cashflow eligible for materialization?

The source is a functional expectation, not confirmation that the rule was implemented or executed.