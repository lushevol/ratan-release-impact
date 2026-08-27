---
type: concept
title: Trade-Confirmation-Driven Cashflow STP
tags: [trade-confirmation, cashflow, STP, straight-through-processing, settlement, cashflow-stp, exception-management, ratan]
related: [cdu, ratan, trade-cashflow-reference-linkage, cashflow-reference-consistency-validation, comp-status-driven-stp, cashflow-status-lifecycle, tds3, stella, murex-211, trade-cashflow-correlation-by-trade-version, murex-comp-confirmation-exception-resolution, cashflow-lifecycle-state-model]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/CDU Trade Confirmation Notification & Cashflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md"]
---

# Trade-Confirmation-Driven Cashflow STP

Trade-confirmation-driven cashflow STP uses trade affirmation or confirmation status as an input to determine whether related cashflows may enter straight-through processing.

The newer *Trade Confirmation & Cashflow STP* source describes this as a proposed [[ratan]] control: an affirmed or confirmed trade status resolves a cashflow's `Pending Confirmation/Affirmation` exception. [[tds3]] is intended to provide Ratan with generic trade SCBML as the universal golden source for these decisions.

The deprecated *CDU Trade Confirmation Notification & Cashflow* source adds a stale-cashflow safeguard to the general confirmation-driven STP principle represented by [[comp-status-driven-stp]]. In its proposed CDU-to-Ratan flow, confirmation status alone is insufficient: Ratan must identify the relevant cashflow and validate that its linkage reference corresponds to the confirmed trade state. If the expected cashflow is missing or the linkage is inconsistent, Ratan must block STP and raise an operational exception.

> [!warning]
> The CDU-to-Ratan requirement described above is deprecated and does not establish that this control is current or implemented.

The rules differ by originating trade system and must not be treated as one common correlation algorithm.

## Stella Rule

For Stella-derived trades, Ratan correlates trade and cashflow records using `Trade_ID` and `Trade_Lake_Trade_Major_version`.

The statuses `AFFIRMED`, `CONFIRMED`, and `NONCONFIRMED` can close `Pending Confirmation/Affirmation`. The source does not specify whether closing a Stella exception moves the cashflow to STP, leaves it NSTP, or triggers another disposition.

`NONCONFIRMED` requires particular clarification because the source permits it to close a confirmation-related exception. See [[what-does-nonconfirmed-mean-for-cashflow-stp]].

## Murex Rule

For Murex 2.11, Ratan matches `Source_System_Trade_Internal_Id` from trade SCBML to cashflow `Trade_Id`. A status of `COMP` can close `Pending Confirmation/Affirmation`.

Promotion to STP is explicitly limited to cashflows for which that exception is the only exception. The detailed extraction and closure rule is documented in [[murex-comp-confirmation-exception-resolution]].

## Version Control

For several Stella update-like events, CDU is expected to confirm the latest trade major version. This is intended to prevent an older trade version from resolving cashflow confirmation handling after a newer version exists.

The authoritative CDU status contract and version-selection rule remain open in [[what-is-the-authoritative-cdu-confirmation-status-contract]].