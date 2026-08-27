---
type: query
title: What Is the Canonical Aspire Accounting File Naming and Uniqueness Key?
created: 2026-08-24
updated: 2026-08-24
tags: [file-naming, idempotency, accounting, open-question]
related: [accounting-feed-file-generation-idempotency, accounting-aspire-execution, fileit]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
---
# What Is the Canonical Aspire Accounting File Naming and Uniqueness Key?

The scenario examples use `RATAN_PAYMENT_TRANSACTION_HK_20250220_01.csv`, while the job walkthrough uses `HK_20250220_01.csv`.

The design needs a canonical filename format and an enforceable uniqueness definition, including whether identity comprises country, local business date, sequence, destination, content version, or execution ID. It must also define how failed generation and failed delivery affect safe regeneration.