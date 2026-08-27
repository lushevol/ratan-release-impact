---
type: concept
title: Nostro Selection Economic-Change Detection
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, amendments, economic-change, cashflow-grouping]
related: [cashflow-versioning, amendment-driven-cashflow-correlation, ratan-cash-settlement-group-management-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md"]
---
# Nostro Selection Economic-Change Detection

A new and withdrawal cashflow pair is economically changed when their returned `nostroId` values differ. This applies when a portfolio becomes RFI-eligible, ceases to be RFI-eligible, or maps to a different RFI configuration.

The pairing assumption uses seven unchanged factors:

```text
bookingEntityId + counterpartyFmId + paymentCurrency + paymentAmount + ValueDate + Direction + settlementMethod
```

An otherwise `NonEcoAmend` group with a changed selected Nostro must be reclassified as economic and follow existing economic-change processing. The source evaluates the two currently grouped messages; it does not define configuration version pinning or historical-rule reconstruction.