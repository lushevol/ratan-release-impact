---
type: concept
title: CN Migration Cutover Value-Date Rules
tags: [cn, migration, cutover, value-date, settlement]
related: [cn-trade-migration, murex-2-11, stella, ratan, early-settled-cashflow-migration-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md"]
created: 2026-08-23
updated: 2026-08-23
---
# CN Migration Cutover Value-Date Rules

The proposed CN cutover model partitions settlement ownership by value date.

- VD on or before 10 May is intended for Murex 2.11 → Ratan settlement, completed by EOD on 10 May.
- 11–12 May is reserved for migration activity.
- VD on or after 13 May is intended for Stella → Ratan FMRP processing.
- A client may request a VD 13 May payment to settle early on 10 May, which creates an overlap requiring [[early-settled-cashflow-migration-handling]].

The source labels these dates as assumptions. They should not be treated as confirmed historical migration dates without corroborating records.

Migrated Stella trades are intended to start with an effective date of 12 May. FO/MO updates may only advance that effective date; cashflows with an earlier VD are not intended to be affected by later market events.