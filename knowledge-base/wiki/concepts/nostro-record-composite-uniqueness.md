---
type: concept
title: Nostro Record Composite Uniqueness
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, uniqueness, duplicate-detection, static-data, validation]
related: [nostro-records, nostro-upload-api, nostro-upload-atomic-validation, fmid-country-time-zone-resolution]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Maintenance By Uploading CSV File.md"]
---
# Nostro Record Composite Uniqueness

Nostro record composite uniqueness is the duplicate-detection behavior applied to CSV uploads of [[nostro-records]].

The documented duplicate combination is:

```text
legalEntityFmId, currency, settlementMeans, settlementAccount, startDate, endDate
```

An upload failure example reports error code `800400117` when this combination already exists.

`legalEntityFmId` therefore has a documented role in nostro duplicate detection in addition to its mapping-related context in [[fmid-country-time-zone-resolution]]. This source does not establish that the listed fields are a database unique constraint, nor does it specify how date overlaps, null values, or duplicates within the same file are evaluated.