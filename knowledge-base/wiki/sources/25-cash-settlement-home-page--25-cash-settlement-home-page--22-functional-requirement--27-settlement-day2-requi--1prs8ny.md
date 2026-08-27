---
type: source
title: Accounting Enhancement — Prepare Nostro Account Info before Send
created: 2026-08-23
updated: 2026-08-23
tags: [functional-requirement, accounting, nostro, delayed-send, data-consistency]
related: [ratan-cash-settlement-accounting-service, held-accounting-request-nostro-regeneration, when-and-how-is-ebbsaccountnum-derived-for-held-accounting-tasks, does-nostro-refresh-regenerate-accounting-requests-for-netted-released-and-withdrawn-cashflows, what-is-the-atomicity-and-cutoff-contract-for-nostro-refresh-before-accounting-send, nostro-notification-and-refresh, settlement-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Accounting Enhancement — Prepare Nostro Account Info before Send

## Summary

This functional requirement addresses stale Nostro data in accounting information that is generated while an accounting task is in `HOLD` and sent later to an unspecified downstream system.

The confirmed requirement is that applicable held tasks must regenerate the Nostro-related portion of their accounting request before downstream dispatch when a Nostro refresh has occurred. The source does not require regeneration of unrelated request data.

The required service change is in [[ratan-cash-settlement-accounting-service]].

## Confirmed requirement

When accounting information was generated against an old Nostro account, and that Nostro account is refreshed before scheduled dispatch, all applicable tasks must regenerate their partial Nostro-related request information before they are sent downstream.

This is a pre-send outbound-payload freshness requirement. It does not establish that persisted cashflow Nostro identifiers, SWIFT fields, SSI data, or historical records must be rewritten.

## First scenario: fail and reinstate tasks

The source gives a lifecycle example in which `fail` and `reinstate` generate tasks in `HOLD` using the old Nostro, a Nostro refresh occurs, and later task generation uses the new Nostro. At the scheduled send time, the source requires regeneration of the Nostro-related partial request information for all applicable tasks before sending.

The source does not define whether repeated task references represent replacement tasks, distinct tasks, or consolidated work items. It also does not define deduplication or supersession behavior.

## `ebbsAccountNum`

The question asks when `ebbsAccountNum` is populated. The answer only specifies regeneration of partial request information related to Nostro before send.

The document does not explicitly establish whether `ebbsAccountNum` is within that regenerated subset, its precise derivation rule, its null or error handling, or whether it is populated both at task creation and at dispatch preparation. These uncertainties are tracked in [[when-and-how-is-ebbsaccountnum-derived-for-held-accounting-tasks]].

## Unanswered netting scenario

The source asks whether refreshed Nostro `nostro2` should be used when:

1. `c1 + c2` net to `c3`.
2. `c3` is released from `HOLD` using `nostro1`.
3. `c1` is withdrawn and released from `HOLD` using `nostro1`.
4. Nostro data is refreshed.
5. The scheduled date is reached.
6. `c3` and `c1` are sent.

No answer is provided. Therefore, this source does not establish the send or regeneration outcome for netted, released, or withdrawn cashflows. See [[does-nostro-refresh-regenerate-accounting-requests-for-netted-released-and-withdrawn-cashflows]].

## Scope boundary

This requirement extends [[nostro-notification-and-refresh]] for delayed accounting dispatch. It is related to, but not evidence for, [[nostro-stamping]], dedicated Nostro selection, RFI Nostro selection, SWIFT propagation, or MT210 behavior.