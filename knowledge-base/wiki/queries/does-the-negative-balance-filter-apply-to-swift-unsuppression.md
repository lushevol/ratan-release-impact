---
type: query
title: Does the Negative-Balance Filter Apply to Swift Unsuppression?
created: 2026-08-24
updated: 2026-08-24
tags: [swift, unsuppression, reinstatement, reversal, accounting-feed]
related: [swift-reinstatement-and-unsuppression, ebbs, ratanone, what-is-the-authoritative-ebbs-accounting-feed-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design.md"]
---
# Does the Negative-Balance Filter Apply to Swift Unsuppression?

The documented filter is:

```text
reversal flag = reinstate
AND last published balance < 0
```

The same design distinguishes `reinstate` from `SwiftUnSuppressed`:

- `FAILED` → `reinstate`
- `SWIFT_SUPPRESSED` → `SwiftUnSuppressed`

## Open question

Does `last published balance < 0` constrain only the `reinstate` path, as the literal filter indicates, or must it also be applied when an unsuppressed Swift item is approved with `reversal flag = SwiftUnSuppressed`?

Resolution requires the detailed selection logic, test cases for both paths, and the authoritative EBBS accounting-feed state machine. Until then, the negative-balance condition should not be generalized to Swift unsuppression.