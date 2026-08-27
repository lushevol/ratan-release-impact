---
type: concept
title: Dashboard Cashflow Status Counting
created: 2026-08-23
updated: 2026-08-23
tags: [dashboard, cashflow, status, exception-monitoring, counting]
related: [ratan-cashflow-dashboard, ratan, grouped-cashflow-monitoring, group-pending-monitoring, failed-cashflow-status-eligibility, failed-cashflow-reinstatement, aspire-payment-accounting, timer-based-dashboard-exception-visibility, what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/RATAN Cashflow Dashboard.md"]
---
# Dashboard Cashflow Status Counting

The RATAN Cashflow Dashboard defines count banners using four distinct fields: Cashflow State, Accounting Status, Swift Status, and Group State.

## Source-Defined Predicates

| Banner | Field and predicate |
|---|---|
| Waiting VD Today | `Cashflow State = "WAITING"` and `Payment Date = Current Date` |
| Failed VD Today | `Cashflow State = "FAILED"` and `Payment Date = Current Date` |
| Error | `Cashflow State = "Error"` and `Payment Date >=Current Date` and `Payment Date<=Current Date + 7D` |
| Accounting Error | `Accounting Status in ('SENT', 'DISABLED','HOLDING','REJECTED','MISSING_INFO')` |
| Swift Error | `Swift Status in ('AMH Error', 'FMSGW Error', 'FMSRE Error', 'MX Generation Error', 'Ratan Internal Error', 'SCPAY Error')` |
| Group Pending | `Group State ='PENDING'` |
| Group Error | `Group State ='ERROR'` |

Queued and Hold appear as banner labels but have no predicates in the source.

## Interpretation Boundaries

`FAILED` is used by the Failed VD Today banner and is relevant to [[failed-cashflow-status-eligibility]] and [[failed-cashflow-reinstatement]]. The source does not establish that the separately written cashflow-state value `Error` is part of the same authoritative lifecycle or status catalogue.

The Accounting Error list must not be assumed to be Aspire-specific. While it is related in terminology to [[aspire-payment-accounting]], this source does not identify Aspire as the accounting-status provider.

Group counts are group-level predicates and should not be interpreted as cashflow counts. They supplement [[grouped-cashflow-monitoring]] rather than define its state model.

## Unresolved Semantics

The requirement does not define:

- the authoritative catalogue or case sensitivity of status values;
- whether one cashflow can count in multiple banners;
- whether counts are distinct or overlapping;
- the time zone for `Current Date`;
- whether `Current Date + 7D` means calendar days or business days;
- whether payment-date boundaries are inclusive beyond the written operators.

Timezone interpretation remains linked to [[what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields]].