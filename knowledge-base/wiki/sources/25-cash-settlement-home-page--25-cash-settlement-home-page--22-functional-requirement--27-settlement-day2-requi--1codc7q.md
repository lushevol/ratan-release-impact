---
type: source
title: Tanzania SCB DAR In-Country UAT
created: 2026-08-23
updated: 2026-08-23
tags: [uat, tanzania, scb, fmsgw, ratan, amh, manual-entity-settlement, swift]
related: [tanzania-scb-dar, manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, fmsgw-manual-payment-validation-queues, high-value-payment-queue, duplicate-message-queue-processing, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, what-is-the-authoritative-mt103-ack-dependent-mt202cov-release-contract, is-tanzani-the-intended-country-identifier-for-tanzania]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/007 TANZANIA SCB TANZANI DAR(In Country).md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Tanzania SCB DAR In-Country UAT

This UAT record documents seven FMSGW scenarios for Tanzania SCB DAR in-country manual-entity settlement processing. Every recorded scenario is marked **PASS**. The tested scope covers manual-queue deletion and approval, duplicate-message handling, and inbound message routing between [[ratan]], [[fmsgw]], and [[amh]].

## Reported Results

| Scenario | Scope | Message types | Reported passing behavior |
|---|---|---|---|
| 1 | Manual Queue | MT103, MT202 | A message deleted from Manual Release Queue enters a Low Value, Threshold, or High Value Approval Queue; after approval it is sent to the deletion queue. |
| 2 | Manual Queue | MT103, MT202 | A high-value message received from RATAN is approved, sent to AMH, ACKed to RATAN, and a notification is sent. |
| 3 | Duplicate Message | MT103, MT202, MT202COV | Selecting Process in Duplicate Message Queue advances the transaction to SCB Specific Validations. |
| 4 | Duplicate Message | MT103, MT202, MT202COV | Selecting Terminate results in `NACKED TERMINATED`, visible in Global Search. |
| 5 | Inbound Message | MT103, MT202COV | Messages are sent to AMH and ACKed to RATAN; MT202COV is released after successful MT103 ACK. |
| 6 | Inbound Message | MT202 | MT202 is sent to AMH and ACKed to RATAN. |
| 7 | Inbound Message | MT192, MT292 | MT192 and MT292 are sent to AMH and ACKed to RATAN. |

## Evidence and Limits

The sheet provides PASS results, screenshots, and transaction references `DV50M0 0127115005` and `M00127115245`. It supports successful execution of the listed Tanzania configuration paths, but does not establish retry behavior, correlation keys, ACK/NACK semantics, authorization controls, queue-failure handling, or AMH business acceptance.

The source alternates between **Delete Rule Queue** and **Delete Message Queue** without stating whether they are the same queue. It also uses the deployment identifier `TANZANI DAR` in the filename, while the document context identifies Tanzania. See [[is-tanzani-the-intended-country-identifier-for-tanzania]].

## Related Evidence

This source adds country-specific evidence to [[country-specific-settlement-uat-coverage]] and [[manual-entity-settlement-onboarding]]. It supports the limited UAT observation recorded for the ACK-gated MT202COV path, but does not resolve [[what-is-the-authoritative-mt103-ack-dependent-mt202cov-release-contract]].