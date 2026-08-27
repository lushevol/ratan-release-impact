---
type: source
title: Sprint 13 (31th Oct 2022–11th Nov 2022)
authors: []
year: 2022
url: ""
venue: "CN Settlement Demo Session"
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, materialization, netting, demo-requirements, sprint-13]
related: [ratan, stella, cashflow-blotter, cashflow-record, cashflow-materialization, stella-cashflow-amendment-supersession, ratan-manual-netting-transformation, what-is-the-authoritative-ratan-cashflow-materialization-threshold-and-vd-calendar, does-stella-amendment-discard-mean-delete-supersede-or-hide-the-original-cashflow, what-is-the-authoritative-ratan-manual-netting-api-and-resultant-cashflow-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 13 (31th Oct 2022- 11th Nov 2022).md"]
---
# Sprint 13 (31th Oct 2022–11th Nov 2022)

This Sprint 13 document defines a functional demonstration scope for RATAN cashflow storage and materialization. It specifies expected outcomes for mocked Stella messages and manual netting; it does not contain evidence that the cases were executed, passed, accepted, deployed, or used in production.

## Demonstration Scope

- Cashflow data store in Ratan
- Cashflow materialization

## User Cases

| NO. | Description | Steps | Expected Result |
| --- | --- | --- | --- |
| 1 | Stella New & VD-7 | 1. Mock Stella new message with payment date as VD-7 2. Manually push new message to Ratan workflow 3. Load cashflow from cashflow blotter | 1. Ratan can store cashflow in database as 'Projected' cashflow 2. Display in cashflow blotter GUI. |
| 2 | Stella New & VD-5 | 1. Mock Stella new message with payment date as VD-5 2. Manually push new message to Ratan workflow 3. Load cashflow from cashflow blotter | 1. Ratan can store cashflow in database as 'Queued' cashflow 2. Display in cashflow blotter GUI. |
| 3 | Stella New & VD-4 | 1. Mock Stella new message with payment date as VD-4 2. Manually push new message to Ratan workflow 3. Load cashflow from cashflow blotter | 1. Ratan can store cashflow in database as 'Queued' cashflow 2. Display in cashflow blotter GUI. |
| 4 | Stella VD-7 and run materialization on VD-5 | 1. Mock Stella new message with payment date as VD-7 2. Manually push new message to Ratan workflow 3. Run the materialization job on VD-5 | 1. Ratan store the cashflow as 'Projected' on VD-7 2. Ratan move the status to 'Queued' on VD-5 |
|  | Stella New + Amendment (VD-4) | 1. Mock Stella new message with payment date as VD-4 2. Mock Stella Amendment message on same cashflow | 1. Display the amendment cashflow only and discard the new |
| 5 | Netting Status Moving | 1. Mock component cashflows 2. Run the netting API manually | 1. Component cashflow moved to 'Netted' 2. Resultant cashflow created as 'Queued'. |

## Requirement-Level Findings

For mocked Stella New messages, the intended initial RATAN state is `Projected` at VD-7 and `Queued` at VD-5 and VD-4. Cashflows are expected to be visible in [[cashflow-blotter]].

The specified materialization behavior is a transition from `Projected` at VD-7 to `Queued` when the materialization job is run on VD-5. See [[cashflow-materialization]].

For an Amendment following a New message for the same cashflow, the intended result is display of the amended cashflow only. The meaning of “discard the new” is not defined; see [[stella-cashflow-amendment-supersession]].

Manual invocation of the netting API is expected to transition component cashflows to `Netted` and create a resultant `Queued` cashflow. See [[ratan-manual-netting-transformation]].

## Boundaries and Unknowns

The document does not define the VD calendar or time-zone convention, treatment at VD-6 or other dates, materialization scheduling or failure handling, amendment correlation keys, record retention, or the Netting API contract. It concerns RATAN, Stella, and Cashflow Blotter in the stated demo context and does not establish later group-blotter, lien-aware, or bulk-STP behavior.