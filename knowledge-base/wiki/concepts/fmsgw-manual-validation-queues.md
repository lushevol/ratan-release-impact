---
type: concept
title: FMSGW Manual Validation Queues
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, validation, manual-processing, settlement, queues]
related: [fmsgw, amh, manual-entity-settlement-enablement, what-is-the-authoritative-manual-cancellation-queue-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/004 KENYA SCB KENYA B NBO(GBS).md"]
---
# FMSGW Manual Validation Queues

FMSGW manual validation queues provide an operational path for exceptions and approval-gated settlement messages rather than immediate downstream release.

## Tested Queue Behaviors

For the Kenya / SCB Kenya B / NBO (GBS) UAT configuration:

- **Back Valued Messages Queue:** back-value-dated messages were listed with validation-failure details. Processing produced an ACK to the inbound system and a notification.
- **High Value Payment Queue:** DEF-rule high-value `MT103` and `MT202` messages required approval before FMSGW forwarded them to [[amh]], returned an ACK to RATAN, and sent a notification.
- **Manual Cancellation Queue:** cancelled trades could be further processed or terminated. `MTn92` entries supported search, a detail screen with **Data** and **Action audit** tabs, comments, and Process to the next eligible-currency validation check.
- **Duplicate Message Queue:** duplicate `MT103`, `MT202`, and `MT202COV` messages could be processed and advanced to SCB Specific Validations.

These results are UAT evidence for one configuration. They do not define queue ownership, permissions, notification recipients, processing time limits, or rollback behavior.