---
type: concept
title: Split Cashflow Withdrawal Propagation
tags: [cashflow, splitting, withdrawal, cancellation, swift-suppression, uat]
related: [cashflow-splitting, ratan-fail-and-autofail-status-transitions, cashflow-pre-fail-state-restoration, murex-2-11-cashflow-suppression, what-is-the-authoritative-split-child-lifecycle-after-parent-withdrawal]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT/Cashflow Splitting UAT For ASPIRE.md"]
---
# Split Cashflow Withdrawal Propagation

Split cashflow withdrawal propagation concerns the treatment of child cashflows when their gross parent, or a parent entering a net-resultant auto-distribution flow, is subsequently withdrawn.

## Reported UAT coverage

The ASPIRE UAT record reports Pass for HK, TW, and TH scenarios involving:

- a manually split gross cashflow followed by a subsequent withdrawal and continued manual child release;
- automatic cancellation of a failed child after withdrawal;
- automatic cancellation of a SWIFT-suppressed child after withdrawal;
- withdrawal after netting and automatic distribution, together with SWIFT suppression.

For HK, the gross-withdrawal substeps explicitly expect accounting-information generation. The equivalent TW and TH withdrawal rows are marked Pass but leave several expected-result cells blank.

## Limits of the evidence

This source demonstrates that these scenarios were exercised, not an authoritative state-transition contract. It does not state:

- the exact withdrawal trigger and processing order;
- whether cancellation is limited to failed or SWIFT-suppressed children;
- the outcome for unreleased valid children or already released children;
- the final cancellation statuses;
- accounting-event cardinality, retry, or idempotency behavior.

The source uses `swift_suppress`, but does not name Murex 2.11. It must not be used to attribute this suppression behavior to [[murex-2-11-cashflow-suppression]].

See [[what-is-the-authoritative-split-child-lifecycle-after-parent-withdrawal]] for the missing lifecycle definition.