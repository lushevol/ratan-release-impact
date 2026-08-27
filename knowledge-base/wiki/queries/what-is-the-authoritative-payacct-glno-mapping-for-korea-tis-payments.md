---
type: query
title: What Is the Authoritative PAYACCT_GLNO Mapping for Korea TIS Payments?
created: 2026-08-23
updated: 2026-08-23
tags: [tis, ratan, payacct-glno, suspense-account, korea-migration]
related: [korea-tis-payment-type-classification, ratan-tis-payment-query-integration, ratan, tis, oltp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# What Is the Authoritative PAYACCT_GLNO Mapping for Korea TIS Payments?

## Question

Which `PAYACCT_GLNO` values are authoritative for Korean pay-side UINOs, particularly FCY routes, and which replacement accounts must be configured?

## Evidence

The field-mapping logic specifies:

```text
KRW/KRO SCBLKR route → 000287
FCY route → 040446
```

The value sample for `PAYACCT_GLNO` is `040434`, and the mapping remarks state that new accounts are needed to replace both `000287` and `040434`.

## Why it matters

An incorrect suspense-account value can lead to incorrect payment accounting, failed downstream validation, or manual remediation in OLTP(UI).

## Needed decision

Confirm approved GL accounts by UINO and currency, identify whether replacement accounts have been created, and assign accountable owners for RATAN configuration and TIS validation.