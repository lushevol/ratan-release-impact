---
type: source
title: Kenya SCB Kenya B NBO (GBS) UAT Testing
created: 2026-08-23
updated: 2026-08-23
tags: [uat, settlement-day-2, manual-entities, kenya, fmsgw, swift]
related: [fmsgw, amh, scb-kenya-b, settlement-day-2, manual-entity-settlement-enablement, fmsgw-manual-validation-queues, what-is-the-authoritative-ratan-fmsgw-ack-and-release-contract, what-is-the-authoritative-manual-cancellation-queue-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/004 KENYA SCB KENYA B NBO(GBS).md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Kenya SCB Kenya B NBO (GBS) UAT Testing

This UAT document records FMSGW test results for the Kenya / SCB Kenya B / NBO (GBS) manual-entity settlement configuration within [[settlement-day-2]]. All documented test cases passed.

The evidence supports the tested RATAN → FMSGW → AMH routing, acknowledgement, approval, and queue-processing behaviors for this configuration. It does not establish performance characteristics, resilience behavior, production readiness, or applicability to other entities and countries.

## Findings

- Standard inbound `MT103/202COV`, `MT202`, and `MT192/292` messages were routed from RATAN through FMSGW to [[amh]], with an ACK returned to RATAN.
- `MT202COV` release is stated to depend on successful acknowledgement of the associated `MT103`.
- Back-value-dated messages were placed in the Back Valued Messages Queue with validation-failure details, an ACK, and a notification.
- DEF-rule high-value `MT103` and `MT202` messages required approval from the High Value Payment Queue before forwarding to AMH.
- Cancelled trades and `MTn92` messages used the Manual Cancellation Queue, including comments and Action audit information.
- Duplicate `MT103`, `MT202`, and `MT202COV` messages advanced to SCB Specific Validations after a user performed Process in the Duplicate Message Queue.

## Source Test Matrix

| **[S.no](http://S.no)** | **Squads** | **Type/Functions** | **Test Case/Scenario** | **Test Steps** | **Expected Result** | **Test Result(Pass / Fail/ Blocked/ Descoped)** | **Tested By** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FMSGW | Inbound Message | MT103/202COV | Settlement message MT103/202COV received from RATAN and sent to AMH. ACK message is sent back to RATAN. | MT103/202COV is sent to AMH and ACK message is sent back to RATAN. | Pass | DV39M00126810103 ![image-2026-7-8_11-19-42.png](attachments/image-2026-7-8_11-19-42.png) ![image-2026-7-8_11-20-29.png](attachments/image-2026-7-8_11-20-29.png) ![image-2026-7-8_11-20-48.png](attachments/image-2026-7-8_11-20-48.png) ![image-2026-7-27_13-12-34.png](attachments/image-2026-7-27_13-12-34.png) |
| MT202 Cov should be released upon MT103 getting ACK successfully. |
| 2 | FMSGW | Inbound Message | MT202 | Settlement message MT202 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT202 is sent to AMH and ACK is message is sent back to RATAN. | Pass | DV39M00126080255 ![image-2026-7-8_11-23-18.png](attachments/image-2026-7-8_11-23-18.png) ![image-2026-7-8_11-24-10.png](attachments/image-2026-7-8_11-24-10.png) ![image-2026-7-27_13-14-4.png](attachments/image-2026-7-27_13-14-4.png) |
| 3 | FMSGW | Inbound Message | MT192/292 | Settlement message MT192/292 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT192/292 is sent to AMH and ACK is message is sent back to RATAN. | Pass | ![image-2026-7-16_9-53-0.png](attachments/image-2026-7-16_9-53-0.png) ![image-2026-7-16_9-55-55.png](attachments/image-2026-7-16_9-55-55.png) ![image-2026-7-16_9-56-29.png](attachments/image-2026-7-16_9-56-29.png) ![image-2026-7-16_9-58-5.png](attachments/image-2026-7-16_9-58-5.png) ![image-2026-7-16_9-59-11.png](attachments/image-2026-7-16_9-59-11.png) ![image-2026-7-16_9-58-52.png](attachments/image-2026-7-16_9-58-52.png) ![image-2026-7-16_15-20-59.png](attachments/image-2026-7-16_15-20-59.png) ![image-2026-7-16_15-21-26.png](attachments/image-2026-7-16_15-21-26.png) ![image-2026-7-16_9-59-51.png](attachments/image-2026-7-16_9-59-51.png) ![image-2026-7-16_10-1-52.png](attachments/image-2026-7-16_10-1-52.png) ![image-2026-7-20_9-13-32.png](attachments/image-2026-7-20_9-13-32.png) ![image-2026-7-27_13-22-8.png](attachments/image-2026-7-27_13-22-8.png) |
| 4 | FMSGW | Inbound Message | ANY | Back Value Dated message received from RATAN and listed in Back Valued Messages Queue when processed ACK message is sent to inbound system and notification will be sent | Transaction should be present in Back Valued Messages Queue with Validation Failure details and ACK should be sent to inbound system and notification will be sent | Pass | ![image-2026-7-28_22-32-54.png](attachments/image-2026-7-28_22-32-54.png) ![image-2026-7-28_22-33-31.png](attachments/image-2026-7-28_22-33-31.png) ![image-2026-7-28_22-34-3.png](attachments/image-2026-7-28_22-34-3.png) ![image-2026-7-28_22-34-41.png](attachments/image-2026-7-28_22-34-41.png) ![image-2026-7-28_22-35-44.png](attachments/image-2026-7-28_22-35-44.png) ![image-2026-7-28_22-36-59.png](attachments/image-2026-7-28_22-36-59.png) ![image-2026-7-28_22-38-28.png](attachments/image-2026-7-28_22-38-28.png) ![image-2026-7-28_22-39-26.png](attachments/image-2026-7-28_22-39-26.png) |
| 6 | FMSGW | Inbound Message | MT103,MT202 | Settlement message hit DEF rule with High Value payment (MT103/MT202) received from RATAN is listed in High value payment Queue once approved then sent to AMH. ACK is message is sent back to RATAN and notification will be sent | MT103/MT202 is sent to AMH and ACK is message is sent back to RATAN and notification will be sent | Pass | ![image-2026-7-13_15-17-4.png](attachments/image-2026-7-13_15-17-4.png) ![image-2026-7-13_15-18-44.png](attachments/image-2026-7-13_15-18-44.png) ![image-2026-7-13_15-25-22.png](attachments/image-2026-7-13_15-25-22.png) ![image-2026-7-13_15-24-42.png](attachments/image-2026-7-13_15-24-42.png) ![image-2026-7-13_15-29-10.png](attachments/image-2026-7-13_15-29-10.png) ![image-2026-7-27_13-30-0.png](attachments/image-2026-7-27_13-30-0.png) |
| 7 | FMSGW | Inbound Message | MT103, MT202 | Settlement for Cancel Trade where Original message released | 1. MT202/MT103 is sent to AMH and ACK is message is sent back to RATAN. | Pass | ![image-2026-7-13_18-20-8.png](attachments/image-2026-7-13_18-20-8.png) ![image-2026-7-13_18-19-39.png](attachments/image-2026-7-13_18-19-39.png) ![image-2026-7-16_9-59-51.png](attachments/image-2026-7-16_9-59-51.png) ![image-2026-7-16_9-58-52.png](attachments/image-2026-7-16_9-58-52.png) ![image-2026-7-16_10-1-52.png](attachments/image-2026-7-16_10-1-52.png) ![image-2026-7-29_16-24-6.png](attachments/image-2026-7-29_16-24-6.png) |
| 2. As the trade is cancelled so the transaction will be available in Manual Cancellation Queue, |
| an ACK is sent to inbound system and User is sent notification through email |
| 3. In Manual Cancellation Queue user can further process or terminate the transaction |
| 8 | FMSGW | Validation Queue | MTn92 | Swift Payment message where message type is MTn92 will flow to "Manual Cancellation" queue and User will perform Process action on the payment transaction to next Eligible currency validation check | 1. User should be able to login and should be able to open the queue | Pass | ![image-2026-7-16_10-54-50.png](attachments/image-2026-7-16_10-54-50.png) ![image-2026-7-16_10-56-5.png](attachments/image-2026-7-16_10-56-5.png) ![image-2026-7-16_10-57-24.png](attachments/image-2026-7-16_10-57-24.png) ![image-2026-7-16_10-57-54.png](attachments/image-2026-7-16_10-57-54.png) ![image-2026-7-16_10-58-36.png](attachments/image-2026-7-16_10-58-36.png) ![image-2026-7-16_10-59-18.png](attachments/image-2026-7-16_10-59-18.png) ![image-2026-7-16_10-59-52.png](attachments/image-2026-7-16_10-59-52.png) ![image-2026-7-16_11-4-6.png](attachments/image-2026-7-16_11-4-6.png) ![image-2026-7-27_13-36-45.png](attachments/image-2026-7-27_13-36-45.png) ![image-2026-7-27_13-35-49.png](attachments/image-2026-7-27_13-35-49.png) |
| 2.Search will display Single or Multiple entries depending on the validation check |
| 3.Detail screen popup window should be opened with tabs - "Data" and "Action audit" |
| 4.User should be able to add comment and Payment transaction should be released for next Eligible currency validation check and it should be disappeared from the Manual cancellation queue. |
| 9 | FMSGW | Duplicate Message | MT103/MT202/ MT202COV | Processing of Duplicate payment message from Duplicate message Queue | 1) Login to Manual Queue -> Navigate to Validation->Duplicate Message Queue and search for the trade in the queue | Pass | ![image-2026-7-10_15-56-4.png](attachments/image-2026-7-10_15-56-4.png) ![image-2026-7-10_15-57-10.png](attachments/image-2026-7-10_15-57-10.png) ![image-2026-7-10_15-58-3.png](attachments/image-2026-7-10_15-58-3.png) ![image-2026-7-10_15-58-29.png](attachments/image-2026-7-10_15-58-29.png) ![image-2026-7-10_15-59-27.png](attachments/image-2026-7-10_15-59-27.png) |
| 2) Perform Process action on the transaction |
| Expectation: |
| 1) Transaction message should be found in Duplicate Message Queue. |
| 2) On Process, Transaction will move to next validations i.e., check for SCB Specific Validations |

## Scope Limitations

The source does not provide message payloads, ACK schemas, correlation keys, rule thresholds, notification contracts, build versions, environment details, or failure and recovery cases. Test case number 5 is absent without explanation.