---
type: concept
title: Hot NSTP Rule Exception Reconciliation
created: 2026-08-24
updated: 2026-08-24
tags: [NSTP, exception-reconciliation, hot-rules, cash-settlement, workflow]
related: [nstp-rules, orchestration, razor-release-boundary-for-hot-rule-evaluation, rule-sync-idempotency-and-version-ordering, cashflow-release-and-netting-race-condition]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Hot NSTP Rule Exception Generation.md"]
---
# Hot NSTP Rule Exception Reconciliation

## Definition

Hot NSTP rule exception reconciliation is the process of applying a changed NSTP rule set to cashflows that have already entered workflow. It generates exceptions when a newly created or changed rule applies and reconciles exceptions when a rule is removed or no longer applies.

The source limits this behavior to cashflows that have not yet been released to Razor.

## Required Outcomes

- Newly applicable NSTP rules result in corresponding exceptions for eligible cashflows.
- Removed or no-longer-applicable NSTP rules result in corresponding exception removal or another defined terminal transition.
- Cashflows already released to Razor are excluded from this processing.
- Repeated or concurrent processing should not create duplicate exceptions or remove exceptions incorrectly.

The last requirement is an operational implication; the source does not prescribe an idempotency mechanism.

## Important Semantics to Define

A complete design must establish:

- The identity of an exception and its relationship to a cashflow and rule.
- Whether multiple rules can independently support one exception.
- Whether removal means physical deletion, cancellation, closure, or obsolescence.
- How manually modified or resolved exceptions are treated.
- The rule version or effective time used for reevaluation.
- How partial failures are retried and reconciled.
- How eligibility is protected when Razor release occurs concurrently.

This concept is related to, but distinct from, [[rule-sync-idempotency-and-version-ordering]] and [[cashflow-release-and-netting-race-condition]]. Those pages must not be treated as defining the NSTP implementation contract.