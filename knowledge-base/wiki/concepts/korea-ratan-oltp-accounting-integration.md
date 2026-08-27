---
type: concept
title: Korea RATAN-to-OLTP Accounting Integration
created: 2026-08-23
updated: 2026-08-23
tags: [korea, ratan, oltp, payment-accounting, real-time-integration]
related: [payment-accounting-flow, ratan-accounting-status-lifecycle, oltp-accounting-message-contract, oltp-accounting-eligibility-blacklist]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# Korea RATAN-to-OLTP Accounting Integration

This is the Korea-specific implementation of [[payment-accounting-flow]] in which [[ratan]] replaces Murex-KR as the real-time sender of cashflow accounting entries to [[oltp]].

The cashflow population is intended to remain unchanged from the Murex-KR-to-RATAN population. RATAN creates a two-leg Bridge/Nostro accounting entry, delivers it through Solace, and waits for the OLTP outcome before recording success.

The requirement defines no cutover plan, parallel-run reconciliation, rollback process, duplicate-message handling, or timeout-resolution model.