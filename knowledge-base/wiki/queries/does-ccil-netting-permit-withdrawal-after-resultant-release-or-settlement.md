---
type: query
title: Does CCIL Netting Permit Withdrawal After Resultant Release or Settlement?
created: 2026-08-23
updated: 2026-08-23
tags: [ccil, netting, withdrawal, resultant-cashflow, lifecycle]
related: [ccil-manual-netting, automatic-un-netting-on-trade-market-events, ccil]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/02 CCIL Netting.md"]
---
# Does CCIL Netting Permit Withdrawal After Resultant Release or Settlement?

## Open Question

What is the authoritative CCIL behavior when a component is withdrawn after its resultant reaches `RELEASED` or `SETTLED`?

## Evidence

The source specifies automatic un-netting for CCIL when withdrawal occurs before the resultant is `RELEASED` or `SETTLED`: the resultant becomes `DEAD`, the withdrawn component becomes `CANCELLED`, and unaffected components return to `Pending Netting`.

A separate row describes withdrawal after release or settlement, but it invokes generic **Net Selected Cashflow** and explicitly expects payment type `Bilateral Netting`, not `CCIL Netting`. Its final state is incomplete because it does not state the outcome for one component.

## Needed Resolution

Confirm whether the Bilateral scenario was included accidentally, whether a separate CCIL post-release/post-settlement contract exists, and whether component withdrawal should be permitted at that lifecycle stage.