---
type: query
title: What Is the Complete Nostro CSV Upload Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, csv, api-contract, static-data, open-question]
related: [nostro-upload-api, nostro-csv-bulk-maintenance, nostro-upload-atomic-validation, nostro-record-composite-uniqueness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Maintenance By Uploading CSV File.md"]
---
# What Is the Complete Nostro CSV Upload Contract?

The requirement documents `POST /v2/static/nostros/upload`, a `file` parameter, and a separate `directConfirm` boolean reference. It does not define a complete client-consumable upload contract.

## Questions to resolve

- Is the request `multipart/form-data`, and where is `directConfirm` provided?
- What CSV headers, column order, delimiter, character encoding, and quoting rules are required?
- Which columns are mandatory, and what date formats are accepted for `startDate` and `endDate`?
- What currencies and `settlementMeans` values are valid?
- What are the maximum file size and record-count limits?
- How are blank values, duplicate rows in the same file, and overlapping effective dates handled?
- Does the response have a formal schema beyond the documented examples?

Resolving these points is required before implementing a reliable client for [[nostro-upload-api]].