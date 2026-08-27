---
type: concept
title: Swift Reinstatement and Unsuppression
created: 2026-08-24
updated: 2026-08-24
tags: [swift, reversal, reinstatement, unsuppression, accounting-feed, cash-settlement]
related: [ratanone, ebbs, accounting-feed-withdrawal-as-reversal, what-is-the-authoritative-ebbs-accounting-feed-state-machine, does-the-negative-balance-filter-apply-to-swift-unsuppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design.md"]
---
# Swift Reinstatement and Unsuppression

Swift-related reversal actions are distinguished by the preceding status and their reversal flag in the RATANONE settlement-accounting design.

## Defined action paths

- A status change from `FAILED` results in a reinstatement action with `reversal flag = reinstate`.
- A status change from `SWIFT_SUPPRESSED` results in approval after unsuppression with `reversal flag = SwiftUnSuppressed`.

The two paths must not be treated as interchangeable solely because both concern reversal-related processing.

## Explicit balance filter

The documented filter is:

```text
reversal flag = reinstate
AND last published balance < 0
```

The source explicitly associates this condition with `reinstate`; it does not say that the same negative-balance condition applies to `SwiftUnSuppressed`. This ambiguity is tracked in [[does-the-negative-balance-filter-apply-to-swift-unsuppression]].

## Relationship to accounting reversals

This concept is a status-specific extension of [[accounting-feed-withdrawal-as-reversal]]. It does not define the complete accounting-feed state machine, the identity used to match original and reversal records, or whether a reversal can itself be reversed. Those lifecycle details remain open in [[what-is-the-authoritative-ebbs-accounting-feed-state-machine]].