---
type: entity
title: Data Persistence Node
created: 2026-08-24
updated: 2026-08-24
tags: [workflow, persistence, cashflow, architecture]
related: [cashflow-lifecycle-stamping, lifecycle-service, cashflow-precheck-validation, ratan-stella-message-event-source]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Cashflow Lifecycle Stamping Logic.md"]
---
# Data Persistence Node

The Data Persistence Node is the workflow component that currently couples cashflow persistence with precheck and stamping responsibilities.

## Current responsibilities

The documented flow includes:

- Precheck and enrichment.
- Validation.
- Persistence of `RatanStellaMessageEvent`.
- Construction of SCBML.
- Lifecycle-request construction.
- Handoff to lifecycle processing.

For Withdrawals, the path also includes cashflow existence checks, unnetting checks, and holding-queue decisions. For New cashflows, the documented admission requirement is `PROJECTED` status.

## Proposed change

The design proposes simplifying the Data Persistence Node and moving stamping to a separate API and reusable lifecycle action in [[entities/lifecycle-service]].

This proposal is not evidence that the change was approved or implemented. The source does not define the resulting transaction boundaries, persistence guarantees, or failure handling.
