---
type: query
title: What Is the Complete Accounting Behavior for Failed and SWIFT-Suppressed Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [failed-cashflow, swift-suppressed, accounting, ratan, korea]
related: [failed-cashflow-accounting, ratan-accounting-status-lifecycle, korea-ratan-oltp-accounting-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# What Is the Complete Accounting Behavior for Failed and SWIFT-Suppressed Cashflows?

The requirement includes `Failed` and `Swift_suppressed` cashflows in accounting scope, but provides business posting directions only for new and withdrawal events.

It defines `MISSING_INFO` when a `SWIFT_SUPPRESSED` cashflow lacks a Nostro account, but does not state when accounting is generated, reversed, suppressed, or otherwise handled for other failed or suppressed cases. Confirm event-specific posting, reversal, and status rules without generalizing from [[failed-cashflow-accounting]].