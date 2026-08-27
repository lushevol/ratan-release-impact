---
type: query
title: How Does LMS Account for Status-Only Settled Stella Cashflows?
tags: [lms, liquidity, settlement-status, stella, migration, cn]
related: [lms, early-settled-cashflow-migration-handling, cn-trade-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md"]
created: 2026-08-23
updated: 2026-08-23
---
# How Does LMS Account for Status-Only Settled Stella Cashflows?

The preferred migration option marks a Stella cashflow `SETTLED` even though the economic payment was completed earlier through Murex 2.11 and no Razor or SWIFT action occurs during the status update.

The source’s sample shows different LMS balances under normal feeding and an undefined “Revived approach.” The authoritative feed event, balance semantics, accounting treatment, and break-handling process require confirmation.