---
type: concept
title: OLTP Accounting Eligibility Blacklist
created: 2026-08-23
updated: 2026-08-23
tags: [oltp, accounting, eligibility, blacklist, nox, nos]
related: [korea-ratan-oltp-accounting-integration, settlement-method-update]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# OLTP Accounting Eligibility Blacklist

RATAN sends Korean accounting to OLTP for NOS cashflows and, in stated business rules, for selected NOX accounts including `KRO UIBOK` and `KRO BOKSEO`.

The implemented control is a blacklist rather than an allowlist: NOX accounts `CCY UISUS` and `CCY UIDD` are not sent to OLTP; other NOX accounts are eligible. A newly excluded account requires a RATAN code change, making eligibility-exclusion governance a deployment concern.

The `KRO BOKSEO` treatment is unresolved because the same requirement says users manually query SSDR and manually upload the accounting to OLTP.