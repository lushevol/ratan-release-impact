---
type: concept
title: Pending Confirmation/Affirmation
tags: [cash-settlement, confirmation, affirmation, ratan, stella, murex]
related: [ratan, stella, murex, scbml, cashflow-multi-exception-generation, maker-checker-settlement-control]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md"]
---
# Pending Confirmation/Affirmation

Pending Confirmation/Affirmation is a maker/checker exception in [[ratan]] for a cashflow whose cashflow-level affirmation and parent-trade confirmation are both missing.

## Evaluation logic

Ratan evaluates confirmation in this sequence:

1. Read confirmation status from the cashflow message.
2. If the cashflow is not confirmed, query the parent trade by trade ID.
3. Treat the cashflow as confirmed if either cashflow-level or trade-level confirmation is present.
4. If a cashflow arrives first, a later matching trade confirmation should trigger a scan of related Murex and Stella cashflows with the same trade ID and remove the exception.

Expected status values are:

- Stella Trade `Trade_State`: `NONCONFIRMED`, `AFFIRMED`, or `CONFIRMED`.
- Murex Trade `Source_System_Validation_Status`: `COMP`.
- Murex Cashflow SCBML workflow-state XPath: `COMP`.
- Stella Cashflow uses the corresponding SCBML workflow-state XPath, but the source marks this mapping TBD.

## Exclusions

Do not generate the exception when:

- `Cashflow.Cashflow_Event_Reason==Reversal`
- `Entity.Counterparty_Is_Internal==Y`
- A component cashflow with the same trade ID is confirmed

## Remediation behavior

The Cashflow Affirmation section is always visible to makers. It is mandatory only when the exception exists. A maker enters affirmation details; the checker sees those details as read-only and can approve or reject them but cannot alter them.

When a checker rejects only affirmation details, Pending Confirmation/Affirmation reopens for maker re-entry. SSI data is read-only and Back Value is hidden during that targeted maker rework cycle.

The source uses both “Pending Confirmation/Affirmation” and “Pending Affirmation.” The canonical label remains unresolved.