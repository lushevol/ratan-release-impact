---
type: concept
title: NDS Netting Key
created: 2026-08-22
updated: 2026-08-22
tags: [NDS, netting, correlation, NID]
related: [nds-auto-netting, ratan-cashflow-id-management, cashflow-logical-model, duplicate-payment-prevention]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# NDS Netting Key

The NDS Netting Key is the composite identity used to determine which component cashflows may be combined by RATAN.

It consists of:

- Booking Entity
- Counterparty
- Same value date
- Currency
- NID

NID is the correlation component linking NDS, NDS Fixing, and parent-trade cashflows. The source demonstrates that this key is not necessarily an economic uniqueness key: non-economic trade-reference changes and manual FXD bookings can create duplicate payments that still satisfy the grouping conditions.

NID stability across amendments and rebookings therefore requires explicit confirmation before the key can be treated as a sufficient duplicate-prevention control.