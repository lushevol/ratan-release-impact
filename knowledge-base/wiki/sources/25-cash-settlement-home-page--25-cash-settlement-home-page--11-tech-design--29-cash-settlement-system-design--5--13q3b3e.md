---
type: source
title: How to Import Country Name Data Set to Static Data Service
authors: []
year: 2024
url: ""
venue: Cash Settlement System Design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, static-data, country-data, rdm, flyway, api]
related: [static-data-service, rdm, ratan-static-cashflow-country-mapping, country-reference-data-reload, what-is-the-validated-and-rollback-safe-country-data-reload-procedure, what-is-the-canonical-country-dataset-schema-and-rdm-transformation, what-is-the-authoritative-static-data-service-country-upload-endpoint, cash-settlement-data-store-requirements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/How to import country name data set to Static Data Service.md"]
---
# How to Import Country Name Data Set to Static Data Service

This operational document describes initialization and replacement of country-name reference data held by [[ratan-static-cashflow-country-mapping]] through the [[static-data-service]].

## Documented operating paths

- For a database without data, use a Flyway script to initialize the database.
- For a database with existing data, download the country dataset from [[rdm]], remove lines 1 through 11, save the remaining content as a CSV file, delete all existing country mappings, and upload the prepared file.

The source does not identify the Flyway migration, its version, or whether its seed data is equivalent to the RDM download.

## Documented API definitions

The following tables preserve the API details as written in the source, including the inconsistent upload URL hyperlink.

| API Name | HTTP Method | URL | Note |
| --- | --- | --- | --- |
| [clean DB](http://localhost:8989/v1/cashflow/country/cleanDB) | DELETE | [http://{static service domain name}/v1/cashflow/country/cleanDB](http://localhost:8989/v1/cashflow/country/cleanDB) | this api will remove all data from table ratan_static_cashflow_country_mapping |

```bash
curl --location --request DELETE 'http://localhost:8989/v1/cashflow/country/cleanDB' --data-raw ''
```

| API Name | HTTP Method | URL | Note |
| --- | --- | --- | --- |
| [upload ](http://localhost:8989/v1/cashflow/country/cleanDB)flie | POST | [http://{static service domain name}/v1/cashflow/country/upload](http://localhost:8989/v1/cashflow/country/cleanDB) | this api will upload file and then will read all data from the file to save to DB table ratan_static_cashflow_country_mapping |

```bash
curl --location --request POST 'http://localhost:8989/v1/cashflow/country/upload' \
  --form 'file=@"/C:/Users/1662744/Downloads/Country-20240111.csv"'
```

## Interpretation and constraints

The populated-database procedure is a [[country-reference-data-reload|replace-all reload]]: `cleanDB` is stated to remove every record from `ratan_static_cashflow_country_mapping` before the replacement file is uploaded.

The cURL example identifies `/v1/cashflow/country/upload` as the upload endpoint, whereas the upload table's visible hyperlink targets `cleanDB`. Treat the upload endpoint as unresolved until verified through the relevant service contract.

The source does not state authentication, authorization, environment controls, pre-upload validation, rollback, transaction boundaries, duplicate handling, CSV schema, encoding, upload response contract, or availability behavior while replacement is in progress. The required manual removal of lines 1–11 is also unexplained.