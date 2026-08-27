---
type: source
title: "Enable Settlement for Manual Entities — Bahrain SCB UAT"
authors: []
year: 2026
url: ""
venue: "UAT evidence"
tags: [uat, cash-settlement, manual-entities, bahrain, scb, fmsgw]
related: [ratan, amh, bahrain-scb-bahrai-man-gbs, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, back-valued-message-queue, high-value-payment-queue, manual-cancellation-queue, duplicate-message-queue-processing, fmsgw]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/001 BAHRAIN-SCB BAHRAI MAN(GBS).md"]
---
# Enable Settlement for Manual Entities — Bahrain SCB UAT

## Summary

This source records UAT evidence for settlement processing for the manual entity `BAHRAIN-SCB BAHRAI MAN(GBS)`. The system under test is [[fmsgw]], with inbound settlement messages received from [[ratan]] and supported messages forwarded to [[amh]].

All nine visible test cases are marked **Pass**. The numbering skips test case 5, so the source does not establish whether that case was omitted, descoped, or documented elsewhere.

## Tested behaviors

- `MT103/202COV` routing from RATAN to AMH with an ACK returned to RATAN.
- Release of `MT202COV` after successful acknowledgement of the related `MT103`.
- Standalone `MT202` routing and acknowledgement.
- `MT192/292` routing and acknowledgement.
- Back-value-dated message handling through the Back Valued Messages Queue.
- High-value payment handling through the High Value Payment Queue after a DEF rule match.
- Cancelled-trade handling through the Manual Cancellation Queue.
- `MTn92` processing and release to the next eligible-currency validation check.
- Duplicate-message processing from the Duplicate Message Queue to SCB Specific Validations.

## UAT matrix

| S.no | Squad | Type/Functions | Test Case/Scenario | Expected Result | Result | Tester / Identifier |
|---:|---|---|---|---|---|---|
| 1 | FMSGW | Inbound Message | `MT103/202COV` | Send the settlement message to AMH, return an ACK to RATAN, and release `MT202COV` after successful `MT103` acknowledgement. | Pass | Screenshots attached |
| 2 | FMSGW | Inbound Message | `MT202` | Send `MT202` to AMH and return an ACK to RATAN. | Pass | Gokul; `S00000120389` |
| 3 | FMSGW | Inbound Message | `MT192/292` | Send `MT192/292` to AMH and return an ACK to RATAN. | Pass | Gokul; `DV55M00127113942` |
| 4 | FMSGW | Inbound Message | Any back-value-dated message | Place the transaction in the Back Valued Messages Queue with validation-failure details, send an ACK to the inbound system, and send a notification. | Pass | `DV55M00127114754` |
| 6 | FMSGW | Inbound Message | `MT103`, `MT202` high-value payment matching a DEF rule | Place the message in the High Value Payment Queue; after approval, send it to AMH, return an ACK to RATAN, and send a notification. | Pass | Screenshots attached |
| 7 | FMSGW | Inbound Message | `MT103`, `MT202` cancellation where the original message was released | Send the message to AMH, return an ACK, place the transaction in the Manual Cancellation Queue, notify the user by email, and allow processing or termination. | Pass | Gokul; `M00127113321` |
| 8 | FMSGW | Validation Queue | `MTn92` | Allow the user to search the Manual Cancellation Queue, inspect Data and Action audit tabs, add a comment, process the transaction, and release it to the next eligible-currency validation check. | Pass | `DV55M00127113321` |
| 9 | FMSGW | Duplicate Message | `MT103`, `MT202`, `MT202COV` | Find the transaction in the Duplicate Message Queue and move it to SCB Specific Validations after Process. | Pass | Screenshots attached |

## Evidence references

The source includes the following attachment references:

- Test 1: `image-2026-6-29_10-57-42.png`, `image-2026-6-29_10-58-55.png`, `image-2026-6-29_10-59-36.png`, `image-2026-7-27_10-31-42.png`, `image-2026-7-27_10-33-2.png`
- Test 2: `image-2026-7-6_11-36-49.png`, `image-2026-7-6_11-36-10.png`
- Test 3: `image-2026-7-27_10-54-35.png`, `image-2026-7-27_10-55-38.png`, `image-2026-7-27_10-53-42.png`, `image-2026-7-13_17-56-23.png`, `image-2026-7-13_17-56-51.png`
- Test 4: `image-2026-7-28_17-13-8.png`, `image-2026-7-28_17-14-27.png`, `image-2026-7-28_17-14-54.png`, `image-2026-7-28_17-18-54.png`, `image-2026-7-28_17-19-27.png`, `image-2026-7-28_17-19-58.png`, `image-2026-7-28_17-21-21.png`, `image-2026-7-28_17-22-36.png`, `image-2026-7-28_17-23-30.png`
- Test 6: `image-2026-7-10_16-50-1.png`, `image-2026-7-10_16-52-55.png`, `image-2026-7-10_17-0-21.png`, `image-2026-7-27_11-8-30.png`, `image-2026-7-13_11-10-43.png`, `image-2026-7-13_11-11-22.png`, `image-2026-7-13_11-11-51.png`, `image-2026-7-22_10-7-57.png`, `image-2026-7-28_17-27-56.png`
- Test 7: `image-2026-7-6_12-9-0.png`, `image-2026-7-8_8-28-37.png`, `image-2026-7-8_8-29-8.png`, `image-2026-7-27_11-11-58.png`
- Test 8: `image-2026-7-6_12-33-59.png`, `image-2026-7-27_11-20-47.png`, `image-2026-7-6_12-47-18.png`, `image-2026-7-27_11-16-32.png`
- Test 9: `image-2026-7-10_16-34-53.png`, `image-2026-7-10_16-36-41.png`, `image-2026-7-10_16-40-33.png`, `image-2026-7-10_16-41-16.png`, `image-2026-7-22_10-11-16.png`

The attachment content is not represented in the text source; ACK payloads, timestamps, queue records, notification contents, and downstream AMH confirmations therefore remain unverified from the extracted text alone.

## Limitations and open questions

- Test case 5 is absent.
- ACK terminology varies between “ACK sent to RATAN” and “ACK sent to inbound system.”
- Notification recipients, templates, timing, delivery status, and retry behavior are unspecified.
- The DEF rule and high-value threshold are not identified.
- The exact validation state transitions and audit records are not provided.
- The relationship between cancelled trades and `MTn92` entries in the Manual Cancellation Queue is not defined.
- No negative, blocked, or descoped test results are recorded.

## Related wiki context

This UAT evidence extends [[entities/fmsgw]] with manual-entity settlement results and relates to [[concepts/fmsgw-inbound-message-routing]], [[concepts/settlement-acknowledgement-flow]], and the queue-specific exception workflows documented in the linked concept pages.