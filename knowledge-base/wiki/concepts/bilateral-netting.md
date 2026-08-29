---
type: concept
title: Bilateral Netting
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, bilateral-netting, cashflow-lifecycle]
related: [bilateral-netting-eligibility, netting-resultant-cashflow-lifecycle, netting-withdrawal-timing, netting-exception-recovery, cashflow-blotter, netting-static-blotter, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# Bilateral Netting

Bilateral netting combines multiple eligible cashflows into one resultant cashflow between matching parties and settlement attributes.

## Normal lifecycle

1. A live manual netting rule is maintained in the [[netting-static-blotter]].
2. Eligible component cashflows appear in the cashflow blotter with `WAITING / Pending Netting`.
3. The user selects the components and submits the netting operation, including affirmation information where required.
4. Components transition to `NETTED`.
5. A resultant cashflow is created with `Affirmation status = 'Affirmed'`, `Payment type = 'Bilateral Netting'`, and completed `NSTP process complete (MAKER_CHECKER)`.
6. Ops releases the resultant from [[ratan]].

The source requires the resultant amount to be correct but does not define the calculation formula.

## Eligibility

Selected cashflows must match on booking entity, counterparty, value date, and currency. A mismatch blocks the operation. Released or settled component cashflows cannot be selected for netting.

[[bilateral-netting-eligibility]] describes these constraints in detail.

## Reversal and exception paths

Manual un-netting changes the resultant to `DEAD` and restores its components to `WAITING / Pending Netting`. A component withdrawal before resultant finality triggers automatic un-netting; withdrawal after release or settlement has a different, incompletely specified outcome.

Fail/reinstate, hold/unhold, suppression rejection, and Settle As Gross can preserve or restore a cashflow’s ability to participate in later netting. See [[netting-exception-recovery]] and [[netting-withdrawal-timing]].

## Evidence boundary

This page reflects the stated functional requirement. It does not establish broader accounting, settlement-finality, or integration rules beyond the behavior explicitly assigned to this bilateral-netting workflow.