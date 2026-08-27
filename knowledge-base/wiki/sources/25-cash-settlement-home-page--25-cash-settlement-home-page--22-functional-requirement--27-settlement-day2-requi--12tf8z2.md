---
type: source
title: Sri Lanka SCB Colombo CMB (In Country) UAT Testing
created: 2026-08-23
updated: 2026-08-23
tags: [uat, settlement, sri-lanka, fmsgw, manual-entity]
related: [sri-lanka-scb-colombo-cmb, shalini-fonseka, ratan, fmsgw, amh, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, mt103-mt202cov-acknowledgement-sequencing, back-valued-message-queue, high-value-payment-queue, manual-cancellation-queue, duplicate-message-queue-processing, def-rule-high-value-payment-routing, what-is-the-missing-sri-lanka-colombo-uat-test-case-5]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/010 SRI LANKA SCB COLOMBO CMB(In Country).md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Sri Lanka SCB Colombo CMB (In Country) UAT Testing

This UAT record covers inbound settlement-message processing for [[sri-lanka-scb-colombo-cmb]]. It records passing FMSGW scenarios for messages received from [[ratan]], routed or released to [[amh]], and acknowledged back to RATAN or the inbound system.

## Recorded UAT Cases

| S.no | Squad | Type/Functions | Test Case/Scenario | Test Steps | Expected Result | Result | Test Evidence | Tested By |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FMSGW | Inbound Message | MT103/202COV | Settlement message MT103/202COV received from RATAN and sent to AMH. ACK message is sent back to RATAN. MT202 Cov should be released upon MT103 getting ACK successfully. | MT103/202COV is sent to AMH and ACK message is sent back to RATAN. | Pass | image-2026-7-14_17-22-42.png; image-2026-7-14_17-23-6.png | Shalini Fonseka |
| 2 | FMSGW | Inbound Message | MT202 | Settlement message MT202 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT202 is sent to AMH and ACK is message is sent back to RATAN. | Pass | image-2026-7-14_17-29-5.png | Shalini Fonseka |
| 3 | FMSGW | Inbound Message | MT192/292 | Settlement message MT192/292 received from RATAN and sent to AMH. ACK is message is sent back to RATAN. | MT192/292 is sent to AMH and ACK is message is sent back to RATAN. | Pass | image-2026-7-14_17-29-54.png; image-2026-7-14_17-31-3.png | Shalini Fonseka |
| 4 | FMSGW | Inbound Message | ANY | Back Value Dated message received from RATAN and listed in Back Valued Messages Queue when processed ACK message is sent to inbound system and notification will be sent | Transaction should be present in Back Valued Messages Queue with Validation Failure details and ACK should be sent to inbound system and notification will be sent | Pass | image-2026-7-15_15-56-13.png; image-2026-7-15_15-56-57.png | Shalini Fonseka |
| 6 | FMSGW | Inbound Message | MT103,MT202 | Settlement message hit DEF rule with High Value payment (MT103/MT202) received from RATAN is listed in High value payment Queue once approved then sent to AMH. ACK is message is sent back to RATAN and notification will be sent | MT103/MT202 is sent to AMH and ACK is message is sent back to RATAN and notification will be sent | Pass | image-2026-7-15_15-58-48.png; image-2026-7-15_15-59-21.png; image-2026-7-15_16-0-5.png; image-2026-7-15_16-0-33.png | Shalini Fonseka |
| 7 | FMSGW | Inbound Message | MT103, MT202 | Settlement for Cancel Trade where Original message released. MT202/MT103 is sent to AMH and ACK is message is sent back to RATAN. As the trade is cancelled so the transaction will be available in Manual Cancellation Queue, an ACK is sent to inbound system and User is sent notification through email. In Manual Cancellation Queue user can further process or terminate the transaction. | MT202/MT103 is sent to AMH and ACK is message is sent back to RATAN. | Pass | image-2026-7-14_17-31-51.png; image-2026-7-14_17-33-1.png | Shalini Fonseka |
| 8 | FMSGW | Validation Queue | MTn92 | Swift Payment message where message type is MTn92 will flow to "Manual Cancellation" queue and User will perform Process action on the payment transaction to next Eligible currency validation check. User should be able to login and should be able to open the queue. Search will display Single or Multiple entries depending on the validation check. Detail screen popup window should be opened with tabs - "Data" and "Action audit". User should be able to add comment and Payment transaction should be released for next Eligible currency validation check and it should be disappeared from the Manual cancellation queue. | User should be able to login and should be able to open the queue. | Pass | Cash flow is-M00127114523 | |
| 9 | FMSGW | Duplicate Message | MT103/MT202/ MT202COV | Processing of Duplicate payment message from Duplicate message Queue. Login to Manual Queue -> Navigate to Validation->Duplicate Message Queue and search for the trade in the queue. Perform Process action on the transaction. | Transaction message should be found in Duplicate Message Queue. On Process, Transaction will move to next validations i.e., check for SCB Specific Validations. | Pass | Cash flow id-M00127114976 | |

## Findings

All eight listed scenarios are marked Pass. The passing record supports Sri Lanka-specific UAT coverage of:

- [[fmsgw-inbound-message-routing]] for MT103/MT202COV, MT202, and MT192/MT292 messages;
- [[settlement-acknowledgement-flow]] from FMSGW to RATAN or the inbound system;
- ACK-dependent [[mt103-mt202cov-acknowledgement-sequencing]];
- [[back-valued-message-queue]] handling with validation-failure details and notification;
- approval-gated [[high-value-payment-queue]] handling triggered by a [[def-rule-high-value-payment-routing]];
- [[manual-cancellation-queue]] processing for cancelled trades and MTn92 messages; and
- [[duplicate-message-queue-processing]] forwarding to SCB-specific validations.

## Evidence Limits

The record does not provide message identifiers, execution timestamps, environment details, approval identities, or the contents of its image evidence. Cases 8 and 9 identify cashflows but do not name a tester or provide screenshot references. The register also omits serial number 5; therefore, passing listed cases do not establish that all planned UAT cases passed.

The MT103/MT202COV case states that MT202COV should be released after successful MT103 acknowledgement, but does not specify correlation keys, timeout handling, retry behavior, or duplicate-ACK behavior. These remain open in [[what-is-the-authoritative-mt103-ack-dependent-mt202cov-release-contract]].