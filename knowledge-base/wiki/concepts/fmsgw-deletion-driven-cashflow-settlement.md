---
type: concept
title: FMSGW Deletion-Driven Cashflow Settlement
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, settlement, swift, fmsgw, status-synchronization, ratan]
related: [ratan, fmsgw, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--198hh9i, what-is-the-authoritative-cov-swift-status-display-rule, what-is-the-post-settlement-fmsgw-status-correction-and-idempotency-contract, what-accounting-events-are-suppressed-by-using-settled-instead-of-swift-suppressed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow status sync with FMSGW deletion.md"]
---
# FMSGW Deletion-Driven Cashflow Settlement

This is a Ratan-specific operational lifecycle rule for synchronizing cashflow state with downstream SWIFT outcomes from [[fmsgw|FMSGW]].

## Status Allowlist

After a SWIFT message has been generated and sent downstream, Ratan must move the related cashflow from `RELEASED` to `SETTLED` when the received status is one of:

- `FMSGW Deleted`
- `FMSRE Deleted`
- `Manual Delete`
- `Released by SCPAY`
- `Released by AMH`

`SETTLED` is required instead of `SWIFT_SUPPRESSED` in this flow because the latter may cause duplicate accounting. This rule must not be generalized to unrelated Ratan status workflows without supporting evidence.

## COV Pair Completion

An MT103/202 COV cashflow requires a terminal status for both component messages. Ratan transitions to `SETTLED` only when each message's response belongs to the allowlist.

The two statuses do not need to be identical. For example, `FMSGW Deleted` paired with `Manual Delete`, or `Released by AMH` paired with `Released by SCPAY`, satisfies the rule.

When one component has an allowed deletion-related status and the other has an error response, the cashflow remains `RELEASED`.

## Display Status Versus Settlement Eligibility

`Check in FMSGW` is a diagnostic/display indication that the two COV message values differ. It does not determine eligibility on its own:

- Different values, both in the allowlist, permit `SETTLED`.
- An allowed value paired with an error does not permit settlement.

The requirement is ambiguous about whether identical deletion responses should also display `Check in FMSGW`; see [[what-is-the-authoritative-cov-swift-status-display-rule]].

## Boundaries

The requirement does not specify idempotency, response ordering, timeout behavior, later corrections, or whether `SETTLED` can be reversed. It also gives only a business rationale for avoiding `SWIFT_SUPPRESSED`, rather than an accounting-event specification.