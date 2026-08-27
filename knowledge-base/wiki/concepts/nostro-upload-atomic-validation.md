---
type: concept
title: Nostro Upload Atomic Validation
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, validation, atomicity, csv, batch-processing, data-integrity]
related: [nostro-upload-api, nostro-csv-bulk-maintenance, nostro-record-composite-uniqueness, bulk-manual-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Maintenance By Uploading CSV File.md"]
---
# Nostro Upload Atomic Validation

Nostro upload atomic validation is the documented rule that one invalid value in a submitted CSV file causes all uploaded data to fail.

The requirement illustrates an error at line 2 and explicitly states that, if an error value exists in the upload file, all data fails. This means the [[nostro-upload-api]] does not document partial acceptance of valid rows in a failed submission.

The rule should not be generalized to [[bulk-manual-stp]] or other batch operations, whose partial-success behavior may follow different contracts. The requirement does not describe transaction boundaries, rollback implementation, or whether validation occurs before any persistence attempt.