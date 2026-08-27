---
type: source
title: IRS Cashflow Processing Design
tags: [cash-settlement, irs, netting, lifecycle, orchestration]
related: [irs-cashflow-processing, irs-counterpart-leg-matching, withdrawal-new-cashflow-and-razor-release-check, ratan-cash-settlement-orchestration, camunda-api-response, lifecycle-service, netting-service, rule-service, razor, scbml]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# IRS Cashflow Processing Design

This design note describes an incomplete IRS-specific cashflow-processing path across orchestration, lifecycle, rule, and netting components. The intended flow introduces counterpart-leg coordination before generic netting eligibility processing.

## Delivery Status

The orchestration insertion, lifecycle trade lookup, and lifecycle waiting-state action are marked Done. The lifecycle withdrawal-and-release lookup is Pending. The IRS rule and netting-service counterpart lookup are In Progress. The note contains no populated critical test cases.

## Source Change Register

| Module | Changes | Description |
| --- | --- | --- |
| ratan-cash-settlement-orchestration | 1.1 Add a new sub process for IRS as above orchestration aisle. ( Done ) | after 1_2 CloseException&&SuppressionCheck and before 1_3 NettingEligibleCheck |
| ratan-cashflow-lifecycle-servie | 2.1 Provide a new API to query the cashflow is a withdrawal & new cashflow and if it has been released to Razor before ( Pending ) 2.2 Provide a trade query API to query the trade id related cashflows list. ( **Done **) 2.3 Add a new action 'WaitingLeg' to change status from QUEUED to WAITING + PendingAnotherLeg ( Done ) | 1. Query stella message table, if it is a withdrawal & new cashflow, its event is 'Withdrawal_New', 'pre_cashflow_id' not null. Query scbml history table, check if it has been released before |
| ratan-rule-service | 3.1 Provide a new rule type 'IRS' to check if it is IRS product and if netting id is null. (In Progress) | New rule type should not show in GUI drop down list. |
| ratan-cash-settlement-netting-service | 4.1 Provide a API to query it another leg is already in system. (**In Progress**) | Same VD / CCY / Client / TradeId (call 2.2 API to query) and status in Waiting + PendingAnotherLeg, if existing Net both cashflows. Return CamundaApiResponse with SUCCESS if not existing Call status update action refer to 2.3 to change current cashflow to Waiting + PendingAnotherLeg. Return camunda response with 'FILTERED' if any exception Return camunda response with FILTERED. Error message in description |

## Critical Test Case

| Case No | | | |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

## Design Boundaries

The source specifies that the proposed `IRS` rule checks an IRS product and a null netting ID, but it does not define IRS-product classification or the authoritative netting-ID source. It also does not provide API schemas, database queries, correlation keys, response payloads, concurrency controls, or acceptance criteria.

The source names `ratan-cashflow-lifecycle-servie`, which may refer to [[lifecycle-service]], but this identity is not confirmed. Its use of `PendingAnotherLeg` must also not be assumed to be the same state model described by [[pending-fixing-and-waiting-another-leg]].

See [[irs-cashflow-processing]], [[irs-counterpart-leg-matching]], and [[withdrawal-new-cashflow-and-razor-release-check]].