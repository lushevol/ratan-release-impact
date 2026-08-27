---
type: concept
title: FMRP Payment Insertion Eligibility
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, payment-insertion, entity-eligibility, precious-metals, murex-211]
related: [fmrp, murex-211, precious-metal-cashflow-vostro-requirement, precious-metal-currency-classification, ratan-murex-211-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
---
# FMRP Payment Insertion Eligibility

FMRP payment insertion is conditionally routed by `PayInsertionFilter` in the revised RATAN-11101 workflow.

A payment is discarded when either condition applies:

1. Its Murex entity has no matching `M_ENTITY` entry in `FMRP_ENTITY_DBF`.
2. Any payment flow under the same `M_TRN_REF` uses a currency where `CURRENCY_DBF.M_BUL_CUR_FL='Y'`.

Otherwise, the payment is processed and routed to `SNTR`.

## Trade-level precious-metal exclusion

The precious-metal test is not limited to the current flow. It searches all `PAY_FLOW_DBF` records sharing the current flow's trade reference. A single qualifying currency leg therefore excludes all payment flows for that trade from FMRP insertion.

This is an FMRP-specific routing rule. It is related to [[precious-metal-cashflow-vostro-requirement]] and [[precious-metal-currency-classification]], but the source does not establish that the same exclusion applies to other settlement workflows.

## Revision status

This filter replaces the earlier direct insertion route from `docPayment` to `INIT2SNTR`. The subsequent `SNTR` processing behavior is not defined in the source.