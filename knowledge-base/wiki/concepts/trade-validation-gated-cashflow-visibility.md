---
type: concept
title: Trade-Validation-Gated Cashflow Visibility
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, trade-validation, settlement, RATAN, FMRP, blotter]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--mg1utu, cashflow-lifecycle-state-model, fmrp-cashflow-publication-lifecycle, fmrp-cashflow-status-synchronization, fmrp-murex-cashflow-status-synchronization, scbml-cashflow-payload]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process.md"]
---
# Trade-Validation-Gated Cashflow Visibility

## Definition

Trade-validation-gated cashflow visibility separates cashflow generation from settlement availability. Stella and Murex 2.11 may generate cashflows when a trade is booked, but RATAN keeps those cashflows in `HOLD` and hides them from the settlement blotter until the associated parent trade reaches an accepted validation state.

## Processing model

1. A source system sends cashflow SCBML to RATAN.
2. RATAN evaluates the trade state in the message.
3. If the state is not accepted, RATAN correlates the cashflow with its parent trade.
4. RATAN applies the source-system-specific validation rule.
5. A validated result changes the cashflow to `VALIDATED`, removes the `HOLD` restriction, and permits normal settlement processing.
6. TDS3 trade-status messages can trigger the same release for already-held cashflows.

The control is about visibility and processing, not about preventing the source system from generating cashflows.

## Source-specific validation

Stella uses `Trade_ID`, `Trade_Lake_Trade_Major_version`, `Trade_State`, and `Action_Type`. Murex 2.11 uses `Source_System_Trade_Internal_Id` and `Source_System_Validation_Status`. The two rules must remain separate because their identifiers and status vocabularies differ.

Certain Stella entities and product combinations bypass the MO validation gate. The bypass configuration is tracked separately in [[queries/what-is-the-authoritative-mo-validation-bypass-configuration]].

## Operational consequence

A cancellation or amendment can arrive after an original cashflow has become visible. The requirement explicitly allows a previously validated cashflow to be processed before the later cancellation version is validated. This creates a reconciliation and timing control that should be addressed in the settlement lifecycle.

This concept extends [[concepts/cashflow-lifecycle-state-model]] and [[concepts/fmrp-cashflow-publication-lifecycle]] with an explicit parent-trade validation gate.