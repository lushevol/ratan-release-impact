---
type: concept
title: Cash Settlement Dashboard Operational Read Model
tags: [cash-settlement, dashboard, query-service, graphql, read-model, operations]
related: [cash-settlement-query-service-graphql-read-model, query-service, cashflow-notification-and-auto-refresh, value-date-bounded-cashflow-queries, cashflow-blotter, cashflow-data, cashflow-data-history]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Query Service -Dashboard.md"]
---

# Cash Settlement Dashboard Operational Read Model

The Cash Settlement dashboard is designed as a consolidated operational read model served by the [[entities/query-service]]. Its `cashflowDashboard` operation combines five metric groups: status counts, failed-cashflow counts, volume by value date, exception counts, and top exposure.

## Metric Groups

### Status Counts

`Status_Num` provides operational counts for cashflow processing states, including waiting, error, queued, NACK, hold, failed-today, and group-level error and pending counts.

The design uses the identifier `Wating_Today_Num`, preserving the source typo. The API example also requests `Group_Num`, although the declared model defines `Group_Error_Num` and `Group_Pending_Num`.

### Failed-Cashflow Counts

`Failed_Num` separates:

- Total, internal, and external failed cashflows.
- Today, yesterday, and prior-date failures.

This enables operational users to distinguish current failures from older outstanding failures and to separate internal from external cashflows.

### Volume by Value Date

`Volume_By_VD` counts cashflows in the `VD`, `VD1`, `VD2`, and `VDM` buckets. These buckets are also used by the exception aggregation.

### Exception Counts

The declared model represents exceptions as a list of records containing an exception code and counts by value-date bucket:

```erl
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
```

The example query instead represents exceptions as separate objects for each value-date bucket and names individual exception fields. This representation must be reconciled before the schema is treated as authoritative.

### Top Exposure

`Top_Exposure` returns exposure records containing an amount, counterparty, and type:

```erl
type TopExposure{
    Exposure_List:[Exposure]
}

type Exposure{
    Amount:String
    Counter_Party:String
    Type:String
}
```

Top exposure is intended to include only outstanding cashflows pending Ops action. The qualifying statuses stated by the source are `WAITING`, `ERROR`, `QUEUED`, `READY`, `HOLD`, `NACK`, and `FAILED`.

The design does not define whether ranking is gross or net, whether negative amounts are ranked by absolute value, how currencies are handled, or whether records are aggregated by counterparty, cashflow, or exposure type.

## Dashboard Interaction Requirements

The dashboard should:

- Refresh when cashflow statuses change.
- Allow users to select a datapoint and see the associated cashflow details.
- Accept filters and return or display filter values in alphabetical order.
- Display all exceptions using a scrollable list.
- Restrict `QUEUED` to the next five business days.

The source does not define the event or subscription mechanism for refresh, the detail-row response contract, or the exact filtering and sorting semantics.

## Design Significance

Combining the metrics into one dashboard operation reduces the need for the UI to coordinate independent summary requests. It also creates a contract boundary where status semantics, date bucketing, exception representation, exposure policy, pagination, nullability, and authorization must be defined consistently.

This read model should be distinguished from the underlying current and historical cashflow stores represented by [[entities/cashflow-data]] and [[entities/cashflow-data-history]]. The source does not establish which tables or projections implement the dashboard.
