---
type: source
title: RFI Nostro Stamping Based on Portfolio — Change List and API
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, nostro, rfi, portfolio, static-data, api]
related: [rfi-nostro-stamping-based-on-portfolio, dedicated-nostro-selection, default-versus-rfi-nostro-configuration, what-is-the-authoritative-rfi-nostro-selection-and-fallback-rule, what-are-the-finddedicated-and-finddedicateds-api-contracts, what-is-the-required-outcome-when-rfi-changes-in-a-non-economic-amendment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md"]
---
# RFI Nostro Stamping Based on Portfolio — Change List and API

This functional requirement introduces portfolio-dedicated `RFI` Nostros alongside conventional `DEFAULT` Nostros. It defines static-data validation, cross-service propagation, selected external API payloads, and a KRW-specific MT210 condition.

## Core invariants

```text
nostroType value: DEFAULT or RFI

if DEFAULT will check dedicated field must null
if RFI will check dedicated field must not null

nostroType do not allow update
dedicated allow update
```

An `RFI` Nostro therefore requires dedicated information, represented in the supplied contracts by a portfolio. A `DEFAULT` Nostro must have `dedicated: null`. Classification is immutable after creation, whereas the dedicated information may be updated.

## Changing services

| # | Service name | Required change |
|---:|---|---|
| 1 | `ratanone-static-data-service` | Add `NostroType` to `ratan_static__cashflow_nostro`; add `nostro_dedicated_info`; provide `findDedicated` to `ssi-serivce`; provide `findDedicateds` to `group-serivce`; allow all Nostro query APIs to filter by `nostroType`, with an empty value retrieving all types; update Nostro CRUD. |
| 2 | `ratan-cash-settlement-group-management-service` | For qualifying non-economic amendments, additionally consider whether RFI changed between prior and current states. |
| 3 | `ratan-cash-settlement-ssi-stamping-service` | Change Nostro lookup when a cashflow references SSI; consider trade-stamp compatibility during lookup; support `nostroType` and portfolio in maker/checker ad hoc handling. |
| 4 | `ratan-cash-settlement-query-service` | Return `Nostro_Type` and `Dedicated` in cashflow detail; derive cashflow-detail `nostroType` from the domain event. |
| 5 | `ratan-cashflow-lifecycle-service` | Publish domain events including `nostroType`; return `nostroType` from `/v2/ratan/cashflow/move/status`. |
| 6 | `ratanone-foundation` | Add `Nostro_Type` to queries. |
| 7 | `ratanone-swift-service` | Generate MT210 tag 25 when `ccy=KRW` and `sendersCorrespondent53Account!=null`. |
| 8 | `ratanone-db-repository` | Add a `ratanone_validation_rule` for UI validation and migrate RFI Nostro data with dedicated information. |

## Static Nostro API contracts

### Create Nostro

```http
POST /v2/static/nostros
```

```json
{
  "legalEntity": "test12",
  "legalEntityFmId": "test12",
  "settlementCurrency": "test12",
  "settlementMeans": "WMSUS",
  "currencyPair": "test12",
  "settlementAccount": "test12",
  "startDate": "2026-01-09",
  "endDate": "9999-12-31",
  "sendersCorrespondent53Swift": "",
  "sendersCorrespondent53Fullname": "",
  "sendersCorrespondent53Address": "",
  "sendersCorrespondent53City": "",
  "sendersCorrespondent53Postcode": "",
  "sendersCorrespondent53Account": "",
  "noticeToReceive": "N",
  "primary": "N",
  "ebbsNostroAccount": "test12",
  "tlmSetId": "",
  "nostroType": "RFI",
  "dedicated": {
    "portfolio": "test12"
  }
}
```

```json
{
  "result": "success",
  "nostroId": "1068878d-9b84-4e47-b659-099f44f98a56"
}
```

### Update Nostro

```http
POST /v2/static/nostros
```

```json
{
  "id": "1068878d-9b84-4e47-b659-099f44f98a56",
  "legalEntity": "test13",
  "legalEntityFmId": "test13",
  "settlementCurrency": "test13",
  "settlementMeans": "WMSUS",
  "currencyPair": "test13",
  "settlementAccount": "test13",
  "startDate": "2026-01-09",
  "endDate": "9999-12-31",
  "sendersCorrespondent53Swift": "",
  "sendersCorrespondent53Fullname": "",
  "sendersCorrespondent53Address": "",
  "sendersCorrespondent53City": "",
  "sendersCorrespondent53Postcode": "",
  "sendersCorrespondent53Account": "",
  "noticeToReceive": "N",
  "primary": "N",
  "ebbsNostroAccount": "test13",
  "tlmSetId": "",
  "nostroType": "RFI",
  "dedicated": {
    "portfolio": "test13"
  }
}
```

The response is the same as for create. `nostroType` cannot be updated; `dedicated` can be updated.

### Filtered Nostro loading

```http
GET /v2/static/nostros?nostroType=RFI&page=0&size=4
```

```text
nostroType value: null or DEFAULT or RFI
```

An empty/default `nostroType` filter retrieves all types.

```json
{
  "nostroType": "RFI",
  "dedicated": {
    "portfolio": "test13"
  }
}
```

```json
{
  "nostroType": "DEFAULT",
  "dedicated": null
}
```

### Nostro audit

```http
GET /v2/static/nostros/audit/1068878d-9b84-4e47-b659-099f44f98a56
```

The audited `cashflowNostro` preserves the type and dedicated information:

```json
{
  "nostroType": "RFI",
  "dedicated": {
    "portfolio": "test13"
  }
}
```

## NSTPSSI maker/checker contracts

### Maker

```http
POST /api/ratan/v1/camunda/task/NSTPSSI/maker
```

```json
{
  "fitNostro": {
    "settlementMeans": "NOS",
    "settlementAccount": "USD MAIN",
    "sendersCorrespondent53Swift": "SCBLUS33XXX",
    "sendersCorrespondent53Fullname": "STANCHART NY",
    "sendersCorrespondent53Address": "1095 AVENUE OF THE AMERICAS NEW YORK",
    "sendersCorrespondent53City": "NEW YORK 10036",
    "sendersCorrespondent53Account": "3582088442001",
    "noticeToReceive": "N",
    "nostroType": "RFI",
    "dedicatedPortfolio": "123"
  }
}
```

### Checker

```http
POST /api/ratan/v1/camunda/task/NSTPSSI/checker
```

```json
{
  "fitNostro": {
    "settlementMeans": "NOS",
    "settlementAccount": "USD MAIN",
    "sendersCorrespondent53Swift": "SCBLUS33XXX",
    "sendersCorrespondent53Fullname": "STANCHART NY",
    "sendersCorrespondent53Address": "1095 AVENUE OF THE AMERICAS NEW YORK",
    "sendersCorrespondent53City": "NEW YORK 10036",
    "sendersCorrespondent53Account": "3582088442001",
    "noticeToReceive": "N",
    "nostroType": "RFI",
    "dedicatedPortfolio": "123"
  }
}
```

## Cashflow-detail GraphQL additions

```graphql
graphCashFlowDetails(cashflowIds: ["M0176275724"]) {
  ratanNostroCandidates {
    Account {
      SCB_Nostro_Account_Number
      SCB_Nostro_Account_Type
      Beneficiary_BIC_code
      Beneficiary_Account_Name
      Beneficiary_Account_Name_2
      Beneficiary_Street_Address
      Beneficiary_City
      Beneficiary_Account_Number
      Intermediary_BIC_code
      Intermediary_Account_Name
      Intermediary_Street_Address
      Intermediary_City
      Intermediary_Account_Number
      Beneficiary_Bank_BIC_code
      Beneficiary_Bank_Account_Name
      Beneficiary_Bank_Street_Address
      Beneficiary_Bank_City
      Beneficiary_Bank_Account_Number
      Beneficiary_Correspondent_BIC_code
      Beneficiary_Correspondent_Account_Name
      Beneficiary_Correspondent_Street_Address
      Beneficiary_Correspondent_City
      Beneficiary_Correspondent_Account_Number
      Ordering_Customer_BIC_Code
      Ordering_Customer_Account_Name
      Ordering_Customer_Street_Address
      Ordering_Customer_City
      Ordering_Customer_Account_Number
      Counterparty_CMS_Account_Number
      EBBS_Bridge_Account_Number
      EBBS_Account_Number
      Booking_Entity_Correspondent_BIC_code
      Booking_Entity_Correspondent_Account_Name
      Booking_Entity_Correspondent_Street_Address
      Booking_Entity_Correspondent_City
      Booking_Entity_Correspondent_Account_Number
    }
    SSI_Id
    SSI_Unique_Id
    SSI_Source
    SSI_Priority
    Swift_Message_Type
    CFI_Code
    Payment_Currency
    Counterparty_SCI_FMID
    SCB_Entity_SCI_FMID
    Remittance_Information_1
    Remittance_Information_2
    Remittance_Information_3
    Remittance_Information_4
    Sender_To_Receiver_Information_1
    Sender_To_Receiver_Information_2
    Sender_To_Receiver_Information_3
    Sender_To_Receiver_Information_4
    Sender_To_Receiver_Information_5
    Sender_To_Receiver_Information_6
    Is_Third_Party_Payment
    Swift_Payment_Method
    Swift_Payment_Date
    Charge_Bearer
    Nostro_Swift_Message_Type
    Nostro_Type
    Dedicated {
      Portfolio
    }
  }
  ratanAffirmation {
    Affirmed_By
    Phone_Email
    Affirmed_At
  }
}
```

Candidate records demonstrate the following representations:

```json
{
  "Nostro_Type": "RFI",
  "Dedicated": {
    "Portfolio": "abc33"
  }
}
```

```json
{
  "Nostro_Type": "DEFAULT",
  "Dedicated": null
}
```

## Deprecated manual-split interface

The following interface is explicitly struck through in the requirement and must not be treated as an active contract without confirmation:

```http
~~POST /ratan/v1/cashSettlement/cashflows/manualSplit~~
```

Its historical payload shape contained:

```json
{
  "nostroAccount": {
    "id": "",
    "legalEntity": "",
    "createdAt": "",
    "updatedAt": "",
    "primaryFlag": "",
    "nostroType": "RFI",
    "dedicated": {
      "portfolio": "abc"
    }
  }
}
```

## Delivery gaps

The source does not define the portfolio source or matching method, RFI-versus-DEFAULT precedence, zero/multiple-match handling, or the action required after an RFI change in a non-economic amendment. It also names `findDedicated` and `findDedicateds` without defining their protocol contracts. These gaps are tracked in [[what-is-the-authoritative-rfi-nostro-selection-and-fallback-rule]], [[what-are-the-finddedicated-and-finddedicateds-api-contracts]], and [[what-is-the-required-outcome-when-rfi-changes-in-a-non-economic-amendment]].