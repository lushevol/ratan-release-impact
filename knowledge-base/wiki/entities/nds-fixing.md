---
type: entity
title: NDS Fixing
created: 2026-08-22
updated: 2026-08-22
tags: [NDS-Fixing, product-typology, cash-settlement, FXD]
related: [nds-auto-netting, nds, n dirs, net-resultant-cashflow, nds-duplicate-payment-prevention, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# NDS Fixing

NDS Fixing is a product typology that participates in NDS auto-netting except where the parent trade is NDIRS and the payment is the specified deliverable-currency USD flow.

For the NDIRS case, the NDS Fixing payment is intended to be STP, is not netted, and uses NID to correlate the fixing payment with the parent NDIRS trade and payment. For other qualifying parent typologies, the payment is expected to wait with `Pending NDS Netting`.

The test scenarios show that NDS Fixing payments can be duplicated by non-economic amendments, re-fixing, or manual FXD bookings. Eligibility based only on NID and status can therefore produce an incorrect net resultant.