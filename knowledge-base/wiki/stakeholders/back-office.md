---
type: stakeholder
title: Back Office
created: 2026-08-24
updated: 2026-08-24
tags: [back-office, trade-validation, murex-211, trade-status]
related: [murex-211, ratan, trade-validation-cashflow-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/UAT test cases - Murex 2.11 booking.md"]
---
# Back Office

Back Office (BO) is a trade-status control role in the tested Murex 2.11 workflows. BO rejects trades to `TQRY` in scenarios involving rework, C&R, and cancellation.

These status transitions influence which trade and cashflow versions remain in RATAN’s Group Blotter and which replacement payment is eligible for automatic release after validation. The source does not specify BO ownership beyond rejection actions or define additional approval requirements.