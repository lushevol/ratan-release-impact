---
type: concept
title: NDS Cashflow Processing
tags: [cash-settlement, cashflow, nds, netting, lifecycle, orchestration]
related: [nd-parent-trade-metadata, nstp-and-ndirs-rule-routing, ratan-mxg-cashflow-adaptor, ratan-cash-settlement-orchestration, netting-service, lifecycle-service, rule-service, what-is-the-authoritative-nds-cashflow-processing-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NDS Cashflow Processing Design.md"]
created: 2026-08-24
updated: 2026-08-24
---
# NDS Cashflow Processing

NDS cashflow processing is the change scope described by the source across cashflow candidate netting, lifecycle precheck, persistence and attribute stamping, rule evaluation, message mapping, and workflow orchestration.

## Documented Changes

- `ratan-cash-settlement-netting-service` receives a cron-driven scan of cashflow candidates and netting path.
- `ratan-cashflow-lifecycle-service` refactors precheck and decouples data persistence from attribute stamping.
- `ratan-rule-service` adds and changes rules based on NID and ND parent typology.
- [[ratan-mxg-cashflow-adaptor]] maps NID from MXML to [[scbml]].
- [[ratan-cash-settlement-orchestration]] adds an unnamed node after Pre-check.

## Scope Boundary

The source does not define what “NDS” expands to, nor does it provide a complete state machine. It is therefore not evidence for exact node ownership, terminal statuses, transactionality, or retry behavior.

The NDS flow depends on [[nd-parent-trade-metadata]] being available for [[nstp-and-ndirs-rule-routing]].