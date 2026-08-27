---
type: project
title: FMRP China Cash Settlement
status: complete
owner: ""
start_date: 2023-04-01
target_date: 2023-06-30
created: 2026-08-22
updated: 2026-08-22
tags: [fmrp-china, cash-settlement, q2-2023, delivery-plan]
related: [fmo-post-trade-portal, blade, stella, ratan, client-level-cashflow-netting, irs-auto-netting, hold-and-un-hold, manual-failure-and-reinstatement, settle-as-gross, adhoc-settlement-instructions, cashflow-status-and-substate-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# FMRP China Cash Settlement

## Summary

FMRP China Cash Settlement is the Q2 2023 delivery scope documented in the 26-auto-netting-page-md-files--156-cash-settlement-home-page-cash-settlement-home-page-fmrp-china-cash-settlemen--q1ja52 source record. The delivery demonstrated operational controls and automated processing for cashflow netting, settlement exceptions, failed processing, gross settlement, and settlement-instruction maintenance.

## Delivery scope

The demonstrated functions were:

- Client-level cashflow netting, including mixed-currency selections.
- Hold and un-hold for `Waiting` and `Ready` cashflows.
- Automatic netting of IRS fixed and floating legs.
- Manual failure and reinstatement.
- Gross settlement as an alternative to pending netting conditions.
- Adhoc settlement-instruction entry for `Waiting` and `Ready` cashflows.

## System flow

The documented test flow begins with trade booking in [[blade]]. [[stella]] sends resulting cashflows to [[ratan]]. Operators then access the cashflow blotter in [[fmo-post-trade-portal]] to inspect and operate on the cashflows.

The source does not establish ownership boundaries or identify which system is authoritative for the complete cashflow lifecycle.

## Completion and evidence

The source records demonstrations and stated expected results, but it does not provide a formal release sign-off, defect list, execution metadata, or complete traceability from trades to expected-result cashflow identifiers. The delivery should therefore be treated as documented demo scope rather than independently verified production readiness.

## Retrospective

The delivery established a useful operational workflow vocabulary, especially around component and resultant cashflows, status/substate transitions, operator comments, and exception recovery. Follow-up documentation should normalize lifecycle states, reconcile test identifiers, and specify the omitted NSTP and exception-handling rules.
