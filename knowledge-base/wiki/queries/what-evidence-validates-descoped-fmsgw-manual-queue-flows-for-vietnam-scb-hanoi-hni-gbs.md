---
type: query
title: What Evidence Validates Descoped FMSGW Manual-Queue Flows for Vietnam SCB Hanoi HNI(GBS)?
created: 2026-08-23
updated: 2026-08-23
tags: [query, fmsgw, uat, manual-queues, vietnam, coverage-gap]
related: [vietnam-scb-hanoi-hni-gbs-settlement-uat-coverage, high-value-payment-queue, manual-cancellation-queue, fmsgw-duplicate-message-processing, fmsgw, vietnam-scb-hanoi-hni-gbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/012 VIETNAM SCB HANOI HNI(GBS).md"]
---

# What Evidence Validates Descoped FMSGW Manual-Queue Flows for Vietnam SCB Hanoi HNI(GBS)?

## Question

What approved test evidence is available for the Vietnam SCB Hanoi HNI(GBS) flows that were descoped because production scenarios were unavailable?

## Unvalidated areas

The source provides no execution evidence for:

- DEF-rule high-value MT103/MT202 routing through the High Value Payment Queue.
- Cancelled-trade processing through the Manual Cancellation Queue.
- MTn92 processing, user actions, comments, audit details, and release to the next eligible-currency validation.
- Duplicate MT103, MT202, or MT202 COV processing through Duplicate Message Queue and subsequent SCB-specific validations.

## Evidence needed

A complete follow-up should identify test data or approved production-like scenarios, queue screenshots or audit records, message delivery records, ACK records, notification evidence, and final transaction states. The result should distinguish unavailable test data from unavailable system capability.

Until such evidence is found, these paths should remain marked as unvalidated for this entity.