---
type: query
title: When Can Reversal Cashflows STP in CN Day 1?
tags: [reversal, stp, nstp, cn-day-1, settlement-control]
related: [stella-trade-event-to-settlement-control, released-settled-amendment-control, trade-event-triggered-cashflow-stp, ratan]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control.md"]
---
# When Can Reversal Cashflows STP in CN Day 1?

The source gives incompatible guidance for reversals after a released or settled cashflow.

The consolidated Drop 2/Drop 3 matrix routes cancellation withdrawals and amendment-related reversals to NSTP. However, the trade-cancellation scenario says that China Day 1 can STP a reversal and automatically generate MT192/MT292.

## Required decision

Define the governing rule by business event, source, delivery phase, prior payment state, and availability of trade-event information in the cashflow message. Confirm whether the STP statement is a limited cancellation path, a superseded design, or a future-state capability.

This decision affects [[stella-trade-event-to-settlement-control]] and [[trade-event-triggered-cashflow-stp]].