---
type: entity
title: SWAPSWIRE
created: 2026-08-23
updated: 2026-08-23
tags: [trade-booking-system, clearing, SWAPSWIRE, payment-risk]
related: [murex, ratan, clearing-trade-payment-risk, clearing-status-propagation, source-system-based-nstp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Clearing Trades & Payment Risk.md"]
---
# SWAPSWIRE

SWAPSWIRE is a trade-booking source system identified as a significant clearing-payment risk source.

## Clearing-status behavior

The first version of a SWAPSWIRE trade does not contain clearing status. A subsequent modify message adds the status, potentially up to two hours later. The initial payment can therefore reach RATAN without the indicator.

The source also states that SWAPSWIRE trades are marked for novation to a Clearing House.

## Control relevance

A SWAPSWIRE payment may require source-system-based NSTP in RATAN so that original bilateral payment C1 cannot be released before novation. This is a proposed mitigation, not evidence that all SWAPSWIRE payments are clearing trades.

Trade-population analysis is required to identify false positives before applying a blanket rule.