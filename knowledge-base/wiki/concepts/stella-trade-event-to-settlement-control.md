---
type: concept
title: Stella Trade Event to Settlement Control
tags: [stella, trade-events, stp, nstp, reversal, rebook, settlement-control]
related: [stella, ratan, released-settled-amendment-control, trade-event-triggered-cashflow-stp, cashflow-netting-and-auto-un-netting, undo-revive-cashflow-control]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control.md"]
---
# Stella Trade Event to Settlement Control

Stella business events determine whether Ratan cancels prior cashflows, generates reversal and rebook exceptions, permits STP, or routes cashflows to NSTP.

## Released or settled threshold

For amendment, partial termination, termination, novation, fixing, and cancellation:

- If the original cashflow is not released or settled, a withdrawal cancels the old cashflow and replacement cashflows can become live.
- If the original cashflow is released or settled, the withdrawal is treated as a reversal and replacement cashflows as rebooks. These require controlled exception handling in the interim design.

This extends [[released-settled-amendment-control]] with event-specific requirements.

## New-trade restrictions

Close Out and Portfolio Reassignment cashflows generated on a new trade must be forced to NSTP when:

```text
Trade ID <> Parent Trade ID
```

The applicable exception is `Close Out / Port Reassign`. Settlement Ops determines whether to suppress, release, or manually net payments. The portfolio reassignment design is explicitly described as backlog work for non-economic-amendment treatment and should not be treated as final target-state policy.

## Expiry and fixing

Expiry cashflows are non-economic and discarded. Fixing can proceed normally before release; a re-fixing after release requires reversal/rebook treatment.

## Delivery-phase ambiguity

The document says released-cashflow reversals are NSTP in Drop 2/Drop 3 because trade-event information is unavailable in cashflow messages. It separately says a China Day 1 cancellation reversal can STP with automatic MT192/MT292 generation. This must be resolved before implementation.

See [[when-can-reversal-cashflows-stp-in-cn-day-1]].