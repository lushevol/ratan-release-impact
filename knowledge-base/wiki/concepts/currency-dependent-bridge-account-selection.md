---
type: concept
title: Currency-Dependent Bridge-Account Selection
tags: [static-data, bridge-account, currency, korea, accounting]
related: [scfb-seoul, ratan-static-data-service, centralized-static-configuration-management, korea-cashflow-migration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# Currency-Dependent Bridge-Account Selection

Currency-dependent bridge-account selection resolves a bridge account using both the booking entity and a currency classification.

For `SCFB_SEOUL` / FMID `10036645`, the design maps `KRW` to `000287` and `FCY` to `040446`. It requires a `currency` attribute on `com.scb.ratan.sd.entity.EbbsAccount`.

The source does not define whether `FCY` means all non-KRW ISO currencies or a narrower configured group. This ambiguity is tracked in [[how-is-fcy-defined-for-korea-bridge-account-selection]].