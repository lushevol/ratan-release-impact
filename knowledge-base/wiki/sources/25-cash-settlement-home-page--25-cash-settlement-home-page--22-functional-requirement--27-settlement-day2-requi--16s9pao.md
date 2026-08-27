---
type: source
title: Pakistan SCB Karachi KHI (In Country) Settlement UAT
created: 2026-08-23
updated: 2026-08-23
tags: [uat, settlement-day-2, manual-entity, pakistan, fmsgw, ratan, amh]
related: [pakistan-scb-karachi-khi-in-country, pakistan-manual-entity-settlement-uat, what-is-missing-pakistan-scb-karachi-uat-test-case-5, ratan, fmsgw, amh, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, mt103-mt202cov-acknowledgement-sequencing, back-valued-message-queue, high-value-payment-queue, def-rule-high-value-payment-routing, manual-cancellation-queue, duplicate-message-queue-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/014 PAKISTAN SCB KARACHI KHI(In Country).md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Pakistan SCB Karachi KHI (In Country) Settlement UAT

This source records UAT results for enabling Settlement Day 2 processing for [[pakistan-scb-karachi-khi-in-country]]. All eight documented test cases are marked as passed. The tested path is primarily [[ratan]] → [[fmsgw]] → [[amh]], with an acknowledgement returned to RATAN.

The evidence supports the documented Pakistan scenarios only. It does not establish a universal contract for every message type, rule configuration, or manual entity.

## UAT coverage

| Case | Function | Scenario | Expected or recorded outcome | Result | Tester |
| ---: | --- | --- | --- | --- | --- |
| 1 | Inbound Message | MT103/202COV | MT103/202COV received from RATAN, sent to AMH, and acknowledged back to RATAN. `MT202 Cov should be released upon MT103 getting ACK successfully.` | `PASS M00127114476 DV97M00127114476` | Zainab |
| 2 | Inbound Message | MT202 | MT202 received from RATAN, sent to AMH, and acknowledged back to RATAN. | `PASS M00127114484` | Zainab |
| 3 | Inbound Message | MT192/292 | MT192/292 received from RATAN, sent to AMH, and acknowledged back to RATAN. | `PASS M00127114694 DV97M00127114694` | Zainab |
| 4 | Inbound Message | ANY back value-dated message | Transaction is present in Back Valued Messages Queue with Validation Failure details; ACK is sent to the inbound system and notification is sent. | `M00127114472 PASS` | Not recorded |
| 5 | — | Not documented | Not documented. | Not recorded | Not recorded |
| 6 | Inbound Message | MT103, MT202 hitting DEF rule with High Value payment | Message is listed in High Value Payment Queue; after approval it is sent to AMH, ACK is sent back to RATAN, and notification is sent. | `Pass` | Zainab |
| 7 | Inbound Message | Settlement for Cancel Trade where Original message released | MT202/MT103 is sent to AMH and acknowledged to RATAN. The cancelled transaction is available in Manual Cancellation Queue; an ACK and email notification are sent; the user can process or terminate it. | `M00127114456 PASS` | Zainab |
| 8 | Validation Queue | MTn92 | MTn92 flows to Manual Cancellation Queue. The user can search entries, view `Data` and `Action audit` tabs, add a comment, process the payment, and release it to the next Eligible currency validation check. It then disappears from the queue. | `M00127114488 PASS` | Zainab |
| 9 | Duplicate Message | MT103/MT202/MT202COV | The transaction is found in Duplicate Message Queue. On Process, it moves to the next validations: SCB Specific Validations. | `M00127114476 PASS` | Not recorded |

## Observed behaviour

- Standard inbound scenarios for MT103/202COV, MT202, and MT192/292 passed through [[fmsgw-inbound-message-routing]] to AMH, with acknowledgement returned to RATAN.
- The MT202COV scenario records the dependency captured by [[mt103-mt202cov-acknowledgement-sequencing]]: release follows successful MT103 acknowledgement.
- A back value-dated message was placed in the [[back-valued-message-queue]] with validation-failure details, acknowledgement, and notification.
- Tested MT103 and MT202 messages matching a `DEF` rule required manual approval in the [[high-value-payment-queue]] before release to AMH.
- Cancelled-trade and MTn92 scenarios used the [[manual-cancellation-queue]].
- A duplicate-message scenario advanced from the Duplicate Message Queue to SCB-specific validations after manual processing.

## Evidence limitations and follow-up

Test Case 5 is absent from the source sequence; see [[what-is-missing-pakistan-scb-karachi-uat-test-case-5]]. Tester attribution is absent for Cases 4 and 9, and Case 6 has no transaction identifier.

`M00127114476` is recorded for both Case 1 and Case 9. The source does not establish whether this reuse is intentional, represents duplicate-message correlation, or is a documentation error. Exact `DEF` rule conditions, ACK payloads, notification recipients, and final downstream validation states are also not specified.