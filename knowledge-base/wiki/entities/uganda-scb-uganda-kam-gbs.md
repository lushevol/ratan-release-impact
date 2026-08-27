---
type: entity
title: "UGANDA SCB UGANDA KAM(GBS)"
created: 2026-08-23
updated: 2026-08-23
tags: [manual-entity, Uganda, settlement, UAT, SCB]
related: [ratan, fmsgw, amh, manual-entity-settlement-enablement, settlement-day-2, uganda-manual-entity-settlement-uat]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/006 UGANDA SCB UGANDA KAM(GBS).md"]
---

# UGANDA SCB UGANDA KAM(GBS)

`UGANDA SCB UGANDA KAM(GBS)` is the Uganda-specific manual settlement entity tested for Settlement Day 2 enablement.

## UAT scope

The recorded tests cover inbound settlement messages processed by [[entities/fmsgw]], originating from [[entities/ratan]] and routed to [[entities/amh]]. The scenarios include:

- `MT103/202COV`, `MT202`, and `MT192/292` settlement routing with ACK return.
- Back-value-dated message handling.
- DEF-rule high-value payment approval.
- Cancel-trade settlement.
- `MTn92` manual cancellation processing.
- Duplicate-message processing through `SCB Specific Validations`.

All listed test cases are marked **Pass**.

## Observed behavior

The UAT records that `MT202 COV` is released after the related `MT103` receives a successful ACK. High-value payments are held in the `High value payment Queue` until approval. Cancelled or special messages are exposed through the `Manual Cancellation Queue` for user action, while duplicate messages can be processed and advanced to the next validation stage.

The evidence is specific to this entity and should not be generalized to other manual entities without equivalent testing.

## Limitations

The source does not identify test case 5, define the exact DEF rule, specify formal ACK contracts, or confirm production enablement approval.

See [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--18efgz3]] for the complete UAT matrix.
