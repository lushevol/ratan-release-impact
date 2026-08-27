---
type: source
title: "UGANDA SCB UGANDA KAM(GBS) — Manual-Entity Settlement UAT"
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, settlement-day-2, manual-entity, UAT, Uganda, FMSGW]
related: [uganda-scb-uganda-kam-gbs, manual-entity-settlement-enablement, settlement-day-2, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, back-valued-message-queue, high-value-payment-queue, manual-cancellation-queue, duplicate-message-queue-processing, country-specific-settlement-uat-coverage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/006 UGANDA SCB UGANDA KAM(GBS).md"]
---

# UGANDA SCB UGANDA KAM(GBS) — Manual-Entity Settlement UAT

## Scope

This source records Settlement Day 2 user acceptance testing for enabling settlement for the manual entity `UGANDA SCB UGANDA KAM(GBS)`. The tested processing path involves [[entities/ratan]], [[entities/fmsgw]], and [[entities/amh]].

All recorded test cases are marked **Pass**. The supplied document contains screenshot attachment references, but the screenshot contents are not independently available in this summary.

## UAT results

| S.no | Squad | Type / Function | Test case / scenario | Expected result | Test result | Evidence |
|---:|---|---|---|---|---|---|
| 1 | FMSGW | Inbound Message | `MT103/202COV` settlement message received from `RATAN` and sent to `AMH`; an ACK message is sent back to `RATAN`. `MT202 COV` should be released after `MT103` receives a successful ACK. | `MT103/202COV` is sent to `AMH` and an ACK message is sent back to `RATAN`. | Pass | `attachments/image-2026-7-27_15-8-3.png`, `attachments/image-2026-7-10_14-52-1.png`, `attachments/image-2026-7-10_14-50-44.png`, `attachments/image-2026-7-10_14-51-8.png` |
| 2 | FMSGW | Inbound Message | `MT202` settlement message received from `RATAN` and sent to `AMH`; an ACK message is sent back to `RATAN`. | `MT202` is sent to `AMH` and an ACK message is sent back to `RATAN`. | Pass | `attachments/image-2026-7-8_13-35-47.png`, `attachments/image-2026-7-27_15-11-6.png`, `attachments/image-2026-7-8_13-34-56.png`, `attachments/image-2026-7-8_13-35-26.png` |
| 3 | FMSGW | Inbound Message | `MT192/292` settlement message received from `RATAN` and sent to `AMH`; an ACK message is sent back to `RATAN`. | `MT192/292` is sent to `AMH` and an ACK message is sent back to `RATAN`. | Pass | `attachments/image-2026-7-8_13-27-36.png`, `attachments/image-2026-7-8_13-29-56.png`, `attachments/image-2026-7-8_13-30-24.png`, `attachments/image-2026-7-8_13-31-5.png`, `attachments/image-2026-7-8_13-31-22.png`, `attachments/image-2026-7-8_13-33-53.png`, `attachments/image-2026-7-27_15-13-16.png` |
| 4 | FMSGW | Inbound Message | An `ANY` back-value-dated message received from `RATAN` is listed in the `Back Valued Messages Queue`. A processed ACK is sent to the inbound system and a notification is sent. | The transaction is present in the `Back Valued Messages Queue` with validation failure details; an ACK is sent to the inbound system and a notification is sent. | Pass | `attachments/image-2026-7-13_20-24-39.png`, `attachments/image-2026-7-13_20-27-31.png`, `attachments/image-2026-7-13_20-30-51.png`, `attachments/image-2026-7-13_20-33-13.png`, `attachments/image-2026-7-13_20-33-39.png`, `attachments/image-2026-7-13_20-34-20.png`, `attachments/image-2026-7-13_20-35-35.png`, `attachments/image-2026-7-27_15-17-6.png`, `attachments/image-2026-7-27_15-17-53.png` |
| 6 | FMSGW | Inbound Message | An `MT103` or `MT202` settlement message that hits a DEF rule is listed in the `High value payment Queue`. After approval, it is sent to `AMH`; an ACK is sent to `RATAN` and a notification is sent. Test identifier: `M00127115325`. | `MT103/MT202` is sent to `AMH`; an ACK is sent to `RATAN` and a notification is sent. | Pass | `attachments/image-2026-7-21_13-22-22.png`, `attachments/image-2026-7-21_13-23-34.png`, `attachments/image-2026-7-21_13-23-59.png`, `attachments/image-2026-7-21_13-26-47.png`, `attachments/image-2026-7-21_13-27-50.png`, `attachments/image-2026-7-21_13-29-5.png`, `attachments/image-2026-7-21_13-30-19.png`, `attachments/image-2026-7-21_13-31-0.png`, `attachments/image-2026-7-21_13-31-32.png`, `attachments/image-2026-7-21_13-32-59.png`, `attachments/image-2026-7-27_15-23-7.png` |
| 7 | FMSGW | Inbound Message | Settlement for a cancelled trade where the original message was released. `MT202/MT103` is sent to `AMH` and an ACK is sent to `RATAN`. The cancelled transaction becomes available in the `Manual Cancellation Queue`; an ACK is sent to the inbound system, an email notification is sent to the user, and the transaction can be processed or terminated. | The settlement is sent to `AMH`, the acknowledgement is returned, and the cancelled transaction is available for manual processing. | Pass | `attachments/image-2026-7-8_13-0-36.png`, `attachments/image-2026-7-8_13-5-15.png`, `attachments/image-2026-7-8_13-5-55.png`, `attachments/image-2026-7-8_13-6-20.png`, `attachments/image-2026-7-8_13-6-45.png`, `attachments/image-2026-7-8_13-7-31.png`, `attachments/image-2026-7-27_15-27-37.png` |
| 8 | FMSGW | Validation Queue | An `MTn92` SWIFT payment message flows to the `Manual Cancellation` queue. The user opens the queue, searches for entries, reviews the `Data` and `Action audit` tabs, adds a comment, and releases the transaction to the next eligible currency validation check. | The user can process the transaction, release it to the next eligible currency validation check, and remove it from the manual cancellation queue. | Pass | `attachments/image-2026-7-27_15-33-5.png`, `attachments/image-2026-7-27_15-32-42.png`, `attachments/image-2026-7-27_15-34-31.png`, `attachments/image-2026-7-27_15-33-58.png` |
| 9 | FMSGW | Duplicate Message | A duplicate `MT103`, `MT202`, or `MT202COV` payment is processed from the `Duplicate Message Queue`. | The transaction is found in the queue, the user performs `Process`, and the transaction moves to the next validation stage, `SCB Specific Validations`. | Pass | `attachments/image-2026-7-10_14-57-10.png`, `attachments/image-2026-7-10_15-1-56.png`, `attachments/image-2026-7-10_15-4-59.png`, `attachments/image-2026-7-10_15-8-50.png` |

## Findings

The UAT provides country-specific evidence that the tested manual entity supported:

- Standard inbound settlement routing from `RATAN` through `FMSGW` to `AMH`.
- ACK return flows for `MT103/202COV`, `MT202`, and `MT192/292`.
- Dependent release of `MT202 COV` after a successful `MT103` ACK.
- Back-value-dated exception handling with queue placement, validation-failure details, acknowledgement, and notification.
- DEF-rule high-value payment approval before downstream release.
- Cancel-trade settlement with manual cancellation follow-up.
- User-driven `MTn92` processing through the manual cancellation queue.
- Duplicate-message processing that advances transactions to `SCB Specific Validations`.

These results are UAT evidence for `UGANDA SCB UGANDA KAM(GBS)` and do not, by themselves, establish production go-live approval or equivalent behavior for other manual entities.

## Data-quality and terminology notes

The source numbering skips test case **5**. No case description, result, or explanation is supplied for the omission.

The source uses `Manual Cancellation Queue`, `Manual cancellation queue`, and `Manual Cancellation`. This summary preserves the terms used in the source; the canonical queue name should be confirmed.

The ACK descriptions refer variously to acknowledgements sent to `RATAN` and to the inbound system. The document does not define whether these references represent the same acknowledgement contract or separate message types and destinations.

The DEF-rule criteria, approval authority, notification recipient, rejection behavior, and subsequent currency validation are not specified.

## Related wiki context

This source extends [[concepts/manual-entity-settlement-enablement]] and [[concepts/country-specific-settlement-uat-coverage]] with Uganda-specific UAT evidence. It also provides evidence relevant to [[concepts/fmsgw-inbound-message-routing]], [[concepts/settlement-acknowledgement-flow]], [[concepts/back-valued-message-queue]], [[concepts/high-value-payment-queue]], [[concepts/manual-cancellation-queue]], and [[concepts/duplicate-message-queue-processing]].
