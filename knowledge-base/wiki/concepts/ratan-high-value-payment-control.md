---
type: concept
title: RATAN High-Value Payment Control
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, high-value-payment, authorization-limits, payment-routing, settlement]
related: [ratan, fmsgw, bcs, fmrp, loaniq, high-value-payment-queue, high-value-payment-approval-queue, stp-nstp-and-last-user-message-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN.md"]
---
# RATAN High-Value Payment Control

RATAN High-Value Payment Control is the proposed RATAN-side design for enabling [[fmsgw]] to route payment messages by amount threshold into queues requiring distinct approval levels.

## RATAN responsibilities

For FMRP/LOANIQ cashflows, RATAN is required to:

- Display a USD-equivalent cashflow amount in the Cashflow Blotter.
- Support USD-equivalent filtering through custom filters and directly in the blotter.
- Supply STP/NSTP status and user attribution to FMSGW.
- Enforce specified authorization-profile limits.

The authorization-profile specification changes only `FMO_OPS_BOS`, from less than USD 300 million to less than USD 500 million. No `FMO_OPS_BOSM` profile is required.

## Flow-specific limits

The design is not uniform across all cashflow types. [[bcs]] is in scope for routing and authorization controls but is explicitly excluded from USD-equivalent blotter display, amount filtering, and High Value exception display enhancements. [[fmrp]] and [[loaniq]] receive the full blotter and message-enrichment scope.

## Affirmation control

BCS has a confirmed authorization-limit check for update affirmation status. FMRP has no confirmed equivalent: its pending choice is to remove the list-view action or enforce an authorization-limit check. This distinction must be preserved in any control design or implementation evidence.

## Underspecified elements

The source does not provide FMSGW queue thresholds, queue names, profile-to-queue mappings, or a DEF Rule contract. The message fields used for STP/NSTP classification and user attribution are also provisional; see [[stp-nstp-and-last-user-message-contract]].