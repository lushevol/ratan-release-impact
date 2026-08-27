---
type: concept
title: Korea Cashflow Migration
tags: [korea, cashflow, migration, accounting, oltp]
related: [oltp-accounting, ebbs, scfb-seoul, ebbs-vs-oltp-accounting-flow, entity-scoped-validation-rollout]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# Korea Cashflow Migration

Korea Cashflow Migration moves Korea settlement-accounting processing to [[oltp-accounting]] while retaining the common task lifecycle used for [[ebbs]].

The strategic routing configuration identifies `SCFB_SEOUL` with FMID `10036645` and country code `KR`. The migration changes downstream payload construction, publication topics, bridge-account selection, retry eligibility, and response handling without defining a wholly separate end-to-end workflow.