---
type: concept
title: Payment and Cashflow Suppression Governance
created: 2026-08-22
updated: 2026-08-22
tags: [payment-suppression, cashflow-suppression, accounting, controls]
related: [mx211-cash-settlement-decommission, settlement-suppression-exceptions, clearing-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/Settlement Touchpoints.md"]
---
# Payment and Cashflow Suppression Governance

Payment and cashflow suppression governance defines the criteria, identifiers, operational statuses, authorization, reporting, and accounting treatment used to prevent a payment or downstream processing from occurring.

The source records product- and client-specific examples, including HUCUN, commodity flows, CDS premiums, bond workflows, and a USD gold-purchase payment under Murex FX facing SCB London. That gold case is explicitly intended to prevent duplicate payment because local FMO CC arranges payment; it must not be generalized to other Murex FX or commodity payments.

Statuses and identifiers such as `SUPP`, `SENT`, `SUPPRESSXXX`, and suppression-table records are incomplete or inconsistent in the source. Canonical semantics and downstream accounting consequences require confirmation.