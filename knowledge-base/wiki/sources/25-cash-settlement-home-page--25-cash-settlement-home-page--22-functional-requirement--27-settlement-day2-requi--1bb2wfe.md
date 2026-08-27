---
type: source
title: "Auto Netting Datetime Calculation"
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page — Functional Requirement"
tags: [cash-settlement, auto-netting, functional-requirement, settlement-day2, datetime-calculation]
related: [cashflow-auto-netting, business-calendar-relative-netting-time, auto-netting-rule-management, manual-cashflow-netting, netting-un-net-lifecycle, netting-resultant-cashflow-lifecycle, what-is-the-canonical-pending-auto-netting-state-model, what-is-the-authoritative-auto-netting-cutoff-time-semantics]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Datetime Calculation.md"]
---

# Auto Netting Datetime Calculation

## Summary

This functional-requirement discussion addresses how [[concepts/cashflow-auto-netting]] calculates its execution datetime, how weekends and currency holidays affect that calculation, and how cashflows arriving after the calculated datetime should be handled.

The document records proposed behavior and illustrative scenarios. It does not record formal approval, implementation sign-off, or an authoritative final policy.

## Scope

The discussion covers:

- The `VD-1 5AM` value configured in Netting Static.
- The difference between weekend handling and currency-holiday handling.
- Late-arriving cashflows and multiple auto-netting batches.
- The relationship between release date and calculated auto-netting datetime.
- Manual versus automated handling after the netting datetime.
- Withdrawal of a cashflow from an existing netted result and replacement netting.

## Reported XAU/USD discrepancy

| Currency | Payment Date | Date from Netting Static | Auto netting date | CCY Calendar |
| --- | --- | --- | --- | --- |
| XAU | 2025-11-12 | VD-1 5AM | 2025-11-11 5AM | working day on 2025-11-11 |
| USD | 2025-11-12 | VD-1 5AM | 2025-11-10 5AM | USD holiday on 2025-11-11 |

For the example, XAU and USD have the same payment date and configured offset, but USD is calculated for the preceding working date because 2025-11-11 is a USD holiday.

The solution discussion proposes skipping weekends but not currency holidays. Under that proposal, the USD datetime would remain 2025-11-11 5:00, even though that date is a USD holiday. Dinesh confirmed that a datetime falling on an Operations vacation day is acceptable if Operations manually nets the cashflows.

## Original issue timeline

```text
| Event | System Date time | Trade | | Cashflow | Currency | Payment Date | Calculated auto netting date time | Cashflow State | Cashflow Sub State Type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| New cashflow | 2025-11-07 4:00 | T1 | | C1 | XAU | 2025-11-12 | 2025-11-11 5:00 | WAITING | Pending Auto Netting |
| C2 | USD | 2025-11-12 | 2025-11-10 5:00 | WAITING | Pending Auto Netting |
| New cashflow | 2025-11-10 3:00 | T2 | | C3 | XAU | 2025-11-12 | 2025-11-11 5:00 | WAITING | Pending Auto Netting |
| C4 | USD | 2025-11-12 | 2025-11-10 5:00 | WAITING | Pending Auto Netting |
| Auto Netting job | 2025-11-10 5:00 | | | N1 | USD | 2025-11-12 | NA | WAITING | Pending Exception |
| | | C2 | USD | | NA | NETTED | |
| | | C4 | USD | | NA | NETTED | |
| New cashflow | 2025-11-10 7:00 | T3 | | C5 | XAU | | | | |
| | 2025-11-10 7:00 | C6 | USD | | | | |
| | 2025-11-10 7:15 | T4 | | C7 | XAU | | | | |
| | 2025-11-10 7:15 | | C8 | USD | | | | |
| Auto Netting job | 2025-11-10 7:30 | | | N2 | USD | 2025-11-12 | NA | WAITING | Pending Exception |
| | | C6 | USD | | NA | NETTED | |
| | | C8 | USD | | NA | NETTED | |
| Auto Netting job | 2025-11-11 5:00 | | | N3 | XAU | 2025-11-12 | NA | WAITING | Pending Exception |
| | | C1 | XAU | | NA | NETTED | |
| | | C3 | XAU | | NA | NETTED | |
| | | C5 | XAU | | NA | NETTED | |
| | | C7 | XAU | | NA | NETTED | |
```

The timeline illustrates separate batches for USD cashflows at 5:00 and 7:30 on 2025-11-10, followed by an XAU batch at 5:00 on 2025-11-11. It does not define the authoritative inclusion boundary for cashflows created after the calculated datetime.

## Release date comparison

| Cashflow | Currency | Payment Date | Date from Netting Static | Auto netting date (VD-1 without holiday) | Release Date(VD-1 BD) |
| --- | --- | --- | --- | --- | --- |
| C1 | XAU | 2025-11-12 | VD-1 5AM | 2025-11-11 5:00 | 2025-11-11 |
| C2 | USD | 2025-11-12 | VD-1 5AM | 2025-11-11 5:00 | 2025-11-10 |

The USD example shows that a cashflow may be released before its calculated auto-netting datetime. The document does not establish whether these dates must satisfy a formal invariant.

## Proposed behavior after the netting datetime

The discussion proposes configurable handling for cashflows arriving after the netting datetime:

1. Move the cashflow to `Pending Manual Net` for user processing.
2. Automatically net the cashflow after the netting datetime.

The scope of this configuration is not specified. It is also unclear whether a cashflow arriving during job execution belongs to the current batch or a subsequent batch.

## Withdrawal and replacement netting

The illustrative scenario creates `N1` for `C1`, `C2`, and `C3`. Withdrawal of `C1` makes `N1` `DEAD` and `C1` `CANCELLED`. The remaining cashflows and new cashflow `C4` are then either:

- returned to `Pending Auto Netting` and included in replacement resultant `N2`; or
- assigned `Pending Netting`, with no subsequent job shown in the alternative scenario.

The distinction between these states and their processing channels remains unresolved.

## Evidence and limitations

The examples use illustrative trades, cashflows, resultant cashflows, dates, and currencies. The document supports the reported XAU/USD discrepancy and the described scenario behavior, but does not establish that the same behavior applies to all currencies, products, or configurations.

The holiday policy, late-arrival policy, job scheduling behavior, and post-withdrawal state model require confirmation before being treated as authoritative.

## Related wiki topics

- [[concepts/business-calendar-relative-netting-time]]
- [[concepts/cashflow-auto-netting]]
- [[concepts/auto-netting-rule-management]]
- [[concepts/manual-cashflow-netting]]
- [[concepts/netting-un-net-lifecycle]]
- [[concepts/netting-resultant-cashflow-lifecycle]]
- [[queries/what-is-the-canonical-pending-auto-netting-state-model]]
- [[queries/what-is-the-authoritative-auto-netting-cutoff-time-semantics]]