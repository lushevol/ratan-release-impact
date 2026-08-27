---
type: concept
title: Ad-Hoc SSI Stamping Exclusion
created: 2026-08-24
updated: 2026-08-24
tags: [SSI, ad-hoc-stamping, maker-checker, automation-safety]
related: [ssi-change-notification-re-stamping, bulk-maker-checker-processing, ssi-stamping-reference-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md"]
---
# Ad-Hoc SSI Stamping Exclusion

Ad-hoc SSI stamping is manual or exceptional settlement-instruction work that must be protected from automatic SSI notification processing.

## Exclusion behavior

The notification queries use two safeguards:

1. A cashflow with an existing `stamped_nostro_account` record is excluded from the NA1 missing-nostro candidate set.
2. A cashflow with a `maker_checker_request` whose `state != 'AUTO_CLOSED'` is excluded from relevant re-stamping candidates.

NA2 and NA3 also include exception codes such as `SETTLEMENT_ACCOUNT_OR_MEANS_MISMATCH_EXCEPTION` and `ADHOC_SSI_EXCEPTION` when excluding records associated with non-closed maker-checker activity.

## Purpose

These exclusions prevent automatic re-stamping from overriding a manually selected SSI or interfering with a pending approval. They do not define the complete maker-checker state machine, and the source does not confirm whether other terminal states should be treated as closed.

The selection and exclusion SQL is documented in [[ssi-change-notification-re-stamping]] and [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1j9svpi]].