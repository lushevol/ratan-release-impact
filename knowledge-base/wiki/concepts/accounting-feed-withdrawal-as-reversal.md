---
type: concept
title: Accounting-Feed Withdrawal as Reversal
created: 2026-08-24
updated: 2026-08-24
tags: [accounting, withdrawal, reversal, cash-settlement]
related: [ebbs, aspire, cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
---
# Accounting-Feed Withdrawal as Reversal

The proposed accounting-feed rule represents a withdrawal using the reversal direction of the original `New` transaction record. It explicitly avoids treating withdrawal as a completely new generated feed type.

The source does not specify reversal record fields, correlation keys, accounting signs, duplicate controls, or whether a reversal may be emitted after the original file has been acknowledged.