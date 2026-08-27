---
type: entity
title: NDIRS
created: 2026-08-22
updated: 2026-08-22
tags: [NDIRS, product-typology, cash-settlement, interest-rate-derivative]
related: [nds-fixing, nds-auto-netting, nds-duplicate-payment-prevention, cashflow-exception-handling, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# NDIRS

NDIRS is a product typology with a specific exception to the general NDS Fixing netting flow.

The USD NDS Fixing cashflow associated with an NDIRS parent trade is intended to settle STP in the deliverable currency and remain outside auto-netting. The source uses NID as the correlation identifier between the NDS Fixing payment and the parent NDIRS trade/payment.

The requirement does not fully specify precedence between this NDIRS STP rule and the generic rule that places NDS Fixing cashflows into `WAITING` with `Pending NDS Netting`. This is tracked in [[queries/what-is-the-precedence-between-ndirs-stp-and-pending-nds-netting]].