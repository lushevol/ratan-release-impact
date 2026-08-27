---
type: entity
title: Nostro Upload API
created: 2026-08-23
updated: 2026-08-23
tags: [api, rest, nostro, csv, static-data]
related: [nostro-records, nostro-csv-bulk-maintenance, nostro-upload-atomic-validation, nostro-record-composite-uniqueness, what-is-the-complete-nostro-csv-upload-contract, what-are-the-directconfirm-state-transitions-for-nostro-upload]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Maintenance By Uploading CSV File.md"]
---
# Nostro Upload API

The Nostro Upload API is the documented REST interface for bulk creation or update of [[nostro-records]]:

```text
POST /v2/static/nostros/upload
```

The documented request includes a `file` parameter and refers separately to a `directConfirm` boolean. Request encoding is unspecified.

The API enforces [[nostro-upload-atomic-validation]]: an error in any uploaded row causes the complete file to fail. Its duplicate-validation rule is documented in [[nostro-record-composite-uniqueness]].

A successful response uses `status: 200` and places the successful record count in `errorMessage`. Clients must therefore evaluate `status` rather than treating a non-null `errorMessage` by itself as a failure indicator.