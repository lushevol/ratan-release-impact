---
type: query
title: Why Does RAT_CN_ACC_HK Identify Two Different Accounting Jobs?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, control-m, accounting, aspire, ebbs, data-quality]
related: [ratan, controlm, aspire, itrs-to-control-m-file-monitor-mapping, 26-auto-netting-page-md-files--77-ratan-51358-ratan-51358-ratan-infra-control-m-job-details-ratan--p7oaav]
sources: ["RATAN - 51358/RATAN/RATAN -Infra/Control-M Job Details RATAN.md"]
---
# Why Does RAT_CN_ACC_HK Identify Two Different Accounting Jobs?

The inventory records `RAT_CN_ACC_HK` in two different Control-M folders:

- `RATAN_CN_AUTO_JOB_P`, described as eBBS accounting for HK and annotated “It will be manually triggered from 30th May”.
- `RATAN_Settlement_Aspire_P`, described as Aspire accounting for HK and mapped by ITRS to `RATAN_PAYMENT_TRANSACTION_HK`.

It is unclear whether these are distinct jobs sharing an identifier, a folder-level migration or replacement, or a documentation error.

## Information needed

Confirm the unique Control-M identifiers, active folder paths, commands, schedules, owners, and whether eBBS and Aspire outputs are separate operational processes. Confirm the year and current validity of the manual-trigger note.