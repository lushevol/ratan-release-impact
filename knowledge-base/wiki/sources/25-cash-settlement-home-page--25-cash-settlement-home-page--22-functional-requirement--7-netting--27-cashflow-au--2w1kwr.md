---
type: source
title: "Cash Settlement Home Page — Cashflow Auto Netting Functional Requirement — 2024"
authors: []
year: 2024
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/4922680"
venue: "Azure DevOps functional requirement"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, cashflow, auto-netting, functional-requirement, RATAN, 2024Q3]
related: [ratan, cash-settlement-home-page, cashflow-auto-netting, auto-netting-rule-management, business-calendar-relative-netting-time, cashflow-blotter-action-eligibility, cashflow-exception-handling, cashflow-failure-and-reinstatement, pending-fixing-stp-nstp-control, what-are-the-canonical-cashflow-state-and-sub-state-values]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Cashflow Auto Netting- 2024.md"]
---
# Cash Settlement Home Page — Cashflow Auto Netting Functional Requirement — 2024

## Summary

This document is a 2024 Q3 functional requirement for a proposed RATAN capability that allows Data Ops users to configure cashflow auto-netting rules through the Cash Settlement Home Page. Matching cashflows are held in **Pending Auto Netting** until a configured business-calendar-relative netting datetime. At execution, eligible cashflows are netted only with other cashflows selected by the same rule and sharing the Day 1 backend netting key.

This page records requirement-level evidence. It does not establish implementation, UAT completion, production deployment, formal approval, or go-live authorization.

## Scope

The requested Day 1 capability includes:

- An Auto Netting Rule Blotter accessible only to the Data Ops profile.
- A shared UI with the manual netting rule blotter and a manual/auto indicator.
- Selection of available rule fields and addition of exclusion criteria.
- Mandatory Booking Entity selection.
- Netting time expressed as `VD`, `VD-1`, or `VD-2` plus a time.
- Duplicate-condition prevention.
- Rule update and delete actions.
- Rule-scoped netting without cross-rule netting.
- Processing after manual netting rule checks and before multiple-exception checks.

The following are explicitly outside Day 1:

- Currency-pair conditions.
- Additional netting keys such as `structure id`.
- Configurable rule priority.
- A refresh or reprocessing function for cashflows already held in Pending Auto Netting.

## Day 1 Backend Netting Key

The Day 1 backend netting key is:

1. Booking Entity
2. Counterparty
3. Currency
4. Payment Date

The key is separate from the rule conditions. A rule determines eligibility; the backend key determines which eligible cashflows form one netting group.

## Rule Selection and Precedence

Cashflows are processed within the individual rule that selects them. A cashflow matching multiple rules is assigned to the rule with the earliest calculated netting datetime. If calculated netting datetimes are equal, system creation time determines the order.

For example:

| Rule | Configured netting time |
|---|---|
| rule1 | VD-1 18:00 |
| rule2 | VD 16:00 |
| rule3 | VD 18:00 |

A cashflow matching all three rules is processed by `rule1`, because `VD-1 18:00` is earliest.

## Business-Calendar Mapping

| Booking entity jurisdiction | Home currency |
|---|---|
| INDIA | INR |
| CHINA | CNY |
| SINGAPORE | SGD |
| MALAYSIA | MYR |
| UK | GBP |
| GERMANY | EUR |

The source states that netting-date calculation uses the business calendar associated with the booking entity's home currency.

## Queue and Action Behavior

A cashflow matching an auto-netting rule is held in **Pending Auto Netting** until the configured netting datetime.

The specified actions are:

- **Settle as gross**, with a warning. Whether bulk settlement is allowed is unresolved.
- **Net selected cashflow**, with a warning that the cashflow is intended for auto netting.

Other actions, including suppress, fail, and hold, are disabled in the same manner as for Pending Netting. “Net selected cashflow” is permitted for cashflows in Pending Netting, Pending Auto Netting, and Pending Exception.

Cashflows received after the configured netting datetime are not held for auto netting and are sent to Pending Netting for manual action.

## Lifecycle Requirements

- If only one cashflow remains at execution time, it is released from Pending Auto Netting to multiple-exception checking and should trigger **Single Cashflow**.
- A netting resultant is held NSTP.
- A manually or system-un-netted component cashflow skips auto-netting rule checks and is held NSTP.
- Trade affirm or confirm of a component cashflow does not affect the cashflow and follows Pending Netting behavior.
- A cancellation before execution removes the cancelled cashflow from the auto-netting queue.
- A cancellation after execution deadens the resultant, cancels the withdrawn component, and releases surviving components to Pending Exception.

## Requirement Lifecycle Examples

### Auto-netting execution

| Event | Cashflow ID | Cashflow Version | Cashflow Status | Cashflow Sub Status Type | Cashflow Sub Status |
|---|---|---:|---|---|---|
| Cashflow hit netting rule | C01 | 1 | WAITING | Pending Auto Netting | Pending Operator? |
| Cashflow hit netting rule | C02 | 1 | WAITING | Pending Auto Netting | Pending Operator? |
| Auto netting job on netting date time | C01 | 2 | NETTED | NA | NA |
| Auto netting job on netting date time | C02 | 2 | NETTED | NA | NA |
| Auto netting job on netting date time | N01 | 1 | WAITING | Pending Exception | Pending Operator |

The `Pending Operator?` notation is preserved from the source and is not a confirmed canonical sub-status.

### Manual un-netting

| Event | Cashflow ID | Cashflow Version | Cashflow Status | Cashflow Sub Status Type | Cashflow Sub Status |
|---|---|---:|---|---|---|
| Cashflow hit netting rule | C01 | 1 | WAITING | Pending Auto Netting | Pending Operator? |
| Cashflow hit netting rule | C02 | 1 | WAITING | Pending Auto Netting | Pending Operator? |
| Auto netting job on netting date time | C01 | 2 | NETTED | NA | NA |
| Auto netting job on netting date time | C02 | 2 | NETTED | NA | NA |
| Auto netting job on netting date time | N01 | 1 | WAITING | Pending Exception | Pending Operator |
| User unnet the netting resultant cashflow | N01 | 2 | DEAD | NA | NA |
| User unnet the netting resultant cashflow | C01 | 3 | WAITING | Pending Exception | Pending Operator |
| User unnet the netting resultant cashflow | C02 | 3 | WAITING | Pending Exception | Pending Operator |

### Upstream cancellation after netting

| Event | Cashflow ID | Cashflow Version | Cashflow Status | Cashflow Sub Status Type | Cashflow Sub Status |
|---|---|---:|---|---|---|
| Cashflow hit netting rule | C01 | 1 | WAITING | Pending Auto Netting | Pending Operator? |
| Cashflow hit netting rule | C02 | 1 | WAITING | Pending Auto Netting | Pending Operator? |
| Cashflow hit netting rule | C03 | 1 | WAITING | Pending Auto Netting | Pending Operator? |
| Auto netting job at netting date time | C01 | 2 | NETTED | NA | NA |
| Auto netting job at netting date time | C02 | 2 | NETTED | NA | NA |
| Auto netting job at netting date time | C03 | 2 | NETTED | NA | NA |
| Auto netting job at netting date time | N01 | 1 | WAITING | Pending Exception | Pending Operator |
| Withdrawal C01 | N01 | 2 | DEAD | NA | NA |
| Withdrawal C01 | C01 | 3 | CANCEL | NA | NA |
| Withdrawal C01 | C02 | 3 | WAITING | Pending Exception | Pending Operator |
| Withdrawal C01 | C03 | 3 | WAITING | Pending Exception | Pending Operator |

### Upstream cancellation before netting

| Event | Cashflow ID | Cashflow Version | Cashflow Status | Cashflow Sub Status |
|---|---|---:|---|---|
| Cashflow hit netting rule | C01 | 1 | WAITING | Pending Auto Netting |
| Cashflow hit netting rule | C02 | 1 | WAITING | Pending Auto Netting |
| Cashflow hit netting rule | C03 | 1 | WAITING | Pending Auto Netting |
| Withdrawal C1 | C01 | 2 | CANCEL | NA |
| Auto netting job on netting date time | C02 | 2 | NETTED | NA |
| Auto netting job on netting date time | C03 | 2 | NETTED | NA |
| Auto netting job on netting date time | N01 | 1 | WAITING | Pending Exception |

## Operational Caveat

Rule changes are prospective only. If a rule is updated or deleted after a cashflow enters Pending Auto Netting, the existing cashflow remains in that queue and must be manually checked by Ops. The requirement does not define an alert, reconciliation report, owner, SLA, or safe rejection path for such stranded items.

## Review History

| Date | Attendees | Comment |
|---|---|---|
| 2024-07-16 | Dinesh, Wayne, Pradeesh, Babu, Shiau Fong | |
| 2024-07-22 | Pradeesh, Babu | Reviewed the requirement for day1 scope |

## Related Wiki Pages

The requirement extends [[entities/ratan]], [[concepts/ad-hoc-cashflow-netting]], [[concepts/cashflow-blotter-action-eligibility]], [[concepts/cashflow-exception-handling]], [[concepts/cashflow-failure-and-reinstatement]], and [[concepts/pending-fixing-stp-nstp-control]]. Its candidate state values should be compared with [[queries/what-are-the-canonical-cashflow-state-and-sub-state-values]].
