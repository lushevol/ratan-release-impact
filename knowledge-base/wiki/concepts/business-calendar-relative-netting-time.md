---
type: concept
title: Business-Calendar-Relative Netting Time
created: 2026-08-22
updated: 2026-08-22
tags: [business-calendar, netting-time, booking-entity, cash-settlement, scheduling]
related: [cashflow-auto-netting, auto-netting-rule-management, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Cashflow Auto Netting- 2024.md"]
---
# Business-Calendar-Relative Netting Time

Business-calendar-relative netting time is the scheduling model in which an auto-netting rule specifies a relative business date and time rather than a fixed calendar timestamp.

## Supported Expressions

Day 1 supports:

- `VD` plus time.
- `VD-1` plus time.
- `VD-2` plus time.

Booking Entity is mandatory because the calculated netting date uses the business calendar associated with the booking entity's home currency.

## Home-Currency Mapping

| Booking entity jurisdiction | Home currency |
|---|---|
| INDIA | INR |
| CHINA | CNY |
| SINGAPORE | SGD |
| MALAYSIA | MYR |
| UK | GBP |
| GERMANY | EUR |

The requirement does not fully define whether `VD` means payment date, valuation date, or another business date in every context. It also leaves time-zone handling, non-business-day rollover, and event-time versus receipt-time authority unresolved. These questions are tracked in [[queries/what-is-the-authoritative-auto-netting-cutoff-time-semantics]].
