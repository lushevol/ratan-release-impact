---
type: source
title: Nigeria SCB Nigeria LAG(GBS) UAT Testing
authors: []
year: 2026
url: ""
venue: Internal UAT documentation
created: 2026-08-23
updated: 2026-08-23
tags: [uat, nigeria, scb, fmsgw, ratan, amh, manual-entity-settlement]
related: [scb-nigeria-lag-gbs, ratan, fmsgw, amh, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, back-valued-message-queue, high-value-payment-queue, manual-cancellation-queue, duplicate-message-queue-processing, def-rule, country-specific-settlement-uat-coverage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/009 NIGERIA SCB NIGERIA LAG(GBS).md"]
---

# Nigeria SCB Nigeria LAG(GBS) UAT Testing

This source records UAT evidence for settlement enablement of [[scb-nigeria-lag-gbs]]. All documented test cases are marked **Pass**. The covered path is [[ratan]] → [[fmsgw]] → [[amh]], with acknowledgement returned to RATAN and manual queue handling for defined exceptions.

## Findings

- Standard `MT103/202COV`, `MT202`, and `MT192/292` inbound messages were routed to AMH and acknowledged to RATAN.
- For the `MT103/MT202COV` pair, `MT202COV` should be released only after the associated `MT103` receives a successful ACK.
- Back value-dated messages entered the [[back-valued-message-queue]] with validation-failure details, acknowledgement, and notification.
- `MT103` and `MT202` messages that hit a [[def-rule]] as high-value payments required queue approval before routing to AMH.
- Cancelled trades and `MTn92` messages used the [[manual-cancellation-queue]].
- Processed duplicate messages progressed to SCB Specific Validations.

The source does not include Case 5, define the DEF rule, or specify the state reached after the eligible-currency validation check.

## UAT Test Results

| [S.no](http://S.no) | Squads | Type/Functions | Test Case/Scenario | Test Steps | Expected Result | Test Result(Pass / Fail/ Blocked/ Descoped) | Tested By |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FMSGW | Inbound Message | MT103/202COV | Settlement message MT103/202COV received from RATAN and sent to AMH. ACK message is sent back to RATAN. | MT103/202COV is sent to AMH and ACK message is sent back to RATAN. | Pass | Evidence screenshots: `image-2026-7-27_16-14-14.png`, `image-2026-7-27_16-17-17.png`, `image-2026-7-27_16-18-6.png`, `image-2026-7-28_12-24-5.png`, `image-2026-7-28_12-24-47.png`, `image-2026-7-28_12-22-45.png` |
| MT202 Cov should be released upon MT103 getting ACK successfully. |
| 2 | FMSGW | Inbound Message | MT202 | Settlement message MT202 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT202 is sent to AMH and ACK is message is sent back to RATAN. | Pass | Evidence screenshots: `image-2026-7-27_16-19-58.png`, `image-2026-7-27_16-24-2.png`, `image-2026-7-27_16-23-21.png` |
| 3 | FMSGW | Inbound Message | MT192/292 | Settlement message MT192/292 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT192/292 is sent to AMH and ACK is message is sent back to RATAN. | Pass | Evidence screenshots: `image-2026-6-26_14-1-27.png`, `image-2026-6-26_14-2-0.png`, `image-2026-7-27_16-27-52.png`, `image-2026-7-27_16-26-36.png` |
| 4 | FMSGW | Inbound Message | ANY | Back Value Dated message received from RATAN and listed in Back Valued Messages Queue when processed ACK message is sent to inbound system and notification will be sent | Transaction should be present in Back Valued Messages Queue with Validation Failure details and ACK should be sent to inbound system and notification will be sent | Pass | `M00127114772`; evidence screenshots: `image-2026-7-31_12-38-17.png`, `image-2026-7-31_12-40-5.png`, `image-2026-7-31_12-42-11.png`, `image-2026-7-31_12-42-39.png`, `image-2026-7-31_12-43-13.png`, `image-2026-7-31_12-45-15.png`, `image-2026-7-31_12-45-39.png`, `image-2026-7-31_12-46-17.png`, `image-2026-7-31_13-14-13.png`, `image-2026-7-31_13-14-36.png`, `image-2026-7-31_13-20-42.png`, `image-2026-7-31_13-25-0.png` |
| 6 | FMSGW | Inbound Message | MT103,MT202 | Settlement message hit DEF rule with High Value payment (MT103/MT202) received from RATAN is listed in High value payment Queue once approved then sent to AMH. ACK is message is sent back to RATAN and notification will be sent | MT103/MT202 is sent to AMH and ACK is message is sent back to RATAN and notification will be sent | Pass | Evidence screenshots: `image-2026-7-9_17-29-36.png`, `image-2026-7-9_17-31-43.png`, `image-2026-7-9_17-34-37.png`, `image-2026-7-9_17-35-44.png`, `image-2026-7-9_17-39-14.png`, `image-2026-7-9_17-41-36.png`, `image-2026-7-9_17-42-50.png`, `image-2026-7-27_16-40-27.png` |
| 7 | FMSGW | Inbound Message | MT103, MT202 | Settlement for Cancel Trade where Original message released | 1. MT202/MT103 is sent to AMH and ACK is message is sent back to RATAN. | Pass | `DV82M00126026660`; evidence screenshots: `image-2026-7-27_16-45-42.png`, `image-2026-7-27_16-46-12.png`, `image-2026-7-27_16-50-43.png`, `image-2026-7-27_16-51-23.png` |
| 2. As the trade is cancelled so the transaction will be available in Manual Cancellation Queue, |
| an ACK is sent to inbound system and User is sent notification through email |
| 3. In Manual Cancellation Queue user can further process or terminate the transaction |
| 8 | FMSGW | Validation Queue | MTn92 | Swift Payment message where message type is MTn92 will flow to "Manual Cancellation" queue and User will perform Process action on the payment transaction to next Eligible currency validation check | 1. User should be able to login and should be able to open the queue | Pass | Evidence screenshots: `image-2026-7-27_16-52-50.png`, `image-2026-7-27_16-54-4.png`, `image-2026-7-27_16-54-44.png`, `image-2026-7-27_16-55-38.png` |
| 2.Search will display Single or Multiple entries depending on the validation check |
| 3.Detail screen popup window should be opened with tabs - "Data" and "Action audit" |
| 4.User should be able to add comment and Payment transaction should be released for next Eligible currency validation check and it should be disappeared from the Manual cancellation queue. |
| 9 | FMSGW | Duplicate Message | MT103/MT202/ MT202COV | Processing of Duplicate payment message from Duplicate message Queue | 1) Login to Manual Queue -> Navigate to Validation->Duplicate Message Queue and search for the trade in the queue | Pass | Evidence screenshots: `image-2026-7-10_11-16-2.png`, `image-2026-7-10_11-17-15.png`, `image-2026-7-10_11-19-55.png`, `image-2026-7-10_11-24-7.png`, `image-2026-7-10_11-25-45.png` |
| 2) Perform Process action on the transaction |
| Expectation: |
| 1) Transaction message should be found in Duplicate Message Queue. |
| 2) On Process, Transaction will move to next validations i.e., check for SCB Specific Validations |

## Scope Limitations

The test document provides screenshot-based evidence but does not provide tester names, environment details, planned test totals, failure-path evidence, retry behavior, timeout handling, or idempotency rules.