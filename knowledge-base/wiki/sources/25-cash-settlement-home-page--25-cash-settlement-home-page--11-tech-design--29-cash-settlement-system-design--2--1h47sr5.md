---
type: source
title: Cash Settlement Query Service Dashboard Design
authors: []
year: 2024
url: ""
venue: "Cash Settlement System Design"
tags: [cash-settlement, query-service, graphql, dashboard, cashflow]
related: [query-service, cash-settlement-platform, cash-settlement-query-service-graphql-read-model, cashflow-notification-and-auto-refresh, value-date-bounded-cashflow-queries, cashflow-blotter]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Query Service -Dashboard.md"]
---

# Cash Settlement Query Service Dashboard Design

## Summary

This technical design specifies a GraphQL dashboard read interface for the [[entities/query-service]] within the [[entities/cash-settlement-platform]]. The dashboard is intended to provide a real-time operational view of cashflow status counts, failed cashflows, volumes by value-date bucket, exceptions, and top exposure.

The design requires automatic refresh when cashflow statuses change, drill-down from dashboard datapoints to cashflow details, alphabetically sorted filter values, a scrollable list of all exceptions, and business-date-specific handling for queued cashflows and Friday `VD-1` values.

## Product Requirements

- Display cashflow counts by processing status in real time.
- Automatically refresh the dashboard when cashflow statuses change.
- Display the underlying cashflow details when an operator selects a datapoint.
- Support filters whose values are alphabetically sorted.
- Restrict `QUEUED` to the next five business days.
- Calculate top exposure only from outstanding cashflows pending Ops action: `WAITING`, `ERROR`, `QUEUED`, `READY`, `HOLD`, `NACK`, and `FAILED`.
- On Friday, include Saturday, Sunday, and Monday in `VD-1`.
- Include all exceptions in a scrollable list.

## GraphQL Data Model

The source defines the following dashboard model:

```erl
type GraphCashFlowDashBoard{
    Status_Num:CashflowStatusNum
    Failed_Num:CashflowFailedNum
    Volume_By_VD:VolumeByVD
    Exception_Num:ExceptionNum
    Top_Exposure:TopExposure
}

type TopExposure{
    Exposure_List:[Exposure]
}

type Exposure{
    Amount:String
    Counter_Party:String
    Type:String
}
type ExceptionNum{
    VD_Exceptions:[VDException]
}

type VDException{
    Exception_Code:String
    VD_Num:Int
    VD1_Num:Int
    VD2_Num:Int
    VDM_Num:Int
}
type VolumeByVD{
    VD_Num:Int
    VD1_Num:Int
    VD2_Num:Int
    VDM_Num:Int
}
type CashflowFailedNum{
    Total_Num:Int
    Internal_Total_Num:Int
    External_Total_Num:Int
    Total_Today_Num:Int
    Internal_Today_Num:Int
    External_Today_Num:Int


    Total_Yesterday_Num:Int
    Internal_Yesterday_Num:Int
    External_Yesterday_Num:Int

    Total_PriorDates_Num:Int
    Internal_PriorDates_Num:Int
    External_PriorDates_Num:Int

}
type CashflowStatusNum{
    Wating_Today_Num:Int
    Error_Num:Int
    Queued_Num:Int
    Nack_Num:Int
    Hold_Num:Int
    Group_Error_Num:Int
    Group_Pending_Num:Int
    Failed_Today_Num:Int
}
```

## API Contract

| API Name | Interface | Method | Request Sample | Header | Note |
| --- | --- | --- | --- | --- | --- |
| Query Cashflows | http://{domain}/[graphql](https://uklvadapp1346.uk.dev.net:8868/graphql) | Post | `{ cashflowDashboard( filter: [] page: 0 size: 6 ) { ... } }` |  |  |

The request is a GraphQL POST operation named `cashflowDashboard`. It accepts a filter list, a zero-based page number, and a page size.

The complete request shape shown in the source is:

```graphql
{ cashflowDashboard( filter: [] page: 0 size: 6 ) { Status_Num { Wating_Today_Num Error_Num Queued_Num Nack_Num Hold_Num Group_Num Failed_Today_Num } Volume_By_VD{ VD_Num VD1_Num VD2_Num VDM_Num } Exception_Num{ VD_Exception{ High_Value_Num GSAM_Num Missing_Vostor_Num Missing_Nostor_Num Back_Value_Date_Num Secondary_Vostro_Num Pending_Affirmation_Num } VD1_Exception{ High_Value_Num GSAM_Num Missing_Vostor_Num Missing_Nostor_Num Back_Value_Date_Num Secondary_Vostro_Num Pending_Affirmation_Num } VD2_Exception{ High_Value_Num GSAM_Num Missing_Vostor_Num Missing_Nostor_Num Back_Value_Date_Num Secondary_Vostro_Num Pending_Affirmation_Num } VDM_Exception{ High_Value_Num GSAM_Num Missing_Vostor_Num Missing_Nostor_Num Back_Value_Date_Num Secondary_Vostro_Num Pending_Affirmation_Num } } Top_Exposure{ Exposure_List { Amount Counter_Party Type } } Failed_Num { Total_Num Internal_Total_Num External_Total_Num Total_Today_Num Internal_Today_Num External_Today_Num Total_Yesterday_Num Internal_Yesterday_Num External_Yesterday_Num Total_PriorDates_Num Internal_PriorDates_Num External_PriorDates_Num } } }
```

## Illustrative Response

The source provides this response example:

```json
{ "data": { "cashflowDashboard": { "Status_Num": { "Wating_Today_Num": 5, "Error_Num": 0, "Queued_Num": 0, "Nack_Num": 0, "Hold_Num": 0, "Group_Error_Num": 51, "Group_Pending_Num": 7094, "Failed_Today_Num": 0 }, "Volume_By_VD": { "VD_Num": 5, "VD1_Num": 4, "VD2_Num": 0, "VDM_Num": 0 }, "Exception_Num": { "VD_Exceptions": [ { "Exception_Code": "ReInstate", "VD_Num": 1, "VD1_Num": 0, "VD2_Num": 0, "VDM_Num": 0 }, { "Exception_Code": "Missing Vostro", "VD_Num": 1, "VD1_Num": 0, "VD2_Num": 0, "VDM_Num": 0 }, { "Exception_Code": "Pending Affirmation", "VD_Num": 0, "VD1_Num": 1, "VD2_Num": 0, "VDM_Num": 0 }, { "Exception_Code": "Murex IRS", "VD_Num": 1, "VD1_Num": 0, "VD2_Num": 0, "VDM_Num": 0 } ] }, "Top_Exposure": { "Exposure_List": [ { "Amount": "-17736934.095781", "Counter_Party": "BOA*MMB", "Type": "BANK" }, { "Amount": "2002.020000", "Counter_Party": "LEONTEQ SECUR*ZRH", "Type": "FININST" }, { "Amount": "2002.000000", "Counter_Party": null, "Type": "null" }, { "Amount": "1001.000000", "Counter_Party": "LEONTEQ SECUR*ZRH", "Type": "null" }, { "Amount": "-773.818065", "Counter_Party": "SCB SUZHOU*SUZ", "Type": "INTECOM" } ] }, "Failed_Num": { "Total_Num": 336, "Internal_Total_Num": 3, "External_Total_Num": 333, "Total_Today_Num": 0, "Internal_Today_Num": 0, "External_Today_Num": 0, "Total_Yesterday_Num": 0, "Internal_Yesterday_Num": 0, "External_Yesterday_Num": 0, "Total_PriorDates_Num": 336, "Internal_PriorDates_Num": 3, "External_PriorDates_Num": 333 } } } }
```

These values are illustrative and do not establish production baselines, freshness, or correctness.

## Contract Inconsistencies

The declared model and example query do not describe one unambiguous GraphQL contract:

- The model declares `Group_Error_Num` and `Group_Pending_Num`, while the query requests `Group_Num`.
- The model declares `VD_Exceptions:[VDException]`, while the query requests separate `VD_Exception`, `VD1_Exception`, `VD2_Exception`, and `VDM_Exception` objects.
- The model declares generic exception fields such as `Exception_Code` and `VD_Num`, while the query requests named fields including `High_Value_Num`, `GSAM_Num`, `Missing_Vostor_Num`, and `Pending_Affirmation_Num`.
- `Wating_Today_Num` is consistently misspelled in the model and query. The compatibility policy for correcting it is not defined.
- The model uses nullable-looking `String` fields, and the response contains `null` values for `Counter_Party` and `Type`, but nullability is not explicitly specified.
- `Amount` is represented as a `String`, although the sample contains decimal-looking positive and negative values. Currency, precision, aggregation, and ranking semantics are unspecified.
- The effect of `page` and `size` on dashboard summaries, exposure rows, and drill-down detail rows is not defined.

## Evidence and Limitations

The source directly documents the intended requirements, proposed GraphQL types, request shape, and sample response. It does not document implementation queries, storage schemas, indexes, authorization or data-entitlement behavior, refresh events, consistency guarantees, performance targets, availability targets, or a canonical business-day calendar.

The source also references diagrams that are not available in the supplied text. The dashboard design should therefore be treated as an intended contract proposal rather than validated production behavior.

## Related Designs

This design should be compared with the existing [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--29-cash-settlement-system-design--3--1tc15rv|Cash Flow Query Model]] and [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--29-cash-settlement-system-design--3--16coite|Cash Settlement Query Service Design]]. It is specifically relevant to the [[concepts/cash-settlement-query-service-graphql-read-model]], [[concepts/cashflow-notification-and-auto-refresh]], [[concepts/value-date-bounded-cashflow-queries]], and [[entities/cashflow-blotter]].
