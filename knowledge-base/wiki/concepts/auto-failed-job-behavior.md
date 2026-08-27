---
type: concept
title: Auto-Failed Job Behavior
created: 2026-08-22
updated: 2026-08-22
tags: [autofail, auto-jobs, cashflow-lifecycle, regression-testing]
related: [cashflow-fail-and-reinstatement, regression-failure-triage, uber-regression-testing, ratan-one]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/UBER regression - round 2.md"]
---
# Auto-Failed Job Behavior

## Definition

Auto-failed job behavior is the automated handling of cashflows that cannot proceed through a job, with the audit action recorded as `AutoFail` rather than `Fail`.

## Regression evidence

The auto-jobs package contained seven cases and reported failures improving from six to two. The primary issue was that scripts searched for the former `Fail` action while the implementation recorded `AutoFail`. The source also states that transactional behavior for the job was still to be finalized.

Bug `11222354`, titled `Uber Auto Failed Job Error while handling cashflows`, was raised for the behavior.

## Testing implication

Regression scripts must assert the canonical action name and verify:

- The cashflow state after automatic failure
- The audit-trail action and actor fields
- Transactional behavior when one or more cashflows fail
- Reinstatement behavior, if supported
- Idempotency and repeat-job behavior

The source does not establish whether `AutoFail` is the final canonical action across every workflow. This should be confirmed before updating all related tests.