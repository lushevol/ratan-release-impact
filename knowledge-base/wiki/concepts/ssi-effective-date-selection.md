---
type: concept
title: SSI Effective-Date Selection
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, effective-date, value-date, restamping, elastic-search]
related: [ssi-plus, dqsl, ratan-ssi-stamping, vostro-nostro-ssi-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# SSI Effective-Date Selection

SSI effective-date selection filters SSI records against the cashflow value date (VD) before best-match processing.

An SSI with `End_EffectiveDate` is eligible when `VD <= End_EffectiveDate`; an SSI with `Start_EffectiveDate` is eligible when `VD >= Start_EffectiveDate`. A record with neither field is eligible. SSI+ may publish an old end-dated record and a new start-dated record with an `_ED` suffix concurrently.

RATAN applies this logic to automatic stamping and Vostro candidate queries for exception handling. On an SSI update from [[dqsl]], it must identify impacted cashflows and re-trigger stamping. Time-zone semantics, records with both dates, overlap resolution, and re-stamping boundaries are not specified.