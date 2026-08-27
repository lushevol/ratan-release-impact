---
type: source
title: "Cash Settlement Home Page — Tech Design — 2026 Design — Auto Release Process"
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-release, RATAN, SWIFT, netting, concurrency]
related: [ratan, lifecycle-service, netting-service, razor, auto-release, payment-release-concurrency-control, last-mile-payment-release-control, cashflow-netting-renetting, auto-netting-rule-check, auto-netting-persistence-model, event-driven-component-cashflow-status-management, resultant-cashflow-status-consistency, is-minor-version-validation-enforced-at-every-ratan-status-transition, what-was-the-complete-root-cause-of-the-2026-double-netting-incident]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Auto Release Process.md"]
---
# Cash Settlement Home Page — Auto Release Process

## Summary

This technical-design document addresses the 2026 design for automatic payment release in RATAN. It proposes simplifying the actions available on `READY` cashflows, removing an unspecified tactical control once a strategic solution is available, and introducing a final control before payments leave RATAN for the SWIFT network.

The proposed design uses multiple controls rather than relying on a single lock. These controls include current-status validation, cache-based locking, business-version and minor-version validation, workflow publication gates, SWIFT-service duplicate detection, Message Bridge tracking-ID deduplication, cashflow-group validation, and final payment-amount reconciliation.

The document also records a production netting incident involving 357 component cashflows and two resultants, `N00000267689` and `N00000266337`. The stated root causes include allowing `Net` from `NETTED`, removal of minor-version validation from the status-movement API, and an incomplete third item recorded as `Lock space`.

## Design Context

The document identifies three intended directions:

1. Simplify the process by removing redundant actions from `READY` payments.
2. Remove an unspecified tactical control because the strategic solution is expected to resolve the underlying problem.
3. Add a last-mile control, tracked under Market Efficiency, before sending payment from RATAN to the SWIFT network. The control should include internal reconciliation of payment amounts and prevent duplicate or incorrect payments.

These directions are proposals and should not be treated as approved or deployed decisions without corroborating evidence.

## Release-State Requirements

The 21 January 2026 discussion identifies two publication gates:

- Workflow should publish a cashflow to the SWIFT service only after confirming that its current state is `READY + NA + NA`.
- The SWIFT service should generate SWIFT only after confirming that its current state is `READY + NA + PendingAck`.

The intended future direction is synchronized release processing to reduce races between status write-back and SWIFT generation. The document does not confirm that this design has been implemented or enabled in production.

## Actions Allowed Post Pending Release

| | Source Cashflow Status | Source Cashflow SubStatus | Source Cashflow SubStatusType | Action | Target Cashflow Status | Target Cashflow SubStatus | Target Cashflow SubStatusType | OPS operation? | System job? | Control? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | READY | NA | NA | IsNstpChecker | WAITING | PendingVerification | PendingException | | No | , Status Machine Control |
| 2 | READY | NA | NA | IsNstp | WAITING | PendingOperator | PendingException | | No | , Status Machine Control |
| 3 | READY | NA | NA | SentToRazor | READY | NA | PendingAck | No | Yes, Specifically for LOANIQ now | , Release job as expected |
| 4 | READY | NA | NA | GenerateSwift | READY | NA | PendingAck | No | Yes, Withdrawal | , Release job as expected |
| 5 | READY | NA | NA | AutoSplitFail | READY | NA | PendingException | No | Yes | , Release job triggered exception |
| 6 | READY | NA | NA | EarlyRelease | READY | NA | NA | | No | , Status Machine Control |
| 7 | READY | NA | NA | UnNet | DEAD | NA | NA | | Yes, Withdrawal component | , Status Machine Control |
| 8 | READY | NA | NA | UnSplit | DEAD | NA | NA | | Yes, Withdrawal component | , Status Machine Control |
| 9 | READY | NA | NA | ReSplit | DEAD | NA | NA | | | |
| 10 | READY | NA | NA | Hold | HOLD | PendingVerification | NA | | No | , Status Machine Control |
| 11 | READY | NA | NA | ManualSwiftSuppress | WAITING | PendingVerification | SwiftSuppression | | No | , Status Machine Control |
| 12 | READY | NA | NA | Fail | WAITING | PendingVerification | PendingManualFail | | No | , Status Machine Control |
| 13 | READY | NA | NA | Withdrawal | CANCELLED | NA | NA | No | Yes, Withdrawal | , Status Machine Control |
| 14 | READY | NA | NA | FullUtilize | UTILIZED | NA | NA | | No | , Status Machine Control, No Payment generated |
| 15 | READY | NA | NA | PartialUtilize | PARTIALLY_UTILIZED | NA | NA | | No | , Status Machine Control, No Payment generated |
| 16 | READY | NA | NA | AutoUtilize | UTILIZED | NA | NA | No | Yes | , Release job won't take it UTIL payments |
| 17 | READY | NA | NA | Pastdue | PASTDUE | NA | NA | No | Yes | , Release job won't take it UTIL payments |
| 18 | READY | NA | NA | TechFail | QUEUED | NA | PendingException | No | Yes | , Status Machine Control |
| 19 | READY | NA | NA | Net | NETTED | NA | NA | | No | Added by Jan 2026, Only allowed 10 mins before cutoff |
| 20 | READY | NA | NA | RevertToQueued | QUEUED | NA | NA | No | Yes | , Status Machine Control |
| 21 | READY | NA | NA | Split | SPLIT | NA | NA | | Yes | Added by Jan 2026, Only allowed 10 mins before cutoff |
| 22 | READY | NA | NA | AutoFail | FAILED | NA | NA | No | Yes | , Status Machine Control and it won't happen |
| 23 | READY | NA | NA | ManualSuppress | WAITING | PendingVerification | CashflowSuppression | | No | , Status Machine Control |
| 24 | READY | NA | NA | New | QUEUED | NA | NA | No | Yes, Undo | |
| 25 | READY | NA | PendingException | Fail | WAITING | PendingVerification | PendingManualFail | | No | , Status Machine Control |
| 26 | READY | NA | PendingException | AutoFail | FAILED | NA | NA | No | Yes | , Status Machine Control |
| 27 | READY | NA | PendingAck | Release | RELEASED | NA | NA | No | Yes | , Release job as expected on swift generation |
| 28 | READY | NA | PendingAck | SwiftUpdate | READY | NA | PendingAck | No | Yes | , Release job as expected on swift generation |
| 29 | READY | NA | PendingAck | Settle | SETTLED | NA | NA | No | Yes | , Release job as expected on swift generation |
| 30 | READY | NA | PendingAck | ResendToRazor | READY | NA | PendingAck | | No | , Edge case, SWIFT do duplication check |
| 31 | READY | NA | PendingAck | ReGenerateSwift | READY | NA | PendingAck | | No | , Edge case, SWIFT do duplication check |
| 32 | READY | NA | PendingAck | Withdrawal | QUEUED | NA | NA | No | Yes, Withdrawal | , Worst case Status wrongly updated without SWIFT generation. Worth to assess making release job a sync flow. C1, 1, N, READY, Pending Ack → No SWIFT generation as Status write back failure C1, 2, W, QUEUED → WAITING (Reversal) → Expected to be CANCELLED, and the payment nothing can be done but only SUPPRESSED |
| 33 | READY | NA | PendingAck | TechFail | QUEUED | NA | PendingException | No | No | , Defined but redundant transaction |
| 34 | READY | NA | PendingAck | Fail | WAITING | PendingVerification | PendingManualFail | | No | , Status Machine Control |
| 35 | READY | NA | PendingAck | AutoFail | FAILED | NA | NA | No | Yes | , Status Machine Control, only happen when SWIFT generation failure, no concurrency issue |
| 36 | READY | NA | PendingAck | New | QUEUED | NA | NA | No | Yes, Undo | |

## System Process Interaction Matrix

| Jobs | | Auto release (every 30 mins) | Auto Fail (21:00 GMT) | Auto Materialize (2:00 GMT) | SSI Refresh (adhoc) | Trade Confirmation (adhoc) |
| --- | --- | --- | --- | --- | --- | --- |
| | Scope | READY+NA+NA → Pending Ack | PROJECTED/QUEUED/WAITING/READY→ FAILED | PROJECTED→ WAITING | WAITING ↔ READY | WAITING → (READY) |
| Auto release (every 30 mins) | READY+NA+NA → Pending Ack | - | Yes, but workflow/Swift service control could resolve it Going forward to make job synchronized | NO | Yes, but workflow/Swift service control could resolve it Going forward to make job synchronized | NO |
| Auto Fail (21:00 GMT) | PROJECTED/QUEUED/WAITING/READY→ FAILED | | - | NO | NO | NO |
| Auto Materialize (2:00 GMT) | PROJECTED→ WAITING | - | - | - | NO | NO |
| SSI Refresh (adhoc) | WAITING ↔ READY | - | - | - | - | ?? |
| Trade Confirmation (adhoc) | WAITING → (READY) | - | - | - | - | - |
| User actions | Scope | | | | | |
| Net/Unnet | QUEUED/WAITING/READY → NETTED | Yes, but current control by 10 mins Going forward to make job synchronized | ?? rare | NO | NO | NO |
| Split/Unsplit | QUEUED/WAITING/READY → SPLIT | ?? rare | NO | NO | ?? |
| ManualSuppress/UnSuppress/Approve | PROJECTED/QUEUED/WAITING/READY/FAILED → CASHFLOW_SUPPRESSED | NO | NO | May break the manual action | NO |
| Submit/Approve/Reject | WAITING → READY | NO | NO | NO | May break the manual action | ?? Potential conflict that user submit and confirmation came |
| Adhoc SSI | READY → WAITING | NO | NO | ?? | NO | NO |
| SettleAsGross | WAITING | NO | NO | NO | NO | NO |
| Comment | Any | NO | NO | NO | NO | NO |
| Manual Fail/Approve | PROJECTED/QUEUED/WAITING/READY/HOLD → FAILED | ?? | NO | NO | May break the manual action | NO |

## Concurrency and Duplication Controls

The design describes the following defence-in-depth controls:

- Cache-based locks to block concurrent OPS and system operations on the same cashflow.
- Current-status validation after an operation, protecting against stale blotter or UI state.
- Camunda cache-level filtering using cashflow ID, business version, and minor version.
- Message Bridge tracking-ID checks to prevent repeated consumption or publication.
- SWIFT-service duplicate detection using cashflow ID and business version.
- Database completion marking by the auto-release job to prevent another scan from processing the same item.
- Cashflow-group controls that block additional upstream cashflows as `ERROR` and alert OPS/PSS.
- Non-economic amendment detection.
- NSTP treatment for post-payment-release reversal and rebook to avoid duplicate payments.
- Trade validation before a cashflow appears in the cashflow blotter.

The document does not establish whether every listed control is currently deployed, atomically enforced, or independently tested.

## Production Netting Incident

The incident involved netting over 357 component cashflows and generated two resultants: `N00000267689` and `N00000266337`.

| Time | Actor | Event |
|---|---|---|
| 02:07:39 | user1 | Triggered netting call; lifecycle check cashflow status |
| 02:07:43 | user1 | Lock acquired by Netting Service |
| 02:07:44 | user2 | Triggered netting call; lifecycle check cashflow status |
| 02:07:49 | user1 | Net completion; lock released (`N00000266337`) |
| 02:07:52 | user2 | Lock acquired by Netting Service |
| 02:07:58 | user2 | Net completion; `N00000267689` and `N00000266337`; `N00000266337` netting ID lost component cashflows |

The stated root causes are:

1. `NETTED` status allowed the `Net` action, which in a specific context permitted a wrong or duplicate action.
2. The status-movement API no longer validated minor version.
3. `Lock space`.

The third item is incomplete in the source and must not be interpreted without the original incident record.

## Implications and Open Questions

The incident demonstrates that locking serializes access but does not guarantee semantic correctness. A second process must revalidate current status and version after acquiring the lock and before committing a transition.

The source leaves open whether `Net` should remain available from `NETTED`, whether minor-version validation is enforced at every relevant layer, what the tactical control is, whether synchronized release is implemented, and what checks belong in the final last-mile gate.

See [[is-minor-version-validation-enforced-at-every-ratan-status-transition]] and [[what-was-the-complete-root-cause-of-the-2026-double-netting-incident]].