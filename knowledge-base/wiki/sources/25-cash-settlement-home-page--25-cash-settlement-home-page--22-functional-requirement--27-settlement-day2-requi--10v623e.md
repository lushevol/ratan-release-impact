---
type: source
title: Nostro Maintenance By Uploading CSV File
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, nostro, static-data, csv, api, bulk-maintenance]
related: [nostro-records, nostro-upload-api, nostro-csv-bulk-maintenance, nostro-upload-atomic-validation, nostro-record-composite-uniqueness, what-is-the-complete-nostro-csv-upload-contract, what-are-the-directconfirm-state-transitions-for-nostro-upload]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Maintenance By Uploading CSV File.md"]
---
# Nostro Maintenance By Uploading CSV File

This functional requirement defines a bulk static-data maintenance capability through which users upload a CSV file to create or update [[nostro-records]].

## API contract

| Function | URL | Method | Params | Successful Response | Fail Response | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| Upload Nostro File | /v2/static/nostros/upload | POST | file | { "status": 200, "errorCode": null, "errorMessage": "10", //10 means upload successful nostros count "metadata": null } | { "status": 400, "errorMessage": "there are some error value found at line 2. legalEntityFmId, currency, settlementMeans, settlementAccount, startDate, endDate combination already exists ", "errorCode": "800400117", "metadata": {} } | if there is a error value in the upload file all data will be failed. directConfirm: true: nostro will be save_confirmed false: nostro will be update_pending |
| directConfirm（true/false) |  |  |  |  |  |  |

The endpoint is [[nostro-upload-api]]:

```text
POST /v2/static/nostros/upload
```

The source names `file` as a parameter and separately names `directConfirm (true/false)`. It does not specify the request encoding or whether `directConfirm` is sent as a multipart field, query parameter, or another parameter type.

## Documented processing rules

- A CSV file is used to update nostro records in bulk.
- If any uploaded row contains an error, all file data fails; the requirement does not permit partial acceptance.
- A duplicate is reported when this combination already exists:

```text
legalEntityFmId, currency, settlementMeans, settlementAccount, startDate, endDate
```

- `directConfirm: true` results in `save_confirmed`.
- `directConfirm: false` results in `update_pending`.
- On success, `errorMessage` contains the successful nostro-record count, despite its error-oriented field name.

## Scope and limitations

The requirement establishes duplicate-validation behavior but does not establish that the six-field combination is a database-level unique constraint. It also does not define the CSV column schema, date formats, required fields, allowed values, file-size limits, row limits, or validation of duplicate rows within a submitted file.

The state labels `save_confirmed` and `update_pending` are not defined further. The requirement does not clarify whether pending status applies to every imported record or only to updates of existing records.

This is an upstream static-data maintenance interface. It does not demonstrate downstream LMS distribution, accounting treatment, or reconciliation effects. It is related to settlement static-data controls, but the source does not state that it is limited to manual entities.