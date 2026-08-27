---
type: concept
title: IRS Net-over-Net
created: 2026-08-22
updated: 2026-08-22
tags: [IRS, auto-netting, resultant-cashflow, cash-settlement]
related: [cashflow-auto-netting, irs-resultant-cashflow-netting, netting-resultant-cashflow, swift-versus-cashflow-suppression, taifex, citic, lch, hkex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS.md"]
---
# IRS Net-over-Net

IRS net-over-net is the auto-netting treatment in which IRS aggregation cashflows, identified by `Cashflow__Payment_Type == "IRS Netting"`, may be included in a further netting operation.

## Venue-specific scope

The source distinguishes two scopes:

- For [[taifex]] and [[citic]], auto-netting is restricted to IRS products. The rules also require an IRS taxonomy condition.
- For [[lch]], [[hkex]], and the ECLIPS scope, IRS Netting cashflows are included with other eligible cashflows for the same booking entity, counterparty, currency, and payment date.

This is not a universal policy: each rule is restricted to its defined FMID pair.

## Resultant and suppression treatment

The generated resultant cashflow uses `Clearing_Swift_Suppress` and is NSTP for Maker+Checker. To avoid preempting IRS aggregation cashflows, auto-netting rule approval must precede the update of the corresponding SWIFT-suppression rule.

A non-auto-netted IRS Netting cashflow must not be suppressed merely because it has a netting identifier; an auto-netted IRS Netting cashflow can satisfy the updated suppression condition.

## Open semantics

For TAIFEX and CITIC, the documented expression permits an `IRS Netting` payment type or an empty/null `Cashflow__Netting_Id`, provided the IRS taxonomy condition is met. The source does not explicitly establish whether all unnetted IRS cashflows are intentionally eligible.