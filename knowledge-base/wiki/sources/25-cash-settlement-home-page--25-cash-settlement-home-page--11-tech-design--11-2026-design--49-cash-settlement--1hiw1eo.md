---
type: source
title: RDM API Call for Compensation
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, rdm, static-data, holiday-calendar, api-integration]
related: [rdm, 51358-ratanone-static-data-service, rdm-api-based-holiday-compensation, rdm-api-pagination-and-reconciliation, ratan-indonesia-onshoring-2026, indonesia-environment-readiness-dependencies, what-is-the-approved-rdm-api-contract-for-indonesia-holiday-compensation, what-are-the-authoritative-ratan-holiday-update-and-deletion-semantics, what-is-the-approved-indonesia-rdm-api-schedule-and-data-freshness-sla, how-should-ratan-manage-kong-authentication-for-scheduled-rdm-api-calls]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md"]
---
# RDM API Call for Compensation

## Summary

This technical design proposes direct, scheduled RDM API retrieval as compensation for Indonesia's inability to mount NAS and process RDM files locally. The selected approach is an end-of-day API synchronization for currency holidays, special holidays, and country codes.

Currency-holiday data is required by `51358-ratan-cash-settlement-group-management-service` to calculate cash-settlement cutoff dates from static data maintained by `51358-ratanone-static-data-service`. Country-code data is required for SSI stamping. The design rejects GDC-to-ID synchronization because GDC and Indonesia should remain separated and because RDM-FILEIT may be retired.

The design is directionally selected but not implementation-ready. API routes, authentication, schedule, failure handling, reconciliation safeguards, and update semantics require confirmation.

## Scope of Reviewed File Consumers

| Consumer | RDM file | Persistence or downstream data | Need for Indonesia |
| --- | --- | --- | --- |
| `BcdfReconFileConsumer` | `all_rdm_bcdf_CurrencyHoliday` | `ratan_static_brdm_history`; currency-holiday processing | Yes |
| `RdmCommonFileConsumer` | `rdm_bcdf_rules_engine_configuration`, `rdm_bcdf_murex_structures_and_strategies`, `rdm_bcdf_15a6_registered_staff` | `ratan_rdm_15a6_registered_staff`, `ratan_rdm_structures_strategies`, `ratan_rdm_rules_engine_configuration` | No, based on the current rule-check usage review |
| `CountryCodeBcdfReconFileConsumer` | `rdm_bcdf_countrycode` | `ratan_static_cashflow_country_mapping` | Yes |
| `BrdmMessageConsumer` | `rdm_bcdf_bankcode` | `ratan_static_brdm_record` | No, based on the stated UK CHAPS-only `queryLei` use case |

The exclusions for common RDM files and bank-code/LEI data are limited to the reviewed Indonesia scope. They are not evidence that these datasets can be retired for all regions or future Indonesia requirements.

## Selected Design

| Option | Decision | Rationale |
| --- | --- | --- |
| No RDM-file synchronization database change; retain GDC behavior | Not selected | Indonesia needs compensation data. |
| Synchronize from GDC | Not selected | Does not adequately separate GDC and Indonesia; RDM-FILEIT may be retired. |
| EOD calls to RDM APIs | Selected | Intended to support both GDC and Indonesia. |

The selected flow is documented by [[rdm-api-based-holiday-compensation]].

## Legacy Real-Time Holiday Message

The existing real-time path uses topic `Rdm_Currency_Holiday_Weekend_In`. `RdmMessageConsumer.onRdmHolidayWeekendMessageReceived()` stores an RDM message, synchronizes the holiday table, saves or updates `ACTIVE` records, deletes `DELETED` records, and emits `Static_Data_Holiday_Update_In`. The source notes no consumer was found for the emitted topic.

```json
{
  "code": "200",
  "status": "Success",
  "header": {
    "serviceName": "RDM00463",
    "serviceVersion": "v1",
    "generatedTimestamp": "2022-03-29 17:38:27 HKT",
    "trackingId": "c9a6c97b-77ae-4a47-8099-8bf6d948907d"
  },
  "data": {
    "centerId": 43,
    "isoCurrencyCode": "ZWL",
    "isoMicCode": "XAG",
    "isoCountryCode": "ZW",
    "relatedFinancialCenter": "Harare",
    "eventYear": 2052,
    "eventDate": "28122053",
    "eventDayOfWeek": "Sat",
    "eventName": "Weekend",
    "dayType": "WKD",
    "fileType": "C",
    "entityState": "ACTIVE",
    "createdTime": "29032022 17:30:45",
    "modifiedTime": null
  }
}
```

## Legacy FileIT Notification

```json
{
  "IMFTFileNotification": {
    "Header": {
      "Version": "1.0",
      "Identifier": "BRDM_BNKCODE_GL",
      "UUID": "5d127960-2cf6-42fa-82fa-f6604ca119fd",
      "SrcJMSID": "ID:10.23.100.84865f197508a37380:0",
      "Source": "38430-RDM",
      "Target": "51358-RATAN",
      "Country": "GL",
      "Timestamp": "2025-06-09 01:15:29.487 +0800"
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
      "SubComponent": "BRDM_RATAN_BNKCODE_GL",
      "SrcFilePath": "/share/imft070/ratanone/all_rdm_bcdf_15a6_registered_staff_§_1.dat.gz",
      "Component": "CFT",
      "TrackingID": "F0901193"
    }
  }
}
```

The notification topic is `Rdm_FileIT_Notification_In`. This NAS-dependent process cannot be directly used by Indonesia under the stated infrastructure policy.

## API Endpoints Recorded in the Design

The following values are copied as recorded. They contain inconsistent paths and malformed Markdown targets in staging and development rows, so they must be validated before configuration.

| Environment | Currency-holiday URL | Special-holiday URL |
| --- | --- | --- |
| dev | `https://10.83.161.226:8453/rdm_api/service/v2/holidayCalendarCurrencyHldyWkend?dateFrom=20250101&dateTo=20261231&page=1&entityState=DELETED` | `https://10.83.161.226:8453/rdm_api/service/v2/holidayCalendarSpecial?dateFrom=20250101&dateTo=20261231&page=2` |
| stg | Visible URL: `https://gateway-stg.51242.app.standardchartered.com/rdm_api/service/v2/holidayCalendarCurrencyHldyWkend?dateFrom=20250101&dateTo=20261231`; linked target uses `/service/v1/holidayCalendarCurrencyHldyWkend` | Visible URL: `https://gateway-stg.51242.app.standardchartered.com/rdm_api/service/v2/holidayCalendarSpecial?dateFrom=20250101&dateTo=20261231&page=2`; linked target uses the v1 currency-holiday route |
| prod | `https://gateway.51242.app.standardchartered.com/rdm_api/service/v2/holidayCalendarCurrencyHldyWkend?dateFrom=20250101&dateTo=20261231` | `https://gateway.51242.app.standardchartered.com/rdm_api/service/v2/holidayCalendarSpecial?dateFrom=20250101&dateTo=20261231&page=2` |

| Environment | Country-code URL |
| --- | --- |
| dev | `https://10.83.161.226:8453/rdm_api/service/v1/countries` |
| stg | Visible URL: `https://gateway-stg.51242.app.standardchartered.com/rdm_api/service/v1/countries`; linked target mixes gateway and development URLs |
| prod | `https://gateway.51242.app.standardchartered.com/rdm_api/service/v1/countries` |

A staging test route is recorded as returning HTTP `200` with a null response body:

```text
https://gateway-stg.51242.app.standardchartered.com/rdm_api/service/rdmdata?api=/v2/holidayCalendarCurrencyHldyWkend&dateFrom=20220209&dateTo=20260210
```

## Reconciliation and Pagination Proposal

For currency holidays, the source proposes querying existing entries by RDM unique key rather than performing an expensive date-range comparison.

```text
(1)query by rdmUniqueKeys ~~@Query(""" SELECT * FROM ratan_static_cashflow_currency_holiday holiday WHERE holiday.version = :version AND holiday.rdm_unique_key IN (:rdmUniqueKeys) AND holiday.ratan_label = :ratanLabel """)~~ ~~findByVersionAndRdmUniqueKeysAndRatanLabel~~ findByVersionAndRdmUniqueKeyIn
(2)just insert/delete no need to update ratan holiday, cause query by RdmUniqueKeys from RDM-API.response.data(only filter RdmUniqueKeys)
(3）in RDM, currencyHoliday.primaryKey = ( center_id, event_date, event_name, file_type) **only 1 center Id for each currency**
DELETE: if primaryKey change --->DELETE
UPDATE: if !primaryKey change --->UPDATE
```

The documented pagination calculation is:

```text
Integer totalPageNo = (totalRecords+ pageSize-1) / pageSize;
Boolean fetchNextPage = dataQuery.getPage()<= totalPageNo;
```

Currency-holiday retrieval starts at page `1`; country-code retrieval starts at page `0`. The country endpoint uses a default page size of `100` according to the source.

The source states that API date filtering is `>= dateFrom` and `< dateTo`. It also records different date formats between real-time messages and API responses:

```text
RDM real-time message:
eventDate: "28122053"
createdTime: "29032022 17:30:45"

RDM API response:
eventDate: "17/05/2025"
createdTime: "03/03/2025 01:29"
modifiedTime: "31/07/2025 15:30"
```

`DateConvertUtil` is proposed for conversion before legacy holiday-entity creation logic is used.

## Scheduler Authorization

The intended internal endpoints are:

```text
/v1/static/data/recon/currencyHoliday
/v1/static/data/recon/specialHoliday
/v1/static/data/recon/countryCode
```

The protected action is:

```text
RATAN_INTERNAL_FUNC:STATIC_SERVICE:FETCHANDUPDATE
```

The source states that `ratanone-control-m` already has this action and asks whether GDC Control-M should invoke Indonesia production endpoints because Control-M is deprecated and expected to be replaced.

## Timing and Operational Risks

RDM is stated to call CoppClark at 08:00 HK and offer processed data after 09:00 HK. Indonesia is stated to temporarily add currency-holiday data before 18:00 IST. However, the listed Indonesia Control-M schedule is “After 8am IST,” which does not clearly align with RDM availability.

The source also leaves unresolved:

- Kong LDAP/client setup, token renewal, and credential rotation.
- Whether a token should be stored in `localThread`.
- The behavior for timeouts, partial pagination, empty successful responses, and reconciliation deltas.
- Whether updates with an unchanged RDM primary key can alter settlement-relevant fields.
- Whether the existing holiday reconciliation safeguard of no automatic database synchronization and a greater-than-20 difference threshold will be retained.
- Whether `Static_Data_Holiday_Update_In` intentionally has no consumer.

## Related Pages

- [[rdm]] is the reference-data provider and API dependency.
- [[51358-ratanone-static-data-service]] is the static-data owner in the proposed flow.
- [[rdm-api-based-holiday-compensation]] describes the selected NAS-free integration pattern.
- [[rdm-api-pagination-and-reconciliation]] captures the required idempotency and completeness controls.
- [[ratan-indonesia-onshoring-2026]] and [[indonesia-environment-readiness-dependencies]] provide delivery context.
- [[what-is-the-approved-rdm-api-contract-for-indonesia-holiday-compensation]] tracks endpoint and response-contract validation.
- [[what-are-the-authoritative-ratan-holiday-update-and-deletion-semantics]] tracks the unresolved update model.
- [[what-is-the-approved-indonesia-rdm-api-schedule-and-data-freshness-sla]] tracks timing and freshness requirements.
- [[how-should-ratan-manage-kong-authentication-for-scheduled-rdm-api-calls]] tracks authentication ownership and lifecycle.