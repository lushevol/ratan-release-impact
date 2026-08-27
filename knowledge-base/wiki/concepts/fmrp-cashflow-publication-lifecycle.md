---
type: concept
title: FMRP Cashflow Publication Lifecycle
created: 2026-08-24
updated: 2026-08-24
tags: [FMRP, cashflow, lifecycle, state-transition, RATAN]
related: [fmrp, murex-211, murex-ratan-cashflow-message-contract, what-does-math-mean-in-the-fmrp-cashflow-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change.md"]
---
# FMRP Cashflow Publication Lifecycle

The FMRP lifecycle tracks an eligible Murex payment flow in `SCB_FMRP_DBF`, publishes it to RATAN, and synchronizes acknowledgement and release responses.

## Documented states and operations

| State or operation | Documented behavior |
|---|---|
| `INIT` | Existing record eligible for initial publication when the action is `FAIS`, `I2SR`, or `FMIS`. |
| `SENT` | Record is inserted or updated before outbound publication. |
| `CANC` | A previously sent record is cancelled by `FMSI`; a later `FMIS` can replay it. |
| Acknowledged | `M_RATAN_ID` and `M_ACK_DATETIME` are updated; `PAYFLOW_DBF.M_REASONS` receives message details. |
| `MATH` | Release processing status written by `syncRelease`; exact meaning is undefined. |
| Published | `M_PUB_DATETIME` is written after outbound publication. |

## Action routing

`FAIS`, `FMIS`, `FMSI`, and `I2SR` route to FMRP. `RI2C`, `MCXI`, and `MIXC` route to MLS. The eligible payment status transitions are `INIT` to `SNTR` and `SNTR` to `INIT`.

## Important uncertainty

The source does not define whether `MATH` is a terminal state, whether it corresponds to `RLSR`, or what subsequent transitions are allowed. See [[queries/what-does-math-mean-in-the-fmrp-cashflow-lifecycle]].