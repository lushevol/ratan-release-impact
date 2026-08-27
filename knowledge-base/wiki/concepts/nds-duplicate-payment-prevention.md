---
type: concept
title: NDS Duplicate Payment Prevention
created: 2026-08-22
updated: 2026-08-22
tags: [NDS, duplicate-payment, risk-control, auto-netting]
related: [nds-auto-netting, nds-netting-key, duplicate-payment-prevention, nds-fixing, ndirs, murex-2-11]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# NDS Duplicate Payment Prevention

NDS Duplicate Payment Prevention is the control problem created when multiple economically equivalent NDS Fixing payments pass RATAN's normal netting eligibility checks.

The source identifies duplicates caused by:

- Non-economic amendments that change trade references without changing the underlying payment.
- Manual booking of an additional FXD trade.
- Re-fixing and cancellation/rebook sequences.
- Additional fixing payments carrying the same or a replacement NID.

Cases 18 and 20 show duplicate NDS Fixing payments that are STP for NDIRS. Cases 21 and 22 show duplicates included in a net resultant, including an incorrect amount in case 21. Case 23 shows a duplicate payment being STP after a prior payment was released.

Matching by NID, status, value date, currency, entity, and counterparty is therefore insufficient without an economic-identity check, duplicate detection, or an explicit operational hold. The source provides no completed remediation or acceptance decision.