---
type: concept
title: Nostro Configuration
created: 2026-08-22
updated: 2026-08-22
tags: [nostro, cash-settlement, static-data]
related: [cash-settlement, ratan-settlement-korea, 51358-ratanone-db-repository]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# Nostro Configuration

A Nostro account is a bank account held with another bank, commonly maintained by currency and used to support settlement and reconciliation.

## Korea Release

[[chg1016055]] includes Korea Nostro data and associated audit records. PIT defines these expected counts:

- Korea Nostro records: `115`
- Korea Nostro audit records: `115`

The checks query `ratanone.ratan_static__cashflow_nostro` and `ratanone.nostro_manipulation_audit`. The source provides production screenshots but leaves the textual Results cell blank.