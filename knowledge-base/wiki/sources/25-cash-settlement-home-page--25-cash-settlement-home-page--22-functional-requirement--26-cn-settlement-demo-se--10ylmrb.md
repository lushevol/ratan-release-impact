---
type: source
title: Sprint 17
authors: []
year: 0
url: ""
venue: "CN Settlement Demo Session"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cn, demo, functional-requirement, cashflow, netting]
related: [ratan, stella, cashflow-blotter, value-date-based-cashflow-materialization, cashflow-lifecycle-supersession-and-audit-history, cashflow-netting-and-un-netting-state-transitions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 17.md"]
---
# Sprint 17

This functional/demo specification defines nine CN settlement acceptance cases for [[ratan]]. It specifies expected behavior for cashflow ingestion, value-date materialization, lifecycle display and audit history, netting, and un-netting.

The document contains expected results only. It does not provide execution evidence, screenshots, logs, approvals, or test sign-off. Its statements should therefore be treated as proposed acceptance criteria rather than validated production behavior.

## Acceptance Criteria

| NO. | Description | Steps | Expected Result | Cashflow SCBML |
| --- | --- | --- | --- | --- |
| 1 | Stella cashflow from CCS trade | 1. Mock the Stella CCS cashflow 1. Initial exchange cashflows which value date is T+2 2. Final exchange cashflows which value date is in 1 year 2. Manually push new message to Ratan workflow 3. Load cashflow from cashflow blotter | 1. Cashflow with value date as T+2 is moved to 'QUEUED' status 2. Cashflow with value date as 1 year remains in 'PROJECTED' status | |
| 2 | Stella cashflow forward trade (T+5) | 1. Mock the Stella Forward cashflow, value date is T+5 2. Manually push new message to Ratan workflow 3. Load cashflow from cashflow blotter | 1. Cashflow with value date as T+5 is moved to 'QUEUED' status | |
| 3 | Stella cashflow forward trade (T+6) | 1. Mock the Stella Forward cashflow, value date is T+6 2. Manually push new message to Ratan workflow 3. Load cashflow from cashflow blotter | 1. Cashflow with value date as T+6 is still in 'PROJECTED' status | |
| 4 | Stella VD-7 and run materialization on VD-5 | 1. Mock the Stella Forward cashflow, value date is T+7 2. Manually push new message to Ratan workflow 3. Run the materialization job on T+2( in the VD -5 window) | 1. Cashflow status is 'PROJECTED' status on T( VD -7) 2. Cashflow status moved to 'QUEUED" status on T+2( VD-5) | |
| 5 | Stella Spot New + Amendment | 1. Mock Stella Spot trade cashflow 2. Mock Stella Spot trade amendment cashflow | 1. Only the latest amendment event displayed in cashflow blotter 2. Cashflow New + Amendment audit is available in cashflow history page | |
| 6 | Stella Spot New + Withdrawal | 1. Mock Stella Spot trade cashflow 2. Mock Stella Spot trade Withdrawal cashflow | 1. Only the latest Withdrawal event displayed in cashflow blotter 2. Cashflow New + Withdrawal audit is available in cashflow history page | |
| 7 | Murex Spot New + Amendment | 1. Book Murex Spot trade 2. Perform C&R on Murex Spot trade | 1. Only the latest amendment event displayed in cashflow blotter 2. Cashflow New + Amendment audit is available in cashflow history page | |
| 8 | Netting | 1. Book Spot trades from Murex 2.11 2. Mock Stella Spot trade cashflow 3. Perform the netting from Ratan cashflow blotter | 1. Component cashflow moved to 'Netted' 2. Resultant cashflow created as 'Queued'. 3. Amount of netting resultant cashflow is sum of component cashflows 4. Same netting id for component & resultant cashflow | |
| 9 | Un-Netting | 1. Perform the un-net from GUI | 1. Component cashflow status moved back to 'Queued' 2. Resultant cashflow status moved to 'Dead' | |

## Intended Status Behavior

The cases specify per-cashflow status determination rather than a single status for all legs of a trade:

- A [[stella]] CCS initial exchange at T+2 is expected to be `QUEUED`, while a final exchange one year ahead remains `PROJECTED`.
- A Stella forward cashflow at T+5 is expected to be `QUEUED`; at T+6 it is expected to remain `PROJECTED`.
- A T+7 forward cashflow is expected to transition from `PROJECTED` to `QUEUED` when the materialization job runs at the stated VD-5 window.
- Netting is expected to move components to `Netted` and create a resultant cashflow in `Queued`.
- Un-netting is expected to return components to `Queued` and move the resultant to `Dead`.

The document does not define whether T+n uses business or calendar days, the governing calendar, timezone, cutoff time, or the materialization job schedule.

## Lifecycle Display and Audit Requirements

For Stella spot amendments and withdrawals, and for a Murex spot amendment following C&R, the active [[cashflow-blotter]] must display only the latest lifecycle event. The Cashflow History Page must retain the corresponding full event sequence:

- New plus Amendment;
- New plus Withdrawal; or
- New plus Amendment for the Murex scenario.

The source does not expand C&R, define handling of out-of-order or duplicate events, or specify display fields for a withdrawal.

## Netting Requirements

The netting case combines spot cashflows booked in Murex 2.11 with mocked Stella spot cashflows. Expected behavior is:

1. Each component becomes `Netted`.
2. The resultant is created as `Queued`.
3. The resultant amount equals the sum of component amounts.
4. Components and resultant share one Netting ID.

The source does not define eligibility criteria, signed-amount conventions, Netting ID generation, failure handling, or atomicity. See [[what-are-the-netting-eligibility-and-netting-id-rules-for-cn-cashflows]].