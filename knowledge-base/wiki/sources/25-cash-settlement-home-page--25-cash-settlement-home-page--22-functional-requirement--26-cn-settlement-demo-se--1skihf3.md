---
type: source
title: CN Settlement Demo Session — Sprint 14
authors: []
year: 2022
url: ""
venue: "CN Settlement Demo Session"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, ratan, cashflow, netting, functional-requirement, sprint-14]
related: [ratan, stella, cashflow-blotter, cashflow-materialization, cashflow-status-lifecycle, cashflow-amendment-supersession, cashflow-netting-and-un-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md"]
---
# CN Settlement Demo Session — Sprint 14

This functional demo specification covers Ratan cashflow storage, materialization, netting, and un-netting for Sprint 14, dated 14–28 November 2022. It defines expected behaviour only; it does not contain test execution evidence, pass/fail results, logs, or production validation.

[[Stella]] provides mocked `New` and `Amendment` messages that are manually pushed into the Ratan workflow. Ratan is expected to persist and display the resulting records in the [[Cashflow Blotter]].

## Functional scope

- Cashflow data storage in Ratan
- Cashflow materialization
- Netting and un-netting initiated from the GUI

## User cases

| NO. | Description | Steps | Expected Result |
| --- | --- | --- | --- |
| 1 | Stella New & VD-7 | 1. Mock Stella new message with payment date as VD-7 2. Manually push new message to Ratan workflow 3. Load cashflow from cashflow blotter | 1. Ratan can store cashflow in database as 'Projected' cashflow 2. Display in cashflow blotter GUI. |
| 2 | Stella New & VD-5 | 1. Mock Stella new message with payment date as VD-5 2. Manually push new message to Ratan workflow 3. Load cashflow from cashflow blotter | 1. Ratan can store cashflow in database as 'Queued' cashflow 2. Display in cashflow blotter GUI. |
| 3 | Stella New & VD-4 | 1. Mock Stella new message with payment date as VD-4 2. Manually push new message to Ratan workflow 3. Load cashflow from cashflow blotter | 1. Ratan can store cashflow in database as 'Queued' cashflow 2. Display in cashflow blotter GUI. |
| 4 | Stella VD-7 and run materialization on VD-5 | 1. Cashflow imported on VD-7 as 'Projected' (022022112410, 022022112405) 2. Run the materialization job on VD-5 | 1. Ratan moves the status to 'Queued' on VD-5 |
| 5 | Stella New + Amendment (VD-4) | 1. Mock Stella new message with payment date as VD-4 2. Mock Stella Amendment message on same cashflow | 1. Display the amendment cashflow only and discard the new |
| 6 | Netting | 1. Mock component cashflows 2. Perform Netting from GUI | 1. Component cashflow moved to 'Netted' 2. Resultant cashflow created as 'Queued'. 3. Amount of netting resultant cashflow is sum of component cashflows 4. Same netting id for component & resultant cashflow |
| 7 | Un-Netting | 1. Perform the un-net from GUI | 1. Component cashflow status moved back to 'Queued' 2. Resultant cashflow status moved to 'Dead' |

## Specified lifecycle

The specification establishes the individual-cashflow transitions `Projected → Queued`, `Queued → Netted`, `Netted → Queued`, and resultant `Queued → Dead`. It does not define the scheduler, frequency, or full eligibility criteria for materialization.

The netting expectation is that component and resultant cashflows share a netting ID, and that the resultant amount is the sum of component amounts. Currency, rounding, and eligibility constraints are not specified.

## Boundaries

This source concerns individual cashflows in Ratan. It does not establish group-blotter rules, lien handling, Korea migration behaviour, or that the materialization job is the same as the [[Auto-Netting Job]].