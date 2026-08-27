---
type: query
title: What Is the Authoritative EBBS Accounting-Feed State Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [ebbs, accounting-feed, state-machine, swift, cash-settlement]
related: [ebbs, ratanone, swift-reinstatement-and-unsuppression, accounting-feed-withdrawal-as-reversal, what-are-the-authoritative-accounting-feed-task-state-transitions, are-aspire-and-ebbs-distinct-accounting-targets-or-names-for-one-feed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design.md"]
---
# What Is the Authoritative EBBS Accounting-Feed State Machine?

The Swift generation design names `FAILED` and `SWIFT_SUPPRESSED` as preceding statuses for distinct reversal-related actions, but contains no actual status-machine definition despite having a “Status Machine” section.

## Evidence currently available

- `FAILED` leads to a reinstatement action with `reversal flag = reinstate`.
- `SWIFT_SUPPRESSED` leads to approval after unsuppression with `reversal flag = SwiftUnSuppressed`.
- Publishing is controlled by value-date eligibility and validation retry behaviour.

## Questions to resolve

- What are all EBBS accounting-feed states and permitted transitions?
- Are `FAILED` and `SWIFT_SUPPRESSED` mutually exclusive lifecycle states?
- What state records retry exhaustion?
- How do feed publication status, reversal status, and accounting-task status relate?
- Can a reversal action be reversed or reinstated again?
- What keys correlate the original New feed with its withdrawal reversal?

This query should be resolved with the authoritative lifecycle specification and reconciled with [[what-are-the-authoritative-accounting-feed-task-state-transitions]]. It must not assume that EBBS and Aspire are the same target; that identity question is tracked separately in [[are-aspire-and-ebbs-distinct-accounting-targets-or-names-for-one-feed]].