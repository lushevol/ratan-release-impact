---
type: concept
title: Functional versus Data Entitlement
created: 2026-08-24
updated: 2026-08-24
tags: [entitlement, authorization, functional-access, data-access, ratan, ces, ems2]
related: [ces, ems2, ratan-data-entitlement, what-is-the-authoritative-ratan-ces-entitlement-api-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and CES 55508.md"]
---
# Functional versus Data Entitlement

The RATAN–CES overview separates functional entitlement from data entitlement.

- **Functional entitlement** controls whether a user can access menus, buttons, and application functions. The source assigns this responsibility to [[ems2]].
- **Data entitlement** controls which data a user may view after access to a relevant function. The source assigns scoped cashflow-blotter data entitlement to [[ces]].

CES is stated to apply to data entitlement in the RATAN Cashflow blotter and BCS Cashflow blotter only, qualified as the current scope. The source does not define how CES and EMS2 decisions are composed in the UI or backend, or whether any conflicting decisions can occur.

This boundary must not be conflated with settlement business-rule evaluation performed by other RATAN rule components.