---
type: concept
title: Swift Suppression
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, swift, suppression, accounting, razor]
related: [ratan, razor, suppression-maker-checker-workflow, suppression-rule-management, cashflow-accounting-eligibility, cashflow-amendment-supersession, cashflow-status-lifecycle, cashflow-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Swift Suppression.md"]
---
# Swift Suppression

Swift Suppression transitions a cashflow to `SWIFT SUPPRESSED` after Checker approval. It prevents SWIFT generation but does not prevent accounting.

On value date, [[ratan]] sends `SWIFT SUPPRESSED` cashflows to [[razor]] by EOD. Razor bypasses SWIFT generation and produces accounting entries.

## Post-value-date lifecycle events

After value-date accounting EOD:

- Cancellation of a suppressed cashflow requires a Razor feed for reversal accounting.
- Amendment requires reversal accounting for the withdrawn original and a new accounting entry for the replacement cashflow.
- A replacement cashflow can remain `SWIFT SUPPRESSED`, or it can be `READY`; a `READY` replacement is shown as SWIFT eligible.

Swift Suppression is not explicitly equated with the document's earlier term “Payment Suppression.” See [[is-payment-suppression-the-same-as-swift-suppression]].