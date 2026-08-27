---
type: project
title: RATAN-Murex 2.11 Cashflow Integration
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, murex-211, fmrp, cashflow-integration, workflow]
related: [fmrp, murex-211, scb-fmrp-dbf, fmrp-murex-cashflow-status-synchronization, fmrp-payment-insertion-eligibility, fmrp-outbound-cashflow-enrichment, fmrp-retry-and-purge-policy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
status: on-hold
owner: ""
start_date: 2023-01-17
target_date: ""
---
# RATAN-Murex 2.11 Cashflow Integration

## Purpose

This project configuration integrates Murex 2.11 payment workflows with FMRP/RATAN settlement processing. The documented design includes external-settlement routing, FMRP status persistence, outbound `MxPayML` enrichment, MQ transport, insertion filtering, retry handling, and inbound acknowledgement processing.

## Recorded changes

RATAN-11101 changes payment insertion by removing the direct `docPayment → INIT2SNTR` link and introducing `PayInsertionFilter`, which routes eligible records to `SNTR` and discarded records to `FmrpPurge`.

RATAN-10822 replaces the legacy inbound acknowledgement router and formulas with new router, acknowledgement, and release components. Their definitions are not included in the source.

## Status

The document describes intended configuration and a January 2023 update, but provides no evidence of release approval, UAT completion, production deployment, or current ownership. The project is therefore recorded as `on-hold` pending confirmation rather than as complete.

## Risks and open questions

- The final inbound acknowledgement and release state model is unavailable.
- The meanings and relationship of RATAN, `razorID`, RAZOR, and MLS are not defined.
- The source contains UAT MQ endpoints only.
- The retry design purges after three attempts without documented escalation.
- The outbound entity identifier mapping requires recipient-contract validation.