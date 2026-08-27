---
type: source
title: Qatar SCB Doha FMSGW UAT
authors: []
year: 2026
url: ""
venue: UAT testing
created: 2026-08-23
updated: 2026-08-23
tags: [uat, qatar, scb-doha, fmsgw, ratan, settlement-messages, manual-entities]
related: [ratan, fmsgw, amh, qatar-scb-doha, ratan-fmsgw-amh-settlement-message-routing, fmsgw-manual-payment-validation-queues, what-is-the-authoritative-mt103-ack-dependent-mt202cov-release-contract, what-are-the-fmsgw-ack-failure-retry-and-idempotency-rules-for-ratan-settlement-messages, what-are-the-authorization-and-terminal-outcome-rules-for-fmsgw-manual-queues]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/002 QATAR SCB DOHA DOH(GBS).md"]
---
# Qatar SCB Doha FMSGW UAT

This source records UAT evidence for settlement-message processing for the Qatar SCB Doha (DOH/GBS) manual-entity scope. It tests the path from [[ratan]] through [[fmsgw]] to [[amh]], including acknowledgement return, validation queues, manual processing, notifications, and audit visibility.

## UAT outcome

Eight documented scenarios passed. The source numbering is 1, 2, 3, 4, 6, 7, 8, and 9; scenario 5 is not present. The all-pass result supports the listed UAT paths only and does not establish production readiness, resilience, or behavior outside Qatar SCB Doha.

| Scenario | Message or condition | Passed behavior | Tester |
| --- | --- | --- | --- |
| 1 | MT103/MT202COV | FMSGW sent messages from RATAN to AMH and returned an ACK to RATAN. | M00127115372 |
| 2 | MT202 | FMSGW sent MT202 from RATAN to AMH and returned an ACK to RATAN. | DVQAM00127114408 |
| 3 | MT192/MT292 | FMSGW sent cancellation-related messages from RATAN to AMH and returned an ACK to RATAN. | Not specified |
| 4 | Back-value-dated message | FMSGW placed the transaction in Back Valued Messages Queue with validation-failure details, sent an ACK to the inbound system, and issued a notification. | Not specified |
| 6 | High-value MT103/MT202 matching DEF rule | FMSGW placed payment in High Value Payment Queue; after approval, it sent the message to AMH, returned an ACK, and issued a notification. | M00127115373 |
| 7 | Cancelled trade after original-message release | Original MT103/MT202 was sent to AMH with ACK returned to RATAN; cancelled transaction became available in Manual Cancellation Queue with ACK and email notification. | DVQAM00127114702 |
| 8 | MTn92 | FMSGW routed message to Manual Cancellation Queue. A user could search, view Data and Action audit tabs, add a comment, and process it to eligible-currency validation. | M00127115369 |
| 9 | Duplicate MT103/MT202/MT202COV | FMSGW placed the message in Duplicate Message Queue; Process advanced it to SCB-specific validations. | Not specified |

## Confirmed workflow patterns

- The tested nominal routing path is [[ratan]] → [[fmsgw]] → [[amh]], followed by an ACK from FMSGW to RATAN.
- A source note states that MT202COV should be released only after MT103 receives a successful ACK.
- Exceptional messages can remain operationally visible in dedicated validation queues while ACK and notification behavior occurs.
- Manual Cancellation Queue processing exposes Data and Action audit tabs and permits comments before progression.
- Queue processing and release behavior is documented only for the Qatar SCB Doha UAT scope.

## Source limitations

The source does not define ACK type or semantics, correlation identifiers, retry policy, idempotency, AMH failure handling, negative acknowledgements, timeout behavior, notification recipients, or queue authorization rules. It does not test high-value rejection or expiry, duplicate termination, or MT202COV behavior after absent or unsuccessful MT103 acknowledgement.

Referenced screenshots remain source evidence:

- `attachments/image-2026-7-29_11-56-39.png`
- `attachments/image-2026-7-27_12-33-35.png`
- `attachments/image-2026-7-13_14-34-50.png`
- `attachments/image-2026-7-29_12-3-57.png`
- `attachments/image-2026-7-8_9-51-26.png`
- `attachments/image-2026-7-30_13-0-31.png`
- `attachments/image-2026-7-10_16-23-30.png`

See [[ratan-fmsgw-amh-settlement-message-routing]] and [[fmsgw-manual-payment-validation-queues]] for the concepts derived from this UAT evidence.