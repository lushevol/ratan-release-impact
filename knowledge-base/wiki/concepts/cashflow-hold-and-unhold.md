---
type: concept
title: Cashflow HOLD and UNHOLD
tags: [cashflow, hold, unhold, ratan, lifecycle, versioning]
related: [ratan, cashflow-hold-unhold-authorization, cashflow-event-versioning, cashflow-withdrawal-and-new, failed-cashflow-status, cashflow-split-and-unsplit, cashflow-suppression, swift-suppression, what-actions-are-authoritatively-permitted-while-a-cashflow-is-on-hold, what-is-the-authoritative-hold-unhold-status-restoration-and-eligibility-matrix]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Hold UnHold.md"]
---
# Cashflow HOLD and UNHOLD

In the Ratan functional requirement, HOLD is a user-initiated cashflow lifecycle control used before cashflow cutoff when settlement users need to investigate or supplement trade or cashflow information.

## HOLD state

HOLD creates a new cashflow version with:

- Main status: `HOLD`
- Sub-status type: `Cashflow Hold`
- Sub-status: `Pending Verification`

The source uses both `HOLD` and “ON HOLD”; `HOLD` is the literal used in its transition examples. A mandatory comment is required when applying HOLD.

The requirement says HOLD is eligible from any state except `RELEASED`, `NET`, or `SPLIT`, but only enumerates a partial set of source states. The authoritative eligibility model remains open in [[what-is-the-authoritative-hold-unhold-status-restoration-and-eligibility-matrix]].

## UNHOLD restoration

UNHOLD creates a further cashflow version and restores the exact pre-HOLD status and sub-status values, rather than routing all cashflows to a common state. Examples include restoration to `QUEUED`, `WAITING / Pending Another Leg / Pending Verification`, `WAITING / Pending Netting / Pending Verification`, and `READY`.

UNHOLD also requires a mandatory comment. Its authorization controls are documented in [[cashflow-hold-unhold-authorization]].

## Lifecycle interactions

- A trade amendment cancels or withdraws the held predecessor and retains HOLD on the new cashflow reference/version.
- A trade withdrawal makes the held New event inactive and progresses the withdrawal event to `CANCELLED`.
- If the value date has passed and the cashflow becomes `FAILED`, UNHOLD is disabled and subsequent processing belongs to the fail process described in [[failed-cashflow-status]].
- The source proposes that a held split parent cannot be un-split until HOLD is removed, but labels this rule “to do in 2024”; it is not evidence of a delivered control.

## Processing effects and unresolved scope

The requirement says HOLD stops materialization, exception checking, and SSI stamping. However, it separately lists Adhoc SSI, Netting, Un-Net, [[swift-suppression]], and [[cashflow-suppression]] as available from HOLD. This should not be interpreted as a complete or internally consistent state machine; see [[what-actions-are-authoritatively-permitted-while-a-cashflow-is-on-hold]].

## Bulk operations

Bulk HOLD and bulk UNHOLD are required capabilities. The source's examples establish the intended support but contain malformed row data. Each item in a bulk UNHOLD operation should therefore be treated as requiring its own restoration, segregation-of-duties, and authorization-limit validation pending clarification.