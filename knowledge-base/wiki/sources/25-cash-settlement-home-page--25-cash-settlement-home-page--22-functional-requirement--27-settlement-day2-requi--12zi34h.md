---
type: source
title: Bangladesh SCB Dhaka DAC In-Country UAT Testing
authors: []
year: 2026
url: ""
venue: Internal UAT evidence
created: 2026-08-23
updated: 2026-08-23
tags: [uat, bangladesh, fmsgw, manual-entity-settlement, swift, settlement-day-2]
related: [scb-dhaka-dac-in-country, fmsgw, ratan, amh, country-specific-settlement-uat-coverage, ratan-fmsgw-amh-settlement-message-routing, mt202cov-ack-dependent-release, back-valued-message-queue, def-rule-high-value-payment-routing, fmsgw-duplicate-message-processing, was-bangladesh-duplicate-message-reprocessing-executed-and-validated, are-delete-rule-queue-and-delete-message-queue-the-same-fmsgw-queue, when-will-bangladesh-deferred-stp-release-be-uat-tested]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/015 BANGLADESH SCB DHAKA DAC(In Country).md"]
---
# Bangladesh SCB Dhaka DAC In-Country UAT Testing

This source records FMSGW UAT evidence for [[scb-dhaka-dac-in-country]], a Bangladesh in-country manual settlement entity. The document contains an empty RATAN section and nine FMSGW scenarios.

## Outcome Summary

Seven scenarios passed and two were de-scoped. No scenario was recorded as failed or blocked.

- **Passed:** inbound MT103/MT202COV, MT202, and MT192/MT292 routing; manual-queue deletion approval; back-valued message handling; DEF-rule high-value approval; duplicate-message queue placement.
- **De-scoped:** scheduler-driven deferred STP release; explicit duplicate-message processing into subsequent SCB-specific validation.

This is country-specific UAT evidence. It supports the stated FMSGW behaviour for Bangladesh, not a global specification of [[ratan]], [[fmsgw]], or [[amh]].

## UAT Test Matrix

| ID | Squad | Function | Scenario | Expected result | Evidence | Result |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | FMSGW | Inbound Message | MT103/202COV from RATAN to AMH, with ACK returned to RATAN | MT103/202COV reaches AMH; ACK returns to RATAN; MT202COV releases after successful MT103 ACK | ![image-2026-7-14_14-13-5.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-14_14-13-5.png) ![image-2026-7-14_14-13-30.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-14_14-13-30.png) | PASS |
| 2 | FMSGW | Inbound Message | MT202 from RATAN to AMH, with ACK returned to RATAN | MT202 reaches AMH and ACK returns to RATAN | ![image-2026-7-14_14-14-43.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-14_14-14-43.png) | PASS |
| 3 | FMSGW | Inbound Message | MT192/292 from RATAN to AMH, with ACK returned to RATAN | MT192/292 reaches AMH and ACK returns to RATAN | ![image-2026-7-14_14-15-15.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-14_14-15-15.png) ![image-2026-7-14_14-16-22.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-14_14-16-22.png) | PASS |
| 4 | FMSGW | Manual Queue | Delete MT103/MT202 from Manual Release Queue | Message enters the applicable Low Value, Threshold, or High Value Approval Queue; an approver can filter and approve it; it reaches the Delete Message Queue | ![image-2026-7-20_14-28-4-1.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-20_14-28-4-1.png) ![image-2026-7-20_14-28-11-1.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-20_14-28-11-1.png) ![image-2026-7-20_14-28-36-1.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-20_14-28-36-1.png) | PASS |
| 5 | FMSGW | Inbound Message | Back-valued message from RATAN | Message appears in Back Valued Messages Queue with validation-failure details; ACK and notification are sent | ![image-2026-7-14_14-17-19.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-14_14-17-19.png) | PASS |
| 6 | FMSGW | Inbound Message | MT103/MT202 matching DEF rule and high-value condition | Message enters High Value Payment Queue; after approval it reaches AMH; ACK and notification are sent | ![image-2026-7-20_14-27-26.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-20_14-27-26.png) ![image-2026-7-20_14-27-50.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-20_14-27-50.png) | PASS |
| 7 | FMSGW | Deferred Message Queue | Scheduled STP release for MT103, MT202, or MT202COV above the high-value setup | Deferred message releases automatically to High Value Approval Queue; approved message reaches AMH | Back-valued UAT dates and manually processed May data made the deferred-queue scenario inapplicable | De-scope |
| 8 | FMSGW | Duplicate Message | Potential duplicate MT103, MT202, or MT202COV | Transaction is available in the Duplicate Message Queue | ![image-2026-7-22_11-10-54-1.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-22_11-10-54-1.png) ![image-2026-7-22_11-11-0-1.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-22_11-11-0-1.png) ![image-2026-7-22_11-11-6-1.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-22_11-11-6-1.png) ![image-2026-7-22_11-11-14-1.png](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h/image-2026-7-22_11-11-14-1.png) | PASS |
| 9 | FMSGW | Duplicate Message | Process a message from the Duplicate Message Queue | On Process, the message moves to subsequent SCB-specific validations | Recorded as covered by case 8, but case 8 documents only queue presence | De-scope |

## Supported Findings

The passed cases support Bangladesh-specific evidence for:

- [[ratan-fmsgw-amh-settlement-message-routing]] for MT103/MT202COV, MT202, and MT192/MT292.
- [[mt202cov-ack-dependent-release]]: MT202COV release follows a successful MT103 ACK.
- [[back-valued-message-queue]] handling with validation-failure details and an ACK.
- [[def-rule-high-value-payment-routing]] followed by approval and dispatch to AMH.
- Duplicate-message detection and placement in the Duplicate Message Queue.

## Scope Limitations

The source does not evidence scheduler-driven deferred-message release for Bangladesh. Case 7 was explicitly de-scoped and cannot support a claim that deferred STP release works.

Duplicate reprocessing is not independently confirmed. Case 9 was de-scoped as allegedly covered by case 8, while case 8's stated expected result verifies only queue placement. See [[was-bangladesh-duplicate-message-reprocessing-executed-and-validated]].

The deletion workflow uses both “Delete Rule Queue” and “Delete Message Queue” without defining their relationship. See [[are-delete-rule-queue-and-delete-message-queue-the-same-fmsgw-queue]].

The source states that notifications are sent in cases 5 and 6 but does not identify recipients, delivery status, notification content, or audit evidence. Screenshot filename dates should not be treated as authoritative test-execution dates without supporting metadata.