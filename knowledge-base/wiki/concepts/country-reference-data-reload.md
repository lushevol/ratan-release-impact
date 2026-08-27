---
type: concept
title: Country Reference Data Reload
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, static-data, reference-data, reload, csv]
related: [static-data-service, rdm, ratan-static-cashflow-country-mapping, what-is-the-validated-and-rollback-safe-country-data-reload-procedure, what-is-the-canonical-country-dataset-schema-and-rdm-transformation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/How to import country name data set to Static Data Service.md"]
---
# Country Reference Data Reload

Country reference data reload is the documented replacement procedure for existing country mappings in [[ratan-static-cashflow-country-mapping]].

## Procedure model

1. Download the country dataset from [[rdm]].
2. Remove lines 1–11 from the downloaded file.
3. Save the prepared content as a CSV file.
4. Call the Static Data Service `cleanDB` endpoint to delete all existing rows.
5. Upload the prepared file through Static Data Service.

For an empty database, the source instead directs operators to use Flyway initialization.

## Risk boundary

This is a destructive, replace-all process rather than an incremental import. The source does not document a backup, validation gate, maintenance window, rollback method, atomic swap, or consumer behavior while the table may be empty or partially populated.

The manual preprocessing step is a material dependency: the source does not define the removed rows, expected header behavior, CSV format, encoding, required fields, or validation criteria.