---
type: concept
title: Amendment Withdrawal-Driven STP
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, amendments, withdrawals, STP, workflow, NSTP]
related: [ratanone, scbml, nstp-service, major-version-cashflow-grouping, cashflow-lifecycle-state-machine-restructuring, original-replacement-cashflow-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events.md"]
---
# Amendment Withdrawal-Driven STP

Amendment withdrawal-driven STP is the proposed RATANONE behavior in which the completion status of a withdrawn cashflow determines when its replacement cashflow can proceed straight through processing.

## Proposed flow

When a major-version group contains both a withdrawal and a new cashflow:

1. The group is marked as an amendment group.
2. The new cashflow receives a RATAN-generated amendment event.
3. The new cashflow is blocked in workflow with `WAITING`, `Reversal_Rebook`, and `Pending Verification`.
4. The withdrawal receives the amendment event and is processed through workflow.
5. Eligible withdrawal outcomes can move the linked new cashflow to STP.

The source lists these withdrawal outcomes as eligible:

| Main status | Sub status | Sub-status type |
|---|---|---|
| `CANCELLED` | `NA` | `NA` |
| `NOSTRO_MATCHED` | `NA` | `NA` |
| `NETTED` | `NOSTRO_MATCHED` | — |

The withdrawal is also subject to NSTP rule checking. The source does not define the authoritative event values, the deterministic withdrawal-to-replacement matching algorithm, or the exact STP transition contract.

## Risk

Delays or failures in withdrawal status updates can leave replacement cashflows blocked. Incorrect matching or failed status write-back could allow the wrong cashflow to proceed, so this design should not be treated as a complete production control specification.