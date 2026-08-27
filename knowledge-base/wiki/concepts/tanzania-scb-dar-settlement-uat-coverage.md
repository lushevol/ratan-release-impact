---
type: concept
title: Tanzania SCB DAR Settlement UAT Coverage
created: 2026-08-23
updated: 2026-08-23
tags: [uat, tanzania, fmsgw, settlement, manual-queue, duplicate-message, inbound-routing]
related: [tanzania-scb-dar, country-specific-settlement-uat-coverage, fmsgw-manual-payment-validation-queues, duplicate-message-queue-processing, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, what-is-the-authoritative-mt103-ack-dependent-mt202cov-release-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/007 TANZANIA SCB TANZANI DAR(In Country).md"]
---
# Tanzania SCB DAR Settlement UAT Coverage

Tanzania SCB DAR has documented UAT coverage for seven FMSGW settlement-message scenarios, all recorded as PASS.

## Covered Paths

- Manual Release Queue deletion routes MT103 and MT202 through Low Value, Threshold, or High Value Approval Queue and onward to a stated deletion queue.
- High-value approval forwards MT103 and MT202 to AMH, returns an ACK to RATAN, and reports a notification.
- Duplicate-message Process advances MT103, MT202, and MT202COV to SCB Specific Validations.
- Duplicate-message Terminate produces `NACKED TERMINATED` and Global Search visibility.
- Inbound routing sends MT103, MT202COV, MT202, MT192, and MT292 from RATAN to AMH and returns ACKs to RATAN.
- The MT202COV path was tested with release after successful MT103 ACK.

## Scope Boundary

The evidence is country-specific and scenario-specific. It does not demonstrate negative paths, retries, idempotency, authorization behavior, timing limits, delivery confirmation for notifications, or protocol-level correlation and ordering rules. It contributes evidence to [[country-specific-settlement-uat-coverage]] rather than defining a universal FMSGW contract.