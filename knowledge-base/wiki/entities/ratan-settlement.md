---
type: entity
title: Ratan Settlement
created: 2026-08-22
updated: 2026-08-24
tags: [Ratan-Settlement, settlement, cashflows, migration, ratan, capability, provisional, functional-area]
related: [fxo-mini-trade-migration-ratan-cash-settlement, murex-2-11, stella, cash-settlement-migration, trade-cashflow-reconciliation, ratan, post-trade-orchestration, uber-validation, payment-identification, ratan-settlement-suppression-rule-check, ratan-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md", "RATAN/RATAN -Core Function copy/Function_RATAN-Settlement  0.0_Uber Validation+Payment Identify.md", "RATAN/RATAN -Core Function copy/RATAN-Settlement  2_Suppression Rule Check.md"]
---
# RATAN Settlement

## Identity and source boundaries

The cash-settlement runbook describes Ratan Settlement as the target settlement service receiving cashflows from [[murex-2-11]] and [[stella]]. It treats the Murex-to-Ratan and Stella-to-Ratan feeds as separate operational and reconciliation paths.

The function document identifies “RATAN Settlement,” from its filename, as a provisionally identified RATAN function or capability. It does not establish whether RATAN Settlement is a service, module, workflow, or broader business capability.

The suppression-rule-check source identifies RATAN Settlement as a functional area from its filename. Its available source metadata does not establish the exact system boundary, service ownership, lifecycle responsibilities, or relationship to other settlement components.

## Associated functional context

The function document associates RATAN Settlement with “Uber Validation” and “Payment Identify.” Its available material does not provide a workflow, validation logic, payment-processing responsibility, interface, or operational owner.

The suppression-rule-check source filename associates this functional area with a suppression rule check. The behavior and implementation of that check are documented separately in [[ratan-settlement-suppression-rule-check]], subject to verification when the source body becomes available.

Ratan Settlement may relate to [[post-trade-orchestration]], but the function document states that this relationship requires confirmation from the source body.

## Controls and monitoring

According to the cash-settlement runbook, cashflows entering Ratan Settlement are controlled through High Risk NSTP rules and temporary suppression or un-suppression. Monitoring covers pending states including:

- `Pending Auto Netting`
- `Pending Netting`
- `Pending Another Leg`

## Evidence expected

The cash-settlement plan calls for:

- Group Blotter checks
- Cashflow Blotter checks
- Future seven-day exports
- Cashflow-feed reconciliation
- Cancellation reconciliation

The runbook does not provide the resulting evidence or sign-off.

## Unresolved scope

The suppression-rule-check source requires confirmation of:

- Whether RATAN Settlement is a module, service, workflow, or documentation grouping.
- Which settlement records or cashflows it processes.
- Which component evaluates suppression rules.
- How suppression interacts with settlement orchestration and rule services.
- Whether suppression is distinct from suspension.