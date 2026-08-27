---
type: concept
title: MO Detective Controls
created: 2026-08-23
updated: 2026-08-23
tags: [detective-controls, operations, trade-controls, cash-settlement]
related: [ratan, trade-blotter, trade-review, issue-tracking-and-technical-debt-governance, nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis.md"]
---
# MO Detective Controls

## Definition

MO Detective Controls are operational checks intended to identify trade, cashflow, booking, fixing, P&L, and exception inconsistencies requiring investigation or remediation.

The 2023 Q4 analysis tracked these controls under `RATAN-16851`.

## Control scenarios

The source recorded analysis or engagement for the following scenarios:

- Cross Currency Swaps with an initial exchange but no final exchange tick.
- A mismatch between a predefined index and its corresponding fixing schedule.
- ND Cross Currency trades with outstanding amounts after the fixed-trade near-leg fixing date.
- BTB flatness checks and exception monitoring.
- A P&L-related rule under solution engagement.

The ND Cross Currency scenario was on hold because the booking model had not been finalized.

## Q4 2023 status

On 2023-11-03, the workstream was in progress. By 2023-11-20:

- Three rules were in development.
- One additional rule awaited business requirements from Kunal.
- One P&L rule was undergoing solution engagement with Liam.

These updates show progressive control development rather than a complete, signed-off control framework.

## Interpretation

Each control must remain attached to its specific trade scenario. The source does not establish that all rules were implemented, deployed, or accepted after the November updates.