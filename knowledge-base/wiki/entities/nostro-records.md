---
type: entity
title: Nostro Records
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, settlement, static-data, reference-data]
related: [nostro-upload-api, nostro-csv-bulk-maintenance, nostro-record-composite-uniqueness, settlement-accounting, fmid-country-time-zone-resolution]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Maintenance By Uploading CSV File.md"]
---
# Nostro Records

Nostro records are settlement reference-data records maintained through the CSV upload interface documented by [[nostro-upload-api]].

For duplicate validation during CSV upload, a record is treated as already existing when the following combination matches an existing record:

```text
legalEntityFmId, currency, settlementMeans, settlementAccount, startDate, endDate
```

The source does not define the full record schema, lifecycle, account ownership model, or downstream use of these records. In particular, it does not establish accounting behavior in [[settlement-accounting]] or LMS consumption.