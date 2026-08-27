---
type: query
title: What Is the Authoritative PRE_ADHOC_ERROR and ADHOC_SSI_EXCEPTION State Model?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, ssi, exception-lifecycle, state-model, auto-stamping]
related: [pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--17g3zt, nostro-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping/Cashflow Auto Stamping.md"]
---
# What Is the Authoritative PRE_ADHOC_ERROR and ADHOC_SSI_EXCEPTION State Model?

The source requires `PRE_ADHOC_ERROR` to close before `ADHOC_SSI_EXCEPTION` generation and to generate again after `ADHOC_SSI_EXCEPTION` closes. It does not define the underlying exception-state model.

## Questions

- Does “generate again” create a new `PRE_ADHOC_ERROR` record or reopen the prior record?
- Is `PRE_ADHOC_ERROR` regenerated unconditionally after `ADHOC_SSI_EXCEPTION` closure?
- Must the initial eligibility conditions be re-evaluated before regeneration?
- What events close each exception, and which component owns those transitions?
- Are repeated ad hoc SSI submit or reject actions idempotent?
- Do ad hoc SSI submit and reject actions create the same exception state and downstream outcome?

## Evidence

[[pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]] records the source's stated ordering but cannot resolve these transition semantics.