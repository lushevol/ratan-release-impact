---
type: source
title: "Vietnam SCB Hanoi HNI(GBS) Settlement UAT"
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, settlement-day-2, uat, vietnam, fmsgw, manual-entities]
related: [vietnam-scb-hanoi-hni-gbs, vietnam-scb-hanoi-hni-gbs-settlement-uat-coverage, fmsgw-inbound-message-routing, ratan-fmsgw-amh-settlement-message-routing, mt103-mt202cov-acknowledgement-sequencing, back-valued-message-queue]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/012 VIETNAM SCB HANOI HNI(GBS).md"]
---

# Vietnam SCB Hanoi HNI(GBS) Settlement UAT

## Scope

This UAT evidence document covers inbound settlement-message processing for **Vietnam SCB Hanoi HNI(GBS)** under the Settlement Day 2 enablement of manual entities. The substantive test evidence concerns the **RATAN → FMSGW → AMH** flow. The source contains no substantive content in its `RATAN:` section.

Raw SWIFT payloads are intentionally not reproduced here because the source includes customer names, account numbers, addresses, transaction references, BICs, and payment values. The controlled source document remains the authoritative location for those artifacts.

## Test outcome summary

| Test case | Squad | Function | Scenario | Result | Evidence or limitation |
|---|---|---|---|---|---|
| 1 | FMSGW | Inbound Message | MT103 with associated MT202 COV | Pass | Settlement messages were reported as sent to AMH, with an ACK returned to RATAN. The MT202 COV was reported as released after successful MT103 acknowledgement. |
| 2 | FMSGW | Inbound Message | MT202 | Pass | MT202 was reported as sent to AMH, with an ACK returned to RATAN. |
| 3 | FMSGW | Inbound Message | MT192/292 | Pass | The source reports the cancellation-related message flow as sent to AMH, with an ACK returned to RATAN. The supplied evidence pairs an MT103 with an MT192; no separate MT292 payload is shown. |
| 4 | FMSGW | Inbound Message | Back value-dated message | Pass | The transaction was expected in the Back Valued Messages Queue with validation-failure details, an ACK to the inbound system, and notification. The sample payload does not independently demonstrate the back-valued condition. |
| 5 | — | — | No numbered test case present | Not documented | The source jumps from test case 4 to test case 6. |
| 6 | FMSGW | Inbound Message | DEF-rule high-value MT103/MT202 processing | Descoped | No production scenario was available. |
| 7 | FMSGW | Inbound Message | Cancelled trade after original-message release | Descoped | No production scenario was available. The expected flow included AMH delivery, ACK, notification, and processing or termination in the Manual Cancellation Queue. |
| 8 | FMSGW | Validation Queue | MTn92 Manual Cancellation Queue processing | Descoped | No production scenario was available. Expected steps included queue access, search, detail and audit views, comments, and release to the next eligible-currency validation. |
| 9 | FMSGW | Duplicate Message | Duplicate MT103, MT202, or MT202 COV | Descoped | No production scenario was available. Expected processing would move the transaction from Duplicate Message Queue to SCB-specific validations. |

## Findings

The document records positive UAT coverage for the principal inbound routing path for Vietnam SCB Hanoi HNI(GBS). It provides additional entity-specific evidence for [[concepts/fmsgw-inbound-message-routing]] and [[concepts/ratan-fmsgw-amh-settlement-message-routing]].

The first test provides a positive-path confirmation of [[concepts/mt103-mt202cov-acknowledgement-sequencing]]: MT202 COV release is dependent on successful MT103 acknowledgement. The source does not establish behavior for missing, delayed, rejected, duplicate, or failed ACKs.

The back-valued-message test reports the expected queue, ACK, and notification behavior described by [[concepts/back-valued-message-queue]]. However, the source does not provide a validation record or distinct value-date evidence proving that the supplied message was actually back-valued.

High-value payment routing, cancelled-trade processing, MTn92 manual cancellation, and duplicate-message processing were not validated in this UAT. Their `Descoped` status indicates a coverage gap, not a functional failure or a product limitation.

## Traceability notes

The source uses both “RATAN” and “inbound system” when describing the ACK recipient. RATAN appears to be the inbound system for the tested flow, but the document does not explicitly define those terms as equivalent.

The test inventory is irregularly numbered: cases 1, 2, 3, 4, 6, 7, 8, and 9 are present, while case 5 is absent. Several steps and expected-result fragments are represented as detached rows in the original table, reducing traceability.

## Related systems

- [[entities/vietnam-scb-hanoi-hni-gbs]] — UAT target settlement entity.
- [[entities/ratan]] — Upstream settlement system.
- [[entities/fmsgw]] — Message gateway under test.
- [[entities/amh]] — Downstream messaging system.
- [[concepts/manual-entity-settlement-onboarding]] — Broader manual-entity enablement context.
- [[concepts/country-specific-settlement-uat-coverage]] — Cross-country UAT coverage framework.