---
type: source
title: Ratan Holiday Data Process from RDM Introduction
authors: []
year: 2025
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, rdm, holiday-calendar, fileit, ratanone, integration]
related: [rdm, ratan-static-rdm-holiday-weekend-message, ratan-static-cashflow-currency-holiday, rdm-holiday-and-weekend-ingestion, holiday-data-composite-duplicate-key, fileit-file-arrival-notification, ordinary-versus-special-holiday-feeds, holiday-calendar-event-model, what-is-the-authoritative-ratan-holiday-data-ingestion-path, what-is-the-ratan-holiday-data-update-and-deduplication-policy, what-is-the-canonical-rdm-holiday-schema, what-is-the-environment-specific-rdm-service-configuration, ratanone, fileit, cft, solace]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# Ratan Holiday Data Process from RDM Introduction

## Summary

This technical-design introduction documents the ingestion of currency holiday, special-holiday, and weekend reference data from [[rdm]] into RATAN. RATAN persists inbound raw messages in [[ratan-static-rdm-holiday-weekend-message]] and normalized calendar records in [[ratan-static-cashflow-currency-holiday]].

The source also documents a FileIT full-data delivery path and states that RATAN is a consumer of FileIT notifications. [[fileit]] delivers a complete BCDF file and emits a notification whose component is [[cft]]. Solace documentation is referenced only for the FileIT notification-message structure.

## Documented storage model

- Raw inbound messages: `ratan_static_rdm_holiday_weekend_message`
- Structured holiday and weekend records: `ratan_static_cashflow_currency_holiday`
- Duplicate-check field: `rdm_unique_key`

The documented composition of `rdm_unique_key` is:

```text
center_id + event_date + event_name + file_type
```

The source does not provide DDL, database constraints, indexes, field types, or update semantics.

## RDM operational access

The production RDM portal is:

<https://rdm.global.standardchartered.com/rdm/rdm/ember/dist/index.html#/home>

It uses SSO. The documented lookup path is **Browse Data** → **Holiday Calendar** → the two weekend panels → search.

Source-specific contacts:

- RDM development SPOC: `Indrani.Kandasamy@sc.com`
- RDM BA: `GokulPrasath.J1@sc.com`

These contacts do not by themselves establish formal ownership of data quality, delivery, ingestion, or reconciliation.

## Holiday-feed service identifiers

| Feed category | Production | Test |
|---|---|---|
| Ordinary holiday | `RDM00463`, `RDM00493`, `RDM00827` | `RDM00463`, `RDM00493`, `RDM00827` |
| Special holiday | `RDM00470` | `RDM00846` |

The functional distinction among the three ordinary-holiday services, and the reason special-holiday identifiers differ by environment, are not specified.

## Full-data FileIT delivery

A documented production-path example is:

```text
/share/imft054/ratanone/all_rdm_bcdf_CurrencyHolidayWknd_15042025_d_1.dat.gz
```

The filename pattern indicates full BCDF delivery of currency holiday and weekend data:

```text
all_rdm_bcdf_CurrencyHolidayWknd_*.dat.gz
```

## RDM holiday-event payload

```js
{
  "code": "200",
  "status": "Success",
  "header": {
    "serviceName": "RDM00827",
    "serviceVersion": "v1",
    "generatedTimestamp": "2025-07-02 20:18:47 HKT",
    "trackingId": "6965a06b-65e1-422c-9314-f3aa7c3fc912"
  },
  "data": {
    "centerId": 7,
    "isoCurrencyCode": "CNY",
    "isoCountryCode": "CN",
    "relatedFinancialCenter": "Beijing",
    "eventYear": 2026,
    "eventDate": "28112026",
    "eventDayOfWeek": "Sat",
    "eventName": "Weekend",
    "dayType": "WKD",
    "fileType": "C",
    "entityState": "ACTIVE",
    "createdTime": "10032022 14:02:50",
    "modifiedTime": "14112023 16:41:44"
  }
}
```

The sample suggests `eventDate` is formatted as `DDMMYYYY`, while `createdTime` and `modifiedTime` use `DDMMYYYY HH:mm:ss`. `generatedTimestamp` carries an `HKT` timezone indicator. The source does not define canonical parsing and timezone rules.

## FileIT notification payload

```js
{
    "IMFTFileNotification": {
        "Header": {
            "Version": "1.0",
            "Identifier": "FRDM_HOLIDAY_GL",
            "UUID": "1ee4498a-21ce-4e96-b32f-3c9ee1809af1",
            "SrcJMSID": "ID:10.23.100.84b4c9197dff184690:0",
            "Source": "38430-RDM",
            "Target": "51358-RATAN",
            "Country": "GL",
            "Timestamp": "2025-07-06 21:34:02.95 +0800"
        },
        "Payload": {
            "Status": {
                "Causes": {
                    "Details": [
                        "File Arrived at Receiver"
                    ]
                },
                "Code": "5000",
                "Reason": "CFT_NOTIFICATION"
            },
            "SubComponent": "FRDM_RATAN_HOLIDAY_GL",
            "SrcFilePath": "/share/imft054/ratanone/all_rdm_bcdf_CurrencyHolidayWknd_05072025_d_1.dat.gz",
            "Component": "CFT",
            "TrackingID": "G0621335"
        }
    }
}
```

The notification supplies routing, traceability, and file-location metadata. The source does not define idempotency keys, retry rules, replay behavior, or processing outcomes after notification receipt.

## Limitations and unresolved design points

The source does not establish whether raw RDM messages and full BCDF files are alternative inputs, sequential processing stages, or sources that require reconciliation. It also does not define handling for changed or deactivated records whose `rdm_unique_key` remains unchanged.

See [[what-is-the-authoritative-ratan-holiday-data-ingestion-path]], [[what-is-the-ratan-holiday-data-update-and-deduplication-policy]], [[what-is-the-canonical-rdm-holiday-schema]], and [[what-is-the-environment-specific-rdm-service-configuration]].