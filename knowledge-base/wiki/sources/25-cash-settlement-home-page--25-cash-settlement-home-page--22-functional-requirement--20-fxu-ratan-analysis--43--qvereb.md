---
type: source
title: FXU and RATAN Dependencies for Expansion to Other Markets
authors: []
year: 2026
url: ""
venue: "Internal functional-requirement note"
tags: [cash-settlement, FXU, RATAN, market-expansion, functional-requirements]
related: [fxu, ratan, blade, stella, razor, fmrp, ebbs, rcs, fxu-settlement-method-amendment, forward-trade-util-stamping, trade-remaining-amount-visibility, fxu-razor-fmrp-routing]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Dependencies for expansion to other Markets.md"]
---
# FXU and RATAN Dependencies for Expansion to Other Markets

## Summary

This internal functional-requirement note identifies dependencies for expanding FXU/RATAN settlement capabilities to additional markets. It describes settlement-method amendments, utilization controls, forward-trade processing, cancellation-related workflows, remaining-amount visibility, and routing between RAZOR and FMRP.

The note records requirements and dependencies rather than evidence of implementation, approval, or a complete technical contract.

## Requirements captured in the source

1. Settlement-method amendment responsibilities are to be clarified. Blade requires a new profile for Ops, and RATAN must trigger a new event to Stella.
2. FMO users require trade-level capability to change the Settlement Method from Gross to UTIL or from UTIL to Gross. A hard block is required when the trade is fully or partially utilized, including utilization of one cashflow or one leg of an FX swap.
3. An Early Utilization workflow is required.
4. A Cancellation Charges workflow is required, including RCS integration for India.
5. An Auto Cancellation workflow is required for unutilized trades.
6. A Time Option workflow is required.
7. Future cashflows may not yet have materialized and therefore would not ordinarily be stamped as UTIL; UTIL stamping is required for forward trades as well.
8. The remaining amount must be visible in the same trade ticket in Blade.
9. FXU provides a utilization window for forward trades. If a forward trade is utilized within that window, RATAN should move its status to Utilized, while the EBBS entry should be passed only on value date.
10. FXU must support integration with both RATAN and RAZOR for a single entity. FXU must identify whether a trade belongs to RAZOR or FMRP and trigger the request to the correct system.
11. Blade requires a single remaining-amount view for FO stakeholders.
12. A hard block is required for Middle Office users.
13. The remaining amount must be displayed in Blade.

## System responsibilities and dependencies

The source assigns a partial responsibility split:

- **Blade**: provide an Ops profile, trade-ticket functionality, and remaining-amount views.
- **RATAN**: process utilization status and trigger a new event to [[entities/stella|Stella]] for settlement-method amendments.
- **Stella**: receive the settlement-method amendment event.
- **FXU**: determine the destination system and coordinate requests to [[entities/razor|RAZOR]] or [[entities/fmrp|FMRP]].
- **EBBS**: receive the accounting entry on value date, even when RATAN has already moved the trade to Utilized during the utilization window.
- **RCS**: provide the India-specific integration identified for the Cancellation Charges workflow.

The note does not specify the authoritative mutation point, event name, event payload, acknowledgement behavior, failure handling, routing key, remaining-amount formula, or detailed workflow state model.

## Important distinctions

The requirements imply that operational utilization status and accounting-feed timing are separate concerns. A trade may become Utilized in RATAN during the forward-trade utilization window, while the corresponding EBBS accounting entry remains deferred until value date.

The requirement to stamp UTIL for forward trades also separates utilization representation from cashflow materialization. This extends the questions addressed by [[concepts/value-date-based-cashflow-materialization]], [[concepts/cashflow-status-lifecycle]], and [[concepts/cashflow-accounting-eligibility]].

## Open specification areas

The source leaves the following areas unresolved:

- The authoritative system for changing Settlement Method.
- The exact Stella event and its contract.
- The scope of the FMO and Middle Office hard blocks.
- Representation of partial utilization and FX-swap-leg utilization.
- The event or batch that sends the EBBS entry on value date.
- The attribute used to route a trade to RAZOR or FMRP.
- Handling of missing or conflicting routing information.
- The calculation and refresh behavior for remaining amount.
- Scope, triggers, approvals, and exception paths for Early Utilization, Cancellation Charges, Auto Cancellation, and Time Option.

## Related pages

- [[entities/fxu]]
- [[entities/ratan]]
- [[entities/blade]]
- [[entities/stella]]
- [[entities/razor]]
- [[entities/fmrp]]
- [[entities/ebbs]]
- [[entities/rcs]]
- [[concepts/fxu-settlement-method-amendment]]
- [[concepts/forward-trade-util-stamping]]
- [[concepts/trade-remaining-amount-visibility]]
- [[concepts/fxu-razor-fmrp-routing]]