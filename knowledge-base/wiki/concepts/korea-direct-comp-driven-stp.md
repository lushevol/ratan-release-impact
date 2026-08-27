---
type: concept
title: Korea Direct COMP-Driven STP
created: 2026-08-23
updated: 2026-08-23
tags: [korea, comp, stp, cashflow-migration, trade-validation, integration]
related: [murex-korea, murex, tds3, ratan-cashflow-lifecycle-service, mxml, scbml, trade-validation-gated-group-processing, trade-validation-group-advancement, cashflow-event-withdrawal-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/COMP status to drive STP process.md"]
---
# Korea Direct COMP-Driven STP

Korea Direct COMP-Driven STP is the stated migration design in which [[murex-korea]] sends a trade message with validation status `COMP` directly to RATAN. The design compensates for the stated inability of [[tds3]] to provide `COMP` for Korea cashflows.

## Intended Message Behavior

The MXML-to-SCBML mapping identifies:

- `tradeStatus/validationLevel = COMP` as the source of the SCBML process substate.
- `mainEvent/action = validation` as the source of the SCBML transaction type.
- The Murex trade-view entity and internal trade ID as direct mappings.
- Trade family, group, and type as inputs to a derived product taxonomy value, illustrated as `CURR|OPT|ASN`.

The mapping applies to illustrated standalone and package-child trade messages, but the source does not define whether package children are processed independently or require package-level completion.

## Cancel and Reissue Dependency

For an unconfirmed original trade that is cancelled and reissued, the stated behavior is that RATAN cancels the original cashflow. The replacement cashflow then waits for the replacement trade to send another `COMP` message.

This statement is presented as an answer under an “OPEN QUESTION” heading and requires implementation and test confirmation. It does not specify idempotency, replay, delayed messages, or out-of-order cancellation and confirmation handling.

## Boundaries

This requirement describes a Korea-specific upstream integration workaround. It does not show that `COMP` is the sole STP eligibility condition, nor does it define cashflow-state, static-data, settlement-eligibility, or group-level conditions. The broader concepts [[trade-validation-gated-group-processing]] and [[trade-validation-group-advancement]] should not be read as overridden by this source.