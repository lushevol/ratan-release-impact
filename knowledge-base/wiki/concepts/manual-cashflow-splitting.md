---
type: concept
title: Manual Cashflow Splitting
tags: [cashflow, settlement, operations, split]
related: [cashflow-un-split, split-cashflow-amendment, cashflow-lineage-and-amendment-correlation, vostro-nostro-ssi-selection, authoritative-split-cashflow-lifecycle]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Split Demo Cases.md"]
---
# Manual Cashflow Splitting

Manual cashflow splitting is an Operations workflow for dividing a gross cashflow into child cashflows so that portions can be settled using different vostro/nostro settlement instructions.

## Workflow

1. The operator selects a gross cashflow.
2. The system generates a child with the original amount by default.
3. Currency-specific decimal and rounding rules constrain entered amounts.
4. When the operator enters a lower amount, the system calculates the balance for a second child.
5. The input must be between zero and the available balance.
6. The operator may use an optional SI lookup.
7. The operator selects **Split Cashflow with Affirmation**, enters affirmation information, and confirms.

## Resulting state

- The parent moves to `SPLIT`.
- Generated children enter `WAITING`.
- Each child has a `Split Cashflow` exception.
- Parent and children share a `Splitting Id`.

This is a split-specific lineage model related to [[cashflow-lineage-and-amendment-correlation]]. It should not be assumed that every `WAITING` cashflow is a split child.

## Boundaries

The requirement implies, but does not explicitly state, that initial child amounts must conserve the parent amount. It also does not define whether one action can create more than two children, the required affirmation fields, SI validation, authorization controls, or rounding-residual allocation.

Manual splitting is distinct from [[threshold-based-cashflow-auto-distribution]], whose trigger is an over-threshold condition at release cut-off rather than an operator action.