---
type: entity
title: ratan_static_cashflow_country_mapping
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, database, table, static-data, country-data]
related: [static-data-service, rdm, country-reference-data-reload, cash-settlement-data-store-requirements, domain-owned-postgresql-schemas, what-is-the-validated-and-rollback-safe-country-data-reload-procedure]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/How to import country name data set to Static Data Service.md"]
---
# ratan_static_cashflow_country_mapping

`ratan_static_cashflow_country_mapping` is the database table identified as the target for Static Data Service country-name reference data.

## Documented lifecycle

- `cleanDB` removes all data from this table.
- The country-file upload API reads the prepared input file and saves its data to this table.
- An empty database is stated to be initialized through Flyway rather than the API reload path.

The source does not specify the database schema, table DDL, columns, primary key, indexes, row identity, constraints, data owner, retention policy, or atomicity of delete-and-upload replacement.