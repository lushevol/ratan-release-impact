---
type: query
title: How Are Three-Agent Trades Handled?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, ssi, agents, exception-handling, fxo]
related: [fxo, ssi-stamping, standard-settlement-instructions, cashflow-status-handling, how-should-swap-agent-and-rfr-be-validated]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# How Are Three-Agent Trades Handled?

## Question

When SSI auto stamping encounters a three-agent trade, is the trade rejected, suspended, routed to NSTP processing, or handled manually?

## Evidence

The FXO checklist states that one-agent and two-agent arrangements are supported and that three-agent arrangements are not supported. It provides no exception path or expected status.

## Information Needed

- How a three-agent arrangement is detected.
- The resulting trade and cashflow statuses.
- Whether SSI stamping is skipped or partially performed.
- The operational queue and responsible team.
- Whether payment messaging and accounting are suppressed.
- Whether an override is available and subject to authorization.
- Required user-facing error messages and UAT scenarios.

This limitation should be resolved alongside [[how-should-swap-agent-and-rfr-be-validated]].