---
type: source
title: RDM Integration via Kong Gateway
authors: [Xinmiao Huang]
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/13292988"
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, rdm, kong, oauth2, reference-data, sit]
related: [rdm, kong, rdm-reference-data-integration-via-kong, what-is-the-production-readiness-plan-for-ratan-rdm-kong-integration, how-should-ratan-handle-rdm-amber-data-quality-and-pagination, ratan-indonesia-onshoring-2026, indonesia-environment-readiness-dependencies, xinmiao-huang]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation/RDM Integration via Kong Gateway.md"]
---
# RDM Integration via Kong Gateway

This technical design documents a SIT-complete integration in which Ratanone consumes [[rdm]] reference-data APIs through [[kong]]. The documented owner is [[xinmiao-huang]], and the related ADO work item is `13292988`.

The integration reuses the existing Kong consumer registration `EDMILDAP_RATAN_EDMI_PROD_Ratanone-PCT2`, previously used for Portfolio query. RDM must grant the consumer ID `EDMILDAP/RATAN_EDMI_PROD` access to the required service scope. The required OAuth scope is `RDMApiService_GET`.

## Delivery status

- Non-production configuration was implemented through ADO pull request `3141169` in `51242-iag-catalyst-idp-service-records`.
- The cited pipeline run is `20260804.1`.
- Production onboarding is explicitly `TBD`; SIT completion is not evidence of production readiness.

The consumer team requires access to these IAG repositories:

- `51242-iag-catalyst-kong-helm`
- `51242-iag-catalyst-idp-service-records`

## Kong environments

| Environment | Base URL |
| --- | --- |
| SIT | `https://gateway-stg.51242.app.standardchartered.com` |
| UAT | `https://gateway-uat-stg.51242.app.standardchartered.com` |
| PROD | `https://gateway.51242.app.standardchartered.com` |

## RDM endpoint catalog

| Function | Exact endpoint |
| --- | --- |
| Currency Holiday | `/rdm_api/service/rdmdata?api=v2/holidayCalendarCurrencyHldyWkend?dateFrom={startDate}&dateTo={endDate}` |
| Special Holiday | `/rdm_api/service/rdmdata?api=v2/holidayCalendarSpecial&dateFrom={startDate}&dateTo={endDate}` |
| Country Code | `/rdm_api/service/rdmdata?api=v1/countries` |

The listed Currency Holiday endpoint contains two `?` delimiters. The demonstrated invocation below uses `&` between query parameters and should be treated as the working form pending producer confirmation.

## Authentication and invocation flow

The integration uses the OAuth 2.0 `client_credentials` grant described in [[rdm-reference-data-integration-via-kong]].

### Step A: Query client information

```bash
GET /api/identity/oauth2/dcr/v1.0/register?client_name=EDMILDAP_RATAN_EDMI_PROD_Ratanone-PCT2 HTTP/1.1
Host: gateway-stg.51242.app.standardchartered.com
Authorization Type: Basic Auth
Username: EDMILDAP/RATAN_EDMI_PROD
password: #Get from OneVault
```

### Step B: Obtain an access token

```bash
POST /oauth2/token?grant_type=client_credentials&scope=RDMApiService_GET HTTP/1.1
Host: gateway-stg.51242.app.standardchartered.com
Authorization Type: Basic Auth
Username: #client_id returned in Step A
password: #client_s[remove me]ecret returned in Step A
```

The documented response contract is:

```text
"scope": "RDMApiService_GET",
"token_type": "Bearer",
"expires_in": 900
```

The bearer-token lifetime is therefore 900 seconds (15 minutes).

### Step C: Invoke RDM

```bash
GET /rdm_api/service/rdmdata?api=v2/holidayCalendarCurrencyHldyWkend&dateFrom=20220301&dateTo=20220315 HTTP/1.1
Host: gateway-stg.51242.app.standardchartered.com
Authorization Type: Bearer Token
Token: #access_token returned in Step B
```

## Currency-holiday response metadata and schema

```text
"serviceName": "holidayCalendarCurrencyHldyWkend",
"serviceVersion": "v2",
"requestParams": "dateTo=20220315&api=v2/holidayCalendarCurrencyHldyWkend&page=1&dateFrom=20220301",
"generatedTimestamp": "2026-08-05 16:03:54 HKT",
"trackingId": "20260805T1603547301",
"totalRecords": "541550",
"pageNo": "1",
"pageSize": "2000"
```

| Field | Data type | Max size | Mandatory |
| --- | --- | --- | --- |
| `centerId` | `INTEGER` | `4` | `Y` |
| `isoCurrencyCode` | `VARCHAR` | `3` | `N` |
| `isoCountryCode` | `VARCHAR` | `2` | `N` |
| `relatedFinancialCenter` | `VARCHAR` | `200` | `N` |
| `eventYear` | `INTEGER` | `4` | `N` |
| `eventDate` | `DATE` | `0` | `Y` |
| `eventDayOfWeek` | `VARCHAR` | `3` | `N` |
| `eventName` | `VARCHAR` | `250` | `Y` |
| `dayType` | `VARCHAR` | `3` | `N` |
| `fileType` | `VARCHAR` | `1` | `Y` |
| `entityState` | `VARCHAR` | `25` | `Y` |
| `createdTime` | `TIMESTAMP` | `0` | `N` |
| `modifiedTime` | `TIMESTAMP` | `0` | `N` |

The sample response reports `dqGrading.dataQuality` as `Amber` and an empty `dqRemarks` value. It also reports `541550` total records with a page size of `2000`. The source does not define the processing meaning of Amber, pagination parameters, retry rules, caching, or compensation-domain consumption rules.

The response sample is timestamped 2026-08-05, after the document update date of 2026-08-04. This discrepancy should be clarified if strict version traceability is required.