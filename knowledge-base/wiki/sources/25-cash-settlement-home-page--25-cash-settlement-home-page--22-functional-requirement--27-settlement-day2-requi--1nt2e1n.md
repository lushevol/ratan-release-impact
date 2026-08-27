---
type: source
title: "GHANA SCB GHANA ACC(GBS) Settlement UAT"
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page UAT testing"
created: 2026-08-23
updated: 2026-08-23
tags: [uat, cash-settlement, manual-entities, ghana, fmsgw, ratan, amh]
related: [ghana-scb-ghana-acc-gbs, manual-entity-settlement-enablement, country-specific-settlement-uat-coverage, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, back-valued-message-queue, high-value-payment-queue, manual-cancellation-queue, duplicate-message-queue-processing, mt202cov-ack-dependent-release]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/008 GHANA SCB GHANA ACC(GBS).md"]
---
# GHANA SCB GHANA ACC(GBS) Settlement UAT

## Scope

This source records UAT evidence for enabling settlement for the manual entity **GHANA SCB GHANA ACC(GBS)**. The tested integration covers [[entities/ratan]], [[entities/fmsgw]], and [[entities/amh]]. All listed test cases are recorded as **Pass**.

The source does not provide an authoritative execution date, release version, environment, tester name, test data, message identifiers, or configuration values. Attachment filenames contain July 2026 dates, but those filenames are not treated as authoritative execution metadata.

## Test coverage

| S.no | Squads | Type/Functions | Test Case/Scenario | Expected Result | Test Result |
|---|---|---|---|---|---|
| 1 | FMSGW | Inbound Message | MT103/202COV. Settlement message MT103/202COV received from RATAN and sent to AMH. ACK message is sent back to RATAN. | MT103/202COV is sent to AMH and ACK message is sent back to RATAN. MT202 Cov should be released upon MT103 getting ACK successfully. | Pass |
| 2 | FMSGW | Inbound Message | MT202. Settlement message MT202 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT202 is sent to AMH and ACK is message is sent back to RATAN. | Pass |
| 3 | FMSGW | Inbound Message | MT192/292. Settlement message MT192/292 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT192/292 is sent to AMH and ACK is message is sent back to RATAN. | Pass |
| 4 | FMSGW | Inbound Message | ANY. Back Value Dated message received from RATAN and listed in Back Valued Messages Queue when processed ACK message is sent to inbound system and notification will be sent. | Transaction should be present in Back Valued Messages Queue with Validation Failure details and ACK should be sent to inbound system and notification will be sent. | Pass |
| 6 | FMSGW | Inbound Message | MT103,MT202. Settlement message hit DEF rule with High Value payment (MT103/MT202) received from RATAN is listed in High value payment Queue once approved then sent to AMH. ACK is message is sent back to RATAN and notification will be sent. | MT103/MT202 is sent to AMH and ACK is message is sent back to RATAN and notification will be sent. | Pass |
| 7 | FMSGW | Inbound Message | MT103, MT202. Settlement for Cancel Trade where Original message released. | MT202/MT103 is sent to AMH and ACK is message is sent back to RATAN. The cancelled transaction is available in Manual Cancellation Queue; ACK and email notification are sent; user can process or terminate it. | Pass |
| 8 | FMSGW | Validation Queue | MTn92. Swift Payment message where message type is MTn92 will flow to "Manual Cancellation" queue and User will perform Process action on the payment transaction to next Eligible currency validation check. | User can log in, open the queue, search entries, view Data and Action audit tabs, add a comment, and release the transaction to the next validation check. | Pass |
| 9 | FMSGW | Duplicate Message | MT103/MT202/ MT202COV. Processing of Duplicate payment message from Duplicate message Queue. | Transaction is found in Duplicate Message Queue. On Process, it moves to the next validation: check for SCB Specific Validations. | Pass |

The source skips test case number 5; no case 5 is included in the supplied document.

## Confirmed behaviors

### Standard inbound routing

The UAT confirms successful routing for:

- `MT103/202COV` from `RATAN` to `AMH`, with an ACK returned to `RATAN`.
- `MT202` from `RATAN` to `AMH`, with an ACK returned to `RATAN`.
- `MT192/292` from `RATAN` to `AMH`, with an ACK returned to `RATAN`.

These results provide Ghana-specific evidence for [[concepts/fmsgw-inbound-message-routing]] and [[concepts/settlement-acknowledgement-flow]].

### ACK-dependent `MT202COV` release

The source states that `MT202COV` should be released after the associated `MT103` receives a successful ACK. This is recorded as a tested behavior for GHANA SCB GHANA ACC(GBS), not as a universal contract for every manual entity or message configuration. See [[concepts/mt202cov-ack-dependent-release]] and [[queries/what-is-the-authoritative-mt103-ack-dependent-mt202cov-release-contract]].

### Back-valued message handling

A back value-dated `ANY` message is expected to appear in the [[concepts/back-valued-message-queue]] with validation failure details. An ACK is sent to the inbound system and a notification is generated. The source records this exception path as passed.

### High-value payment approval

High-value `MT103` and `MT202` messages that hit a `DEF` rule are placed in the [[concepts/high-value-payment-queue]]. After user approval, the message is sent to `AMH`, an ACK is returned to `RATAN`, and a notification is sent. The UAT does not define the conditions, threshold, or full semantics of the `DEF` rule.

### Cancelled-trade processing

For a cancelled trade whose original message was released, the `MT202`/`MT103` is sent to `AMH` and an ACK is returned to `RATAN`. The cancelled transaction is then available in the [[concepts/manual-cancellation-queue]]. The source states that an ACK is sent to the inbound system, the user receives an email notification, and the user can process or terminate the transaction.

### `MTn92` manual processing

`MTn92` payment messages flow to the Manual Cancellation Queue. The user can log in, open the queue, search for single or multiple entries, open a detail popup with `Data` and `Action audit` tabs, add a comment, and release the payment to the next eligible-currency validation check. The transaction should disappear from the queue after release.

The source does not define why all or particular `MTn92` variants are classified for manual cancellation processing, nor does it define the subsequent eligible-currency validation stage.

### Duplicate message processing

Duplicate `MT103`, `MT202`, and `MT202COV` messages are located through `Validation → Duplicate Message Queue`. After the user performs the Process action, the transaction moves to the next validation stage, identified as `SCB Specific Validations`. This confirms the successful path described in [[concepts/duplicate-message-queue-processing]].

## Evidence and limitations

The source references screenshot attachments for every passed test case. The supplied document does not include the screenshot contents as separate evidence in this summary. The UAT confirms successful-path behavior but does not establish:

- ACK timeout, rejection, retry, duplicate-ACK, or missing-ACK behavior.
- Authorization boundaries for queue actions.
- Notification recipients, delivery guarantees, or message content.
- The `DEF` rule criteria or high-value threshold.
- The exact meaning of the next eligible-currency validation check.
- Whether the results generalize to other manual entities.
- The missing test case 5.

## Attachment references

The source references the following attachment filenames:

- `image-2026-7-27_15-42-52.png`
- `image-2026-7-27_15-44-17.png`
- `image-2026-7-27_15-46-36.png`
- `image-2026-7-27_15-46-58.png`
- `image-2026-7-27_15-47-52.png`
- `image-2026-7-27_15-49-16.png`
- `image-2026-7-8_14-0-21.png`
- `image-2026-7-8_14-0-58.png`
- `image-2026-7-27_15-51-53.png`
- `image-2026-7-8_14-5-28.png`
- `image-2026-7-8_14-12-5.png`
- `image-2026-7-13_21-9-26.png`
- `image-2026-7-13_21-10-20.png`
- `image-2026-7-13_21-13-48.png`
- `image-2026-7-13_21-14-34.png`
- `image-2026-7-13_21-15-41.png`
- `image-2026-7-13_21-16-25.png`
- `image-2026-7-13_21-17-52.png`
- `image-2026-7-27_15-55-45.png`
- `image-2026-7-27_15-56-20.png`
- `image-2026-7-31_10-45-6.png`
- `image-2026-7-9_17-50-20.png`
- `image-2026-7-9_17-52-12.png`
- `image-2026-7-9_17-58-7.png`
- `image-2026-7-9_17-57-19.png`
- `image-2026-7-10_12-5-18.png`
- `image-2026-7-10_12-11-17.png`
- `image-2026-7-10_12-12-26.png`
- `image-2026-7-23_12-46-42.png`
- `image-2026-7-27_16-0-9.png`
- `image-2026-7-8_14-19-54.png`
- `image-2026-7-8_14-23-12.png`
- `image-2026-7-8_14-23-45.png`
- `image-2026-7-8_14-25-2.png`
- `image-2026-7-27_16-2-52.png`
- `image-2026-7-27_16-1-52.png`
- `image-2026-7-23_12-48-39.png`
- `image-2026-7-27_16-4-49.png`
- `image-2026-7-10_11-48-6.png`
- `image-2026-7-10_11-49-38.png`
- `image-2026-7-10_11-50-32.png`
- `image-2026-7-10_11-55-7.png`
- `image-2026-7-10_11-56-55.png`
- `image-2026-7-10_11-58-52.png`
