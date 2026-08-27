---
type: source
title: Drop 2 UAT Open Issues and Test Cases
authors: []
year: 0
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [uat, drop-2, cashflow-events-control, open-issues, regression-testing]
related: [what-is-the-authoritative-effective-date-rule-for-trade-amendment-cashflows, should-undo-revive-released-settled-netted-or-split-cashflows, is-expiry-processing-intentionally-excluded-from-refixing-workflows, stella, blade, ratan, pre-post-performance-regression-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/Drop 2 UAT Open Issues and test cases.md"]
---
# Drop 2 UAT Open Issues and Test Cases

This source is a point-in-time UAT issue and action register for Drop 2. It records one critical open defect in [[stella]] and eight incomplete testing, regression-review, or sign-off actions involving [[stella]], [[blade]], and [[ratan]]. It does not provide resolution evidence, approved expected behaviour, or final UAT sign-off.

## Critical Open Defect

Issue 423 is an `OPEN`, `Critical` Stella defect associated with test case `MTC17` and Azure DevOps work item `3875467`, which has a stated ETA of 23rd Apr.

The issue reports asymmetric trade-amendment handling around the amendment effective date:

- Cashflows with `VD<effective date` are touched during the trade amendment.
- Cashflows with `VD>effective date` do not generate a new cashflow during the trade amendment.

The source identifies trades `4330350484` and `4354404271` as traceability examples. It does not specify the intended handling for value dates before, equal to, or after the effective date, nor does it confirm whether the work item was resolved. This is tracked in [[what-is-the-authoritative-effective-date-rule-for-trade-amendment-cashflows]].

## Open Actions and Unresolved Coverage

The action register shows that settlement scenarios, end-to-end retesting, regression-package review, and several specialised scenarios remained pending.

For portfolio reassignment, the proposed tactical approach is that [[blade]] must not permit an effective date or time different from the trade date. The source does not establish that this restriction was approved, implemented, or successfully retested.

For refixing and expiry coverage, manual refixing is reported as done, automatic refixing remains to be booked, and expired items are “not processed.” The reason and intended treatment of expiry remain unclear; see [[is-expiry-processing-intentionally-excluded-from-refixing-workflows]].

For undo after a settled withdrawal FT, the source states that a cashflow will not be revived from `released`, `settled`, `netted`, or `split` status, but immediately marks this expectation for discussion. It is therefore not an approved lifecycle rule. See [[should-undo-revive-released-settled-netted-or-split-cashflows]].

## Regression Governance Status

The Stella regression package required review by Lina and an email from Divya for Olexiy sign-off. The Ratan regression package also required review, with additional undo cases to be included. The HZ duplicate-payment issue was to be added to the regression package.

These entries are evidence of incomplete regression governance and sign-off dependencies, not proof of test completion or product approval.

## Source Tables

### Open Issues

| # | Issue description | **Status** | System | Type | Priority | Test case | Email subject | Ado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 423 | Cashflows VD<effective date are touched in the trade amendment, Cashflow VD>effective date doesn’t generate new cashflow in trade amendment | OPEN | Stella | Defect | Critical | MTC17 | FW: Trade 4330350484 & 4354404271- Amendment information unable to locate in Trade details - MTC17 | [3875467](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/3875467) ETA 23rd Apr |

### Open Actions

| # | Actions | Assignee | Status | Comment |
| --- | --- | --- | --- | --- |
| 1 | Settlement Scenarios | Pradeesh | | |
| 2 | Retest of E2E test cases | Pradeesh | | |
| 3 | Portfolio Reassignment- retest PR following by eco-amend/PR | Pradeesh | | For Tactical solution, Blade should not allow portfolio reassignment to have an effective date (time) different to trade date |
| 4 | Stella Regression Package Review | Lina | | Email from Divya for Olexiy signoff |
| 5 | Refixing (After released) +Expire test | Pradeesh | | Manual refixing done, Auto refixing to be booked, Expired is not processed |
| 6 | HZ duplicate payment issue | | | Email from Divya to be included in regression test package. |
| 7 | Test undo after settled withdrawal FT | Pradeesh | | Cashflow will not be revived if in released/settled/netted/split status Expectation to be discussed? |
| 8 | Ratan Regression test package (undo) review | Lina | | To add a few cases for undo |