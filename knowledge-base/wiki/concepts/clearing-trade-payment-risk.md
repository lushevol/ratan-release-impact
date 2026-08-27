---
type: concept
title: Clearing Trade Payment Risk
created: 2026-08-23
updated: 2026-08-23
tags: [clearing, payment-risk, novation, bilateral-settlement, NSTP]
related: [ratan, murex, clearing-status-propagation, source-system-based-nstp, ratan-netting-rule-check, cashflow-group-completeness-gating, murex-reversal-and-new-cashflow-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Clearing Trades & Payment Risk.md"]
---
# Clearing Trade Payment Risk

Clearing trade payment risk occurs when an original bilateral payment is released before the system knows that the trade will be novated to a clearing counterparty.

## Risk pattern

A trade is initially booked against bilateral client A, and payment C1 is sent to RATAN without a clearing indicator. If C1 enters STP and reaches the VD-1 release cutoff before novation, it may settle bilaterally. Later novation then requires C1 to be recalled or reversed and replacement payment C2 to be generated against the clearing counterparty.

The risk is concentrated in C1, not necessarily C2. C2 can be held as pending netting when the clearing counterparty is known.

## Control principle

Potentially clearing-related payments should remain in NSTP until clearing treatment and novation status are known. This is an instance of [[concepts/cashflow-group-completeness-gating]]: a required trade attribute is missing or not synchronized, so automatic release is unsafe.

## Operational consequences

Premature bilateral release can require payment recall, reversal, replacement cashflow processing, and reconciliation across Murex and RATAN. The source identifies a potentially serious escalation when recall is not completed within 10 days, but does not provide quantified loss or incident data.

## Design implication

The control should distinguish trade-level clearing status, source system, product, and whether an Alpha payment exists. “Novation to Clearing House” alone is not sufficient evidence that every payment from a source system has the same risk profile.