---
type: source
title: Cash Settlement Auto Netting TechDesign
authors: []
year: 2024
url: ""
venue: Internal technical design
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, technical-design, lifecycle, scheduling]
related: [auto-netting-rule-configuration, auto-netting-job-time, single-cashflow-auto-netting-exception, controlm, static-service, what-is-the-canonical-auto-netting-job-schedule-and-timezone, what-is-the-canonical-scbml-indicator-and-xpath-for-settle-as-single, what-action-is-prohibited-for-auto-netting-resultant-cashflows, what-is-the-auto-netting-hint-and-pending-auto-netting-status-transition]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Auto Netting TechDesign.md"]
---
# Cash Settlement Auto Netting TechDesign

This technical design specifies intended changes for cash-settlement auto-netting. It describes responsibilities across the front end, Static service, [[ratanone-rule-service]], [[ratan-rule-service]], [[lifecycle-service]], the netting service, [[nstp]], and [[controlm]]. It is design evidence, not confirmation of implementation, deployment, or production behavior.

## Rule configuration

The existing netting-rule blotter is to be reused with an auto-netting checkbox. When selected, booking entity, currency, and shifter are mandatory. The shifter supports hour and minute selection.

[[ratanone-rule-service]] is intended to persist `isAutoNetting`, support rule updates and deletion, validate booking entity/currency/shifter, perform duplicate checks, support exclusion criteria, and return `VD+Shifter` from rule checking when a hint applies.

A cashflow in `PendingAutoNetting` must not perform `SettleAsGross`. The design also contains an incomplete statement that an “Auto Netting resultant cashflow is not allowed to do” something, without identifying the prohibited action.

## Static data and scheduled time

Static service is to provide an API that calculates auto-netting datetime and a new static table for booking-entity home-currency lookup. The source supplies only this illustrative table:

| id | booking_entity | home_currency |
| --- | --- | --- |
| 1 | SG | USD |
| 2 | UK | USD |

No DDL, keys, constraints, effective dating, lookup semantics, or authoritative source of the static data is provided.

[[lifecycle-service]] is to accept a `shifter` parameter in status-update requests. For the `IsAutoNettingEligible` action, it calculates:

```text
jobTime = VD + Shifter
```

The design requires a `job_time` field in the SCBML history table.

## Auto-netting job processing

Lifecycle is to expose an auto-netting job API. It queries cashflows in `Waiting` and `PendingAutoNetting`, grouped by:

1. booking entity;
2. currency;
3. counterparty;
4. value date; and
5. job time.

The target cashflows must be locked before the job decides whether to invoke netting. The specified decision logic is:

| Group size | Time condition | Action |
| ---: | --- | --- |
| `> 1` | Current time `>= jobTime` | Call the netting service for the cashflows in the group. |
| `> 1` | Current time `< jobTime` | Do nothing. |
| `== 1` | Current time `>= jobTime` | Call status update with action `SettleAsSingle`. |
| `== 1` | Current time `< jobTime` | Do nothing. |

Job-execution results are to be recorded in a job table. The design does not specify locking scope, transaction boundaries, idempotency, retries, stale-lock recovery, or partial-failure handling.

## Single-cashflow handling

The `SettleAsSingle` lifecycle action returns a cashflow to `QUEUED`. [[ratan-rule-service]] is to add an NSTP rule that creates a “Single Cashflow” exception when a new SCBML indicator meets the relevant condition.

The field definition is unresolved. The design refers both to `SettleAsSingle` as an SCBML condition and to a new `SingleCashflow` SCBML indicator whose XPath “should be confirmed.” See [[single-cashflow-auto-netting-exception]] and [[what-is-the-canonical-scbml-indicator-and-xpath-for-settle-as-single]].

## Scheduling and orchestration

[[controlm]] is to run a new job “every 15mins” with this expression:

```text
0 */15 * * *
```

The expression’s effective cadence depends on the ControlM scheduling dialect and timezone; it requires confirmation before operational use.

The design proposes inserting auto-netting orchestration between `1_4_Netting_Eligible` and `1_5_Ssi_Stamping`, linking the new scheduled processing to [[ssi-stamping-hierarchy]].