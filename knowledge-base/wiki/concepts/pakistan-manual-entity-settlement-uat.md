---
type: concept
title: Pakistan Manual-Entity Settlement UAT
created: 2026-08-23
updated: 2026-08-23
tags: [uat, pakistan, manual-entity, settlement, fmsgw, exception-queues]
related: [pakistan-scb-karachi-khi-in-country, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, mt103-mt202cov-acknowledgement-sequencing, back-valued-message-queue, high-value-payment-queue, manual-cancellation-queue, duplicate-message-queue-processing, country-specific-settlement-uat-coverage, what-is-missing-pakistan-scb-karachi-uat-test-case-5]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/014 PAKISTAN SCB KARACHI KHI(In Country).md"]
---
# Pakistan Manual-Entity Settlement UAT

Pakistan-specific UAT for [[pakistan-scb-karachi-khi-in-country]] records successful execution of eight documented FMSGW scenarios.

## Tested scope

The recorded coverage includes:

- inbound delivery of MT103/202COV, MT202, and MT192/292 from RATAN to AMH with acknowledgement back to RATAN;
- MT202COV release after successful MT103 acknowledgement;
- routing of a back value-dated message to the Back Valued Messages Queue;
- approval of DEF-rule high-value MT103 and MT202 messages before onward delivery;
- cancelled-trade and MTn92 handling in the Manual Cancellation Queue; and
- processing a duplicate message into SCB-specific validations.

## Interpretation

All documented cases are marked passed. This demonstrates the observed behaviour for the tested Pakistan scenarios, but does not independently confirm a global rule for other message variants, entities, approval configurations, notification contracts, or terminal queue outcomes.

The test sequence has no documented Case 5. This prevents the record from being treated as complete UAT coverage; see [[what-is-missing-pakistan-scb-karachi-uat-test-case-5]]. It should be considered alongside [[country-specific-settlement-uat-coverage]] rather than generalized to other country configurations.