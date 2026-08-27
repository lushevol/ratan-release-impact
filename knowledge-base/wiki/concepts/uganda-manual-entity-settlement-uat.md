---
type: concept
title: "Uganda Manual-Entity Settlement UAT"
created: 2026-08-23
updated: 2026-08-23
tags: [UAT, Uganda, manual-entity, settlement, FMSGW, Settlement-Day-2]
related: [uganda-scb-uganda-kam-gbs, manual-entity-settlement-enablement, country-specific-settlement-uat-coverage, fmsgw-inbound-message-routing, settlement-acknowledgement-flow, high-value-payment-queue, manual-cancellation-queue, duplicate-message-queue-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/006 UGANDA SCB UGANDA KAM(GBS).md"]
---

# Uganda Manual-Entity Settlement UAT

This finding summarizes the Settlement Day 2 UAT evidence for [[entities/uganda-scb-uganda-kam-gbs]], a manual settlement entity identified as `UGANDA SCB UGANDA KAM(GBS)`.

## Confirmed scenarios

The tested `FMSGW` workflows passed for standard inbound settlement messages, including `MT103/202COV`, `MT202`, and `MT192/292`. Messages were routed to `AMH`, with acknowledgements returned to `RATAN`. The `MT202 COV` flow was specifically dependent on successful acknowledgement of the related `MT103`.

Exception and control workflows also passed:

- Back-value-dated messages appeared in the `Back Valued Messages Queue` with validation failure details, acknowledgement, and notification.
- DEF-rule high-value `MT103` and `MT202` payments entered the `High value payment Queue` and were released to `AMH` after approval. The recorded test identifier was `M00127115325`.
- Cancel-trade settlement was routed downstream and made available in the `Manual Cancellation Queue` for further processing or termination.
- `MTn92` messages could be reviewed through `Data` and `Action audit`, commented on, and released to the next eligible currency validation check.
- Duplicate `MT103`, `MT202`, and `MT202COV` messages could be processed from the `Duplicate Message Queue` and advanced to `SCB Specific Validations`.

## Interpretation

The evidence strengthens [[concepts/manual-entity-settlement-enablement]] and [[concepts/country-specific-settlement-uat-coverage]] by demonstrating successful UAT coverage for this Uganda entity across both straight-through and queue-mediated workflows.

The results are not a production go-live decision and do not establish that the same configuration or behavior applies to other manual entities. The source also omits test case 5 and leaves the formal ACK, DEF-rule, notification, and post-processing contracts unspecified.
