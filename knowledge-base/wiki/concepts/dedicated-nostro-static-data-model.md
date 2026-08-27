---
type: concept
title: Dedicated Nostro Static-Data Model
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, static-data, jsonb, rfi, data-model]
related: [dedicated-nostro-stamping, ratanone-static-data-service, ratanone-db-repository]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md"]
---
# Dedicated Nostro Static-Data Model

The proposed model distinguishes dedicated Nostro records using `nostroType`, such as `DEFAULT` or `RFI`, and `nostroKey`, intended to carry a portfolio-corresponding value. The design also refers to `dedicated_info` JSONB and a dedicated child table.

Partial migration is proposed: existing records receive `nostroType='DEFAULT'`; identified RFI records become `RFI` and receive dedicated data. This is static-data migration, not historical cashflow migration.

The final schema is unresolved. In particular, the stated five-factor duplicate key omits portfolio despite RFI being selected by portfolio plus currency. A uniqueness rule must prevent accidental multiple matches without preventing legitimate separate RFI portfolio mappings.