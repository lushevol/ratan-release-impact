---
type: source
title: "UAT Testing — ZAMBIA SCB ZAMBIA LUS(GBS)"
authors: []
year: 2026
url: ""
venue: "UAT test evidence"
created: 2026-08-23
updated: 2026-08-23
tags: [uat, settlement-day-2, manual-entity, fmsgw, zambia, swift]
related: [fmsgw, amh, zambia-scb-zambia-lus-gbs, manual-entity-settlement-enablement, settlement-day-2, country-specific-settlement-uat-coverage, mt103-mt202cov-acknowledgement-sequencing, fmsgw-manual-cancellation-queue, fmsgw-duplicate-message-processing, high-value-payment-approval-queue, what-is-missing-fmsgw-uat-test-case-5-for-zambia-scb-zambia-lus-gbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/005 ZAMBIA SCB ZAMBIA LUS(GBS).md"]
---
# UAT Testing — ZAMBIA SCB ZAMBIA LUS(GBS)

## Scope

This source records FMSGW UAT evidence for Settlement Day 2 enablement of the manual entity [[zambia-scb-zambia-lus-gbs]]. The recorded scenarios cover standard inbound routing, acknowledgement, exception queues, high-value approval, cancellation handling, and duplicate-message processing.

All listed test cases are marked **Pass**. The evidence consists of screenshot attachments and identifiers, without execution dates, environment details, build versions, defect references, message payloads, ACK contents, or independent AMH-side confirmation.

## Findings

- [[fmsgw]] routed tested MT103/202COV, MT202, and MT192/292 settlement messages from RATAN to [[amh]] and returned ACK messages to RATAN.
- MT202 COV is stated to be released only after successful MT103 acknowledgement; the UAT result is Pass, but no timestamped sequence evidence is provided.
- A back-value-dated message was placed in the Back Valued Messages Queue with validation-failure details; processing produced an inbound ACK and notification.
- High-value MT103 and MT202 messages matching a DEF rule entered the High value payment Queue and, after approval, were sent to AMH with ACK and notification.
- Cancelled-trade processing created a Manual Cancellation Queue item that a user could process or terminate.
- MTn92 messages were processed through the Manual Cancellation Queue into the Eligible currency validation check.
- Duplicate MT103, MT202, and MT202COV messages could be processed from the Duplicate Message Queue into SCB Specific Validations.

## UAT Result Register

| S.no | Squads | Type/Functions | Test Case/Scenario | Test Steps | Expected Result | Test Result(Pass / Fail/ Blocked/ Descoped) | Tested By |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FMSGW | Inbound Message | MT103/202COV | Settlement message MT103/202COV received from RATAN and sent to AMH. ACK message is sent back to RATAN. | MT103/202COV is sent to AMH and ACK message is sent back to RATAN. | Pass | DV52M00127113583 ![image-2026-7-27_13-38-42.png](attachments/image-2026-7-27_13-38-42.png) ![image-2026-7-9_9-35-39.png](attachments/image-2026-7-9_9-35-39.png) ![image-2026-7-20_22-22-54.png](attachments/image-2026-7-20_22-22-54.png) ![image-2026-7-20_22-23-16.png](attachments/image-2026-7-20_22-23-16.png) |
| MT202 Cov should be released upon MT103 getting ACK successfully. |
| 2 | FMSGW | Inbound Message | MT202 | Settlement message MT202 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT202 is sent to AMH and ACK is message is sent back to RATAN. | Pass | ![image-2026-7-27_13-40-12.png](attachments/image-2026-7-27_13-40-12.png) ![image-2026-7-9_9-27-56.png](attachments/image-2026-7-9_9-27-56.png) ![image-2026-7-9_9-27-29.png](attachments/image-2026-7-9_9-27-29.png) |
| 3 | FMSGW | Inbound Message | MT192/292 | Settlement message MT192/292 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT192/292 is sent to AMH and ACK is message is sent back to RATAN. | Pass | ![image-2026-7-27_13-41-10.png](attachments/image-2026-7-27_13-41-10.png) ![image-2026-7-9_10-1-50.png](attachments/image-2026-7-9_10-1-50.png) ![image-2026-7-9_10-2-14.png](attachments/image-2026-7-9_10-2-14.png) |
| 4 | FMSGW | Inbound Message | ANY | Back Value Dated message received from RATAN and listed in Back Valued Messages Queue when processed ACK message is sent to inbound system and notification will be sent | Transaction should be present in Back Valued Messages Queue with Validation Failure details and ACK should be sent to inbound system and notification will be sent | Pass | ![image-2026-7-13_19-50-14.png](attachments/image-2026-7-13_19-50-14.png) ![image-2026-7-13_19-52-3.png](attachments/image-2026-7-13_19-52-3.png) ![image-2026-7-13_19-52-53.png](attachments/image-2026-7-13_19-52-53.png) ![image-2026-7-13_19-53-26.png](attachments/image-2026-7-13_19-53-26.png) ![image-2026-7-13_19-54-28.png](attachments/image-2026-7-13_19-54-28.png) ![image-2026-7-27_13-44-24.png](attachments/image-2026-7-27_13-44-24.png) ![image-2026-7-27_13-44-53.png](attachments/image-2026-7-27_13-44-53.png) ![image-2026-7-27_13-46-14.png](attachments/image-2026-7-27_13-46-14.png) |
| 6 | FMSGW | Inbound Message | MT103,MT202 | Settlement message hit DEF rule with High Value payment (MT103/MT202) received from RATAN is listed in High value payment Queue once approved then sent to AMH. ACK is message is sent back to RATAN and notification will be sent | MT103/MT202 is sent to AMH and ACK is message is sent back to RATAN and notification will be sent | Pass | M00127115344 ![image-2026-7-27_13-53-0.png](attachments/image-2026-7-27_13-53-0.png) ![image-2026-7-27_13-56-50.png](attachments/image-2026-7-27_13-56-50.png) ![image-2026-7-27_13-58-17.png](attachments/image-2026-7-27_13-58-17.png) ![image-2026-7-27_13-59-24.png](attachments/image-2026-7-27_13-59-24.png) ![image-2026-7-27_14-0-4.png](attachments/image-2026-7-27_14-0-4.png) |
| 7 | FMSGW | Inbound Message | MT103, MT202 | Settlement for Cancel Trade where Original message released | 1. MT202/MT103 is sent to AMH and ACK is message is sent back to RATAN. | Pass | ![image-2026-7-9_9-51-0.png](attachments/image-2026-7-9_9-51-0.png) ![image-2026-7-9_9-52-1.png](attachments/image-2026-7-9_9-52-1.png) ![image-2026-7-9_9-54-14.png](attachments/image-2026-7-9_9-54-14.png) ![image-2026-7-9_9-56-24.png](attachments/image-2026-7-9_9-56-24.png) ![image-2026-7-9_9-58-7.png](attachments/image-2026-7-9_9-58-7.png) ![image-2026-7-9_9-58-26.png](attachments/image-2026-7-9_9-58-26.png) ![image-2026-7-27_14-6-31.png](attachments/image-2026-7-27_14-6-31.png) |
| 2. As the trade is cancelled so the transaction will be available in Manual Cancellation Queue, |
| an ACK is sent to inbound system and User is sent notification through email |
| 3. In Manual Cancellation Queue user can further process or terminate the transaction |
| 8 | FMSGW | Validation Queue | MTn92 | Swift Payment message where message type is MTn92 will flow to "Manual Cancellation" queue and User will perform Process action on the payment transaction to next Eligible currency validation check | 1. User should be able to login and should be able to open the queue | Pass | ![image-2026-7-9_10-37-55.png](attachments/image-2026-7-9_10-37-55.png) ![image-2026-7-9_10-39-47.png](attachments/image-2026-7-9_10-39-47.png) ![image-2026-7-9_10-40-34.png](attachments/image-2026-7-9_10-40-34.png) ![image-2026-7-9_10-41-16.png](attachments/image-2026-7-9_10-41-16.png) ![image-2026-7-9_10-41-42.png](attachments/image-2026-7-9_10-41-42.png) ![image-2026-7-9_10-42-14.png](attachments/image-2026-7-9_10-42-14.png) ![image-2026-7-27_15-2-21.png](attachments/image-2026-7-27_15-2-21.png) |
| 2.Search will display Single or Multiple entries depending on the validation check |
| 3.Detail screen popup window should be opened with tabs - "Data" and "Action audit" |
| 4.User should be able to add comment and Payment transaction should be released for next Eligible currency validation check and it should be disappeared from the Manual cancellation queue. |
| 9 | FMSGW | Duplicate Message | MT103/MT202/ MT202COV | Processing of Duplicate payment message from Duplicate message Queue | 1) Login to Manual Queue -> Navigate to Validation->Duplicate Message Queue and search for the trade in the queue | Pass | ![image-2026-7-10_15-12-14.png](attachments/image-2026-7-10_15-12-14.png) ![image-2026-7-10_15-13-28.png](attachments/image-2026-7-10_15-13-28.png) ![image-2026-7-10_15-14-19.png](attachments/image-2026-7-10_15-14-19.png) ![image-2026-7-10_15-14-43.png](attachments/image-2026-7-10_15-14-43.png) ![image-2026-7-10_15-15-40.png](attachments/image-2026-7-10_15-15-40.png) |
| 2) Perform Process action on the transaction |
| Expectation: |
| 1) Transaction message should be found in Duplicate Message Queue. |
| 2) On Process, Transaction will move to next validations i.e., check for SCB Specific Validations |

## Limitations and Open Items

The source skips test case 5. It does not establish whether that case was omitted, descoped, renumbered, or executed separately. It also does not identify the concrete message type used in the `ANY` back-value-date case.

The source provides no authoritative ACK contract, DEF threshold, approval-role model, duplicate-detection key, queue authorization model, or lifecycle-state definition. Its results apply to the tested Zambia configuration and should not be generalized to every manual entity or message format.