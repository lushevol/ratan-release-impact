---
type: concept
title: RATAN Resilience and Control Debt
created: 2026-08-25
updated: 2026-08-25
tags: [RATAN, resilience, control-debt, technical-debt, manual-recovery]
related: [ratan, ratan-temporary-technical-recovery, ratan-technical-recovery-governance, development-team, pss]
sources: ["RATAN/RATAN -Projects/Temporary tech recovery process for Handling Technical Failure Exceptions v1.0.md"]
---

# RATAN Resilience and Control Debt

RATAN resilience and control debt is the operational condition in which recurring technical failures continue to require manual PSS recovery without permanent remediation or automation.

## Classification

If PSS repeatedly performs the same technical recovery but the source-defined urgent thresholds do not otherwise apply, the issue must be classified as resilience or control debt.

More than three manual replays or recoveries within one month requires a permanent fix within one month. A P4 or higher incident, or recurrence of the same issue twice within one week, requires same-week remediation through an ECR or quick fix, with a normal CR possible when lead time permits.

## Prioritization

Resilience and control-debt items should be prioritized above normal enhancement backlog work. Ownership of the repeated manual task should also be reviewed and reassessed.

## Intended resolution

The debt is resolved through a permanent technical fix or automation that prevents recurring PSS intervention. The source does not define the production evidence or closure criteria required to confirm resolution.
