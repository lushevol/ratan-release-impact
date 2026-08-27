---
type: concept
title: Pending NDS Netting
created: 2026-08-22
updated: 2026-08-22
tags: [NDS, NSTP, exception, WAITING, RATAN]
related: [nds-auto-netting, cashflow-exception-handling, cashflow-blotter-action-eligibility, ratan-cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# Pending NDS Netting

`Pending NDS Netting` is the NSTP exception used to hold eligible NDS component cashflows until the next RATAN auto-netting cycle.

A qualifying cashflow should have:

- Main status `WAITING`
- A pending exception containing `Pending NDS Netting`
- A value date within today, tomorrow, or the next business day
- Matching Booking Entity, Counterparty, value date, currency, and NID

The NSTP rule must be live when auto-netting runs. An absent, disabled, or differently named rule may leave cashflows in `WAITING` and prevent processing.

The generic rule does not apply identically to the NDIRS USD NDS Fixing flow, which is intended to be STP. Rule precedence remains unresolved.