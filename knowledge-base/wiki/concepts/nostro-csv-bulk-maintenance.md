---
type: concept
title: Nostro CSV Bulk Maintenance
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, csv, bulk-maintenance, static-data, settlement]
related: [nostro-records, nostro-upload-api, nostro-upload-atomic-validation, nostro-record-composite-uniqueness, manual-entity-go-live-static-data-controls, what-is-the-complete-nostro-csv-upload-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Maintenance By Uploading CSV File.md"]
---
# Nostro CSV Bulk Maintenance

Nostro CSV bulk maintenance is an operational mechanism for maintaining [[nostro-records]] by uploading a CSV file through [[nostro-upload-api]], rather than maintaining records individually.

The interface is located beneath `/v2/static/`, indicating treatment as static or reference data. This is conceptually related to [[manual-entity-go-live-static-data-controls]], but the requirement does not state that the API is exclusive to manual-entity settlement configuration.

The documented capability includes all-or-nothing validation and duplicate detection. The source does not supply a CSV schema, including headers, column sequence, data formats, required fields, or permitted values.